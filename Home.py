import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav
import random

# Expert SEO Setup
inject_seo_meta(
    title="Ph.D. Research Methods Hub | Complete Coursework Platform [2024]",
    description="Complete Ph.D. coursework: Research Methodology (Paper I), Statistics & Computer Applications (Paper II), Ethics in Research (Paper III). Formulas, tutorials, case studies, and cheat sheets.",
    keywords=[
        "phd research methodology",
        "statistics for phd",
        "research ethics course",
        "research design",
        "hypothesis testing",
        "spss tutorial",
        "cronbach alpha",
        "impact factor",
        "plagiarism detection",
        "sampling methods",
        "data collection methods",
        "research report writing"
    ],
    schema_type="Course",
    canonical_url="https://phd-research-hub.dev",
    reading_time=240,
    breadcrumbs=[
        {"name": "Home", "url": "https://phd-research-hub.dev"}
    ],
    course_info={
        "name": "Ph.D. Research Methods - Complete 3-Paper Coursework",
        "description": "Comprehensive doctoral coursework covering Research Methodology, Statistics and Computer Applications, and Ethics in Research and Publications.",
        "level": "Doctoral",
        "prerequisites": "Graduate degree",
        "teaches": ["Research Methodology", "Statistics", "Computer Applications", "Research Ethics", "Publication Ethics"],
        "workload": "PT120H",
        "rating": "4.9",
        "rating_count": 2847
    },
    faq_items=[
        {
            "question": "What is covered in this Ph.D. coursework?",
            "answer": "This platform covers three papers: Paper I (Research Methodology), Paper II (Statistics and Computer Applications), and Paper III (Ethics in Research and Publications)."
        },
        {
            "question": "What is Cronbach's Alpha?",
            "answer": "Cronbach's Alpha is a measure of internal consistency reliability, ranging from 0 to 1. Values above 0.70 are generally considered acceptable for research instruments."
        }
    ]
)

# Styles
apply_custom_css()

# Top Navigation (Home)
show_top_nav(current_page="Home")

# Header
st.markdown("""
<div style="display: flex; align-items: center; justify-content: center; gap: 15px; padding: 20px 0; margin-bottom: 10px;">
    <div style="font-size: 52px;">🎓</div>
    <div>
        <h1 style='margin: 0 !important; font-size: 32px !important; font-weight: 800; letter-spacing: -1px; color: #111827; line-height: 1.1;'>
            Ph.D. Research <span style='background: linear-gradient(135deg, #1e40af 0%, #7c3aed 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Methods</span> Hub
        </h1>
        <div style="font-size: 14px; color: #64748b; margin-top: 5px;">Complete Coursework Platform for Doctoral Research</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Stats
stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
with stats_col1:
    st.markdown("""
    <div style="text-align: center; background: #eff6ff; padding: 12px; border-radius: 8px;">
        <div style="font-size: 24px; font-weight: 700; color: #1e40af;">3</div>
        <div style="font-size: 11px; color: #64748b;">Papers</div>
    </div>
    """, unsafe_allow_html=True)
with stats_col2:
    st.markdown("""
    <div style="text-align: center; background: #f0fdf4; padding: 12px; border-radius: 8px;">
        <div style="font-size: 24px; font-weight: 700; color: #16a34a;">12</div>
        <div style="font-size: 11px; color: #64748b;">Units</div>
    </div>
    """, unsafe_allow_html=True)
with stats_col3:
    st.markdown("""
    <div style="text-align: center; background: #fef3c7; padding: 12px; border-radius: 8px;">
        <div style="font-size: 24px; font-weight: 700; color: #b45309;">50+</div>
        <div style="font-size: 11px; color: #64748b;">Formulas</div>
    </div>
    """, unsafe_allow_html=True)
with stats_col4:
    st.markdown("""
    <div style="text-align: center; background: #faf5ff; padding: 12px; border-radius: 8px;">
        <div style="font-size: 24px; font-weight: 700; color: #7c3aed;">6</div>
        <div style="font-size: 11px; color: #64748b;">Credits</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
 
# Daily Research Tip
tips = [
    "Always backup your raw data in at least 3 locations (3-2-1 rule).",
    "Write your abstract last. It should be a summary of what you did, not a plan.",
    "Use reference management software (Zotero, Mendeley) from Day 1.",
    "Reviewers are critical but their goal is usually to improve your paper.",
    "A null result is still a result. Don't hide it!",
    "Read the journal's 'Guide for Authors' BEFORE formatting your paper.",
    "Correlation does not imply causation. Always check for confounding variables.",
    "Keep a research journal. Document your thought process, not just results.",
    "The h-index is just one metric. It doesn't define your worth as a researcher."
]
todays_tip = random.choice(tips)

st.markdown(f"""
<div style="background: linear-gradient(to right, #fffbeb, #fff); padding: 15px; border-radius: 10px; border-left: 5px solid #fbbf24; margin-bottom: 20px; display: flex; align-items: center; gap: 15px;">
    <div style="font-size: 24px;">💡</div>
    <div>
        <div style="font-weight: 700; color: #b45309; font-size: 14px;">Daily Research Tip</div>
        <div style="font-size: 14px; color: #78350f; font-style: italic;">"{todays_tip}"</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================================
# PAPER I - RESEARCH METHODOLOGY
# ============================================================================
st.markdown("""
<div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 18px; border-radius: 12px; margin-bottom: 15px; border: 1px solid #86efac;">
    <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 12px;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <div style="font-size: 32px;">📝</div>
            <div>
                <h3 style="margin: 0 !important; color: #166534; font-size: 1.2rem;">Paper I: Research Methodology</h3>
                <p style="margin: 0 !important; font-size: 12px; color: #166534;">Foundation of research concepts, design, data collection, and scholarly reporting</p>
            </div>
        </div>
        <div>
             <a href="/Phd_Toolkit" target="_self" style="text-decoration: none;">
                <button style="border: 1px solid #166534; background: white; color: #166534; padding: 5px 10px; border-radius: 5px; cursor: pointer; font-size: 12px; font-weight: 600;">🛠️ Open Toolkit</button>
             </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

p1_col1, p1_col2 = st.columns(2)

with p1_col1:
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #166534;">🔬 Unit I: Introduction to Research</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Types of research • Research procedures • Literature survey • Hypothesis formulation</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit I", key="p1u1", use_container_width=True):
        st.switch_page("pages/9_🔬_Intro_Research.py")
    
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #166534;">📏 Unit III: Measurement & Sampling</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Validity • Reliability • Cronbach's Alpha • Scales • Sampling methods</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit III", key="p1u3", use_container_width=True):
        st.switch_page("pages/11_📏_Measurement_Sampling.py")

with p1_col2:
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #166534;">📋 Unit II: Research Design</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Research design • Questionnaire design • Data collection methods</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit II", key="p1u2", use_container_width=True):
        st.switch_page("pages/10_📋_Research_Design.py")
    
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #166534;">📄 Unit IV: Report & Publication</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Report writing • Publication process • Research metrics • Ethics</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit IV", key="p1u4", use_container_width=True):
        st.switch_page("pages/12_📄_Report_Publication.py")

# ============================================================================
# PAPER II - STATISTICS
# ============================================================================
st.markdown("""
<div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 18px; border-radius: 12px; margin-bottom: 15px; border: 1px solid #93c5fd;">
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
        <div style="font-size: 32px;">📐</div>
        <div>
            <h3 style="margin: 0 !important; color: #1e40af; font-size: 1.2rem;">Paper II: Statistics and Computer Applications</h3>
            <p style="margin: 0 !important; font-size: 12px; color: #1e40af;">Statistical tools and software skills for research data analysis</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

p2_col1, p2_col2 = st.columns(2)

with p2_col1:
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #1e40af;">📐 Unit I: Statistical Foundations</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Hypothesis testing • t-test • ANOVA • Chi-square • Non-parametric tests</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit I", key="p2u1", use_container_width=True):
        st.switch_page("pages/5_📐_Statistical_Foundations.py")
    
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #1e40af;">💻 Unit III: Computer Applications</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Excel • SPSS • R • MATLAB • LaTeX • ATLAS.ti • AMOS</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit III", key="p2u3", use_container_width=True):
        st.switch_page("pages/7_💻_Computer_Applications.py")

with p2_col2:
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #1e40af;">📈 Unit II: Correlation & Regression</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Correlation • Curve fitting • Least squares • Gauss-Markov • Multiple regression</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit II", key="p2u2", use_container_width=True):
        st.switch_page("pages/6_📈_Correlation_Regression.py")
    
    st.markdown("""
    <div style="background: #fef3c7; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #fcd34d;">
        <div style="font-weight: 600; font-size: 14px; color: #92400e;">📝 Formula Cheat Sheet</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">All formulas • Memory tips • Quick reference • Learning strategies</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("View Cheat Sheet", key="cheat", use_container_width=True):
        st.switch_page("pages/8_📝_Formula_Cheat_Sheet.py")

# ============================================================================
# PAPER III - ETHICS
# ============================================================================
st.markdown("""
<div style="background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); padding: 18px; border-radius: 12px; margin-bottom: 15px; border: 1px solid #d8b4fe;">
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
        <div style="font-size: 32px;">📚</div>
        <div>
            <h3 style="margin: 0 !important; color: #7c3aed; font-size: 1.2rem;">Paper III: Ethics in Research and Publications</h3>
            <p style="margin: 0 !important; font-size: 12px; color: #7c3aed;">Building ethical researchers with integrity in scientific conduct</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

p3_col1, p3_col2 = st.columns(2)

with p3_col1:
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #7c3aed;">📖 Unit I: Philosophy & Ethics</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Philosophy • Ethics • Research integrity • FFP • Authorship</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit I", key="p3u1", use_container_width=True):
        st.switch_page("pages/1_📖_Philosophy_Ethics.py")
    
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #7c3aed;">🔧 Unit III: Online Tools</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Open Access • SHERPA/RoMEO • Predatory journals • Turnitin</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit III", key="p3u3", use_container_width=True):
        st.switch_page("pages/3_🔧_Online_Tools.py")

with p3_col2:
    st.markdown("""
    <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #e2e8f0;">
        <div style="font-weight: 600; font-size: 14px; color: #7c3aed;">📊 Unit II: Research Metrics</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Impact Factor • h-index • Scopus • Web of Science • Databases</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Unit II", key="p3u2", use_container_width=True):
        st.switch_page("pages/2_📊_Research_Metrics.py")
    
    st.markdown("""
    <div style="background: #fef2f2; padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 1px solid #fecaca;">
        <div style="font-weight: 600; font-size: 14px; color: #dc2626;">📋 Case Studies</div>
        <div style="font-size: 11px; color: #64748b; margin-top: 4px;">Fraud cases from India & abroad • Ethical dilemmas • Lessons</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("View Case Studies", key="cases", use_container_width=True):
        st.switch_page("pages/4_📋_Case_Studies.py")

st.markdown("---")

# ============================================================================
# FEATURES & REFERENCES
# ============================================================================
st.markdown("### ✨ What Makes This Platform Special")

feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4)
with feat_col1:
    st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <div style="font-size: 28px;">📐</div>
        <div style="font-size: 13px; font-weight: 600; margin-top: 5px;">All Formulas</div>
        <div style="font-size: 11px; color: #64748b;">With derivations & examples</div>
    </div>
    """, unsafe_allow_html=True)
with feat_col2:
    st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <div style="font-size: 28px;">💡</div>
        <div style="font-size: 13px; font-weight: 600; margin-top: 5px;">Memory Tips</div>
        <div style="font-size: 11px; color: #64748b;">Mnemonics & analogies</div>
    </div>
    """, unsafe_allow_html=True)
with feat_col3:
    st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <div style="font-size: 28px;">📊</div>
        <div style="font-size: 13px; font-weight: 600; margin-top: 5px;">Visual Diagrams</div>
        <div style="font-size: 11px; color: #64748b;">Flowcharts & tables</div>
    </div>
    """, unsafe_allow_html=True)
with feat_col4:
    st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <div style="font-size: 28px;">📋</div>
        <div style="font-size: 13px; font-weight: 600; margin-top: 5px;">Case Studies</div>
        <div style="font-size: 11px; color: #64748b;">Real-world examples</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# References
with st.expander("📚 References & Recommended Readings"):
    st.markdown("""
    **Core Textbooks:**
    - **C.R. Kothari** – *Research Methodology: Methods and Techniques*
    - **Gupta & Kapoor** – *Fundamentals of Mathematical Statistics*
    - **Mark Gardener** – *Beginning R*
    - **MATLAB Programming** – *PHI*
    - **SPSS Handbook** – *Himalaya Publishing*
    
    **Additional Resources:**
    - ACM Digital Library
    - IEEE Xplore
    - Elsevier ScienceDirect
    - Springer Nature
    - COPE (Committee on Publication Ethics)
    - ORI (Office of Research Integrity)
    """)

# Footer
show_footer()
