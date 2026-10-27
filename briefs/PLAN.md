# Plan: help and exemplars for every brief

Status: planned, not built (27 Oct 2026). This file is for teachers and maintainers.

## Why

The small Open projects on the tutorials site already have hints, "Show one way" and a teacher-only example. These
briefs are longer, more open and assessed, so students are more likely to get stuck, yet they have none of that help.
This plan gives every brief (A, B, C and any brief added later) the same help. Because the briefs are assessed, each
kind of help comes with a rule about who can see it.

## What every brief gets

| Part | Who sees it | What it is |
|---|---|---|
| **Benchmarks** | Students | Two finished apps at the expected level that work quite differently, shown as screenshots (short clips later). Each shows the output only, never the code, with the caption "one way it could look". Two different apps show the standard without giving one answer to copy. |
| **Hints for each step** | Students | 1 to 3 hints under each "What you'll do" step, from vague to specific. A hint is a general move ("keep your numbers together at the top"), never the finished answer. Folded away so students choose to open them. |
| **Show one way** | Students, recorded | One small piece of code for a step where seeing it really helps, on a separate help page. Students list every piece they used in a "Help I used" row in their hand-in, so the teacher can see it when marking. |
| **Teacher exemplar** | Teachers only | A complete project: the app, the model file (B and C), a filled-in testing record, a reflection, marking points against "Check your app", and the usual mistakes with a question to ask for each. Kept private, never in this public repo. |

## For each brief

- **A. Rules:** two contrasting benchmarks, for example a text app and a colour or sound app. Exemplar: one rules
  app with its testing table, including the edge cases (exactly on a threshold, empty input, something unexpected).
- **B. Trained:** two benchmarks in different modes, for example a pictures app and a poses app. Exemplar: model
  file, app, a testing record with the "try to fool it" results, the cut-off choice and why, and the rule-versus-model
  point.
- **C. Combined:** two benchmarks where the model's answer feeds a rule in different ways. Exemplar: the full app with
  notes on which part is the model and which part is rules, and why that split.

## Where things go

- Benchmarks: `briefs/benchmarks/<brief>-1.png` and `-2.png`, linked from the brief.
- Hints: inside each brief, using `<details>` blocks so they stay folded away.
- Show one way: `briefs/help/<brief>.md`, plus a "Help I used" row added to "What to hand in".
- Exemplars: a private place each school chooses (a private repo or the school's learning platform). This repo only
  says they exist.

## Another route

The briefs could move onto the tutorials site as Open projects. There, hints, "Show one way" (recorded on the "Show
your teacher" card) and the teacher-only example already work. The Python app still runs on the student's laptop.
This would replace the hints and help pages above, but not the exemplar's testing record and marking points. Decide
before building.

## Order

1. B first, once the school-laptop test is done, because it uses the trainer from start to finish.
2. Then A, then C.
3. Every new brief follows this plan from the start.
