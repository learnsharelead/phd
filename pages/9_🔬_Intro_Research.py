import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Introduction to Research | Types, Methods, Hypothesis Formulation [2024]",
    description="Master research fundamentals: types of research (descriptive, analytical, qualitative, quantitative), research procedures, literature survey, problem identification, and hypothesis formulation for Ph.D. scholars.",
    keywords=[
        "types of research",
        "research methodology",
        "qualitative research",
        "quantitative research",
        "descriptive research",
        "hypothesis formulation",
        "literature survey",
        "research problem",
        "experimental research",
        "cross-sectional research",
        "research objectives"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/methodology/introduction",
    reading_time=90,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Introduction to Research", "url": "https://researchethics.dev/methodology/introduction"}
    ],
    course_info={
        "name": "Introduction to Research - Paper I Unit I",
        "description": "Comprehensive introduction to research methodology covering types, procedures, literature survey, and hypothesis formulation.",
        "level": "Doctoral",
        "prerequisites": "Graduate degree",
        "teaches": ["Research Types", "Research Design", "Hypothesis Formulation", "Literature Survey"],
        "workload": "PT15H",
        "rating": "4.9",
        "rating_count": 892
    }
)
apply_custom_css()
show_top_nav(current_page="Intro to Research")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">🔬 Unit I: Introduction to Research</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #166534;">Paper I: Research Methodology — Building the foundation of scholarly inquiry.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📖 Meaning & Types",
    "🔍 Research Procedures",
    "📚 Literature Survey",
    "🎯 Hypothesis",
    "📋 Classification",
    "🧠 Quiz"
])

# =============================================================================
# TAB 1: MEANING AND TYPES OF RESEARCH
# =============================================================================
with tab1:
    st.markdown("## 📖 Chapter 1: Meaning and Types of Research")
    
    st.markdown("### 1.1 What is Research?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Research</b> is a systematic investigation to establish facts, solve problems, or develop new knowledge. It involves careful inquiry, observation, and analysis following scientific methods.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Detective Work</h4>
            <p style="margin: 0 !important; font-size: 13px;">Research is like <b>detective work</b>. You gather clues (data), follow leads (hypotheses), eliminate false trails, and arrive at the truth (conclusions) based on evidence.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📊 Types of Research by Purpose", expanded=True):
        st.markdown("""
        Research can be classified based on its **primary purpose** or **intended outcome**. Understanding these types helps you:
        - Choose the right approach for your research question
        - Set appropriate objectives
        - Select suitable methodologies
        - Communicate your research goals clearly
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 14px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #2563eb;">
                <h4 style="margin: 0 0 8px 0 !important; color: #1e40af;">📝 Descriptive Research</h4>
                <p style="margin: 0 !important; font-size: 13px; line-height: 1.6;">
                <b>Core Purpose:</b> To systematically describe characteristics, behaviors, or phenomena as they exist<br><br>
                <b>Key Question:</b> "What is happening?" "What are the characteristics?"<br><br>
                <b>When to Use:</b><br>
                • When you need to understand current status<br>
                • To establish baseline data<br>
                • To identify patterns and trends<br>
                • When exploring new areas<br><br>
                <b>Common Methods:</b><br>
                • Surveys and questionnaires<br>
                • Observational studies<br>
                • Case studies<br>
                • Longitudinal studies<br>
                • Cross-sectional studies
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **📚 Real-World Examples:**
            
            1. **Market Research:** "What are the smartphone preferences of millennials in urban India?"
               - Survey 1000 millennials
               - Describe brand preferences, features valued, price sensitivity
               - No attempt to explain WHY these preferences exist
            
            2. **Educational Study:** "What is the current state of digital literacy among rural teachers?"
               - Assess skills through tests
               - Document current competency levels
               - Identify gaps and patterns
            
            3. **Health Research:** "What is the prevalence of diabetes in adults aged 40-60?"
               - Screen population sample
               - Report percentage with diabetes
               - Describe demographic distribution
            """)
            
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 14px; border-radius: 8px; margin-bottom: 12px; margin-top: 12px; border-left: 4px solid #16a34a;">
                <h4 style="margin: 0 0 8px 0 !important; color: #166534;">🔬 Analytical Research</h4>
                <p style="margin: 0 !important; font-size: 13px; line-height: 1.6;">
                <b>Core Purpose:</b> To analyze existing information, identify relationships, and explain phenomena<br><br>
                <b>Key Question:</b> "Why is this happening?" "What causes this?"<br><br>
                <b>When to Use:</b><br>
                • When descriptive data already exists<br>
                • To test theories and hypotheses<br>
                • To establish cause-effect relationships<br>
                • To explain patterns observed in descriptive research<br><br>
                <b>Common Methods:</b><br>
                • Statistical analysis (regression, ANOVA)<br>
                • Hypothesis testing<br>
                • Experimental designs<br>
                • Comparative studies<br>
                • Critical evaluation
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **📚 Real-World Examples:**
            
            1. **Business Analytics:** "Why are customers churning?"
               - Analyze customer data
               - Identify factors: poor service, pricing, competition
               - Test hypotheses about causes
               - Quantify impact of each factor
            
            2. **Educational Research:** "What factors affect student performance?"
               - Analyze relationship between study hours, attendance, and grades
               - Use regression to identify significant predictors
               - Explain variance in performance
            
            3. **Social Science:** "How does social media usage affect mental health?"
               - Correlational analysis
               - Control for confounding variables
               - Establish strength and direction of relationship
            """)
            
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); padding: 14px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #7c3aed;">
                <h4 style="margin: 0 0 8px 0 !important; color: #6d28d9;">⚙️ Applied Research</h4>
                <p style="margin: 0 !important; font-size: 13px; line-height: 1.6;">
                <b>Core Purpose:</b> To solve specific, practical problems and generate usable solutions<br><br>
                <b>Key Question:</b> "How can we fix this?" "What works?"<br><br>
                <b>When to Use:</b><br>
                • When facing real-world problems<br>
                • To develop products or interventions<br>
                • To improve processes or policies<br>
                • When immediate application is needed<br><br>
                <b>Common Methods:</b><br>
                • Action research<br>
                • Field experiments<br>
                • Pilot studies<br>
                • Program evaluation<br>
                • Design-based research<br><br>
                <b>Outcome:</b> Solutions, products, policies, interventions
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **📚 Real-World Examples:**
            
            1. **Medical Research:** "Developing a vaccine for COVID-19"
               - Practical goal: prevent disease
               - Clinical trials to test efficacy
               - Immediate application to save lives
            
            2. **Engineering:** "Improving battery life in electric vehicles"
               - Test new materials and designs
               - Optimize charging algorithms
               - Produce marketable solution
            
            3. **Education:** "Designing an effective online learning platform"
               - Test different interface designs
               - Measure learning outcomes
               - Implement best-performing solution
            
            4. **Agriculture:** "Increasing crop yield in drought conditions"
               - Test drought-resistant varieties
               - Develop irrigation techniques
               - Transfer technology to farmers
            """)
            
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%); padding: 14px; border-radius: 8px; margin-bottom: 12px; margin-top: 12px; border-left: 4px solid #ea580c;">
                <h4 style="margin: 0 0 8px 0 !important; color: #c2410c;">🎓 Fundamental/Basic Research</h4>
                <p style="margin: 0 !important; font-size: 13px; line-height: 1.6;">
                <b>Core Purpose:</b> To expand knowledge and understanding without immediate practical application<br><br>
                <b>Key Question:</b> "What is the nature of X?" "How does this work?"<br><br>
                <b>When to Use:</b><br>
                • To build theoretical foundations<br>
                • To understand fundamental principles<br>
                • To explore new phenomena<br>
                • When driven by curiosity, not problems<br><br>
                <b>Common Methods:</b><br>
                • Theoretical modeling<br>
                • Laboratory experiments<br>
                • Mathematical proofs<br>
                • Conceptual analysis<br>
                • Pure observation<br><br>
                <b>Outcome:</b> Theories, principles, laws, new knowledge
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **📚 Real-World Examples:**
            
            1. **Physics:** "Understanding the nature of dark matter"
               - No immediate application
               - Expands understanding of universe
               - May lead to applications decades later
            
            2. **Mathematics:** "Proving new theorems in number theory"
               - Pure intellectual pursuit
               - Builds mathematical knowledge
               - Cryptography applications came much later
            
            3. **Biology:** "How do cells communicate?"
               - Understanding fundamental processes
               - No immediate cure or product
               - Foundation for future medical breakthroughs
            
            4. **Psychology:** "What is the nature of consciousness?"
               - Philosophical and scientific exploration
               - Theoretical frameworks
               - Informs future applied research
            """)
        
        st.markdown("""
        ---
        ### 🔄 The Research Continuum
        
        **Important:** These types are not mutually exclusive! Research often moves along a continuum:
        
        | Stage | Type | Example |
        |-------|------|---------|
        | 1️⃣ | **Basic Research** | Discover that certain bacteria produce antibiotics |
        | 2️⃣ | **Descriptive** | Catalog which bacteria produce which compounds |
        | 3️⃣ | **Analytical** | Understand how these compounds kill pathogens |
        | 4️⃣ | **Applied** | Develop penicillin as a drug |
        
        **Key Insight:** Today's basic research is tomorrow's applied solution. GPS, internet, and lasers all started as basic research!
        """)

    with st.expander("🔢 Quantitative vs Qualitative Research", expanded=True):
        st.markdown("""
        These two paradigms represent fundamentally different approaches to understanding the world. 
        Most research today uses **mixed methods** — combining both approaches for comprehensive insights.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 16px; border-radius: 8px; border-left: 4px solid #2563eb;">
                <h4 style="margin: 0 0 10px 0 !important; color: #1e40af;">📊 Quantitative Research</h4>
                <p style="margin: 0 !important; font-size: 13px; line-height: 1.7;">
                <b>Philosophy:</b> Objective reality exists and can be measured<br><br>
                <b>Focus:</b> Numbers, measurements, statistics<br>
                <b>Data Type:</b> Numerical (scores, counts, ratings, percentages)<br>
                <b>Analysis:</b> Statistical tests (t-test, ANOVA, regression)<br>
                <b>Sample Size:</b> Large (100s-1000s), representative<br>
                <b>Generalizability:</b> High — results apply to population<br>
                <b>Researcher Role:</b> Detached, objective observer<br><br>
                <b>Key Questions:</b><br>
                • How many?<br>
                • How much?<br>
                • What percentage?<br>
                • Is there a relationship?<br>
                • Is the difference significant?
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **📚 Detailed Example: Student Performance Study**
            
            **Research Question:** "Does study time affect exam scores?"
            
            **Quantitative Approach:**
            - **Sample:** 500 students
            - **Data Collection:** 
              - Survey: Hours studied per week (numerical)
              - Exam scores (0-100)
            - **Analysis:** 
              - Correlation coefficient (r = 0.68)
              - Regression: Each hour studied → 3.2 points increase
              - p-value < 0.001 (statistically significant)
            - **Conclusion:** "Study time significantly predicts exam scores (β=3.2, p<0.001). 
              Students who study 10+ hours score 25% higher on average."
            
            **Strengths:**
            - ✅ Precise, objective measurements
            - ✅ Can test hypotheses statistically
            - ✅ Results generalizable to larger population
            - ✅ Can establish correlations and predictions
            - ✅ Replicable — others can verify results
            
            **Limitations:**
            - ❌ May miss context and nuance
            - ❌ Can't explain WHY relationships exist
            - ❌ Reduces complex phenomena to numbers
            - ❌ May not capture unexpected insights
            """)
            
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 16px; border-radius: 8px; border-left: 4px solid #16a34a;">
                <h4 style="margin: 0 0 10px 0 !important; color: #166534;">📝 Qualitative Research</h4>
                <p style="margin: 0 !important; font-size: 13px; line-height: 1.7;">
                <b>Philosophy:</b> Reality is socially constructed, subjective<br><br>
                <b>Focus:</b> Meanings, experiences, perspectives, context<br>
                <b>Data Type:</b> Words, images, videos, observations, narratives<br>
                <b>Analysis:</b> Thematic analysis, coding, pattern identification<br>
                <b>Sample Size:</b> Small (5-30), purposively selected<br>
                <b>Generalizability:</b> Low — deep understanding of specific cases<br>
                <b>Researcher Role:</b> Immersed, interpretive participant<br><br>
                <b>Key Questions:</b><br>
                • Why does this happen?<br>
                • How do people experience X?<br>
                • What does this mean to participants?<br>
                • What is the process?<br>
                • What is the context?
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **📚 Detailed Example: Student Performance Study**
            
            **Research Question:** "How do students experience academic pressure?"
            
            **Qualitative Approach:**
            - **Sample:** 15 students (purposively selected)
            - **Data Collection:**
              - In-depth interviews (1 hour each)
              - Observation of study behaviors
              - Student journals/diaries
            - **Analysis:**
              - Transcribe interviews
              - Code themes: stress, motivation, coping strategies
              - Identify patterns and narratives
            - **Findings:** "Students describe pressure as 'suffocating' but also 'motivating.' 
              Three coping strategies emerged: social support, time management, and avoidance. 
              Pressure is experienced differently based on family expectations and career goals."
            
            **Strengths:**
            - ✅ Rich, detailed understanding
            - ✅ Captures context and complexity
            - ✅ Explores WHY and HOW
            - ✅ Flexible — can adapt during research
            - ✅ Discovers unexpected insights
            
            **Limitations:**
            - ❌ Results not generalizable
            - ❌ Researcher bias possible
            - ❌ Time-consuming analysis
            - ❌ Difficult to replicate exactly
            - ❌ Can't test hypotheses statistically
            """)
        
        st.markdown("""
        ---
        ### 📊 Comprehensive Comparison Table
        
        | Aspect | Quantitative | Qualitative |
        |--------|--------------|-------------|
        | **Paradigm** | Positivist, post-positivist | Interpretivist, constructivist |
        | **Reality** | Objective, single truth | Subjective, multiple truths |
        | **Purpose** | Test theories, measure, predict | Explore, understand, describe |
        | **Reasoning** | Deductive (theory → data) | Inductive (data → theory) |
        | **Design** | Structured, predetermined | Flexible, emergent |
        | **Data** | Numbers, closed-ended | Words, open-ended |
        | **Sample** | Large, random | Small, purposive |
        | **Analysis** | Statistical | Thematic, narrative |
        | **Validity** | Internal, external validity | Credibility, transferability |
        | **Output** | Statistics, graphs, p-values | Themes, quotes, narratives |
        | **Examples** | Surveys, experiments, tests | Interviews, ethnography, case studies |
        
        ### 🔄 Mixed Methods Research
        
        **Best of Both Worlds:** Many modern studies combine both approaches:
        
        **Example: Understanding Employee Satisfaction**
        1. **Quantitative Phase:** Survey 1000 employees → 65% report low satisfaction
        2. **Qualitative Phase:** Interview 20 employees → Discover specific reasons (poor management, lack of growth)
        3. **Integration:** Numbers show WHAT and HOW MUCH; interviews explain WHY
        
        **When to Use Each:**
        - **Quantitative:** When you need to measure, compare, or predict
        - **Qualitative:** When you need to understand experiences, meanings, or processes
        - **Mixed:** When you want comprehensive understanding (most complex research)
        """)

    with st.expander("💡 Conceptual vs Empirical Research", expanded=True):
        st.markdown("""
        This distinction is about the **source of knowledge** — do you think about ideas (conceptual) 
        or observe the world (empirical)?
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: #fef3c7; padding: 16px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 10px 0 !important;">💭 Conceptual Research</h4>
                <p style="margin: 0 !important; font-size: 13px; line-height: 1.7;">
                <b>Core Idea:</b> Research based on abstract thinking, logic, and existing theories<br><br>
                <b>Data Source:</b><br>
                • Existing theories and literature<br>
                • Philosophical analysis<br>
                • Logical reasoning<br>
                • Thought experiments<br><br>
                <b>Method:</b><br>
                • Critical analysis<br>
                • Synthesis of ideas<br>
                • Logical deduction<br>
                • Theoretical modeling<br><br>
                <b>Outcome:</b> New frameworks, models, theories, classifications
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **📚 Detailed Examples:**
            
            1. **Philosophy:** "What is justice?"
               - No experiments or surveys
               - Analyze concepts of fairness, rights, equality
               - Build logical arguments
               - Develop theoretical framework
            
            2. **Economics:** "Developing a new model of consumer behavior"
               - Review existing theories
               - Identify gaps and contradictions
               - Propose new conceptual model
               - Use logical reasoning to justify
            
            3. **Computer Science:** "Proposing a new algorithm complexity class"
               - Mathematical analysis
               - Theoretical proofs
               - No implementation or testing
               - Pure conceptual contribution
            
            **Characteristics:**
            - 📖 Library-based, not lab-based
            - 🧠 Relies on reasoning, not observation
            - 📚 Builds on existing knowledge
            - 💡 Creates new ways of thinking
            - ⚡ Faster — no data collection needed
            """)
            
        with col2:
            st.markdown("""
            <div style="background: #dbeafe; padding: 16px; border-radius: 8px; border-left: 4px solid #2563eb;">
                <h4 style="color: #1e40af; margin: 0 0 10px 0 !important;">🔬 Empirical Research</h4>
                <p style="margin: 0 !important; font-size: 13px; line-height: 1.7;">
                <b>Core Idea:</b> Research based on observation, experience, and evidence from the real world<br><br>
                <b>Data Source:</b><br>
                • Direct observation<br>
                • Experiments<br>
                • Surveys and measurements<br>
                • Real-world data<br><br>
                <b>Method:</b><br>
                • Systematic observation<br>
                • Controlled experiments<br>
                • Data collection and measurement<br>
                • Statistical analysis<br><br>
                <b>Outcome:</b> Evidence-based findings, verified facts, tested hypotheses
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **📚 Detailed Examples:**
            
            1. **Medicine:** "Does aspirin prevent heart attacks?"
               - Clinical trial with 10,000 patients
               - Half receive aspirin, half placebo
               - Measure heart attack rates
               - Evidence: 25% reduction in aspirin group
            
            2. **Psychology:** "Do violent video games increase aggression?"
               - Experiment: Participants play violent vs. non-violent games
               - Measure aggression through behavioral tests
               - Observe and record actual behavior
               - Statistical analysis of results
            
            3. **Environmental Science:** "What is the CO₂ level in the atmosphere?"
               - Install sensors worldwide
               - Collect measurements daily
               - Analyze trends over time
               - Report empirical data: 420 ppm
            
            **Characteristics:**
            - 🔬 Lab or field-based
            - 📊 Relies on data and evidence
            - 🎯 Tests theories against reality
            - ✅ Verifiable and replicable
            - ⏱️ Time-consuming — requires data collection
            """)
        
        st.markdown("""
        ---
        ### ⚖️ Key Differences
        
        | Aspect | Conceptual | Empirical |
        |--------|------------|----------|
        | **Basis** | Ideas, theories | Observations, data |
        | **Approach** | Thinking, reasoning | Observing, measuring |
        | **Verification** | Logical consistency | Empirical evidence |
        | **Setting** | Library, desk | Lab, field |
        | **Tools** | Logic, analysis | Instruments, surveys |
        | **Time** | Faster | Slower |
        | **Cost** | Lower | Higher |
        | **Example** | Philosophical essay | Scientific experiment |
        
        ### 🔄 How They Work Together
        
        **The Scientific Cycle:**
        1. **Conceptual:** Develop theory about how memory works
        2. **Empirical:** Test theory with experiments
        3. **Conceptual:** Refine theory based on results
        4. **Empirical:** Test refined theory
        
        **Example:**
        - **Einstein (Conceptual):** Theorized E=mc² through thought experiments
        - **Scientists (Empirical):** Tested it with atomic experiments
        - **Result:** Theory confirmed by evidence
        
        💡 **Key Insight:** Most Ph.D. research is **empirical** — you collect data to test ideas. 
        But you need **conceptual** work to develop your theoretical framework!
        """)

# =============================================================================
# TAB 2: RESEARCH PROCEDURES
# =============================================================================
with tab2:
    st.markdown("## 🔍 Chapter 2: Research Procedures")
    
    st.markdown("### 2.1 Steps in Research Process")
    
    with st.expander("📋 The Research Process", expanded=True):
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=10, shape=box, style="rounded,filled"];
            
            step1 [label="1. Identify Problem", fillcolor="#dbeafe"];
            step2 [label="2. Review Literature", fillcolor="#dcfce7"];
            step3 [label="3. Formulate Hypothesis", fillcolor="#fef3c7"];
            step4 [label="4. Design Research", fillcolor="#f3e8ff"];
            step5 [label="5. Collect Data", fillcolor="#fed7aa"];
            step6 [label="6. Analyze Data", fillcolor="#fecaca"];
            step7 [label="7. Interpret Results", fillcolor="#e0e7ff"];
            step8 [label="8. Report Findings", fillcolor="#d1fae5"];
            
            step1 -> step2 -> step3 -> step4 -> step5 -> step6 -> step7 -> step8;
        }
        """)
        
        st.markdown("""
        **Detailed Steps:**
        
        | Step | Activities | Output |
        |------|------------|--------|
        | **1. Problem Identification** | Observe, question, read literature | Research problem statement |
        | **2. Literature Review** | Search databases, read, synthesize | Gaps identified, context established |
        | **3. Hypothesis Formulation** | Develop testable predictions | H₀ and H₁ statements |
        | **4. Research Design** | Choose methods, sampling, tools | Research protocol |
        | **5. Data Collection** | Surveys, experiments, interviews | Raw data |
        | **6. Data Analysis** | Statistical/qualitative analysis | Results, patterns |
        | **7. Interpretation** | Relate to hypothesis, literature | Conclusions |
        | **8. Reporting** | Write paper, present findings | Publication |
        """)

    with st.expander("🔄 Interdisciplinary Research", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Interdisciplinary Research</b> integrates knowledge, methods, and perspectives from two or more disciplines to address a complex problem that cannot be solved by a single discipline alone.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Examples:**
        - **Biomedical Engineering:** Biology + Engineering
        - **Environmental Economics:** Ecology + Economics
        - **Cognitive Neuroscience:** Psychology + Neuroscience
        - **Digital Humanities:** Computer Science + Humanities
        
        **Challenges:**
        - Different terminologies and frameworks
        - Publication venue selection
        - Balancing depth vs. breadth
        - Team coordination
        
        **Benefits:**
        - Novel perspectives and solutions
        - Real-world problem solving
        - Innovation at discipline boundaries
        """)

    with st.expander("🧪 Types Based on Control", expanded=True):
        st.markdown("""
        | Type | Control Level | Random Assignment | Example |
        |------|---------------|-------------------|---------|
        | **Experimental** | High | Yes | Lab drug trial |
        | **Quasi-Experimental** | Medium | No | Comparing schools with program vs. without |
        | **Non-Experimental** | Low | No | Survey, observational study |
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: #eff6ff; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🔬 Experimental Research</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                • Researcher manipulates independent variable<br>
                • Random assignment to groups<br>
                • High internal validity<br>
                • Can establish causation
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: #fef3c7; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">⚡ Quasi-Experimental</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                • Groups exist naturally<br>
                • No random assignment<br>
                • More realistic settings<br>
                • Weaker causal inference
                </p>
            </div>
            """, unsafe_allow_html=True)

# =============================================================================
# TAB 3: LITERATURE SURVEY
# =============================================================================
with tab3:
    st.markdown("## 📚 Chapter 3: Literature Survey & Problem Identification")
    
    st.markdown("### 3.1 What is Literature Survey?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Literature Survey/Review</b> is a comprehensive, critical analysis of existing published work related to a research topic. It identifies what is already known, gaps in knowledge, and justifies the research.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Mapping Territory</h4>
            <p style="margin: 0 !important; font-size: 13px;">Literature review is like <b>mapping explored territory</b>. You identify what's discovered, what's unclear, and where the "blank spots" are that need exploration.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📋 Purposes of Literature Review", expanded=True):
        st.markdown("""
        | Purpose | Description |
        |---------|-------------|
        | **Establish Context** | Show where your research fits in existing knowledge |
        | **Identify Gaps** | Find what hasn't been studied or resolved |
        | **Avoid Duplication** | Ensure you're not repeating existing work |
        | **Learn Methods** | Discover appropriate research designs and tools |
        | **Build Theoretical Framework** | Identify theories and concepts to guide research |
        | **Identify Variables** | Discover key variables and relationships |
        | **Justify Research** | Show why your study is needed |
        """)

    with st.expander("🔍 Steps in Literature Review", expanded=True):
        st.markdown("""
        **1. Define Scope**
        - Formulate research questions
        - Identify key concepts and terms
        - Set boundaries (timeframe, geography, etc.)
        
        **2. Search Databases**
        - Use Google Scholar, Scopus, Web of Science
        - Use Boolean operators (AND, OR, NOT)
        - Try synonyms and related terms
        
        **3. Evaluate Sources**
        - Assess quality and relevance
        - Check recency and citations
        - Prioritize peer-reviewed journals
        
        **4. Organize Literature**
        - Use reference management (Zotero, Mendeley)
        - Create summary tables
        - Group by themes or chronology
        
        **5. Synthesize and Write**
        - Don't just summarize — analyze and critique
        - Show connections and contradictions
        - Identify gaps that your research addresses
        """)

    with st.expander("🎯 Research Problem Identification", expanded=True):
        st.markdown("""
        **Sources of Research Problems:**
        
        | Source | Example |
        |--------|---------|
        | Personal experience | Noticing declining student attention |
        | Theory gaps | Theory doesn't explain new phenomena |
        | Literature gaps | "No study has examined..." |
        | Practical problems | Organizations seeking solutions |
        | Technological changes | New tools enable new research |
        | Conflicting findings | Studies disagree, resolution needed |
        
        **Characteristics of Good Research Problem:**
        - ✅ Clear and specific
        - ✅ Researchable (can gather data)
        - ✅ Significant (contributes to knowledge)
        - ✅ Feasible (resources available)
        - ✅ Original (not already solved)
        - ✅ Ethical (doesn't harm participants)
        """)

# =============================================================================
# TAB 4: HYPOTHESIS FORMULATION
# =============================================================================
with tab4:
    st.markdown("## 🎯 Chapter 4: Research Objectives and Hypothesis")
    
    st.markdown("### 4.1 Research Objectives")
    
    with st.expander("🎯 Types of Research Objectives", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🌐 General Objective</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Broad statement of research purpose<br>
                <b>Example:</b> "To understand factors affecting employee retention"
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🔍 Specific Objectives</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Detailed, measurable sub-goals<br>
                <b>Example:</b> "To identify relationship between salary and retention"
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **SMART Objectives:**
        - **S**pecific — Clear and precise
        - **M**easurable — Can be assessed
        - **A**chievable — Realistic given resources
        - **R**elevant — Aligned with research problem
        - **T**ime-bound — Has deadline
        """)

    st.markdown("### 4.2 Hypothesis Formulation")
    
    with st.expander("📐 What is a Hypothesis?", expanded=True):
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb; margin-bottom: 10px;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Hypothesis</b> is a tentative, testable statement predicting a relationship between variables. It's an educated guess based on theory and prior research that can be empirically tested.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Characteristics of Good Hypothesis:**
        - ✅ Testable — Can be verified empirically
        - ✅ Specific — Clearly states relationship
        - ✅ Based on theory/literature
        - ✅ Simple and concise
        - ✅ States expected direction (when possible)
        """)

    with st.expander("⚖️ Types of Hypotheses", expanded=True):
        st.markdown("""
        | Type | Description | Example |
        |------|-------------|---------|
        | **Null (H₀)** | No effect/relationship exists | "There is no difference in scores between groups" |
        | **Alternative (H₁)** | Effect/relationship exists | "Training improves performance" |
        | **Directional** | Specifies direction | "Higher motivation leads to higher grades" |
        | **Non-directional** | Effect exists, direction unknown | "There is a relationship between X and Y" |
        | **Simple** | One IV, one DV | "Smoking causes cancer" |
        | **Complex** | Multiple variables | "Age and education jointly affect income" |
        """)
        
        st.markdown("""
        **Steps in Hypothesis Formulation:**
        1. Review literature for existing relationships
        2. Identify variables (IV, DV)
        3. State relationship in testable form
        4. Express as null and alternative
        5. Ensure it's measurable
        """)

# =============================================================================
# TAB 5: RESEARCH CLASSIFICATION
# =============================================================================
with tab5:
    st.markdown("## 📋 Chapter 5: Research Classification")
    
    with st.expander("⏰ Time-Based Classification", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px;">
                <h4 style="margin: 0 0 8px 0 !important;">📊 Cross-Sectional Research</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Data collected at ONE point in time<br>
                <b>Analogy:</b> A photograph — captures a moment<br>
                <b>Example:</b> Survey of current attitudes<br>
                <b>Pros:</b> Quick, inexpensive<br>
                <b>Cons:</b> Can't show change over time
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: #f0fdf4; padding: 14px; border-radius: 8px;">
                <h4 style="margin: 0 0 8px 0 !important;">📈 Longitudinal/Time-Series</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Data collected OVER time<br>
                <b>Analogy:</b> A movie — shows change<br>
                <b>Example:</b> Tracking cohort for 10 years<br>
                <b>Pros:</b> Shows trends, causation stronger<br>
                <b>Cons:</b> Expensive, attrition
                </p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("🎯 Purpose-Based Classification", expanded=True):
        st.markdown("""
        | Type | Purpose | Questions | Example |
        |------|---------|-----------|---------|
        | **Exploratory** | Discover, understand | "What's going on?" | Initial investigation of new phenomenon |
        | **Descriptive** | Describe characteristics | "What, when, where?" | Census, market survey |
        | **Explanatory** | Explain relationships | "Why? How?" | Regression analysis of causes |
        | **Predictive** | Forecast outcomes | "What will happen?" | Stock market prediction |
        | **Evaluative** | Assess effectiveness | "Does it work?" | Program evaluation |
        """)

    with st.expander("🔬 Complete Classification Summary", expanded=True):
        st.markdown("""
        | Classification | Types |
        |----------------|-------|
        | **By Purpose** | Basic, Applied |
        | **By Approach** | Quantitative, Qualitative, Mixed |
        | **By Logic** | Deductive, Inductive |
        | **By Time** | Cross-sectional, Longitudinal |
        | **By Control** | Experimental, Quasi-experimental, Non-experimental |
        | **By Data Source** | Primary, Secondary |
        | **By Outcome** | Descriptive, Analytical, Predictive |
        | **By Setting** | Laboratory, Field |
        """)
        
        st.graphviz_chart("""
        digraph {
            rankdir=LR; 
            node [fontname="Arial", fontsize=10, shape=box, style="rounded,filled"];
            
            research [label="RESEARCH", fillcolor="#d1fae5", shape=ellipse, fontsize=12];
            
            purpose [label="By Purpose", fillcolor="#dbeafe"];
            approach [label="By Approach", fillcolor="#fef3c7"];
            time [label="By Time", fillcolor="#f3e8ff"];
            control [label="By Control", fillcolor="#fed7aa"];
            
            basic [label="Basic", fillcolor="#bfdbfe", fontsize=9];
            applied [label="Applied", fillcolor="#bfdbfe", fontsize=9];
            quant [label="Quantitative", fillcolor="#fde68a", fontsize=9];
            qual [label="Qualitative", fillcolor="#fde68a", fontsize=9];
            cross [label="Cross-sectional", fillcolor="#e9d5ff", fontsize=9];
            long [label="Longitudinal", fillcolor="#e9d5ff", fontsize=9];
            exp [label="Experimental", fillcolor="#fdba74", fontsize=9];
            quasi [label="Quasi-exp", fillcolor="#fdba74", fontsize=9];
            
            research -> purpose; research -> approach; research -> time; research -> control;
            purpose -> basic; purpose -> applied;
            approach -> quant; approach -> qual;
            time -> cross; time -> long;
            control -> exp; control -> quasi;
        }
        """)


# =============================================================================
# TAB 6: QUIZ
# =============================================================================
with tab6:
    st.markdown("## 🧠 Knowledge Check")
    
    with st.form("quiz_form"):
        st.markdown("Test your understanding of Research Methodology basics.")
        
        q1 = st.radio(
            "1. Which type of research is primarily concerned with finding a solution for a specific practical problem?",
            ["Fundamental Research", "Applied Research", "Conceptual Research", "Descriptive Research"],
            index=None
        )
        
        q2 = st.radio(
            "2. Which variable is manipulated by the researcher in an experimental design?",
            ["Dependent Variable (DV)", "Independent Variable (IV)", "Extraneous Variable", "Confounding Variable"],
            index=None
        )
        
        q3 = st.radio(
            "3. Rejecting a Null Hypothesis when it is actually true is known as:",
            ["Type II Error", "Sampling Error", "Type I Error", "Standard Error"],
            index=None
        )
        
        submitted = st.form_submit_button("Submit Answers")
        
        if submitted:
            score = 0
            
            # Q1 Check
            if q1 == "Applied Research":
                score += 1
                st.success("✅ 1. Correct! Applied research solves practical problems.")
            else:
                st.error("❌ 1. Incorrect. The correct answer is Applied Research.")
                
            # Q2 Check
            if q2 == "Independent Variable (IV)":
                score += 1
                st.success("✅ 2. Correct! The IV is manipulated to observe its effect on the DV.")
            else:
                st.error("❌ 2. Incorrect. The correct answer is Independent Variable (IV).")
                
            # Q3 Check
            if q3 == "Type I Error":
                score += 1
                st.success("✅ 3. Correct! Type I error (False Positive) is rejecting a true Null Hypothesis.")
            else:
                st.error("❌ 3. Incorrect. The correct answer is Type I Error.")
            
            st.metric("Your Score", f"{score}/3")
            if score == 3:
                st.balloons()

# Footer
show_footer()
