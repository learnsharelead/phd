import streamlit as st
import io
from fpdf import FPDF
from utils.styles import apply_custom_css, show_footer
from utils.nav import show_top_nav

apply_custom_css()
show_top_nav(current_page="Downloads")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-radius: 10px; margin-bottom: 20px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📥 Downloadable Study Materials (PDF)</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #92400e;">Download printable PDF notes for all papers.</p>
</div>
""", unsafe_allow_html=True)

# Helper function to create PDF
def create_pdf(title, sections):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, title, ln=True, align='C')
    pdf.ln(10)
    
    # Content
    for section_title, content in sections.items():
        pdf.set_font("Arial", "B", 12)
        pdf.set_fill_color(240, 240, 240)
        pdf.cell(0, 10, section_title, ln=True, fill=True)
        pdf.ln(2)
        
        pdf.set_font("Arial", "", 10)
        # Fix for latin-1 encoding issues common in FPDF
        content = content.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 6, content)
        pdf.ln(5)
        
    return pdf.output(dest="S").encode("latin-1")

# Tabs
tab1, tab2, tab3 = st.tabs(["📝 Paper I: Methodology", "📐 Paper II: Statistics", "📚 Paper III: Ethics"])

# =============================================================================
# PAPER I
# =============================================================================
with tab1:
    st.markdown("### 📥 Paper I: Research Methodology")
    st.info("Download complete PDF notes for Paper I.")
    
    paper1_sections = {
        "Unit I: Introduction to Research": """
Meaning of Research: Systematic process of collecting and analyzing data.
Objectives: To gain familiarity, portray characteristics, test hypotheses.
Types: Fundamental vs Applied, quantitative vs Qualitative.
Research Process: 1. Problem 2. Literature 3. Hypothesis 4. Design 5. Data 6. Analysis 7. Report.
""",
        "Unit II: Research Design": """
Definition: The blueprint for collection, measurement, and analysis of data.
Types: Exploratory (to clarify), Descriptive (characteristics), Experimental (cause-effect).
Variables: Independent (IV), Dependent (DV), Extraneous, Control.
Experimental Designs: CRD, RBD, LSD, Factorial Designs.
""",
        "Unit III: Measurement & Sampling": """
Scales: Nominal (label), Ordinal (rank), Interval (dist), Ratio (zero).
Validity: Content, Criterion, Construct.
Reliability: Test-retest, Split-half, Cronbach's Alpha.
Sampling: Probability (Random, Stratified) vs Non-Probability (Convenience, Snowball).
Sample Size: Cochran's Formula n = Z^2*p*q/e^2.
""",
        "Unit IV: Report Writing": """
Structure: Title, Abstract, Intro, Methods, Results, Discussion, Refs.
Citation Styles: APA (Author, Year), MLA (Author Page), IEEE (Numbers).
Abstract: 150-250 words summary.
Plagiarism: Using others work without credit.
"""
    }
    
    if st.button("Generate Paper I PDF"):
        pdf_bytes = create_pdf("Paper I: Research Methodology - Complete Notes", paper1_sections)
        st.download_button(
            label="📥 Download Paper I PDF",
            data=pdf_bytes,
            file_name="Paper_I_Methodology.pdf",
            mime="application/pdf"
        )
    
    st.markdown("**Preview of Notes:**")
    st.text(paper1_sections["Unit I: Introduction to Research"])

# =============================================================================
# PAPER II
# =============================================================================
with tab2:
    st.markdown("### 📥 Paper II: Statistics")
    st.info("Download complete PDF notes for Paper II.")
    
    paper2_sections = {
        "Unit I: Statistical Foundations": """
Parametric Tests: Assume normal distribution (t-test, ANOVA).
Non-Parametric: Distribution-free (Mann-Whitney, Kruskal-Wallis).
Hypothesis Testing:
- Null (H0): No difference.
- Alternative (H1): Difference exists.
Type I Error (Alpha): Reject true H0.
Type II Error (Beta): Accept false H0.
""",
        "Unit II: Correlation & Regression": """
Pearson Correlation (r): Measures linear relationship (-1 to +1).
R-squared: Variation explained.
Linear Regression: Y = b0 + b1X.
Least Squares Method: Minimizes sum of squared errors.
Assumptions: Linearity, Independence, Homoscedasticity, Normality.
""",
        "Unit III: Computer Applications": """
Excel: Basic stats (AVERAGE, STDEV), charts, pivot tables.
SPSS: Menu-driven analysis, Variable View vs Data View.
R: Statistical programming, extensive packages.
LaTeX: Document preparation for math/science.
""",
        "Unit IV: Formulas Cheatsheet": """
Mean: Sum(X)/n
Variance: Sum(X-Mean)^2 / (n-1)
t-test: (Mean - Mu) / (SD / sqrt(n))
Chi-square: Sum (O-E)^2 / E
Pearson r: Cov(X,Y) / (SDx * SDy)
"""
    }
    
    if st.button("Generate Paper II PDF"):
        pdf_bytes = create_pdf("Paper II: Statistics - Complete Notes", paper2_sections)
        st.download_button(
            label="📥 Download Paper II PDF",
            data=pdf_bytes,
            file_name="Paper_II_Statistics.pdf",
            mime="application/pdf"
        )

# =============================================================================
# PAPER III
# =============================================================================
with tab3:
    st.markdown("### 📥 Paper III: Research Ethics")
    st.info("Download complete PDF notes for Paper III.")
    
    paper3_sections = {
        "Module 1: Philosophy & Ethics": """
Ethics: Moral principles governing research.
Values: Honesty, Integrity, Objectivity.
Theories: Utilitarianism (consequences), Deontology (duty).
""",
        "Module 2: Scientific Misconduct": """
FFP:
- Fabrication: Making up data.
- Falsification: Manipulating data.
- Plagiarism: Stealing ideas/text.
Consequences: Retraction, ban, reputation loss.
""",
        "Module 3: Publication Ethics": """
Authorship: ICMJE Criteria (Contribution, Drafting, Approval, Accountability).
Redundant Publication: Duplicate or Salami Slicing.
COI: Conflict of Interest (Financial/Personal).
""",
        "Module 4: Research Metrics": """
Impact Factor: Avg citations in 2 years.
h-index: h papers with h citations.
Databases: Web of Science, Scopus.
"""
    }
    
    if st.button("Generate Paper III PDF"):
        pdf_bytes = create_pdf("Paper III: Research Ethics - Complete Notes", paper3_sections)
        st.download_button(
            label="📥 Download Paper III PDF",
            data=pdf_bytes,
            file_name="Paper_III_Ethics.pdf",
            mime="application/pdf"
        )

show_footer()
