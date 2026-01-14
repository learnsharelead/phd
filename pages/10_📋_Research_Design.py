import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Research Design & Data Collection | Questionnaire Design, Methods [2024]",
    description="Master research design and data collection: questionnaire design, good questionnaire characteristics, data collection methods, survey design for Ph.D. researchers.",
    keywords=[
        "research design",
        "questionnaire design",
        "data collection methods",
        "survey design",
        "good questionnaire",
        "research methodology",
        "interview methods",
        "observation methods",
        "primary data collection"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/methodology/design",
    reading_time=75,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Research Design", "url": "https://researchethics.dev/methodology/design"}
    ],
    course_info={
        "name": "Research Design & Data Collection - Paper I Unit II",
        "description": "Comprehensive guide to research design, questionnaire preparation, and data collection methods.",
        "level": "Doctoral",
        "prerequisites": "Introduction to Research",
        "teaches": ["Research Design", "Questionnaire Design", "Data Collection Methods"],
        "workload": "PT12H",
        "rating": "4.8",
        "rating_count": 756
    }
)
apply_custom_css()
show_top_nav(current_page="Research Design")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📋 Unit II: Research Design & Data Collection</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #1e40af;">Paper I: Research Methodology — Planning your research and gathering data.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📐 Research Design",
    "📝 Questionnaire Design",
    "✅ Good Questionnaire",
    "📊 Data Collection"
])

# =============================================================================
# TAB 1: RESEARCH DESIGN
# =============================================================================
with tab1:
    st.markdown("## 📐 Chapter 1: Research Design")
    
    st.markdown("### 1.1 What is Research Design?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Research Design</b> is the overall plan or blueprint for conducting research. It specifies the methods and procedures for collecting, measuring, and analyzing data to answer research questions.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Architect's Blueprint</h4>
            <p style="margin: 0 !important; font-size: 13px;">Research design is like an <b>architect's blueprint</b>. Before building (collecting data), you need a detailed plan showing what, how, when, and where everything will happen.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📋 Components of Research Design", expanded=True):
        st.markdown("""
        | Component | Question Answered | Example |
        |-----------|-------------------|---------|
        | **Research Problem** | What to study? | Effect of remote work on productivity |
        | **Research Objectives** | What to achieve? | To measure productivity changes |
        | **Research Questions** | Specific queries? | Does remote work increase output? |
        | **Hypothesis** | Expected outcomes? | H₁: Remote workers are more productive |
        | **Variables** | What to measure? | IV: Work location; DV: Productivity |
        | **Population & Sample** | Who to study? | IT employees; 200 from 5 companies |
        | **Data Collection Method** | How to collect? | Survey + time tracking data |
        | **Data Analysis Plan** | How to analyze? | t-test, regression |
        | **Timeline** | When? | 6 months |
        """)

    with st.expander("🔬 Types of Research Design", expanded=True):
        st.markdown("""
        ### Based on Purpose
        
        | Type | Purpose | Example |
        |------|---------|---------|
        | **Exploratory** | Understand new phenomenon | Focus groups on new product |
        | **Descriptive** | Describe characteristics | Market survey |
        | **Causal/Explanatory** | Establish cause-effect | Drug trial |
        
        ### Based on Time
        
        | Type | Description |
        |------|-------------|
        | **Cross-sectional** | Data at one point in time |
        | **Longitudinal** | Data over multiple time points |
        | **Retrospective** | Looking back at past data |
        | **Prospective** | Following subjects into future |
        
        ### Based on Data Type
        
        | Type | Approach |
        |------|----------|
        | **Quantitative** | Numbers, statistics |
        | **Qualitative** | Words, meanings |
        | **Mixed Methods** | Both combined |
        """)

    with st.expander("⚖️ Choosing Research Design", expanded=True):
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=10, shape=box, style="rounded,filled"];
            
            q1 [label="What's your\\nresearch goal?", fillcolor="#dbeafe", shape=diamond];
            
            explore [label="Explore/Understand", fillcolor="#dcfce7"];
            describe [label="Describe", fillcolor="#fef3c7"];
            explain [label="Explain/Cause", fillcolor="#f3e8ff"];
            
            exploratory [label="Exploratory Design\\nQualitative methods\\nInterviews, FGDs", fillcolor="#bbf7d0"];
            descriptive [label="Descriptive Design\\nSurveys, observations", fillcolor="#fde68a"];
            experimental [label="Experimental Design\\nControl groups, RCT", fillcolor="#e9d5ff"];
            
            q1 -> explore -> exploratory;
            q1 -> describe -> descriptive;
            q1 -> explain -> experimental;
        }
        """)

# =============================================================================
# TAB 2: QUESTIONNAIRE DESIGN
# =============================================================================
with tab2:
    st.markdown("## 📝 Chapter 2: Questionnaire Design and Preparation")
    
    st.markdown("### 2.1 What is a Questionnaire?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Questionnaire</b> is a research instrument consisting of a series of questions designed to gather information from respondents. It's a standardized tool that ensures all respondents answer the same questions.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Interview Script</h4>
            <p style="margin: 0 !important; font-size: 13px;">A questionnaire is like a <b>structured interview script</b> that ensures every respondent is asked the same questions in the same order — ensuring consistency and comparability.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📋 Types of Questions", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🔒 Close-Ended Questions</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Definition:</b> Fixed response options<br>
                <b>Types:</b><br>
                • Yes/No (Dichotomous)<br>
                • Multiple choice<br>
                • Rating scales (Likert)<br>
                • Ranking<br>
                <b>Pros:</b> Easy to analyze, consistent<br>
                <b>Cons:</b> May miss nuances
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🔓 Open-Ended Questions</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Definition:</b> Respondent writes own answer<br>
                <b>Types:</b><br>
                • Short answer<br>
                • Essay/paragraph<br>
                • Fill in the blank<br><br>
                <b>Pros:</b> Rich data, unexpected insights<br>
                <b>Cons:</b> Harder to analyze
                </p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("📐 Questionnaire Structure", expanded=True):
        st.markdown("""
        **Recommended Structure:**
        
        | Section | Content | Purpose |
        |---------|---------|---------|
        | **1. Title & Introduction** | Study purpose, consent, instructions | Set expectations |
        | **2. Screening Questions** | Eligibility criteria | Filter respondents |
        | **3. Warm-up Questions** | Easy, non-threatening questions | Build rapport |
        | **4. Main Questions** | Core research questions | Gather key data |
        | **5. Sensitive Questions** | Personal, controversial topics | After trust built |
        | **6. Demographics** | Age, gender, education | Classify respondents |
        | **7. Thank You** | Appreciation, contact info | Close professionally |
        """)

    with st.expander("✍️ Writing Good Questions", expanded=True):
        st.markdown("""
        **DO:**
        - ✅ Use simple, clear language
        - ✅ Ask one thing at a time
        - ✅ Provide balanced response options
        - ✅ Include "Not Applicable" or "Don't Know" options
        - ✅ Order questions logically
        - ✅ Pilot test before use
        
        **DON'T:**
        - ❌ Use jargon or technical terms
        - ❌ Ask leading questions ("Don't you agree...?")
        - ❌ Use double-barreled questions ("Do you like X and Y?")
        - ❌ Use double negatives
        - ❌ Assume knowledge respondent may not have
        - ❌ Ask sensitive questions early
        """)
        
        st.markdown("""
        **Examples:**
        
        | ❌ Bad | ✅ Good |
        |--------|---------|
        | Do you frequently exercise? | How many days per week do you exercise? |
        | Don't you think pollution is bad? | What is your opinion on pollution? |
        | How satisfied are you with salary and benefits? | How satisfied are you with your salary? (separate question for benefits) |
        """)

# =============================================================================
# TAB 3: PREREQUISITES OF GOOD QUESTIONNAIRE
# =============================================================================
with tab3:
    st.markdown("## ✅ Chapter 3: Prerequisites of a Good Questionnaire")
    
    with st.expander("🎯 Characteristics of Good Questionnaire", expanded=True):
        st.markdown("""
        | Characteristic | Description |
        |----------------|-------------|
        | **Validity** | Measures what it intends to measure |
        | **Reliability** | Consistent results across time and respondents |
        | **Clarity** | Questions are easily understood |
        | **Relevance** | Every question serves the research purpose |
        | **Appropriate Length** | Not too long (respondent fatigue) |
        | **Logical Flow** | Natural progression of topics |
        | **Neutral Wording** | No bias or leading questions |
        | **Comprehensive** | Covers all aspects of research |
        | **Anonymity/Confidentiality** | Respondent feels safe to answer honestly |
        """)

    with st.expander("📋 Checklist for Questionnaire Quality", expanded=True):
        st.markdown("""
        **Content Checks:**
        - [ ] Does each question relate to research objectives?
        - [ ] Is the questionnaire comprehensive enough?
        - [ ] Are sensitive questions necessary?
        
        **Wording Checks:**
        - [ ] Is language simple and jargon-free?
        - [ ] Are questions specific, not vague?
        - [ ] Are questions neutral, not leading?
        - [ ] Single-barreled (one question at a time)?
        
        **Structure Checks:**
        - [ ] Logical flow from easy to difficult?
        - [ ] Sensitive questions placed appropriately?
        - [ ] Clear instructions provided?
        
        **Technical Checks:**
        - [ ] Response options mutually exclusive?
        - [ ] Response options exhaustive?
        - [ ] Layout clear and readable?
        - [ ] Skip patterns clear?
        
        **Practical Checks:**
        - [ ] Piloted with similar sample?
        - [ ] Appropriate length (under 15-20 min)?
        - [ ] Works on target platform (paper/online)?
        """)

    with st.expander("🧪 Pilot Testing", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Pilot Testing</b> (Pre-testing) is a trial run of the questionnaire with a small sample similar to the target population to identify problems before full deployment.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **What to Check in Pilot:**
        
        | Aspect | Questions to Ask |
        |--------|------------------|
        | **Clarity** | Did respondents understand all questions? |
        | **Time** | How long did it take to complete? |
        | **Flow** | Did the sequence feel natural? |
        | **Missing Options** | Did respondents need options not provided? |
        | **Technical Issues** | Any problems with format/skip logic? |
        | **Sensitivity** | Did any questions make respondents uncomfortable? |
        
        **Recommended Pilot Sample:** 10-30 respondents, similar to target
        """)

# =============================================================================
# TAB 4: DATA COLLECTION METHODS
# =============================================================================
with tab4:
    st.markdown("## 📊 Chapter 4: Data Collection Methods")
    
    st.markdown("### 4.1 Overview of Methods")
    
    with st.expander("📋 Primary Data Collection Methods", expanded=True):
        st.markdown("""
        | Method | Description | Best For | Limitations |
        |--------|-------------|----------|-------------|
        | **Surveys** | Questionnaire administration | Large samples, generalizable | Self-report bias |
        | **Interviews** | Direct conversation | Depth, clarification | Time-consuming |
        | **Observation** | Watching behavior | Actual behavior | Observer effect |
        | **Experiments** | Controlled manipulation | Causation | Artificial setting |
        | **Focus Groups** | Group discussion | Explore ideas | Groupthink |
        | **Case Studies** | In-depth exploration | Complex phenomena | Not generalizable |
        """)

    with st.expander("📝 Surveys", expanded=True):
        st.markdown("""
        **Types of Survey Administration:**
        
        | Type | Description | Advantages | Disadvantages |
        |------|-------------|------------|---------------|
        | **Online** | Web-based forms | Cheap, fast, wide reach | Digital divide, low response |
        | **Mail** | Postal questionnaire | Geographic spread | Slow, low response |
        | **Telephone** | Phone interview | Quick, can clarify | Expensive, declining response |
        | **Face-to-face** | In-person | High response, rapport | Very expensive, interviewer bias |
        
        **Popular Online Survey Tools:**
        - Google Forms (Free)
        - Microsoft Forms (Free with Office)
        - SurveyMonkey (Freemium)
        - Qualtrics (Professional)
        - LimeSurvey (Open source)
        """)

    with st.expander("🎤 Interviews", expanded=True):
        st.markdown("""
        **Types of Interviews:**
        
        | Type | Structure | Best For |
        |------|-----------|----------|
        | **Structured** | Fixed questions, fixed order | Comparing responses |
        | **Semi-structured** | Some fixed, some flexible | Exploration with focus |
        | **Unstructured** | Conversational, topics only | Deep exploration |
        
        **Interview Best Practices:**
        - Build rapport first
        - Use open-ended questions
        - Listen actively
        - Follow up on interesting points
        - Take notes or record (with consent)
        - Avoid leading questions
        - Maintain neutrality
        """)

    with st.expander("👁️ Observation", expanded=True):
        st.markdown("""
        **Types of Observation:**
        
        | Type | Description |
        |------|-------------|
        | **Participant** | Researcher joins the group |
        | **Non-participant** | Researcher observes from outside |
        | **Structured** | Predetermined categories/checklist |
        | **Unstructured** | Open, exploratory |
        | **Overt** | Participants know they're observed |
        | **Covert** | Participants don't know |
        
        **Considerations:**
        - Hawthorne Effect: People change behavior when observed
        - Observer bias: Researcher sees what they expect
        - Ethics: Informed consent for overt observation
        """)

    with st.expander("🔬 Choosing Data Collection Method", expanded=True):
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=10, shape=box, style="rounded,filled"];
            
            q1 [label="What do you\\nneed to know?", fillcolor="#dbeafe", shape=diamond];
            
            what [label="What people SAY", fillcolor="#dcfce7"];
            do [label="What people DO", fillcolor="#fef3c7"];
            deep [label="Deep understanding", fillcolor="#f3e8ff"];
            
            survey [label="Surveys/\\nInterviews", fillcolor="#bbf7d0"];
            observe [label="Observation/\\nExperiment", fillcolor="#fde68a"];
            qual [label="Interviews/\\nCase Studies", fillcolor="#e9d5ff"];
            
            q1 -> what -> survey;
            q1 -> do -> observe;
            q1 -> deep -> qual;
        }
        """)
        
        st.markdown("""
        **Factors in Method Selection:**
        - Research objectives and questions
        - Nature of variables (observable vs. internal)
        - Available resources (time, money, personnel)
        - Required sample size
        - Population accessibility
        - Level of control needed
        - Ethical considerations
        """)

# Footer
show_footer()
