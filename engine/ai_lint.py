"""Anti-AI-tell linter.

Catches the language and shape that make a document read as machine-written.

Two ideas drive this:

  1. Vocabulary. Language models reach for a narrow band of words far more often
     than people do. "Leveraged", "spearheaded", "seamless", "robust". None are
     bad English. A document dense with them reads as generated even when every
     fact is true.

  2. Uniformity. This is the louder tell and the harder one to fix by hand.
     People write unevenly - a three-word bullet next to a two-line one, one
     sentence that runs long because the thought did. Generated text comes out
     suspiciously even: every bullet the same length, every bullet opening with
     a past-tense verb, every bullet ending in "resulting in <round number>".
     The linter measures that evenness and complains when it is too clean.

Rules live in rules_ai_tells.yaml. Adding a rule should never require editing
this file.

Usage:
    python -m engine.ai_lint draft.md
    python -m engine.ai_lint draft.md --bullets       (one bullet per line)
    python -m engine.ai_lint draft.md --max block     (exit 1 only on blocks)
"""

from __future__ import annotations

import argparse
import pathlib
import re
import statistics
import sys

import yaml

RULES_PATH = pathlib.Path(__file__).with_name("rules_ai_tells.yaml")
SEVERITY_RANK = {"note": 0, "warn": 1, "block": 2}


class Finding:
    def __init__(self, severity, rule, message, line=None, excerpt="", fix=""):
        self.severity, self.rule, self.message = severity, rule, message
        self.line, self.excerpt, self.fix = line, excerpt, fix

    def __str__(self):
        loc = f"L{self.line}" if self.line else "  "
        s = f"  [{self.severity:<5}] {loc:<5} {self.rule}: {self.message}"
        if self.excerpt:
            s += f"\n              ...{self.excerpt.strip()}..."
        if self.fix:
            s += f"\n              -> {self.fix}"
        return s


def load_rules(path=RULES_PATH):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


# --- vocabulary ---------------------------------------------------------------

def check_phrases(text, rules):
    out = []
    lines = text.splitlines()
    for rule in rules.get("phrases", []):
        rx = re.compile(rule["pattern"], re.IGNORECASE)
        for i, line in enumerate(lines, 1):
            for m in rx.finditer(line):
                lo, hi = max(0, m.start() - 30), min(len(line), m.end() + 30)
                out.append(Finding(
                    rule.get("severity", "warn"), "phrase",
                    f'"{m.group(0)}"', line=i,
                    excerpt=line[lo:hi], fix=rule.get("fix", "")))
    return out


# --- structure ----------------------------------------------------------------

BULLET_RX = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+(.*)$")


def extract_bullets(text, force_all_lines=False):
    if force_all_lines:
        return [l.strip() for l in text.splitlines() if l.strip()]
    out = []
    for line in text.splitlines():
        m = BULLET_RX.match(line)
        if m and m.group(1).strip():
            out.append(m.group(1).strip())
    return out


def check_structure(text, bullets, rules):
    out = []
    s = rules.get("structural", {})
    words = re.findall(r"\b[\w'-]+\b", text)
    n_words = len(words) or 1

    # Bullet-length evenness. Real writing varies; generated writing does not.
    if len(bullets) >= 3:
        lens = [len(b.split()) for b in bullets]
        mean = statistics.mean(lens)
        cv = (statistics.pstdev(lens) / mean) if mean else 0
        floor = s.get("bullet_length_cv_min", 0.18)
        if cv < floor:
            out.append(Finding(
                "warn", "uniform-length",
                f"bullet lengths are too even (variation {cv:.2f}, want >{floor}); "
                f"lengths={lens}",
                fix="let some bullets run short and one run long, the way you would write them"))

        # Same opening verb over and over.
        firsts = {}
        for b in bullets:
            w = re.sub(r"[^\w]", "", b.split()[0]).lower() if b.split() else ""
            firsts.setdefault(w, []).append(b)
        cap = s.get("max_bullets_same_opening_verb", 2)
        for w, group in firsts.items():
            if w and len(group) > cap:
                out.append(Finding(
                    "warn", "repeated-opener",
                    f'{len(group)} bullets all open with "{w}" (max {cap})',
                    fix="vary the opening; not every line has to start with a past-tense verb"))

        # The verb + object + "resulting in <metric>" template.
        shaped = [b for b in bullets
                  if re.search(r"\b(resulting in|leading to|which (led|resulted))\b", b, re.I)]
        if len(shaped) > s.get("max_consecutive_same_shape", 3):
            out.append(Finding(
                "warn", "template-shape",
                f"{len(shaped)} bullets use the same cause-effect template",
                fix="state the outcome plainly in some of them instead"))

    # Em dash density.
    em = text.count("—")
    per100 = em / n_words * 100
    cap = s.get("em_dash_per_100_words_max", 1.2)
    if per100 > cap:
        out.append(Finding(
            "warn", "em-dash",
            f"{em} em dashes in {n_words} words ({per100:.1f}/100, max {cap})",
            fix="use commas, or split the sentence"))

    # "not X, but Y"
    if s.get("forbid_not_x_but_y", True):
        for i, line in enumerate(text.splitlines(), 1):
            m = re.search(r"\bnot (just |merely |only )?[\w\s,'-]{3,40}?,? but\b", line, re.I)
            if m:
                out.append(Finding(
                    "warn", "not-x-but-y", '"not X, but Y" construction',
                    line=i, excerpt=m.group(0),
                    fix="say the positive half on its own"))

    # Rule-of-three rhythm.
    threes = re.findall(r"\b[\w'-]+, [\w'-]+,? and [\w'-]+\b", text)
    cap3 = s.get("max_rule_of_three_lists", 2)
    if len(threes) > cap3:
        out.append(Finding(
            "note", "rule-of-three",
            f"{len(threes)} three-item lists (max {cap3}) - a recognisable LLM cadence",
            fix="make one of them two items or four"))

    # Bolded lead-in on every bullet.
    if s.get("forbid_bold_lead_in_every_bullet", True) and len(bullets) >= 3:
        bolded = [b for b in bullets if re.match(r"^\*\*[^*]{2,40}\*\*[:\-–—]", b)]
        if len(bolded) == len(bullets):
            out.append(Finding(
                "warn", "bold-lead-in",
                "every bullet opens with a bolded label",
                fix="that pattern is a strong generated-text signal; drop it"))

    # Runaway sentences. Checked per line, not across the document: a resume's
    # text layer has no paragraph structure, so splitting the whole thing on
    # sentence punctuation just reports the entire document as one sentence.
    cap_len = s.get("max_sentence_len_words", 42)
    for i, line in enumerate(text.splitlines(), 1):
        for sent in re.split(r"(?<=[.!?])\s+", line.strip()):
            n = len(sent.split())
            if n > cap_len:
                out.append(Finding(
                    "note", "long-sentence", f"{n}-word sentence (max {cap_len})",
                    line=i, excerpt=sent[:80], fix="split it"))

    tg = rules.get("typography", {})
    if tg.get("forbid_arrow_glyph", True) and "→" in text:
        out.append(Finding("warn", "arrow", 'the "→" glyph reads as machine-written in prose',
                           fix="write the word"))
    if tg.get("forbid_emoji", True):
        emoji = re.findall(r"[\U0001F300-\U0001FAFF✀-➿]", text)
        if emoji:
            out.append(Finding("block", "emoji", f"{len(emoji)} emoji in an application document"))
    return out


# --- metrics ------------------------------------------------------------------

def check_metrics(text, rules, evidence=None):
    """Flag numbers with nothing behind them.

    A number you cannot defend in an interview is worse than no number, so
    every figure should map to an entry in the evidence file. `evidence` is a
    set of strings known to be backed; anything else gets flagged.
    """
    out = []
    m_rules = rules.get("metrics", {})
    evidence = evidence or set()
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\b(\d+(?:\.\d+)?)\s*(%|x\b|×)", line):
            val, unit = m.group(1), m.group(2)
            token = m.group(0)
            if any(token in e for e in evidence):
                continue
            try:
                num = float(val)
            except ValueError:
                continue
            if m_rules.get("require_provenance", True) and evidence:
                out.append(Finding(
                    "block", "unsourced-metric",
                    f'"{token}" has no entry in the evidence file',
                    line=i, excerpt=line.strip()[:80],
                    fix="add it to profile/evidence.md with how it was measured, or cut it"))
            elif unit == "%" and num in m_rules.get("suspicious_round", []):
                out.append(Finding(
                    "note", "round-metric",
                    f'"{token}" is a suspiciously round figure',
                    line=i,
                    fix="if it is really 47%, say 47% - round numbers read as invented"))
    return out


# --- driver -------------------------------------------------------------------

def lint(text, rules=None, bullets_mode=False, evidence=None):
    rules = rules or load_rules()
    bullets = extract_bullets(text, force_all_lines=bullets_mode)
    findings = (check_phrases(text, rules)
                + check_structure(text, bullets, rules)
                + check_metrics(text, rules, evidence))
    findings.sort(key=lambda f: (-SEVERITY_RANK[f.severity], f.line or 0))
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description="Lint a draft for AI-generated tells.")
    ap.add_argument("file")
    ap.add_argument("--bullets", action="store_true",
                    help="treat every non-empty line as a bullet")
    ap.add_argument("--evidence", help="evidence file; numbers not found in it are blocked")
    ap.add_argument("--max", choices=["note", "warn", "block"], default="warn",
                    help="minimum severity that causes a non-zero exit (default warn)")
    args = ap.parse_args()

    text = pathlib.Path(args.file).read_text(encoding="utf-8")
    evidence = None
    if args.evidence:
        ev = pathlib.Path(args.evidence).read_text(encoding="utf-8")
        evidence = set(re.findall(r"\b\d+(?:\.\d+)?\s*(?:%|x|×)", ev))

    findings = lint(text, bullets_mode=args.bullets, evidence=evidence)
    counts = {"block": 0, "warn": 0, "note": 0}
    for f in findings:
        counts[f.severity] += 1
        print(f)
    print(f"\n{counts['block']} block, {counts['warn']} warn, {counts['note']} note"
          f"   ({pathlib.Path(args.file).name})")

    threshold = SEVERITY_RANK[args.max]
    return 1 if any(SEVERITY_RANK[f.severity] >= threshold for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
