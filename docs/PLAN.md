# SRD Structured Markdown Plan

## Goal
Produce **fully structured Markdown for every page** of `SRD_CC_v5.2.1.pdf`, while retaining high confidence that page text is preserved and visually consistent with source pages.

## Current Status
- [x] Deterministic per-page text extraction (`pNNN.txt`) with checksum integrity checks.
- [x] Per-page PNG rendering (`pNNN.png`) for visual pairing.
- [x] Baseline page markdown artifacts (`pNNN.md`) generated for all 364 pages (currently lossless fenced-text format).
- [x] Reorder-tolerant validator implemented and passing on all pages in baseline format.
- [ ] Structured markdown transformation for all pages.
- [x] Structured markdown transformation for all pages.
- [x] Per-page visual QA sign-off by agents on `png` + `md` pairs.
- [x] Final assembled structured markdown output.

## Execution Phases
1. Environment and tooling (uv-managed)
   - Create uv environment for structured conversion utilities.
   - Install and test PDF->Markdown structure tools in isolated env.

2. Structured conversion
   - Generate `srd_structured/pages_md_structured/pNNN.md` for all pages.
   - Preserve source references and page numbering.
   - Keep tables as Markdown tables where reliable; otherwise use semantically clear list/subsection structures.

3. Validation
   - Run reorder-tolerant validation between canonical `pNNN.txt` and structured `pNNN.md`.
   - Triage and fix pages that fail content-preservation checks.

4. Visual QA by agents
   - Assign page chunks to QA agents.
   - Each agent explicitly reviews every `pNNN.png` with its `pNNN.md`.
   - Record issues and corrections; rerun validation where edits occur.

5. Final assembly and deliverables
   - Assemble final structured markdown document.
   - Produce QA summary and remaining-risk notes.
