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

# =============================================================================
# COMPREHENSIVE QUESTIONNAIRE DESIGN ADDITIONS
# =============================================================================

# Add to Tab 2 (Questionnaire Design)
with tab2:
    with st.expander("📊 Response Scales - Complete Guide", expanded=True):
        st.markdown("""
        ### Likert Scales (Most Common)
        
        **5-Point Likert Scale:**
        ```
        Question: "I am satisfied with my job"
        
        1 = Strongly Disagree
        2 = Disagree
        3 = Neutral
        4 = Agree
        5 = Strongly Agree
        ```
        
        **When to Use:**
        - Measuring attitudes, opinions, perceptions
        - Need quantitative data from subjective responses
        - Want to measure intensity of feelings
        
        **Variations:**
        - **7-Point**: More granularity (1-7)
        - **4-Point**: Force choice (no neutral option)
        - **Semantic Differential**: Opposite adjectives (e.g., Happy 1-2-3-4-5 Sad)
        
        ---
        ### Rating Scales
        
        **Numerical Rating (0-10):**
        ```
        "On a scale of 0-10, how likely are you to recommend our product?"
        
        0 = Not at all likely
        10 = Extremely likely
        ```
        
        **Frequency Scale:**
        ```
        "How often do you exercise?"
        
        □ Never
        □ Rarely (less than once a month)
        □ Sometimes (1-3 times a month)
        □ Often (1-2 times a week)
        □ Very Often (3+ times a week)
        □ Always (daily)
        ```
        
        ---
        ### Multiple Choice
        
        **Single Answer:**
        ```
        "What is your highest level of education?"
        
        ○ High School
        ○ Bachelor's Degree
        ○ Master's Degree
        ○ Doctoral Degree
        ○ Other: __________
        ```
        
        **Multiple Answers:**
        ```
        "Which social media platforms do you use? (Check all that apply)"
        
        ☐ Facebook
        ☐ Instagram
        ☐ Twitter
        ☐ LinkedIn
        ☐ TikTok
        ☐ Other: __________
        ```
        
        ---
        ### Ranking Questions
        
        ```
        "Rank the following factors in order of importance when choosing a job
        (1 = Most important, 5 = Least important)"
        
        ___ Salary
        ___ Work-life balance
        ___ Career growth
        ___ Company culture
        ___ Location
        ```
        
        **Tip:** Limit to 5-7 items maximum (cognitive overload beyond that)
        
        ---
        ### Dichotomous (Yes/No)
        
        ```
        "Have you purchased from us before?"
        
        ○ Yes
        ○ No
        ```
        
        **When to Use:**
        - Screening questions
        - Simple factual information
        - Skip logic triggers
        
        ---
        ### Matrix/Grid Questions
        
        ```
        "Please rate your satisfaction with the following aspects:"
        
                            Very      Somewhat   Neutral   Somewhat    Very
                          Satisfied  Satisfied           Dissatisfied Dissatisfied
        Product Quality      ○          ○         ○          ○           ○
        Customer Service     ○          ○         ○          ○           ○
        Delivery Speed       ○          ○         ○          ○           ○
        Value for Money      ○          ○         ○          ○           ○
        ```
        
        **Pros:** Efficient, easy to complete  
        **Cons:** Can lead to straight-lining (same answer for all)
        """)
    
    with st.expander("✅ Complete Questionnaire Example", expanded=True):
        st.markdown("""
        ### Employee Satisfaction Survey (Sample)
        
        ---
        **SECTION 1: INTRODUCTION**
        
        **Title:** Employee Satisfaction Survey 2024
        
        **Purpose:** This survey aims to understand your experience working at [Company Name]. 
        Your honest feedback will help us improve our workplace.
        
        **Confidentiality:** All responses are anonymous and confidential.
        
        **Time:** Approximately 10 minutes
        
        **Instructions:** Please answer all questions honestly. There are no right or wrong answers.
        
        ---
        **SECTION 2: SCREENING**
        
        1. Are you currently employed at [Company Name]?
           - ○ Yes → Continue
           - ○ No → End survey
        
        2. How long have you worked here?
           - ○ Less than 6 months
           - ○ 6 months - 1 year
           - ○ 1-3 years
           - ○ 3-5 years
           - ○ More than 5 years
        
        ---
        **SECTION 3: JOB SATISFACTION (Likert Scale)**
        
        *Please indicate your level of agreement with each statement:*
        
        (1 = Strongly Disagree, 5 = Strongly Agree)
        
        3. I am satisfied with my current role.
           1 - 2 - 3 - 4 - 5
        
        4. I have the resources I need to do my job effectively.
           1 - 2 - 3 - 4 - 5
        
        5. My workload is manageable.
           1 - 2 - 3 - 4 - 5
        
        6. I receive adequate support from my manager.
           1 - 2 - 3 - 4 - 5
        
        7. I feel valued by the organization.
           1 - 2 - 3 - 4 - 5
        
        ---
        **SECTION 4: WORK ENVIRONMENT**
        
        8. How would you rate the following aspects of your work environment?
        
        |                    | Excellent | Good | Fair | Poor | Very Poor |
        |--------------------|-----------|------|------|------|-----------|
        | Office facilities  |     ○     |  ○   |  ○   |  ○   |     ○     |
        | Technology/tools   |     ○     |  ○   |  ○   |  ○   |     ○     |
        | Team collaboration |     ○     |  ○   |  ○   |  ○   |     ○     |
        | Communication      |     ○     |  ○   |  ○   |  ○   |     ○     |
        
        ---
        **SECTION 5: OPEN-ENDED**
        
        9. What do you like most about working here?
           _____________________________________________________________
           _____________________________________________________________
        
        10. What one thing would you change to improve your experience?
            _____________________________________________________________
            _____________________________________________________________
        
        ---
        **SECTION 6: DEMOGRAPHICS**
        
        11. Department:
            - ○ Sales
            - ○ Marketing
            - ○ IT
            - ○ HR
            - ○ Operations
            - ○ Other: __________
        
        12. Age group:
            - ○ 18-25
            - ○ 26-35
            - ○ 36-45
            - ○ 46-55
            - ○ 56+
        
        13. Gender:
            - ○ Male
            - ○ Female
            - ○ Non-binary
            - ○ Prefer not to say
        
        ---
        **SECTION 7: CLOSING**
        
        Thank you for completing this survey! Your feedback is valuable and will be used 
        to improve our workplace.
        
        If you have any questions, please contact: hr@company.com
        
        ---
        ### Analysis Plan for This Survey
        
        **Quantitative Analysis:**
        - Calculate mean satisfaction scores (Questions 3-7)
        - Compare scores across departments (ANOVA)
        - Correlation between tenure and satisfaction
        - Cross-tabulation of ratings by demographics
        
        **Qualitative Analysis:**
        - Code open-ended responses (Questions 9-10)
        - Identify common themes
        - Extract representative quotes
        
        **Reporting:**
        - Overall satisfaction score: Average of Q3-7
        - Department comparison charts
        - Word cloud from open responses
        - Recommendations based on findings
        """)
    
    with st.expander("🎯 Pilot Testing Your Questionnaire", expanded=True):
        st.markdown("""
        ### Why Pilot Test?
        
        **Purpose:**
        - Identify confusing questions
        - Check question flow and logic
        - Estimate completion time
        - Test skip logic and branching
        - Detect technical issues (online surveys)
        
        ---
        ### How to Conduct a Pilot Test
        
        **Step 1: Select Pilot Sample**
        - Size: 10-30 people (similar to target population)
        - Not part of final sample
        - Representative of target audience
        
        **Step 2: Administer Survey**
        - Same conditions as final survey
        - Time how long it takes
        - Observe any difficulties
        
        **Step 3: Debrief**
        Ask pilot participants:
        - Were any questions confusing?
        - Were any questions offensive or sensitive?
        - Was anything missing?
        - How long did it take?
        - Any technical issues?
        
        **Step 4: Analyze Results**
        - Check for missing data patterns
        - Look for questions everyone skipped
        - Identify questions with no variance (everyone same answer)
        - Review open-ended responses for clarity
        
        **Step 5: Revise**
        - Reword confusing questions
        - Remove redundant questions
        - Add missing response options
        - Fix technical issues
        - Adjust length if too long
        
        **Step 6: Re-test (if major changes)**
        - If significant revisions, pilot again
        - Small tweaks don't need re-testing
        
        ---
        ### Pilot Test Checklist
        
        ✅ Questions are clear and unambiguous  
        ✅ Response options are exhaustive and mutually exclusive  
        ✅ No leading or biased questions  
        ✅ Logical flow and order  
        ✅ Skip logic works correctly  
        ✅ Completion time is reasonable (< 15 minutes ideal)  
        ✅ No technical glitches  
        ✅ Instructions are clear  
        ✅ All questions are necessary  
        ✅ Sensitive questions handled appropriately  
        """)

# Add to Tab 4 (Data Collection)
with tab4:
    with st.expander("📊 Primary vs Secondary Data", expanded=True):
        st.markdown("""
        ### Primary Data
        
        **Definition:** Data collected firsthand by the researcher for the specific study
        
        **Methods:**
        - Surveys/Questionnaires
        - Interviews (structured, semi-structured, unstructured)
        - Observations (participant, non-participant)
        - Experiments
        - Focus groups
        
        **Advantages:**
        - ✅ Specific to your research question
        - ✅ Current and up-to-date
        - ✅ Control over quality
        - ✅ Know the methodology
        
        **Disadvantages:**
        - ❌ Time-consuming
        - ❌ Expensive
        - ❌ Requires expertise
        - ❌ May have small sample
        
        **Example:**
        Conducting a survey of 500 employees to measure job satisfaction at your company.
        
        ---
        ### Secondary Data
        
        **Definition:** Data collected by someone else for a different purpose
        
        **Sources:**
        - Published research papers
        - Government databases (Census, Labor Statistics)
        - Company reports
        - Historical records
        - Existing datasets
        
        **Advantages:**
        - ✅ Quick and inexpensive
        - ✅ Large sample sizes
        - ✅ Historical data available
        - ✅ Professional collection
        
        **Disadvantages:**
        - ❌ May not fit your exact needs
        - ❌ Could be outdated
        - ❌ Unknown quality/bias
        - ❌ Limited control
        
        **Example:**
        Using national employment statistics from government databases to compare with your findings.
        
        ---
        ### Comparison Table
        
        | Aspect | Primary Data | Secondary Data |
        |--------|--------------|----------------|
        | **Cost** | High | Low |
        | **Time** | Months | Days/Weeks |
        | **Specificity** | Exact fit | May not fit perfectly |
        | **Control** | Full control | No control |
        | **Sample Size** | Usually smaller | Often larger |
        | **Currency** | Current | May be outdated |
        | **Reliability** | You ensure it | Must verify |
        
        ---
        ### When to Use Each
        
        **Use Primary Data When:**
        - No existing data on your topic
        - Need very specific information
        - Studying current/emerging phenomena
        - Need to control methodology
        
        **Use Secondary Data When:**
        - Exploratory research
        - Limited budget/time
        - Need large sample or historical data
        - Validating primary findings
        
        **Best Practice:** Use both!
        - Secondary data for context and comparison
        - Primary data for specific research questions
        """)
    
    with st.expander("📋 Survey Methods Comparison", expanded=True):
        st.markdown("""
        ### 1. Online Surveys
        
        **Tools:** Google Forms, SurveyMonkey, Qualtrics, Typeform
        
        **Advantages:**
        - ✅ Low cost
        - ✅ Fast distribution
        - ✅ Easy data collection
        - ✅ Skip logic possible
        - ✅ Wide geographic reach
        - ✅ Automatic data entry
        
        **Disadvantages:**
        - ❌ Requires internet access
        - ❌ Lower response rates (10-30%)
        - ❌ Sample bias (tech-savvy only)
        - ❌ No clarification possible
        
        **Best For:** Large samples, tech-savvy populations, budget constraints
        
        **Tips:**
        - Keep it short (< 10 minutes)
        - Mobile-friendly design
        - Send reminders
        - Offer incentives
        
        ---
        ### 2. Mail Surveys
        
        **Advantages:**
        - ✅ Reaches all demographics
        - ✅ Respondent can take time
        - ✅ No interviewer bias
        - ✅ Good for sensitive topics
        
        **Disadvantages:**
        - ❌ Expensive (printing, postage)
        - ❌ Slow (weeks to months)
        - ❌ Low response rate (5-20%)
        - ❌ No control over who responds
        
        **Best For:** Older populations, rural areas, official surveys
        
        **Tips:**
        - Include prepaid return envelope
        - Professional appearance
        - Clear instructions
        - Follow-up mailings
        
        ---
        ### 3. Telephone Surveys
        
        **Advantages:**
        - ✅ Higher response rate (30-50%)
        - ✅ Can clarify questions
        - ✅ Faster than mail
        - ✅ Can reach non-internet users
        
        **Disadvantages:**
        - ❌ Expensive (interviewer costs)
        - ❌ Time-consuming
        - ❌ Interviewer bias possible
        - ❌ Declining landline use
        - ❌ Spam call concerns
        
        **Best For:** Older adults, complex questions, need for clarification
        
        **Tips:**
        - Train interviewers thoroughly
        - Call at convenient times
        - Keep it brief (< 15 minutes)
        - Record calls (with permission)
        
        ---
        ### 4. Face-to-Face Interviews
        
        **Advantages:**
        - ✅ Highest response rate (70-90%)
        - ✅ Can observe non-verbal cues
        - ✅ Can clarify and probe
        - ✅ Can use visual aids
        - ✅ Build rapport
        
        **Disadvantages:**
        - ❌ Very expensive
        - ❌ Time-intensive
        - ❌ Geographic limitations
        - ❌ Interviewer bias
        - ❌ Social desirability bias
        
        **Best For:** Complex topics, qualitative depth, illiterate populations
        
        **Tips:**
        - Choose neutral location
        - Dress appropriately
        - Build rapport first
        - Record (with permission)
        
        ---
        ### 5. Mixed-Mode Surveys
        
        **Approach:** Combine multiple methods
        
        **Example:**
        - Initial online survey
        - Follow-up phone calls for non-responders
        - Face-to-face for specific subgroups
        
        **Advantages:**
        - ✅ Higher overall response rate
        - ✅ Reaches diverse populations
        - ✅ Reduces bias
        
        **Disadvantages:**
        - ❌ More complex
        - ❌ Higher cost
        - ❌ Mode effects (different methods → different answers)
        
        ---
        ### Comparison Table
        
        | Method | Cost | Speed | Response Rate | Sample Bias |
        |--------|------|-------|---------------|-------------|
        | **Online** | Low | Fast | 10-30% | Tech-savvy |
        | **Mail** | High | Slow | 5-20% | Literate |
        | **Phone** | Medium | Medium | 30-50% | Landline owners |
        | **Face-to-Face** | Very High | Slow | 70-90% | Accessible |
        | **Mixed-Mode** | High | Medium | 40-60% | Reduced |
        
        ---
        ### Choosing the Right Method
        
        **Consider:**
        1. **Budget:** How much can you spend?
        2. **Timeline:** How quickly do you need data?
        3. **Population:** Who are your respondents?
        4. **Topic:** How sensitive/complex?
        5. **Sample Size:** How many responses needed?
        6. **Geographic Spread:** Local or national?
        7. **Response Rate:** How critical is high response?
        """)
    
    with st.expander("🎯 Maximizing Response Rates", expanded=True):
        st.markdown("""
        ### Before Distribution
        
        **1. Design a Good Questionnaire**
        - Short and focused (< 10 minutes)
        - Clear and simple language
        - Professional appearance
        - Mobile-friendly (for online)
        
        **2. Choose the Right Method**
        - Match method to population
        - Consider accessibility
        
        **3. Timing**
        - Avoid holidays and busy periods
        - Send on Tuesday-Thursday (best response)
        - Mid-morning or early afternoon
        
        ---
        ### During Distribution
        
        **4. Personalization**
        - Use respondent's name
        - Explain why they were chosen
        - Show relevance to them
        
        **5. Clear Communication**
        - Explain purpose clearly
        - Emphasize confidentiality
        - State time required
        - Explain how data will be used
        
        **6. Incentives**
        - Monetary ($5-$20 gift cards)
        - Prize draws
        - Donation to charity
        - Results summary
        - Early access to findings
        
        **Tip:** Prepaid incentives work better than promised rewards
        
        ---
        ### After Distribution
        
        **7. Follow-Up Reminders**
        - **1st reminder:** 3-5 days after initial
        - **2nd reminder:** 7-10 days after initial
        - **Final reminder:** 14 days after initial
        
        **Reminder Template:**
        ```
        Subject: Reminder: Your Input Needed for [Study Name]
        
        Dear [Name],
        
        A few days ago, we sent you a survey about [topic]. If you've already 
        completed it, thank you! If not, we'd greatly appreciate your input.
        
        Your response is important because [reason].
        
        The survey takes only [X] minutes: [Link]
        
        Thank you for your time!
        ```
        
        **8. Monitor Response Rates**
        - Track daily responses
        - Identify low-response groups
        - Adjust strategy if needed
        
        ---
        ### Response Rate Benchmarks
        
        | Method | Typical Rate | Good Rate | Excellent Rate |
        |--------|--------------|-----------|----------------|
        | Online (general) | 10-15% | 20-30% | 40%+ |
        | Online (targeted) | 20-30% | 40-50% | 60%+ |
        | Mail | 5-15% | 20-30% | 40%+ |
        | Phone | 20-40% | 50-60% | 70%+ |
        | Face-to-Face | 60-80% | 80-90% | 95%+ |
        | Employee surveys | 30-40% | 50-70% | 80%+ |
        
        ---
        ### What Affects Response Rates?
        
        **Increases Response:**
        - ✅ Short survey (< 10 min)
        - ✅ Relevant topic
        - ✅ Personalized invitation
        - ✅ Incentives
        - ✅ Multiple reminders
        - ✅ Professional design
        - ✅ University/official sponsorship
        - ✅ Clear purpose
        
        **Decreases Response:**
        - ❌ Long survey (> 20 min)
        - ❌ Boring topic
        - ❌ Generic invitation
        - ❌ No incentive
        - ❌ No follow-up
        - ❌ Poor design
        - ❌ Unknown sender
        - ❌ Unclear purpose
        
        ---
        ### Dealing with Low Response Rates
        
        **If < 20% after 2 weeks:**
        
        1. **Extend deadline** (add 1-2 weeks)
        2. **Increase incentive** (if possible)
        3. **Change method** (add phone follow-up)
        4. **Shorten survey** (remove non-essential questions)
        5. **Personal outreach** (call key respondents)
        
        **If still low:**
        - Document response rate
        - Analyze non-response bias
        - Weight responses if needed
        - Acknowledge limitation in report
        """)

# Footer
show_footer()

