"""Export the fact base as career-ops' cv.md.

The two tools in this project share one source of truth. career-ops reads a
markdown CV to score postings and to compute skill gaps; rather than keeping a
second copy of Asmit's history that could drift from `profile.yaml`, this
regenerates it on demand.

Everything the resume gate enforces still applies: blocked metrics stay out,
unapproved phrasings are marked, and skills carry their evidence state.

    python -m engine.export_cv_md
"""

from __future__ import annotations

import argparse
import pathlib
import sys

from . import build, profile as profile_mod

DEFAULT_OUT = (pathlib.Path(__file__).parents[1]
               / "tools" / "career-ops" / "cv.md")
NL = chr(10)


def to_markdown(prof: profile_mod.Profile, preset: str = "full") -> str:
    doc, _ = build.build_document(prof, preset, draft=True)
    basics = prof.basics
    L: list[str] = [f"# CV -- {basics['name']}", ""]

    L.append(f"**Location:** {basics['location']['render']}  ")
    if basics.get("phone"):
        L.append(f"**Phone:** {basics['phone']}  ")
    L.append(f"**Email:** {basics['email']}  ")
    for link in basics.get("links", []):
        L.append(f"**{link['label'].title()}:** {link['render_as']}  ")
    L.append("")

    for section in doc["sections"]:
        heading = section["heading"]
        if heading == "Education":
            L += ["## Education", ""]
            for e in section["entries"]:
                L.append(f"- {e['left2']}, {e['left']} ({e['right2']}) -- {e['right']}")
            L.append("")
            continue

        L += [f"## {'Work Experience' if heading == 'Experience' else heading}", ""]
        for e in section["entries"]:
            if heading == "Projects":
                L.append(f"### {e['left']}")
                meta = " -- ".join(x for x in (e.get("left2"), e.get("right2")) if x)
                if meta:
                    L.append("")
                    L.append(f"*{meta}*")
            else:
                L.append(f"### {e['left2']} -- {e['right2']}")
                L += ["", f"**{e['left']}**", e["right"]]
            L.append("")
            for b in e["bullets"]:
                L.append(f"- {b}")
            L.append("")

    # Unconfirmed skills are deliberately withheld from this file.
    #
    # career-ops scores postings against cv.md and computes skill gaps from it.
    # Leaving an `ask: true` skill in would make it rate a posting as a match on
    # a tool Asmit has not confirmed using - which is exactly backwards: it
    # would send him toward the jobs he is least able to defend. The resume can
    # still carry them if he vouches for them; the matching engine should not
    # assume them.
    unconfirmed = set(prof.unconfirmed_skills())
    L += ["## Skills", ""]
    for label, values in doc["skills"]:
        kept = [v for v in values.split(", ") if v not in unconfirmed]
        if kept:
            L.append(f"**{label}:** {', '.join(kept)}")
            L.append("")

    # The names are deliberately not written here, not even in a comment:
    # jd-skill-gap reads the whole file as prose, so a commented-out list still
    # counted as evidence and reported the skills as `existing`. The export
    # prints them to the console instead.
    if unconfirmed:
        L += [f"<!-- {len(unconfirmed)} unconfirmed skills withheld from this "
              f"file so job matching is not scored on them. See "
              f"profile/profile.yaml. -->", ""]

    return NL.join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="Export the fact base as cv.md.")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--preset", default="full")
    args = ap.parse_args()

    prof = profile_mod.load()
    text = to_markdown(prof, args.preset)
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")

    print(f"Wrote {out} ({len(text.splitlines())} lines) from profile.yaml.")
    withheld = sorted(prof.unconfirmed_skills())
    if withheld:
        print(f"Withheld {len(withheld)} unconfirmed skills so postings are not "
              f"scored on them:")
        print("  " + ", ".join(withheld))
    print("Regenerate after any profile change - career-ops scores postings "
          "against this file.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
