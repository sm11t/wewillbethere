"""Mark phrasings as approved once Asmit has read them.

Approval is the gate that makes everything else honest: the renderer will not
print a sentence he has not signed off on. This just makes signing off cheap.

    python -m engine.approve --list              # show what is waiting
    python -m engine.approve wd.locator.full     # approve specific phrasings
    python -m engine.approve --all               # approve everything unblocked

Edits profile.yaml in place, line by line, so comments and formatting survive.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

from . import profile as profile_mod

PROFILE_PATH = profile_mod.PROFILE_PATH
ID_RX = re.compile(r"^\s*-?\s*(?:\{\s*)?id:\s*([\w.\-]+)")
APPROVED_RX = re.compile(r"(approved:\s*)false")


def set_approved(ids: set[str], path=PROFILE_PATH) -> list[str]:
    """Flip `approved: false` to true for the named variants. Returns what changed."""
    lines = pathlib.Path(path).read_text(encoding="utf-8").splitlines(keepends=True)
    current: str | None = None
    changed: list[str] = []

    for i, line in enumerate(lines):
        m = ID_RX.match(line)
        if m:
            current = m.group(1)
        if current in ids and APPROVED_RX.search(line):
            lines[i] = APPROVED_RX.sub(r"\1true", line)
            changed.append(current)
            current = None          # one approval per variant block

    if changed:
        pathlib.Path(path).write_text("".join(lines), encoding="utf-8")
    return changed


def main() -> int:
    ap = argparse.ArgumentParser(description="Approve phrasings for use.")
    ap.add_argument("ids", nargs="*", help="variant ids to approve")
    ap.add_argument("--all", action="store_true",
                    help="approve every phrasing that is not blocked")
    ap.add_argument("--list", action="store_true",
                    help="print every unapproved phrasing with its text")
    args = ap.parse_args()

    p = profile_mod.load()

    if args.list or (not args.ids and not args.all):
        pending = [v for v in p.unapproved_variants() if not v.blocked_by]
        blocked = [v for v in p.unapproved_variants() if v.blocked_by]
        print(f"{len(pending)} phrasing(s) waiting for you. Read each one; if it "
              f"does not sound like you said it, edit the text in profile.yaml "
              f"before approving.\n")
        for v in pending:
            print(f"  {v.id}")
            print(f"      {v.text}\n")
        if blocked:
            print(f"{len(blocked)} phrasing(s) cannot be approved yet:")
            for v in blocked:
                print(f"  {v.id}  <- {', '.join(v.blocked_by)}")
        print("\nApprove with:  python -m engine.approve <id> [<id> ...]")
        print("Or all at once: python -m engine.approve --all")
        return 0

    if args.all:
        targets = {v.id for v in p.unapproved_variants() if not v.blocked_by}
    else:
        targets = set(args.ids)
        unknown = {i for i in targets if p.variant(i) is None}
        if unknown:
            print(f"Unknown variant id(s): {', '.join(sorted(unknown))}")
            return 1
        blocked = {i for i in targets if p.variant(i).blocked_by}
        if blocked:
            for i in sorted(blocked):
                print(f"{i} is blocked by {', '.join(p.variant(i).blocked_by)} "
                      f"and cannot be approved yet.")
            return 1

    changed = set_approved(targets)
    print(f"Approved {len(changed)}: {', '.join(sorted(changed))}"
          if changed else "Nothing to approve.")

    after = profile_mod.load()
    total = sum(len(e.variants) for e in after.entries.values())
    print(f"Approval now {total - len(after.unapproved_variants())}/{total}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
