"""Assemble one application folder: a resume and a cover letter, nothing else.

    python -m engine.package mckesson-swe-2027 \
        --letter letters/draft-mckesson-swe-2027.py \
        --slug mckesson-swe-intern-summer-2027

Produces exactly:

    applications/<slug>/resume.pdf
    applications/<slug>/cover-letter.pdf

Everything the build needed to get there - HTML exports, extraction baselines,
previews, the plain-text letter - stays in out/.build/. The application folder
holds only the two files that get uploaded, so there is never a question about
which PDF is the real one at the moment of applying.
"""

from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).parents[1]
BUILD = ROOT / "out" / ".build"
APPS = ROOT / "applications"


def _run(args: list[str]) -> None:
    result = subprocess.run([sys.executable, "-m", *args], cwd=ROOT,
                            capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if "FontBBox" not in line:
            print("   " + line)
    if result.returncode != 0:
        print(result.stderr[-1500:])
        raise SystemExit(f"{args[0]} failed")


def main() -> int:
    ap = argparse.ArgumentParser(description="Package one application.")
    ap.add_argument("preset", help="resume preset from profile/variants.yaml")
    ap.add_argument("--letter",
                    help="path to the letter draft. Omit for the applications "
                         "that take a resume only - some postings ask for no "
                         "letter, and a folder holding exactly what gets "
                         "uploaded should not hold one they did not ask for.")
    ap.add_argument("--slug", help="folder name; defaults to the preset name")
    ap.add_argument("--draft", action="store_true",
                    help="allow phrasings Asmit has not approved yet")
    args = ap.parse_args()

    slug = args.slug or args.preset
    draft = ["--draft"] if args.draft else []

    print(f"resume  [{args.preset}]")
    _run(["engine.publish", args.preset, *draft])
    if args.letter:
        print(f"letter  [{pathlib.Path(args.letter).stem}]")
        _run(["engine.publish_letter", args.letter])

    dest = APPS / slug
    dest.mkdir(parents=True, exist_ok=True)
    for existing in dest.iterdir():
        existing.unlink()

    shutil.copy2(BUILD / f"asmit-{args.preset}.pdf", dest / "resume.pdf")
    if args.letter:
        shutil.copy2(BUILD / f"{pathlib.Path(args.letter).stem}.pdf",
                     dest / "cover-letter.pdf")

    print(f"\napplications/{slug}/")
    for f in sorted(dest.iterdir()):
        print(f"   {f.name:18} {f.stat().st_size // 1024} KB")
    if args.draft:
        print("\nDRAFT: contains phrasings you have not approved. Do not send.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
