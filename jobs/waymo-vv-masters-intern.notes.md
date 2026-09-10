# Waymo — SWE Intern, Fault Protection & Remote Assistance V&V (master's req)

## This is the req the other Waymo posting should have been

Same team, same company, and it inverts every problem the C++ HIL posting had.

| | `waymo-systems-2027` (HIL) | **this one** |
|---|---|---|
| Degree tier | "pursuing a **Bachelor's**", $60/hr | **"currently enrolled in a MS program"**, $70/hr |
| Required language | **C++** — `ask: true`, no project | **Python and SQL** — evidenced 4x and 3x |
| Testing fundamentals | hard requirement, **unevidenced** | not asked for |
| Unconfirmed skills on the page | **C++, Pytest** | **none** |

**Both hard technical requirements are evidenced.** Their entire "You have"
list is: enrolled in an MS programme (he is), enthusiasm for complex systems
(soft), and *"experience with data analysis/modeling using Python and SQL"* —
Python appears against Lead Engine, the WatchDNA pipeline, MyYogaTeacher and
Delhi; SQL against the voice-to-SQL work, Torii's ledger and Lead Engine.

**This is the first preset in the file where nothing on the page is
unconfirmed.** No `ask: true` skill renders. C++ and Pytest were on the HIL
preset only because that application was meaningless without them; nothing here
asks for either, so they come off.

**If only one Waymo slot is spent, spend it here.** The posting says to apply
to your top 3 roles individually — this one and the HIL one are not
interchangeable, and this is the one he actually qualifies for.

## Two of their four "You will" bullets are one project

> *Build automated pipelines using **Python and SQL** to update, version, and
> validate test coverage…*
> *Create **dashboards to monitor, visualize, and analyze** fleet-wide
> autonomous vehicle **fault rates**…*

Lead Engine is a Python and SQL pipeline with a live dashboard **where a failed
scout surfaces the moment it fails.** That is a fault-rate monitor over a
running pipeline, in the same shape if not the same domain. It leads Projects,
and it is the whole second paragraph of the letter.

### A fact was recovered to make this work

The dashboard was one clause at the end of `le.pipeline`'s canonical and had
**never reached a bullet** — every preset until now said nothing about it. It
is split out as its own fact, `le.dashboard`, sourced to his own site
(`site_2026`), which describes the node view as a live pipeline graph where
failed scouts turn red immediately.

This is the profile understating again, exactly as CLAUDE.md warns: the
observability work was there the whole time and nobody wrote it down. Every
future posting that asks for monitoring, visualisation or dashboards now has a
bullet to point at.

**One knock-on:** `prefer_flavors` puts `general` ahead of `ml` on this preset.
Both orders pick the dashboard variant, but with `ml` first the pipeline bullet
reverted to the old cautious "public listing and county records" phrasing, and
the standing instruction of 2026-09-05 is to **name the scout sources.**

## The rest

| Their line | Him |
|---|---|
| "design and implement metrics, test plans, and simulated scenarios ... **after a fault occurs**" | The honest adjacency is instrumentation, not AV testing: Torii's ledger records every call **and every reason one was blocked**, and Lead Engine surfaces failed scouts live. He has built systems that make failure visible; he has not written test plans. |
| "Enthusiasm to understand a complex system and its various components" | Soft, and the personal paragraph is the answer - "I think about problems in systems, and I approach them that way." |
| **Familiarity with AV technology / systems engineering** (preferred) | **Gap.** None. Lynti is the honest connection to the mission and it is used as motivation only. |
| Ambiguous problems, fast pace (preferred) | Soft. |

## Lynti

Same treatment as the HIL letter, at his instruction: exactly what the one
truncated LinkedIn line records — a transportation app, React Native, to
digitize ride booking — and nothing more. No scale, no users, no outcome, no
dates. Placed as **motivation**, ending on the admission that the hard half is
the half he did not build.

It still needs finishing. See `checklists/recover.md`: what did *"digitize ride
booking and ..."* continue into, is it live, is it still running.

## Built

`applications/waymo-vv-masters-intern/` — preset `waymo-vv-masters`, letter
`letters/draft-waymo-vv-2027.py`. Resume ATS PASS, one page, 92% fill, **zero
unconfirmed skills.** Letter one page, 402 words, zero lint blocks.
