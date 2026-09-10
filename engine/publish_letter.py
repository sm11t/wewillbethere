"""Build a cover letter: push to resume.lol, export a PDF, verify, lint.

    python -m engine.publish_letter letters/draft-google-swe-intern.py

Emits three artifacts, because portals want different things:
  .pdf   the letterhead version, matching the resume
  .txt   ASCII, for a paste box
  .html  what was printed
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import sys

from . import ai_lint, ats_check, emit_letter, publish, render
from . import rlol_client as rlol

ROOT = pathlib.Path(__file__).parents[1]
OUT = ROOT / "out" / ".build"
REGISTRY = ROOT / "out" / "rlol-resumes.json"


def load_letter(path: str) -> dict:
    spec = importlib.util.spec_from_file_location("letter_draft", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.LETTER


def main() -> int:
    ap = argparse.ArgumentParser(description="Publish a cover letter.")
    ap.add_argument("draft", help="path to a draft .py defining LETTER")
    ap.add_argument("--max-pages", type=int, default=1)
    args = ap.parse_args()

    letter = load_letter(args.draft)
    stem = pathlib.Path(args.draft).stem
    key = f"letter:{stem}"

    markdown = emit_letter.to_markdown(letter)

    reg = json.loads(REGISTRY.read_text(encoding="utf-8")) if REGISTRY.exists() else {}
    entry = reg.get(key)
    if entry:
        current = rlol.get_resume(entry["id"])
        rlol.update_resume(entry["id"], markdown=markdown,
                           css=emit_letter.css(1.0), meta_css=emit_letter.meta_css(),
                           expected_updated_at=current.get("updated_at"))
        resume_id = entry["id"]
    else:
        created = rlol.create_resume(f"Cover letter - {stem}", markdown=markdown,
                                     css=emit_letter.css(1.0),
                                     meta_css=emit_letter.meta_css())
        resume_id = created.get("id") or created.get("resume_id")
        reg[key] = {"id": resume_id, "name": f"Cover letter - {stem}"}
        REGISTRY.write_text(json.dumps(reg, indent=2), encoding="utf-8")

    html = rlol.get_resume_html(resume_id)

    chosen = None
    for scale, margin, spacing in emit_letter.LADDER:
        styled = publish._printable_html(html, emit_letter.css(scale, spacing),
                                         emit_letter.meta_css(margin))
        pdf_path = publish._print_html(styled, stem)
        pages, chars = publish._measure(pdf_path)
        if chars < 200:
            pdf_path = publish._print_html(styled, stem, budget_ms=45000)
            pages, chars = publish._measure(pdf_path)
        if pages <= args.max_pages:
            chosen = (scale, margin, spacing)
            break
    if chosen is None:
        raise SystemExit("Letter does not fit. Cut a sentence rather than shrink it.")

    render.set_metadata(pdf_path, title=f"{letter['name']} - Cover Letter",
                        author=letter["name"])

    txt_path = OUT / f"{stem}.txt"
    txt_path.write_text(emit_letter.plain_text(letter), encoding="utf-8")

    print(f"resume.lol id: {resume_id}")
    print(f"  fit: scale {chosen[0]}, margin {chosen[1]}in, spacing {chosen[2]}")
    print(f"  {pdf_path.name} ({pdf_path.stat().st_size // 1024} KB), {txt_path.name}")

    report = ats_check.check(pdf_path, emit_letter.expected_strings(letter),
                             max_pages=args.max_pages, check_fill=False)
    print(f"  text: {report['verdict']}  token recall {report['token_recall']:.3f}  "
          f"pages {report['pages']}  fill {report['fill_ratio']:.0%}")
    for p in report["problems"]:
        print(f"    FATAL: {p}")

    body = emit_letter.plain_text(letter)
    findings = ai_lint.lint(body)
    counts = {"block": 0, "warn": 0, "note": 0}
    for f in findings:
        counts[f.severity] += 1
    print(f"  words: {len(body.split())}")
    print(f"  voice lint: {counts['block']} block, {counts['warn']} warn, "
          f"{counts['note']} note")
    for f in findings:
        if f.severity in ("block", "warn"):
            print(f"    {f}")
    return 0 if report["verdict"] != "FAIL" and counts["block"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
