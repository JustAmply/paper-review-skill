---
name: paper-review
description: Use when reviewing scientific or technical manuscripts, papers, theses, master's theses, dissertations, LaTeX drafts, thesis chapters, or final submission drafts for scientific correctness, structure, methodology, claim support, reproducibility, notation, citations, writing quality, and concrete revision planning.
---

# Overview

Use this skill to produce one compileable LaTeX review file that improves scientific quality first, thesis or paper structure second, and writing quality third.

## Default behavior

1. Read the full manuscript before writing findings.
2. Use extra thinking by default.
3. Write one standalone LaTeX review file to `paper-reviews/review-YYYY-MM-DD-HHMMSS.tex`, unless the user gives a different path. Create the output directory if it does not exist.
4. Keep the file compileable with minimal LaTeX scaffolding.
5. Focus on concrete issues and fixes, not generic reviewer prose.
6. Do not require a fixed review template or section layout unless the user asks for one.
7. Treat `proofread`, `flag typos`, `grammar`, `writing quality`, and similar wording as a request to spend more budget on the editorial sweep after the technical audit.
8. Treat `thesis`, `master's thesis`, `dissertation`, `chapter`, `final submission`, `defense`, `advisor feedback`, and similar wording as a request to apply the thesis-specific checks in `references/thesis-rubric.md`.

## Review modes

Choose the narrowest mode that fits the user request:

- **Paper review:** audit a paper or article for technical correctness, claim support, notation, evidence, and concise reviewer-style findings.
- **Thesis-wide review:** audit a full thesis for research question clarity, contribution, chapter structure, methodology, literature synthesis, evaluation, discussion, conclusion alignment, and revision priorities.
- **Chapter review:** audit one thesis chapter for local argument flow, missing definitions, unsupported claims, citation gaps, transitions, and consistency with the stated thesis goals.
- **Methodology/evaluation audit:** audit methods, experiments, datasets, parameters, metrics, baselines, statistical claims, reproducibility, and implementation details.
- **Final submission review:** audit title, abstract, introduction, research questions, figures, tables, captions, citations, references, appendices, placeholders, formatting hazards, and final must-fix items.
- **Advisor feedback integration:** convert supervisor, advisor, examiner, or review feedback into concrete chapter-level edits, identify ambiguous or conflicting feedback, and list clarification questions.

For thesis-related modes, read `references/thesis-rubric.md` when it would improve coverage.

## Primary objective

Prioritize technical correctness over prose quality.

If attention is limited, spend it in this order:

1. equations, derivations, notation, units, definitions, and algorithmic correctness
2. research question, contribution, methodology, evaluation validity, reproducibility, and claim support
3. consistency between claims, evidence, figures, tables, captions, appendices, abstract, introduction, discussion, and conclusions
4. editorial quality, with special attention to high-confidence issues that are cheap to verify and fix

Do not let editorial findings crowd out technical findings.

## What extra thinking is for

Spend extra thinking on:

- whether the paper's main claims are actually supported by the manuscript
- whether equations, notation, units, and quantitative statements are internally consistent
- whether appendix formulas and implementation-facing expressions are correct and unambiguous
- whether inverse-trig expressions, coordinate transforms, and branch conventions are correctly specified
- whether abstract, results, figures, tables, and conclusion agree
- whether claims are overstated, under-qualified, or missing key caveats
- whether any statements seem factually wrong, unsupported, or need verification
- whether there are obvious, high-confidence editorial defects that are fast to confirm and worth surfacing

Do not narrate the reasoning process.

## Workflow

1. Read the full manuscript to understand the main claims, evidence, equations, appendices, and structure.
2. Identify the highest-risk technical content:
   - key equations and derivations
   - symbol definitions
   - quantitative claims
   - coordinate transformations
   - appendix formulas
   - implementation-facing expressions
3. Perform a technical audit first.
4. Re-check the highest-risk technical findings.
5. For theses, audit research question alignment, chapter-to-chapter coherence, methodology, literature synthesis, evaluation, discussion, limitations, and conclusion alignment.
6. Perform a bounded editorial pass after the technical and structural audit.
7. If code execution is available, run `scripts/proofing_scan.py` (or otherwise do the manual pattern scan described below) to catch high-confidence copy/notation defects that are easy to miss.
8. Perform one short final proofing sweep for obvious, high-confidence editorial issues that are cheap to verify.
9. Write the review file.

For long papers, inspect sections in chunks when helpful, but do not force a multi-pass ritual if it does not improve the review.

## Bundled resources

Use `references/review-rubric.md` when a compact review checklist would help structure coverage, especially for long manuscripts or broad proofreading requests.

Use `references/thesis-rubric.md` for master's theses, dissertations, thesis chapters, final submission checks, methodology/evaluation audits, or advisor feedback integration.

Use `scripts/proofing_scan.py` for the mandatory micro-proofing pattern scan when code execution is available. The script accepts PDFs and text-like manuscript files, including `.txt`, `.tex`, and extracted manuscript text.

Example command:

- `python scripts/proofing_scan.py <path-to-pdf-or-text> --max-hits 80`

The proofing scan depends on `pypdf` only when scanning PDFs. If the script reports a missing dependency, install the skill dependencies from the skill directory:

- `python -m pip install -r requirements.txt`

Treat script output as candidates, not final findings. Spot-check each hit against the manuscript before including it in the review.

## Technical audit

### Notation/terminology drift check (required)

For frequently used symbols (especially subscripted/superscripted angles, radii, and frame labels), record:

- where the symbol is first defined
- the **verbal descriptor** attached to it (e.g., "final polar angle at the source radius")
- any later descriptor variants (e.g., "initial inclination") and whether they conflict

Flag conflicts where the same symbol is described with inconsistent temporal/role adjectives (initial/final, source/observer, emission/reception) even if the equations are otherwise correct. These often indicate a real conceptual bug or an implementation-facing ambiguity.

Explicitly check for:

- unsupported or overstated claims
- conclusions that do not follow from the reported results
- inconsistencies between text, equations, figures, tables, and captions
- undefined symbols or symbols used before definition
- notation drift between sections or between the main text and appendix
- unit errors or dimensional inconsistencies
- arithmetic or quantitative inconsistencies
- sign errors, missing factors, normalization ambiguity, or missing case distinctions
- inverse-trig, branch, or quadrant ambiguity, for example `arctan(x/y)` where `atan2` or an explicit branch convention may be needed
- coordinate-system ambiguity, including misuse of terms like initial, final, source, observer, local, global, polar, or azimuthal
- equations that are plausible in prose but ambiguous or wrong as written for implementation
- mismatch between a mathematical definition and an appendix or code-facing formula
- missing assumptions, qualifiers, or uncertainty that materially affect interpretation
- factual statements that appear unsupported or likely incorrect

For thesis work, also explicitly check for:

- unclear or drifting research questions
- stated contributions that do not match the actual results
- chapter order or transitions that obscure the argument
- literature review sections that list prior work without synthesizing it
- methods that are insufficiently justified for the research question
- missing reproducibility details such as datasets, preprocessing, parameters, random seeds, software versions, hardware, prompts, or evaluation scripts
- baselines, ablations, metrics, or comparisons that are missing, unfair, or not explained
- limitations that are missing, understated, or disconnected from the evidence
- abstract, introduction, discussion, and conclusion statements that disagree with each other

When judging technical content, distinguish clearly between:

- **definite error:** contradicted by the manuscript itself or by straightforward math, logic, or internal evidence
- **unsupported claim:** stated more strongly than the manuscript supports
- **likely issue:** plausibly wrong or misleading, but not fully provable from the manuscript alone
- **needs external verification:** may depend on outside literature or facts not established in the manuscript

Do not present verification-needed items as definite errors.

## Coverage requirement

If the manuscript contains equations, derivations, appendices, or implementation formulas, inspect them explicitly.

Do not finish the review without checking the key technical content for:

- branch conventions
- sign conventions
- symbol definitions
- dimensional consistency
- implementation ambiguity

If no concrete technical issues are found, say explicitly that these checks were performed and no concrete issues were identified.

## Editorial review

Editorial review is secondary to technical review, but it is still part of the job.

Look for:

- typos, spelling, grammar, and punctuation issues
- awkward, vague, or ambiguous phrasing
- sentences that obscure a technical point
- broken references or citation mismatches
- inconsistent terminology or notation
- local wording that could be made clearer or more precise
- malformed sentences in derivations or equation-adjacent prose
- obvious bibliography defects, including duplicated punctuation and malformed quoted titles
- capitalization or styling mistakes in proper names, product names, languages, or branded terms
- reference-list hygiene (required): duplicated punctuation (e.g., `, ,` or `" , ,`), malformed quoted titles, inconsistent capitalization, and obvious citation-format glitches

Separate editorial issues into two buckets mentally:

1. **meaningful editorial issues:** affect meaning, create technical ambiguity, or noticeably reduce professionalism
2. **bounded proofing issues:** minor but obvious, high-confidence, low-cost defects that are fast to verify and fix

Always include the meaningful editorial issues.

Also include a bounded number of proofing issues when they are obvious and unambiguous, especially when they occur in:

- derivation-heavy sections
- appendices with implementation formulas
- headings, captions, or references
- repeated terminology or capitalization

Do not spend space on subjective line editing or stylistic preferences.

Cap bounded proofing issues at a small number unless the user explicitly asks for exhaustive proofreading.

## Final proofing sweep

### Mandatory micro-proofing pattern scan (required)

Do a quick, mechanical scan for high-yield, high-confidence defects and include any hits as proofing-sweep items:

- duplicated punctuation and spacing artifacts: `, ,`, `,,`, `..`, `" , ,`, `" ,` variants
- semicolon capitalization anomalies: `;` followed by a capital letter where the second clause is not a new sentence/proper noun
- malformed equation-adjacent grammar frames (common in derivations): `into ... into ...`, `with ... into ...`, `plugging ... into together ...`
- programming/product-name capitalization: JavaScript, iOS, iPhone, etc.
- quadrant/branch ambiguity patterns, especially `arctan(x/y)`-style expressions that should be `atan2(y,x)` or require an explicit branch convention

If code execution is available, prefer running `scripts/proofing_scan.py` and then spot-check the top hits.

Use the returned hits as candidates for the proofing-sweep subsection, and spot-check each before presenting it as an issue.

Before finishing, ask silently:

- Are there any obvious, high-confidence editorial issues still on the page that I can name precisely?
- Did I check the bibliography or references for duplicated punctuation, broken quotation punctuation, or citation-format glitches?
- Did I check dense derivation prose near equations for malformed sentences?
- Did I check appendices for capitalization, terminology, or implementation-facing copy issues?

If yes, include the best few findings instead of omitting them.

## Output contract

The review file content should be LaTeX only.

Do not force a rigid section structure.

Structure the review in whatever way is clearest and most compact, but make sure it covers:

- overall assessment of manuscript quality
- the most important technical findings
- any meaningful editorial findings
- a short proofing-sweep subsection when there are obvious high-confidence copyediting defects worth fixing
- the highest-priority fixes
- a prioritized revision plan when reviewing a thesis, thesis chapter, final submission draft, or advisor feedback
- any items that need external verification

For each technical finding, include:

- location
- problem
- why it matters
- suggested fix

For each editorial finding, include:

- location
- problem
- why it matters
- suggested fix
- optional candidate rewrite for sentence-level edits

For proofing-sweep items, a compact bullet list is acceptable if each bullet includes:

- location
- problem
- suggested fix

For thesis revision plans, group action items into:

- **Must fix:** issues that could materially affect correctness, grade, examiner confidence, reproducibility, or the central argument
- **Should fix:** issues that would noticeably improve clarity, completeness, or professionalism
- **Nice to fix:** low-risk polish that can wait until higher-priority issues are resolved

Put technical and factual issues before prose issues unless the user explicitly asks for a prose-first review.

## Writing rules

- Prefer concrete issues over generic praise or commentary.
- Prefer local, checkable technical failures over broad interpretive commentary.
- Prefer evidence-backed findings over stylistic preferences.
- Keep the review concise and operational.
- If a section of the paper is clean, omit filler.
- If there are only a few real issues, say so and keep the review short.
- Do not pad the review with low-value prose edits when technical scrutiny should be the focus.
- Good findings are things like:
  - branch ambiguity in an inverse-trig expression
  - inconsistent variable definition
  - dimensional mismatch
  - undefined symbol in a key equation
  - mismatch between a derivation and an appendix formula
  - malformed sentence in a dense technical derivation
  - duplicated punctuation in a reference entry
  - capitalization error in a proper name or implementation-facing term
- Lower-value findings are things like:
  - generic overclaiming language without a concrete technical issue
  - broad style commentary
  - subjective rewrite suggestions that do not improve correctness or clarity

## Update behavior

Create a new timestamped review file by default.

Only update an existing review file if the user explicitly asks.

Compilation of the review into PDF is not required unless the user asks for it or it is needed to validate that the LaTeX is compileable.

## References

Use `references/review-rubric.md` if it provides a useful review checklist.
