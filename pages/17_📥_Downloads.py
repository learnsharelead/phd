import streamlit as st
from fpdf import FPDF
from utils.styles import apply_custom_css, show_footer
from utils.nav import show_top_nav
from utils.pdf_content import PAPER_CONTENT
import base64

# Page Config (must be first)
st.set_page_config(page_title="Downloads | Research Ethics Hub", page_icon="📥", layout="wide")

# Styling
apply_custom_css()
show_top_nav(current_page="Downloads")

# Check if user is logged in (optional, but good practice)
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Researcher"

# Header
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%); border-radius: 10px; margin-bottom: 25px;">
    <h1 style="color: #0369a1; margin-bottom: 10px; font-size: 2.5rem;">📥 Study Material Downloads</h1>
    <p style="color: #0c4a6e; font-size: 1.1rem;">Download comprehensive study guides, cheat sheets, and summaries for your Ph.D. coursework.</p>
</div>
""", unsafe_allow_html=True)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Ph.D. Research Methodology Coursework', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        # Latin-1 encoding fix
        encoded_body = body.encode('latin-1', 'replace').decode('latin-1')
        self.multi_cell(0, 6, encoded_body)
        self.ln()

def generate_pdf(title, content_dict):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_title(title)
    
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, title, 0, 1, 'C')
    pdf.ln(10)
    
    for section, text in content_dict.items():
        pdf.chapter_title(section)
        pdf.chapter_body(text)
        
    return pdf.output(dest="S").encode('latin-1')

# Detailed Content
paper1_content = {
    "Unit I: Introduction to Research": """
1. Meaning of Research:
Research is a systematic, scientific, and objective method of inquiry for acquiring knowledge. It involves defining problems, formulating hypotheses, collecting and analyzing data, and reaching conclusions.

2. Objectives of Research:
- To gain familiarity with a phenomenon (Exploratory).
- To portray accurate characteristics of a situation or group (Descriptive).
- To determine the frequency of occurrence (Diagnostic).
- To test a hypothesis of causal relationship (Hypothesis-testing).

3. Types of Research:
- Fundamental (Basic): Research for knowledge's sake, formulating theories (e.g., laws of physics).
- Applied: Research to solve immediate practical problems (e.g., improving crop yield).
- Quantitative: Based on measurement of quantity (Survey, Experiment).
- Qualitative: Concerned with quality or kind (Interview, Observation).

4. Criteria of Good Research:
- Systematic: orderly and efficient.
- Logical: guided by rules of logical reasoning.
- Empirical: deals with concrete data.
- Replicable: results can be verified by others.
""",
    "Unit II: Research Design": """
1. Meaning of Research Design:
It is the conceptual structure within which research is conducted. It constitutes the blueprint for the collection, measurement, and analysis of data.

2. Components of Research Design:
- Sampling Design: Method of selecting items.
- Observational Design: Conditions of observation.
- Statistical Design: How many items observed and how analyzed.
- Operational Design: Techniques for implementation.

3. Types of Research Designs:
- Exploratory Design: Flexible design to discover ideas/insights.
- Descriptive/Diagnostic: Rigid design with specific objectives (Who, What, Where, When).
- Experimental (Causal): Controls variables to test cause-and-effect.

4. Variables:
- Independent Variable (IV): The cause (manipulated).
- Dependent Variable (DV): The effect (measured).
- Extraneous Variable: Variables not studied but affect DV (must be controlled).
""",
    "Unit III: Measurement & Sampling": """
1. Measurement Scales:
- Nominal: Classification only (Gender: Male/Female).
- Ordinal: Ranking/Order (Rank 1, 2, 3).
- Interval: Equal distance, no true zero (Temperature).
- Ratio: True zero point (Weight, Income).

2. Sampling Methods:
- Probability Sampling: Simple Random, Stratified, Cluster, Systematic.
- Non-Probability Sampling: Convenience, Quota, Judgmental, Snowball.

3. Sample Size (Cochran's Formula):
n = (Z^2 * p * q) / e^2
Where Z = 1.96 (for 95% confidence), p = estimated proportion, e = margin of error.

4. Errors:
- Sampling Error: Due to studying a sample rather than population.
- Non-Sampling Error: Measurement errors, non-response, bias.
""",
    "Unit IV: Report Writing": """
1. Structure of Research Report:
- Preliminary Pages: Title, Certification, Declaration, Ack, Abstract.
- Main Text: Introduction, Literature Review, Methodology, Analysis, Findings, Conclusion.
- End Matter: Bibliography/References, Appendices.

2. Writing Abstract:
A concise summary (150-250 words) covering: Background, Purpose, Methods, Key Results, and Conclusion.

3. Citation Styles:
- APA: (Author, Year) - Social Sciences.
- MLA: (Author Page) - Humanities.
- IEEE: [1] - Engineering.
"""
}

paper2_content = {
    "Unit I: Statistical Foundations": """
1. Hypothesis Testing:
- Null Hypothesis (H0): Statement of no significant difference/effect.
- Alternative Hypothesis (H1): Statement of significant difference.
- Type I Error (Alpha): Rejecting H0 when it's true (False Positive).
- Type II Error (Beta): Accepting H0 when it's false (False Negative).

2. Tests of Significance:
- Z-test: For large samples (n>30) or known population SD.
- t-test: For small samples (n<30), population SD unknown. (One-sample, Independent, Paired).
- F-test: Ratio of variances (ANOVA).
- Chi-Square: Test of independence for categorical data.

3. ANOVA (Analysis of Variance):
Used to compare means of 3 or more groups.
F = Variance Between Groups / Variance Within Groups.
""",
    "Unit II: Correlation & Regression": """
1. Correlation Analysis:
- Measures the strength and direction of linear relationship between two variables.
- Pearson's r: Ranges from -1 (Perfect Negative) to +1 (Perfect Positive). 0 means no correlation.
- Coefficient of Determination (R^2): Percentage of variance in DV explained by IV.

2. Regression Analysis:
- Predicting the value of specific variable based on others.
- Simple Linear Regression Model: Y = b0 + b1X + e
  - Y: Dependent Variable
  - X: Independent Variable
  - b0: Intercept
  - b1: Slope
  - e: Error term

3. Assumptions of Linear Regression:
- Linearity: Relationship is linear.
- Independence: Errors are independent.
- Homoscedasticity: Constant variance of errors.
- Normality: Errors are normally distributed.
""",
    "Unit III: Computer Applications": """
1. Types of Software:
- Spreadsheet (Excel): Data entry, basic charts, pivot tables.
- Statistical (SPSS, SAS, R): Complex analysis (ANOVA, Regression, Factor Analysis).
- Qualitative (ATLAS.ti, NVivo): Text analysis, coding.

2. Key Excel Functions:
- =AVERAGE(), =STDEV.P(), =CORREL(), =T.TEST().
- Data Analysis Toolpak: Add-in for Regression, Histograms, etc.

3. SPSS (Statistical Package for Social Sciences):
- Data View vs Variable View.
- Analyze Menu -> Compare Means, Correlate, Regression.
""",
    "Unit IV: Formulas Cheatsheet": """
1. Mean (x-bar) = Sum(x) / n
2. Standard Deviation (s) = Sqrt( Sum(x - x-bar)^2 / n-1 )
3. Standard Error (SE) = s / Sqrt(n)
4. t-statistic = (x-bar - mu) / SE
5. Chi-Square = Sum( (Observed - Expected)^2 / Expected )
6. Pearson Correlation (r) = Cov(x,y) / (SDx * SDy)
"""
}

paper3_content = {
    "Module 1: Philosophy & Ethics": """
1. Introduction:
Ethics (from Greek 'ethos') refers to moral character and principles of right conduct. Research ethics ensures scientific integrity and protection of subjects.

2. Ethical Principles (Belmont Report):
- Respect for Persons: Informed consent, autonomy.
- Beneficence: Do no harm, maximize benefits.
- Justice: Fair distribution of burdens and benefits.

3. Philosophical Frameworks:
- Deontology: Duty-based (follow rules regarding of outcome).
- Consequentialism: Outcome-based (greatest good for greatest number).
- Virtue Ethics: Character-based.
""",
    "Module 2: Scientific Misconduct": """
1. FFP Definition:
- Fabrication: Making up data or results.
- Falsification: Manipulating research materials, equipment, or processes, or changing/omitting data.
- Plagiarism: Appropriating another person's ideas, processes, results, or words without giving appropriate credit.

2. Consequences:
- Retraction of articles.
- Loss of funding.
- Termination of employment.
- Legal action.
""",
    "Module 3: Publication Ethics": """
1. Authorship:
- Substantial contribution to conception/design OR data acquisition/analysis.
- AND drafting/revising critically.
- AND final approval.
- AND agreement to be accountable.

2. Unethical Practices:
- Gift Authorship: Listing authors who didn't contribute.
- Ghost Authorship: Omit authors who contributed.
- Salami Slicing: Splitting data into minimal publishable units.
- Duplicate Publication: Submitting same work to multiple journals.
""",
    "Module 4: Research Metrics": """
1. Impact Factor (IF):
Average number of citations received in a particular year by papers published in the journal during the two preceding years. (Source: Web of Science/Clarivate).

2. h-index:
An author has an index of h if they have published h papers each of which has been cited in other papers at least h times. (Measures productivity + impact).

3. i10-index:
Number of publications with at least 10 citations (Google Scholar metric).
"""
}

# Tabs
tab1, tab2, tab3 = st.tabs(["📝 Paper I", "📐 Paper II", "📚 Paper III"])

with tab1:
    st.markdown("### 📝 Paper I: Research Methodology (Complete Notes)")
    st.write(paper1_content["Unit I: Introduction to Research"]) 
    st.write("*(Preview... download PDF for full content)*")
    
    if st.button("📥 Download Paper I PDF"):
        pdf_data = generate_pdf("Paper I: Research Methodology", paper1_content)
        st.download_button("Click to Save PDF", pdf_data, "Paper_I_Methodology.pdf", "application/pdf")

with tab2:
    st.markdown("### 📐 Paper II: Statistics (Complete Notes)")
    st.write(paper2_content["Unit I: Statistical Foundations"])
    st.write("*(Preview... download PDF for full content)*")

    if st.button("📥 Download Paper II PDF"):
        pdf_data = generate_pdf("Paper II: Statistics & Applications", paper2_content)
        st.download_button("Click to Save PDF", pdf_data, "Paper_II_Statistics.pdf", "application/pdf")

with tab3:
    st.markdown("### 📚 Paper III: Ethics (Complete Notes)")
    st.write(paper3_content["Module 1: Philosophy & Ethics"])
    st.write("*(Preview... download PDF for full content)*")

    if st.button("📥 Download Paper III PDF"):
        pdf_data = generate_pdf("Paper III: Research Ethics", paper3_content)
        st.download_button("Click to Save PDF", pdf_data, "Paper_III_Ethics.pdf", "application/pdf")

show_footer()
