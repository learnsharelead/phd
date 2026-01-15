
# This file contains the comprehensive content for all papers to be used in PDF generation.

PAPER_CONTENT = {
    "Paper I: Research Methodology": {
        "Unit I: Introduction to Research": {
            "1.1 What is Research?": """
Definition: Research is a systematic inquiry to discover or revise facts, theories, applications, etc. It's a methodical process of asking questions and finding answers.

Analogy: Think of research as being a detective. You have a mystery (research problem), you gather clues (data), and you build a case (theory/conclusion).

Key Characteristics:
- Systematic: Follows a structured process
- Controlled: Variables are managed
- Empirical: Based on observation/evidence
- Critical: Scrutinized and validated
            """,
            "1.2 Types of Research": """
Based on Purpose:
- Descriptive: Describes 'what is'. (e.g., Survey of current practices)
- Exploratory: Investigates a new topic. (e.g., Focus groups for a new product)
- Explanatory: Explains 'why'. (e.g., Cause-effect studies, experiments)

Based on Process:
- Qualitative: Explores meanings, experiences. (e.g., Interviews, case studies)
- Quantitative: Measures, uses numbers. (e.g., Surveys with scales, experiments)
- Mixed Methods: Combines both.

Based on Outcome:
- Fundamental (Basic): Expands knowledge. (e.g., How memory works)
- Applied: Solves practical problems. (e.g., Improving memory in students)
            """,
            "1.3 Research Process": """
A typical research process involves:
1. Problem Identification: What do you want to solve?
2. Literature Review: What is already known?
3. Hypothesis Formulation: What do you predict?
4. Research Design: How will you test it?
5. Data Collection: Gather information.
6. Data Analysis: Analyze the findings.
7. Interpretation & Conclusion: What does it mean?
8. Report Writing & Publication: Share your findings.
            """,
            "1.4 Hypothesis Formulation": """
Hypothesis: A testable prediction about the relationship between variables.
- Null Hypothesis (H0): No effect or difference.
- Alternative Hypothesis (H1): An effect or difference exists.

Example:
- H0: There is no difference in test scores between Group A and Group B.
- H1: There is a difference in test scores between Group A and Group B.

Errors:
- Type I Error (False Positive): Rejecting a true Null Hypothesis.
- Type II Error (False Negative): Failing to reject a false Null Hypothesis.
            """
        },
        "Unit II: Research Design & Data Collection": {
            "2.1 Research Design": """
Definition: The blueprint or framework for conducting the study.

Types of Research Design:
- Exploratory Design: flexible, uncovers ideas
- Descriptive Design: accurate portrayal of characteristics
- Experimental Design: Causal relationships, control over variables
- Diagnostic Design: Frequency of occurrence/association

Choice of Design depends on:
- Nature of the problem
- Purpose of the study
- Resources available
            """,
            "2.2 Questionnaire Design": """
Key Principles (KISS): Keep It Short and Simple.
- Avoid double-barreled questions (two questions in one)
- Avoid leading/biased questions
- Use simple language

Types of Questions:
- Open-ended: Respondents answer in their own words
- Closed-ended: Respondents choose from options (e.g., Multiple choice, Likert scale)

Structure:
- Introduction/Consent
- Screening questions
- Main study questions
- Demographics (usually at the end)
            """,
            "2.3 Data Collection Methods": """
Primary Data (collected by you):
- Surveys/Questionnaires (broad reach, quantitative)
- Interviews (deep insights, qualitative)
- Observation (behavior in natural setting)
- Experiments (controlled testing)

Secondary Data (already exists):
- Government publications
- Journals/Books
- Industry reports
- Internet sources
            """
        },
        "Unit III: Measurement & Sampling": {
            "3.1 Measurement Scales": """
NOIR Hierarchy:
1. Nominal: Names/Label (e.g., Gender, Color). Mode only.
2. Ordinal: Order/Rank (e.g., Rank 1st, 2nd, 3rd). Median/Mode.
3. Interval: Difference is meaningful, no true zero (e.g., Temp in Celsius). Mean/Median/Mode.
4. Ratio: True zero exists (e.g., Height, Weight, Income). All stats allowed.
            """,
            "3.2 Validity & Reliability": """
Reliability (Consistency):
- If you measure again, do you get the same result?
- Types: Test-retest, Internal consistency (Cronbach's alpha).

Validity (Accuracy):
- Does it measure what it's supposed to measure?
- Types: Face, Content, Criterion, Construct validity.

Analogy:
- Reliable but not Valid: Hitting the same spot on a target, but not the bullseye.
- Valid & Reliable: Hitting the bullseye consistently.
            """,
            "3.3 Sampling Methods": """
Probability Sampling (Random):
- Simple Random: Lottery method
- Stratified: Divide into subgroups (strata), then random sample
- Systematic: Every nth person
- Cluster: Select entire groups (clusters) randomly

Non-Probability Sampling (Non-Random):
- Convenience: Whoever is available
- Judgmental/Purposive: Researcher's choice
- Quota: Matching population proportions non-randomly
- Snowball: Participants refer others (good for hidden populations)
            """
        },
        "Unit IV: Report Writing & Publication": {
            "4.1 Research Report Structure": """
Standard Structure (IMRAD):
1. Introduction: Problem, objectives, literature
2. Methods: Design, sample, tools, procedure
3. Results: Data presentation, analysis
4. Discussion: Interpretation, limitations, implications
+ Abstract, Reference, Appendices

Features of a Good Report:
- Clarity
- Conciseness
- Accuracy
- Objectivity
- Logical flow
            """,
            "4.2 Research Ethics & Plagiarism": """
Plagiarism: Using others' work without credit.
Forms:
- Verbatim comparison (Copy-paste)
- Mosaic plagiarism (Patchwork)
- Self-plagiarism (Reusing one's own work)

Prevention:
- Proper Citation (APA, MLA, etc.)
- Paraphrasing
- Quotation marks for direct quotes
- Anti-plagiarism software (Turnitin, Urkund)
            """
        }
    },
    "Paper II: Statistics & Computer Applications": {
        "Unit I: Statistical Foundations": {
            "1.1 Central Tendency & Dispersion": """
Mean: Average (Sum / N)
Median: Middle value
Mode: Most frequent value

Variance: Average squared deviation from the mean
Standard Deviation: Square root of variance
Range: Max - Min
            """,
            "1.2 Hypothesis Testing": """
Steps:
1. State H0 and H1
2. Choose significance level (alpha, usually 0.05)
3. Select test statistic (z, t, F, chi-square)
4. Calculate p-value or critical value
5. Decision: Reject H0 if p < alpha

Parametric vs Non-Parametric:
- Parametric (e.g., t-test, ANOVA): Assumes normal distribution, interval/ratio data.
- Non-Parametric (e.g., Mann-Whitney, Kruskal-Wallis): No assumption of normality, ordinal/nominal data.
            """,
            "1.3 Common Tests": """
- t-test: Compare means of 2 groups
- ANOVA: Compare means of 3+ groups
- Chi-square: Test association between categorical variables
- Correlation (r): Relationship between 2 continuous variables
            """
        },
        "Unit II: Correlation & Regression": {
            "2.1 Correlation": """
Pearson's r: Measures linear relationship (-1 to +1).
- +1: Perfect positive
- -1: Perfect negative
- 0: No correlation

Coefficient of Determination (R-squared):
- Proportion of variance in Y explained by X.
- r = 0.8 -> R^2 = 0.64 (64% explained)
            """,
            "2.2 Regression": """
Simple Linear Regression: Y = b0 + b1*X + error
- b0: Intercept
- b1: Slope (change in Y for 1 unit change in X)

Method of Least Squares: Minimizes the sum of squared errors between observed and predicted Y.

Multiple Regression: Y = b0 + b1*X1 + b2*X2 + ...
- Adjusted R-squared used to penalize for extra variables.
            """
        },
        "Unit III: Computer Applications": {
            "3.1 Excel": """
Uses: Data entry, basic stats, charts.
Formulas:
- =AVERAGE(), =STDEV.S()
- =T.TEST(), =CORREL()
Data Analysis Toolpak: For ANOVA, Regression.
            """,
            "3.2 SPSS": """
Statistical Package for the Social Sciences.
- Menu-driven (GUI)
- Views: Data View, Variable View
- Good for: Complex analyses without coding (Factor analysis, etc.)
            """,
            "3.3 R": """
Open-source programming language for stats.
- Pros: Free, huge ecosystem (packages), reproducible (RMarkdown).
- Cons: Steeper learning curve (coding).
            """,
            "3.4 LaTeX": """
Typesetting system for documents.
- Standard in math/science.
- Handles formulas and references strictly.
- Separation of content and formatting.
            """
        },
        "Formula Cheat Sheet": {
            "Key Formulas": """
Mean: sum(x) / n
Standard Deviation (sample): sqrt( sum(x - mean)^2 / (n-1) )
Standard Error: s / sqrt(n)
z-score: (x - mean) / s

t-statistic: (mean - mu) / (s / sqrt(n))
Chi-square: sum( (Observed - Expected)^2 / Expected )
Correlation (r): Covariance(x,y) / (SD(x) * SD(y))
Regression Slope: r * (SD(y) / SD(x))
            """
        }
    },
    "Paper III: Research Ethics & Tools": {
        "Unit I: Philosophy & Ethics": {
            "1.1 Philosophy of Research": """
Epistemology: Study of knowledge (How do we know?).
- Positivism: Objective reality, measurable.
- Interpretivism: Subjective reality, socially constructed.

Axiology: Study of values/ethics.
Ontology: Study of being/existence.
            """,
            "1.2 Scientific Conduct": """
FFP (Research Misconduct):
- Fabrication: Making up data.
- Falsification: Manipulating data/equipment.
- Plagiarism: Stealing ideas/text.

Ethics:
- Informed Consent
- Confidentiality
- Do No Harm (Beneficence/Non-maleficence)
            """
        },
        "Unit II: Research Metrics": {
            "2.1 Journal Metrics": """
Impact Factor (IF): Average citations in a year to papers from previous 2 years.
- (Cites in 2023 to papers of 2021+2022) / (Total papers in 2021+2022)
CiteScore: Scopus metric (4-year window).
SNIP: Source Normalized Impact per Paper.
            """,
            "2.2 Author Metrics": """
h-index: h papers with at least h citations each.
- e.g., h-index 10 means 10 papers cited >= 10 times.
i10-index: Number of papers with >= 10 citations (Google Scholar).
            """,
            "2.3 Databases": """
indexing Databases:
- Web of Science (SCI, SSCI) - Clarivate
- Scopus - Elsevier
- PubMed - Medicine
- Google Scholar - Broad, inclusive
            """
        },
        "Unit III: Online Tools": {
            "3.1 Plagiarism Detection": """
Turnitin / Urkund (Ouriginal):
- Compare against database of internet, journals, student papers.
- Similarity Index: % of matching text.
- NOT "Plagiarism Index" - requires human interpretation.
            """,
            "3.2 Reference Management": """
Tools: Mendeley, Zotero, EndNote.
- Store citations
- Insert in-text citations
- Generate bibliography automatically
            """,
            "3.3 Publishing Tools": """
SHERPA/RoMEO: Check journal copyright/archiving policies.
ORCID: Unique digital identifier for researchers.
ResearchGate/Academia.edu: Academic social networking.
            """
        },
        "Case Studies": {
            "Notable Cases": """
Hwang Woo-suk (Stem Cells): Fabricated data on human cloning. Retracted papers from Science.
Jan Hendrik Schön (Physics): Fabrication & Falsification at Bell Labs. Reused same graphs for different data.
Andrew Wakefield (Vaccines): Falsified data linking MMR vaccine to autism. Retracted from Lancet.
            """
        }
    }
}
