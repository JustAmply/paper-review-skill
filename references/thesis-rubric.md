# thesis review rubric

Use this checklist for master's theses, dissertations, thesis chapters, methodology/evaluation audits, final submission reviews, and advisor feedback integration.

## thesis-wide checklist

- research question is explicit, answerable, and revisited in the conclusion
- title, abstract, introduction, contributions, results, discussion, and conclusion describe the same work at compatible levels of strength
- stated contributions are concrete, defensible, and supported by the manuscript
- chapter order builds a clear argument rather than collecting loosely related sections
- transitions explain why each chapter is needed for the thesis goal
- terminology, notation, abbreviations, datasets, methods, and metrics stay consistent across chapters
- limitations are explicit and proportionate to the evidence
- final claims do not exceed the methods, data, or evaluation

## introduction and contribution checklist

- motivation identifies a real problem without relying on vague importance claims
- research gap follows from the literature or practical context
- research question or objective is stated in a form that can be evaluated
- scope boundaries are clear enough to prevent examiner confusion
- contributions distinguish between implementation work, empirical findings, conceptual analysis, and tooling
- thesis structure paragraph matches the actual chapter contents

## literature review checklist

- related work is synthesized into themes, not only summarized paper by paper
- central and recent work in the area is represented, or omissions are justified by scope
- comparison criteria are clear and relevant to the research question
- cited work is connected to the thesis contribution
- claims about prior work are cited and not overstated
- the literature review makes the research gap sharper by the end of the chapter

## methodology and reproducibility checklist

- chosen method is justified against the research question
- datasets, sources, inclusion criteria, preprocessing, annotation, filtering, and splits are described
- implementation details are sufficient for reproduction: software versions, dependencies, prompts, model versions, hyperparameters, random seeds, hardware, and runtime where relevant
- evaluation protocol specifies metrics, baselines, ablations, statistical tests, and failure criteria where relevant
- experimental comparisons are fair and use comparable inputs, training data, constraints, or assumptions
- ethical, legal, privacy, or bias considerations are addressed when relevant
- threats to validity are named concretely rather than hidden in generic limitation language

## results and discussion checklist

- results answer the research question directly
- figures, tables, captions, and text agree numerically and conceptually
- quantitative claims include enough context to interpret magnitude and uncertainty
- negative or mixed results are discussed rather than ignored
- causal claims are supported by the design; otherwise they are phrased as associations or observations
- discussion separates interpretation from evidence
- limitations explain what cannot be concluded from the work

## conclusion checklist

- conclusion answers the research question without introducing unsupported new claims
- contributions are restated at the strength justified by the results
- future work follows from concrete limitations or observed failure modes
- the final paragraph leaves the examiner with a clear account of what was learned

## final submission checklist

- no visible placeholders remain: TODO, FIXME, TBD, XXX, question marks from unresolved references, or commented instructions meant for drafting
- all figures and tables are referenced, captioned, legible, and discussed
- citations, labels, cross-references, bibliography entries, appendices, and acronyms are complete and consistent
- abstract can stand alone and agrees with the final results
- appendices are referenced from the main text and contain only material that supports the thesis
- acknowledgements, declarations, title page, and institutional formatting requirements are complete if required

## advisor feedback integration checklist

- convert each feedback item into one or more concrete edits
- group edits by chapter or file
- mark unclear feedback as a question instead of guessing
- identify feedback that conflicts with other instructions or thesis constraints
- preserve high-priority technical corrections ahead of local wording preferences
