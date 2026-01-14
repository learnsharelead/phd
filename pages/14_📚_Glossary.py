import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.nav import show_top_nav

apply_custom_css()
show_top_nav(current_page="Glossary")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border-radius: 10px; margin-bottom: 20px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📚 Research Glossary</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #1e40af;">A-Z definitions of key terms across all three papers.</p>
</div>
""", unsafe_allow_html=True)

# Search
search_term = st.text_input("🔍 Search for a term...", "")

# Glossary Data (50+ terms)
glossary = {
    "Alpha (α)": "The probability of making a Type I error (rejecting a true null hypothesis). Conventionally set at 0.05.",
    "Alternative Hypothesis (H₁)": "A statement that there is a statistically significant effect or difference; accepted if the null hypothesis is rejected.",
    "ANOVA": "Analysis of Variance. A statistical test used to compare the means of three or more groups.",
    "Applied Research": "Research aimed at solving practical, real-world problems.",
    "Authorship": "Credit given to individuals who have made substantial contributions to a research work, based on ICMJE criteria.",
    "Basic/Fundamental Research": "Research aimed at expanding knowledge without immediate practical application.",
    "Beta (β)": "The probability of making a Type II error (failing to reject a false null hypothesis). Power = 1 - β.",
    "Bias": "Systematic error that leads to incorrect conclusions. Can be in selection, measurement, or analysis.",
    "Chi-Square Test (χ²)": "A test used to analyze categorical data by comparing observed frequencies to expected frequencies.",
    "CiteScore": "A Scopus metric measuring average citations per document over a 4-year window.",
    "Coefficient of Determination (R²)": "The proportion of variance in the dependent variable explained by the independent variable(s).",
    "Confidence Interval (CI)": "A range of values likely to contain the true population parameter with a specified probability (e.g., 95%).",
    "Confounding Variable": "A variable that influences both the independent and dependent variables, potentially leading to spurious associations.",
    "Correlation": "A statistical measure of the strength and direction of the linear relationship between two variables (-1 to +1).",
    "Cross-Sectional Study": "A study that collects data at a single point in time.",
    "Degrees of Freedom (df)": "The number of values in a calculation that are free to vary.",
    "Dependent Variable (DV)": "The variable being measured or predicted; the outcome variable.",
    "Descriptive Statistics": "Statistics that summarize and describe data (mean, median, mode, standard deviation).",
    "Effect Size": "A quantitative measure of the magnitude of a phenomenon (e.g., Cohen's d, eta-squared).",
    "Empirical Research": "Research based on observation or experiment rather than theory alone.",
    "ESCI": "Emerging Sources Citation Index. An index for journals being evaluated for potential SCI inclusion.",
    "Ethics": "The branch of philosophy dealing with right and wrong conduct; in research, it governs responsible practices.",
    "Fabrication": "Making up data or results and recording/reporting them. A form of research misconduct.",
    "Falsification": "Manipulating research materials or data so that the research is not accurately represented.",
    "F-Test": "A test comparing variances, used in ANOVA to determine if group means differ significantly.",
    "Ghost Authorship": "Excluding contributors who deserve authorship credit.",
    "Gift Authorship": "Adding authors who did not make substantial contributions.",
    "h-index": "An author-level metric where h is the number of papers with at least h citations each.",
    "Hypothesis": "A testable prediction about the relationship between variables.",
    "Impact Factor (IF)": "A measure of the average citations received per paper published in a journal over two years.",
    "Independent Variable (IV)": "The variable manipulated or categorized by the researcher; the predictor.",
    "Inferential Statistics": "Statistics used to make inferences about a population from a sample (t-test, ANOVA, regression).",
    "Informed Consent": "Agreement by participants to take part in research after being fully informed of the procedures and risks.",
    "Interdisciplinary Research": "Research integrating knowledge and methods from two or more disciplines.",
    "Kruskal-Wallis Test": "A non-parametric alternative to one-way ANOVA for comparing three or more groups.",
    "Likert Scale": "A rating scale measuring attitudes, typically 5 or 7 points from 'Strongly Disagree' to 'Strongly Agree'.",
    "Literature Review": "A comprehensive, critical analysis of existing published work related to a research topic.",
    "Longitudinal Study": "A study that collects data from the same subjects over an extended period of time.",
    "Mann-Whitney U Test": "A non-parametric test comparing two independent groups, alternative to independent t-test.",
    "Mean": "The arithmetic average of a set of values.",
    "Median": "The middle value when data is arranged in order.",
    "Meta-Analysis": "A statistical technique that combines results from multiple studies.",
    "Mode": "The most frequently occurring value in a dataset.",
    "Multicollinearity": "A situation where independent variables in a regression are highly correlated with each other.",
    "Null Hypothesis (H₀)": "A statement of no effect or no difference; the hypothesis tested for possible rejection.",
    "Open Access": "The practice of providing unrestricted access to peer-reviewed scholarly research.",
    "Operationalization": "The process of defining variables in terms of measurable operations or indicators.",
    "Outlier": "A data point that differs significantly from other observations.",
    "P-value": "The probability of obtaining results at least as extreme as observed, assuming the null hypothesis is true.",
    "Paired t-Test": "A t-test comparing two related samples (e.g., before and after measurements on same subjects).",
    "Parametric Test": "A statistical test that assumes the data follows a specific distribution (usually normal).",
    "Pearson Correlation (r)": "A measure of linear correlation between two continuous variables.",
    "Peer Review": "The evaluation of research by experts in the same field before publication.",
    "Plagiarism": "Using another person's ideas, words, or work without proper attribution.",
    "Population": "The entire group of individuals or instances about which conclusions are to be drawn.",
    "Power": "The probability of correctly rejecting a false null hypothesis (1 - β). Recommended: ≥0.80.",
    "Predatory Journal": "A journal that prioritizes profit over scholarly quality, often with poor or no peer review.",
    "Primary Data": "Data collected firsthand by the researcher for a specific purpose.",
    "Qualitative Research": "Research focusing on understanding meanings, experiences, and perspectives through non-numerical data.",
    "Quantitative Research": "Research focusing on numerical data and statistical analysis.",
    "Quota Sampling": "A non-probability sampling method where the sample is selected to match population proportions.",
    "Random Sampling": "A sampling method where every member of the population has an equal chance of selection.",
    "Regression Analysis": "A statistical method for modeling the relationship between a dependent variable and one or more independent variables.",
    "Reliability": "The consistency or repeatability of a measurement (e.g., Cronbach's Alpha).",
    "Research Design": "The overall strategy for integrating different components of a study coherently.",
    "Research Integrity": "Adherence to ethical principles and professional standards in research.",
    "Retraction": "Withdrawal of a published paper due to errors, misconduct, or ethical violations.",
    "Salami Slicing": "Dividing one study into multiple publications to inflate publication count.",
    "Sample": "A subset of the population selected for study.",
    "Sampling Error": "The difference between a sample statistic and the true population parameter.",
    "SCI": "Science Citation Index. A prestigious index of high-impact scientific journals.",
    "Scopus": "A major citation database containing 84+ million records from 27,000+ journals.",
    "Secondary Data": "Data collected by someone else for a different purpose, reused in research.",
    "Self-Plagiarism": "Reusing one's own previously published work without proper citation.",
    "Significance Level (α)": "The threshold probability for rejecting the null hypothesis, typically 0.05.",
    "Simple Random Sampling": "A sampling method where each member has an equal probability of selection.",
    "Spearman's Correlation (ρ)": "A non-parametric measure of rank correlation between two variables.",
    "Standard Deviation (SD)": "A measure of the dispersion of data around the mean.",
    "Standard Error (SE)": "The standard deviation of the sampling distribution of a statistic.",
    "Stratified Sampling": "Dividing the population into subgroups (strata) and sampling from each.",
    "Systematic Sampling": "Selecting every kth member from a population list.",
    "t-Test": "A statistical test comparing the means of one or two groups.",
    "Type I Error": "Rejecting a true null hypothesis (false positive). Probability = α.",
    "Type II Error": "Failing to reject a false null hypothesis (false negative). Probability = β.",
    "Validity": "The extent to which a measurement actually measures what it claims to measure.",
    "Variable": "A characteristic or attribute that can take on different values.",
    "Variance": "A measure of the spread of data, equal to the average of squared deviations from the mean.",
    "Web of Science": "A major citation database and source of Impact Factor calculations.",
    "Wilcoxon Test": "A non-parametric test comparing two related samples, alternative to paired t-test.",
    "Z-Score": "The number of standard deviations a data point is from the mean.",
    "Z-Test": "A test comparing a sample mean to a population mean when the population SD is known."
}

# Filter based on search
if search_term:
    filtered = {k: v for k, v in glossary.items() if search_term.lower() in k.lower() or search_term.lower() in v.lower()}
else:
    filtered = glossary

# Display count
st.caption(f"Showing {len(filtered)} of {len(glossary)} terms")

# Display Glossary
for term, definition in sorted(filtered.items()):
    st.markdown(f"""
    <div style="background: #f8fafc; padding: 12px 15px; border-radius: 8px; margin-bottom: 10px; border-left: 4px solid #3b82f6;">
        <strong style="color: #1e40af; font-size: 15px;">{term}</strong>
        <p style="margin: 5px 0 0 0; font-size: 14px; color: #475569;">{definition}</p>
    </div>
    """, unsafe_allow_html=True)

if not filtered:
    st.warning("No terms found. Try a different search query.")

show_footer()
