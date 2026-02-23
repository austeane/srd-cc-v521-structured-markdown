# SRD CC v5.2.1 Structured Markdown

This repository contains a structured Markdown conversion of the Dungeons & Dragons System Reference Document 5.2.1 (SRD 5.2.1).

## What Is Included

- `chapters/`: per-chapter Markdown files split by SRD section/page ranges.
- `SRD_CC_v5.2.1.combined.md`: combined Markdown file containing all pages.
- `docs/QA_SUMMARY.md`: page-level QA outcome summary from visual `png` + `md` review.
- `docs/PLAN.md`: implementation plan used for conversion.
- `docs/WORKLOG.md`: execution log of conversion and QA steps.
- `scripts/split_combined_into_chapters.py`: utility used to generate per-chapter files from the combined Markdown.

## Source and Attribution

This work includes material from the System Reference Document 5.2.1 (“SRD 5.2.1”) by Wizards of the Coast LLC, available at https://www.dndbeyond.com/srd. The SRD 5.2.1 is licensed under the Creative Commons Attribution 4.0 International License, available at https://creativecommons.org/licenses/by/4.0/legalcode.

See `chapters/01-legal-information.md` and `ATTRIBUTION.md` for attribution details.

## Notes

- This repository is a format conversion project and is not affiliated with Wizards of the Coast.
- Markdown conversion and structural normalization may introduce formatting differences from the PDF layout.
