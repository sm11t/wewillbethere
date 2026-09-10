"""Assemble a document from the fact base and a variant preset.

Selection only. This module picks which approved variants appear and in what
order; it never writes prose. If no approved variant covers something a job
asks for, that is reported as a gap rather than papered over with new text.

    python -m engine.build swe-intern --out out/asmit-swe.pdf
    python -m engine.build campus-ta --draft
"""

from __future__ import annotations

import argparse
import pathlib
import sys

import yaml

from . import ai_lint, profile as profile_mod, render

VARIANTS_PATH = pathlib.Path(__file__).parents[1] / "profile" / "variants.yaml"
OUT_DIR = pathlib.Path(__file__).parents[1] / "out"


def load_presets(path=VARIANTS_PATH) -> dict:
    return yaml.safe_load(pathlib.Path(path).read_text(encoding="utf-8"))


def pick_variants(entry, prefer_flavors, draft: bool, limit: int = 2):
    """Choose up to `limit` phrasings of distinct facts for one entry.

    One variant per fact - alternate phrasings of the same fact are mutually
    exclusive, or the page says the same thing twice.
    """
    usable = [v for v in entry.variants
              if not v.blocked_by and (draft or v.approved)]
    by_fact: dict[str, list] = {}
    for v in usable:
        by_fact.setdefault(v.fact_id, []).append(v)

    def rank(v):
        flavor_rank = (prefer_flavors.index(v.flavor)
                       if v.flavor in prefer_flavors else len(prefer_flavors))
        length_rank = {"long": 0, "medium": 1, "short": 2}.get(v.length, 1)
        return (flavor_rank, length_rank)

    chosen = []
    for fact_id in by_fact:
        chosen.append(sorted(by_fact[fact_id], key=rank)[0])
    chosen.sort(key=rank)
    return chosen[:limit]


def build_document(p: profile_mod.Profile, preset_name: str, draft: bool = False) -> tuple[dict, list[str]]:
    cfg = load_presets()
    preset = cfg["presets"][preset_name]
    categories = cfg["skill_categories"]
    prefer = preset.get("prefer_flavors", [])
    bullet_cap = preset.get("bullets_per_entry", 2)
    notes: list[str] = []

    b = p.basics
    contact = [b["location"]["render"]]
    if b.get("phone"):
        contact.append(b["phone"])
    else:
        notes.append("No phone number in the profile - most portals require one.")
    contact.append(b["email"])
    # Display text stays a flat list of strings so ATS expectations and the
    # extraction baseline keep working unchanged; the URLs ride alongside in a
    # lookup the emitter uses to wrap each item in an anchor. Before this, the
    # header rendered as plain text and none of the links opened.
    contact_links = {link["render_as"]: link["url"]
                     for link in b.get("links", []) if link.get("url")}
    for link in b.get("links", []):
        contact.append(link["render_as"])
    if "github" not in {l.get("label") for l in b.get("links", [])}:
        notes.append("No GitHub link - for SWE roles this is close to required.")

    doc = {"name": b["name"], "contact": contact,
           "contact_links": contact_links, "sections": [],
           "title": f"{b['name']} - Resume"}

    # Education
    edu_entries = []
    for e in p.education:
        edu_entries.append({
            "left": e["institution"], "right": e["location"],
            "left2": e["degree"], "right2": e["grad_display"], "bullets": [],
        })
    doc["sections"].append({"heading": "Education", "entries": edu_entries})

    # Experience / Projects / Leadership
    def section_for(kind_key: str, heading: str):
        entries = []
        for eid in preset["entries"].get(kind_key, []):
            entry = p.entries.get(eid)
            if entry is None:
                notes.append(f"Preset references unknown entry '{eid}'.")
                continue
            picked = pick_variants(entry, prefer, draft, limit=bullet_cap)
            if not picked:
                why = "no approved variants" if not draft else "no usable variants"
                notes.append(f"'{eid}' contributed nothing ({why}).")
                continue
            if entry.kind == "project":
                entries.append({
                    "left": entry.name, "right": entry.dates or "",
                    "left2": entry.url, "right2": entry.stack,
                    # Both the title and the visible URL become links. The URL
                    # stays visible on purpose: a link annotation is invisible
                    # to a text extractor, so a printed or parsed copy would
                    # otherwise lose the address entirely.
                    "href": entry.href, "href2": entry.href,
                    "bullets": [v.text for v in picked],
                })
            else:
                entries.append({
                    "left": entry.role, "right": entry.dates or "",
                    "left2": entry.org, "right2": entry.location,
                    "bullets": [v.text for v in picked],
                })
        return {"heading": heading, "entries": entries} if entries else None

    order = {"education": None,
             "experience": ("experience", "Experience"),
             "projects": ("projects", "Projects"),
             "leadership": ("leadership", "Leadership & Teaching"),
             "skills": None}

    for sec_name in preset["sections"]:
        if sec_name in ("education", "skills"):
            continue
        spec = order.get(sec_name)
        if spec:
            s = section_for(*spec)
            if s:
                doc["sections"].append(s)

    # Leadership is appended when the preset lists entries for it but did not
    # name it in `sections`.
    if "leadership" not in preset["sections"] and preset["entries"].get("leadership"):
        s = section_for("leadership", "Leadership & Teaching")
        if s:
            doc["sections"].append(s)

    # Skills, in the preset's category order. Within a category, anything with
    # real evidence comes before anything still marked `ask`, so when a line is
    # trimmed to fit it is the unvouched keyword that falls off the end rather
    # than a tool he can actually talk about.
    eligible = {s["name"]: s for s in p.skills()}
    skills = []
    for cat in preset.get("skill_order", list(categories)):
        # Some skills must not print for a given posting even though they are
        # in the pool. Sorting `ask: true` last is not enough: last still means
        # printed when the line has room, and on a posting that asks for RAG by
        # name, an unvouched "RAG" is exactly the keyword that buys an
        # interview opening on retrieval architecture.
        excluded = set(preset.get("skill_exclude", []))
        members = [n for n in categories.get(cat, [])
                   if n in eligible and n not in excluded]
        # Evidenced before unvouched, then the posting's own vocabulary first
        # within that. A skills line is skimmed, not read, so position is the
        # only thing that decides whether a term registers.
        lead = preset.get("skill_lead", [])
        members.sort(key=lambda n: (bool(eligible[n].get("ask")),
                                    lead.index(n) if n in lead else len(lead)))
        if members:
            skills.append([cat, ", ".join(members)])
    doc["skills"] = skills

    unconfirmed = p.unconfirmed_skills()
    printed = {n for _, v in skills for n in v.split(", ")}
    live = [n for n in unconfirmed if n in printed]
    if live:
        notes.append("ON THE PAGE BUT UNCONFIRMED - be ready to be interviewed on "
                     "each, or cut it: " + ", ".join(live) + ".")
    dropped = p.unevidenced_skills()
    if dropped:
        notes.append(f"Skills omitted for lack of evidence: {', '.join(dropped)}.")

    return doc, notes


def main() -> int:
    ap = argparse.ArgumentParser(description="Build a resume from the fact base.")
    ap.add_argument("preset")
    ap.add_argument("--out")
    ap.add_argument("--draft", action="store_true",
                    help="include variants Asmit has not approved yet")
    args = ap.parse_args()

    p = profile_mod.load()
    doc, notes = build_document(p, args.preset, draft=args.draft)

    out = pathlib.Path(args.out) if args.out else OUT_DIR / f"asmit-{args.preset}.pdf"
    if args.draft:
        doc["title"] = f"{doc['name']} - Resume (DRAFT, unapproved)"

    try:
        report = render.render(doc, out, max_pages=1)
    except render.RenderError as exc:
        print(f"RENDER FAILED\n  {exc}")
        return 2

    print(f"Wrote {out}")
    print(f"  fit: {report['fit']['size']} / leading {report['fit']['leading']} "
          f"after {len(report['fit']['attempts'])} compile(s)")
    print(f"  ATS: {report['verdict']}  token recall {report['token_recall']:.3f}  "
          f"char integrity {report['char_integrity']:.3f}  pages {report['pages']}")
    for pr in report["problems"]:
        print(f"    FATAL: {pr}")
    for w in report["warnings"]:
        print(f"    WARN:  {w}")

    # Lint the prose that actually landed on the page.
    bullets = [b for s in doc["sections"] for e in s["entries"] for b in e["bullets"]]
    findings = ai_lint.lint("\n".join(f"- {b}" for b in bullets))
    counts = {"block": 0, "warn": 0, "note": 0}
    for f in findings:
        counts[f.severity] += 1
    print(f"  voice lint: {counts['block']} block, {counts['warn']} warn, "
          f"{counts['note']} note")
    for f in findings:
        if f.severity in ("block", "warn"):
            print(f"    {f}")

    if notes:
        print("\nNotes:")
        for n in notes:
            print(f"  - {n}")

    if args.draft:
        print("\nDRAFT: contains variants Asmit has not approved. Do not send.")
    return 0 if report["verdict"] != "FAIL" and counts["block"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
