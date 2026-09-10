"""One-line summary per resume variant: does it pass, and does it look full?

    python -m engine.status
"""

from __future__ import annotations

import sys

import json
import pathlib

from . import ats_check, build, emit_rlol, profile as profile_mod, render

# Only presets with a built artifact on disk. `full` is the one that ships;
# the role-specific presets remain in variants.yaml as starting points.
PRESETS = ["full"]


def main() -> int:
    p = profile_mod.load()
    presets = sys.argv[1:] or PRESETS

    print(f"{'preset':<14}{'verdict':<8}{'token':>7}{'chars':>7}{'pages':>7}{'fill':>7}   issues")
    print("-" * 96)
    worst = 0
    for name in presets:
        doc, notes = build.build_document(p, name, draft=True)
        path = f"out/.build/asmit-{name}.pdf"
        # Prefer the expectation recorded at publish time: the shipped document
        # has its skill lines trimmed to one line each, so re-deriving them
        # here would report skills as missing that were never meant to be there.
        recorded = pathlib.Path(f"out/.build/asmit-{name}.expect.json")
        try:
            expected = (json.loads(recorded.read_text(encoding="utf-8"))
                        if recorded.exists()
                        else emit_rlol.expected_strings(doc))
            r = ats_check.check(path, expected, max_pages=1)
        except Exception as exc:
            print(f"{name:<14}ERROR    {exc}")
            worst = 2
            continue
        issues = []
        if r["fill_ratio"] < 0.75:
            issues.append("thin page")
        if r["problems"]:
            issues.append(f"{len(r['problems'])} fatal")
        if any("split some lines" in w for w in r["warnings"]):
            issues.append("pdfminer splits phrases (keywords intact)")
        print(f"{name:<14}{r['verdict']:<8}{r['token_recall']:>7.3f}"
              f"{r['char_integrity']:>7.3f}{r['pages']:>7}{r['fill_ratio']:>7.0%}"
              f"   {', '.join(issues) if issues else 'none'}")
        worst = max(worst, {"PASS": 0, "WARN": 1, "FAIL": 2}[r["verdict"]])

    print()
    print(profile_mod.status_report(p))
    return worst if worst == 2 else 0


if __name__ == "__main__":
    sys.exit(main())
