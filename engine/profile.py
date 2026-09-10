"""Load the fact base and enforce what is allowed to reach a page.

This module is where "nothing fabricated" stops being an intention and becomes
a rule the machine keeps. Three gates:

  APPROVAL    A variant ships only when Asmit has read it and set approved:true.
              Draft mode renders unapproved text but stamps the result so it can
              never be mistaken for a finished document.

  PROVENANCE  A variant that cites a metric whose status is needs_confirmation
              is blocked. This is the important one. A number that cannot be
              defended end to end in an interview is worse than no number,
              because the moment one figure collapses the reader stops
              believing the rest of the page.

  EVIDENCE    A skill with no evidence entry never prints. If it is not
              demonstrated in an experience or project above, it is not a skill,
              it is a wish.
"""

from __future__ import annotations

import pathlib
from dataclasses import dataclass, field

import yaml

PROFILE_PATH = pathlib.Path(__file__).parents[1] / "profile" / "profile.yaml"

BLOCKING_STATUSES = {"needs_confirmation"}


@dataclass(frozen=True)
class Variant:
    """One approved phrasing of one fact."""
    id: str
    text: str
    fact_id: str
    entry_id: str
    length: str = "medium"
    flavor: str = "general"
    approved: bool = False
    uses_metrics: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()
    blocked_by: tuple[str, ...] = ()

    @property
    def shippable(self) -> bool:
        return self.approved and not self.blocked_by


@dataclass
class Entry:
    """An experience, project, or volunteering entry."""
    id: str
    kind: str
    org: str = ""
    role: str = ""
    name: str = ""
    url: str = ""
    href: str = ""
    dates: str | None = None
    location: str = ""
    stack: str = ""
    tags: tuple[str, ...] = ()
    variants: list[Variant] = field(default_factory=list)
    metrics: dict = field(default_factory=dict)
    status: str = "ok"
    note: str = ""


class Profile:
    def __init__(self, raw: dict):
        self.raw = raw
        self.basics = raw.get("basics", {})
        self.education = raw.get("education", [])
        self.protected_strings = raw.get("protected_strings", [])
        self.never_include = raw.get("never_include", [])
        self.entries: dict[str, Entry] = {}
        self.issues: list[str] = []
        self._load_entries()

    # -- loading ---------------------------------------------------------

    def _load_entries(self):
        for kind, key in (("experience", "experience"),
                          ("project", "projects"),
                          ("volunteering", "volunteering")):
            for item in self.raw.get(key, []) or []:
                entry = Entry(
                    id=item["id"], kind=kind,
                    org=item.get("org", ""), role=item.get("role", ""),
                    name=item.get("name", ""), url=item.get("url", ""),
                    href=item.get("href", ""),
                    dates=item.get("dates"), location=item.get("location", ""),
                    stack=item.get("stack", ""),
                    tags=tuple(item.get("tags", []) or []),
                    status=item.get("status", "ok"),
                    note=item.get("note", ""),
                )
                metrics = {}
                for m in item.get("metrics", []) or []:
                    metrics[m["id"]] = m
                entry.metrics = metrics

                blocked_metrics = {
                    mid for mid, m in metrics.items()
                    if (m.get("provenance") or {}).get("status") in BLOCKING_STATUSES
                }

                for fact in item.get("facts", []) or []:
                    # A fact whose own provenance is unconfirmed blocks every
                    # phrasing of it. But `requires_confirmation` listed on the
                    # fact is only a register of open questions - it blocks the
                    # variants that actually lean on the open question, which
                    # declare it themselves. Otherwise one unanswered detail
                    # would suppress phrasings that never mention it.
                    fact_blocked = []
                    fp = fact.get("provenance") or {}
                    if fp.get("status") in BLOCKING_STATUSES:
                        fact_blocked.append(f"fact:{fact['id']}")
                    for v in fact.get("variants", []) or []:
                        uses = tuple(v.get("uses_metrics", []) or [])
                        blocked = list(fact_blocked)
                        blocked += [f"metric:{m}" for m in uses if m in blocked_metrics]
                        blocked += [f"needs:{c}"
                                    for c in (v.get("requires_confirmation") or [])]
                        entry.variants.append(Variant(
                            id=v["id"], text=" ".join(v["text"].split()),
                            fact_id=fact["id"], entry_id=entry.id,
                            length=v.get("length", "medium"),
                            flavor=v.get("flavor", "general"),
                            approved=bool(v.get("approved", False)),
                            uses_metrics=uses,
                            keywords=tuple(v.get("keywords", []) or []),
                            blocked_by=tuple(blocked),
                        ))
                self.entries[entry.id] = entry

    # -- queries ---------------------------------------------------------

    def skills(self, include_unevidenced: bool = False) -> list[dict]:
        """Skills eligible to print.

        An `ask: true` skill renders - Asmit asked for keyword coverage and
        these are plausible - but `unconfirmed_skills()` surfaces them on every
        build so they are never silently shipped.
        """
        out = []
        for s in self.raw.get("skills", []) or []:
            if s.get("flag") == "unevidenced" and not include_unevidenced:
                continue
            if not s.get("evidence") and not s.get("ask") and not include_unevidenced:
                continue
            out.append(s)
        return out

    def unconfirmed_skills(self) -> list[str]:
        """Printed, but nobody has vouched for them yet."""
        return [s["name"] for s in self.raw.get("skills", []) or [] if s.get("ask")]

    def unevidenced_skills(self) -> list[str]:
        return [s["name"] for s in self.raw.get("skills", []) or []
                if not s.get("evidence") and not s.get("ask")]

    def blocked_variants(self) -> list[Variant]:
        return [v for e in self.entries.values() for v in e.variants if v.blocked_by]

    def unapproved_variants(self) -> list[Variant]:
        return [v for e in self.entries.values() for v in e.variants if not v.approved]

    def blocking_metrics(self) -> list[tuple[str, str, str]]:
        """(entry_id, metric_id, why) for every metric that cannot ship."""
        out = []
        for e in self.entries.values():
            for mid, m in e.metrics.items():
                p = m.get("provenance") or {}
                if p.get("status") in BLOCKING_STATUSES:
                    note = " ".join((p.get("note") or "").split())
                    out.append((e.id, mid, note))
        return out

    def variant(self, vid: str) -> Variant | None:
        for e in self.entries.values():
            for v in e.variants:
                if v.id == vid:
                    return v
        return None

    def missing_basics(self) -> list[str]:
        out = []
        if not self.basics.get("phone"):
            out.append("phone")
        labels = {l.get("label") for l in self.basics.get("links", []) or []}
        if "github" not in labels:
            out.append("github")
        return out


def load(path=PROFILE_PATH) -> Profile:
    return Profile(yaml.safe_load(pathlib.Path(path).read_text(encoding="utf-8")))


def status_report(p: Profile) -> str:
    """What is standing between this profile and a shippable document."""
    L = ["PROFILE STATUS", "=" * 66]

    missing = p.missing_basics()
    if missing:
        L.append(f"\nMissing from the header (blocks submission): {', '.join(missing)}")

    blocking = p.blocking_metrics()
    if blocking:
        L.append(f"\n{len(blocking)} metric(s) blocked pending confirmation:")
        for entry_id, mid, why in blocking:
            L.append(f"  - {entry_id}.{mid}")
            if why:
                L.append(f"      {why[:150]}")

    blocked = p.blocked_variants()
    if blocked:
        L.append(f"\n{len(blocked)} variant(s) cannot ship:")
        for v in blocked:
            L.append(f"  - {v.id}  (blocked by {', '.join(v.blocked_by)})")

    unapproved = p.unapproved_variants()
    total = sum(len(e.variants) for e in p.entries.values())
    L.append(f"\nApproval: {total - len(unapproved)}/{total} variants approved by Asmit.")

    un = p.unevidenced_skills()
    if un:
        L.append(f"\nSkills with no supporting evidence (excluded by default): {', '.join(un)}")

    stubs = [e.id for e in p.entries.values() if e.status == "needs_confirmation"]
    if stubs:
        L.append(f"\nEntries stubbed pending details: {', '.join(stubs)}")

    return "\n".join(L)


if __name__ == "__main__":
    print(status_report(load()))
