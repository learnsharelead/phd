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
                • No random assignment<br>
                • Uses existing groups<br>
                • Moderate internal validity<br>
                • More practical in real settings
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    with st.expander("🔬 TRUE EXPERIMENTAL DESIGNS - Complete Guide", expanded=True):
        st.markdown("""
        ### True Experimental Designs: The Gold Standard
        
        True experiments are the **ONLY** research designs that can establish **causation** (X causes Y).
        
        **Three Essential Requirements:**
        1. ✅ **Manipulation** - Researcher controls the independent variable
        2. ✅ **Random Assignment** - Participants randomly assigned to groups
        3. ✅ **Control Group** - Comparison group that doesn't receive treatment
        
        ---
        ## 📋 **Design 1: Pretest-Posttest Control Group Design**
        
        **The Most Common Experimental Design**
        
        **Structure:**
        ```
        Random Assignment
        ↓
        Experimental Group:  O₁  →  X  →  O₂
        Control Group:       O₃  →  -  →  O₄
        
        Where:
        O = Observation/Measurement
        X = Treatment/Intervention
        - = No treatment
        ```
        
        **Example 1: Testing a New Teaching Method** (Education)
        
        **Research Question:** Does active learning improve test scores?
        
        **Procedure:**
        1. **Random Assignment**: 100 students randomly divided into two groups
        2. **Pretest (O₁, O₃)**: Both groups take baseline test
        3. **Treatment**:
           - Experimental group (X): Active learning for 8 weeks
           - Control group (-): Traditional lectures for 8 weeks
        4. **Posttest (O₂, O₄)**: Both groups take final test
        
        **Data:**
        ```
        Experimental Group:
        - Pretest mean (O₁) = 65
        - Posttest mean (O₂) = 82
        - Gain = +17 points
        
        Control Group:
        - Pretest mean (O₃) = 64
        - Posttest mean (O₄) = 70
        - Gain = +6 points
        
        Treatment Effect = (O₂ - O₁) - (O₄ - O₃) = 17 - 6 = 11 points
        
        Statistical Test: Independent t-test on gain scores
        Result: t(98) = 4.52, p < .001
        Conclusion: Active learning caused 11-point improvement
        ```
        
        **Strengths:**
        - ✅ Controls for initial differences (pretest)
        - ✅ Random assignment controls confounds
        - ✅ Can establish causation
        
        **Limitations:**
        - ❌ Pretest may sensitize participants
        - ❌ Testing effect (practice from pretest)
        
        ---
        ## 📋 **Design 2: Posttest-Only Control Group Design**
        
        **Simpler, Avoids Testing Effects**
        
        **Structure:**
        ```
        Random Assignment
        ↓
        Experimental Group:  X  →  O₁
        Control Group:       -  →  O₂
        ```
        
        **Example 2: Drug Effectiveness Trial** (Medicine)
        
        **Research Question:** Does Drug A reduce blood pressure?
        
        **Procedure:**
        1. **Random Assignment**: 200 patients randomly assigned
        2. **Treatment**:
           - Experimental: Drug A for 12 weeks
           - Control: Placebo for 12 weeks
        3. **Posttest Only**: Measure blood pressure after 12 weeks
        
        **Data:**
        ```
        Experimental Group (O₁): Mean BP = 118 mmHg, SD = 8
        Control Group (O₂): Mean BP = 130 mmHg, SD = 10
        
        Difference = 12 mmHg
        t(198) = 9.87, p < .001, d = 1.32 (very large effect)
        
        Conclusion: Drug A causes significant BP reduction
        ```
        
        **When to Use:**
        - ✅ When pretest might affect behavior
        - ✅ When baseline measures unavailable
        - ✅ When testing effect is a concern
        
        **Strengths:**
        - ✅ No testing effect
        - ✅ Simpler and faster
        - ✅ Random assignment ensures equivalence
        
        ---
        ## 📋 **Design 3: Solomon Four-Group Design**
        
        **The Most Rigorous Design - Controls Testing Effects**
        
        **Structure:**
        ```
        Group 1:  O₁  →  X  →  O₂  (Pretest + Treatment)
        Group 2:  O₃  →  -  →  O₄  (Pretest + No Treatment)
        Group 3:       X  →  O₅  (No Pretest + Treatment)
        Group 4:       -  →  O₆  (No Pretest + No Treatment)
        ```
        
        **Example 3: Attitude Change Study** (Psychology)
        
        **Research Question:** Does a diversity workshop change attitudes? Does taking a pretest affect results?
        
        **Results:**
        ```
        Group 1 (Pretest + Workshop): O₂ = 85
        Group 2 (Pretest + No Workshop): O₄ = 70
        Group 3 (No Pretest + Workshop): O₅ = 88
        Group 4 (No Pretest + No Workshop): O₆ = 72
        
        Treatment Effect: (85 + 88)/2 - (70 + 72)/2 = 86.5 - 71 = 15.5 points
        Testing Effect: (85 + 70)/2 - (88 + 72)/2 = 77.5 - 80 = -2.5 points
        
        Conclusion: 
        - Workshop causes 15.5-point improvement
        - Pretest slightly reduces scores (sensitization)
        ```
        
        **Strengths:**
        - ✅ Controls for testing effects
        - ✅ Most rigorous design
        - ✅ Can separate treatment and testing effects
        
        **Limitations:**
        - ❌ Requires large sample (4 groups)
        - ❌ Expensive and time-consuming
        - ❌ Complex analysis
        
        ---
        ## 📋 **Design 4: Factorial Designs**
        
        **Testing Multiple Variables Simultaneously**
        
        **2×2 Factorial Design:**
        ```
        Factor A: Teaching Method (Traditional vs. Active)
        Factor B: Class Size (Small vs. Large)
        
        Four Groups:
        1. Traditional + Small
        2. Traditional + Large
        3. Active + Small
        4. Active + Large
        ```
        
        **Example 4: Optimizing Learning** (Education)
        
        **Results:**
        ```
        Traditional + Small: 75
        Traditional + Large: 68
        Active + Small: 88
        Active + Large: 82
        
        Main Effect of Method: Active > Traditional (+12 points)
        Main Effect of Size: Small > Large (+5 points)
        Interaction: Active learning works better in small classes
        ```
        
        **Advantages:**
        - ✅ Tests multiple factors efficiently
        - ✅ Detects interactions
        - ✅ More realistic (real world has multiple factors)
        
        """)
    
    with st.expander("⚠️ INTERNAL VALIDITY THREATS & CONTROLS", expanded=True):
        st.markdown("""
        ### 8 Major Threats to Internal Validity
        
        **Internal Validity** = Can we confidently say X caused Y?
        
        ---
        #### **1. History**
        
        **Threat:** External events occur during study that affect results
        
        **Example:**
        - Testing exercise program effectiveness
        - During study, COVID-19 pandemic hits
        - Gyms close, people become sedentary
        - Results confounded by pandemic, not just program
        
        **Controls:**
        - ✅ Use control group (both affected equally)
        - ✅ Shorter study duration
        - ✅ Monitor external events
        
        ---
        #### **2. Maturation**
        
        **Threat:** Participants naturally change over time
        
        **Example:**
        - Testing reading program for children
        - Children naturally improve reading as they age
        - Improvement might be maturation, not program
        
        **Controls:**
        - ✅ Control group (matures at same rate)
        - ✅ Shorter study period
        - ✅ Match groups on age/development
        
        ---
        #### **3. Testing**
        
        **Threat:** Taking pretest affects posttest scores
        
        **Example:**
        - IQ test given twice
        - Second score higher due to practice, not treatment
        - Participants remember questions
        
        **Controls:**
        - ✅ Posttest-only design (no pretest)
        - ✅ Solomon Four-Group design
        - ✅ Use alternate forms of test
        - ✅ Longer interval between tests
        
        ---
        #### **4. Instrumentation**
        
        **Threat:** Measurement tool changes during study
        
        **Examples:**
        - Observer becomes more skilled at rating
        - Equipment calibration drifts
        - Survey questions modified mid-study
        
        **Controls:**
        - ✅ Standardize all measurements
        - ✅ Train observers thoroughly
        - ✅ Calibrate equipment regularly
        - ✅ Use same instruments throughout
        
        ---
        #### **5. Statistical Regression**
        
        **Threat:** Extreme scores tend toward average on retest
        
        **Example:**
        - Select students with lowest test scores
        - Provide tutoring
        - Scores improve, but partly due to regression to mean
        - Would have improved somewhat anyway
        
        **Controls:**
        - ✅ Control group with similar extreme scores
        - ✅ Don't select based on extreme scores
        - ✅ Multiple measurements
        
        ---
        #### **6. Selection Bias**
        
        **Threat:** Groups differ before treatment
        
        **Example:**
        - Experimental group: Volunteers (motivated)
        - Control group: Non-volunteers (less motivated)
        - Results confounded by initial motivation
        
        **Controls:**
        - ✅ **RANDOM ASSIGNMENT** (best solution)
        - ✅ Match groups on key variables
        - ✅ Statistical controls (ANCOVA)
        
        ---
        #### **7. Experimental Mortality (Attrition)**
        
        **Threat:** Participants drop out non-randomly
        
        **Example:**
        - Difficult exercise program
        - Less fit participants drop out
        - Only fit participants remain
        - Results biased toward success
        
        **Controls:**
        - ✅ Minimize dropout (incentives, convenience)
        - ✅ Compare dropouts to completers
        - ✅ Intention-to-treat analysis
        - ✅ Over-recruit initially
        
        ---
        #### **8. Diffusion of Treatment**
        
        **Threat:** Control group learns about/receives treatment
        
        **Example:**
        - Teaching new study technique to one class
        - Students talk to friends in control class
        - Control group adopts technique
        - Difference between groups reduced
        
        **Controls:**
        - ✅ Separate groups physically
        - ✅ Use different schools/locations
        - ✅ Delayed treatment for control
        - ✅ Monitor for contamination
        
        ---
        ### **Summary Table**
        
        | Threat | What It Is | Best Control |
        |--------|------------|--------------|
        | History | External events | Control group |
        | Maturation | Natural change | Control group |
        | Testing | Practice effects | Posttest-only design |
        | Instrumentation | Measurement changes | Standardization |
        | Regression | Extreme scores normalize | Control group |
        | Selection | Groups initially different | Random assignment |
        | Mortality | Non-random dropout | Minimize attrition |
        | Diffusion | Treatment spreads | Separate groups |
        """)
    
    with st.expander("🌍 EXTERNAL VALIDITY - Generalizability", expanded=True):
        st.markdown("""
        ### Can Results Generalize Beyond This Study?
        
        **External Validity** = Can we apply findings to other people, places, times?
        
        ---
        #### **1. Population Validity**
        
        **Question:** Do results apply to other people?
        
        **Threats:**
        - College students ≠ general population
        - Volunteers ≠ non-volunteers
        - One culture ≠ all cultures
        
        **Example:**
        - Study uses only male participants
        - Results may not apply to females
        - Limited population validity
        
        **Solutions:**
        - ✅ Representative sampling
        - ✅ Diverse participants
        - ✅ Replicate across populations
        
        ---
        #### **2. Ecological Validity**
        
        **Question:** Do results apply to real-world settings?
        
        **Threats:**
        - Lab ≠ real life
        - Artificial tasks ≠ natural behavior
        - Controlled ≠ messy reality
        
        **Example:**
        - Memory study using nonsense syllables
        - Real-world memory involves meaningful information
        - Low ecological validity
        
        **Solutions:**
        - ✅ Field experiments
        - ✅ Realistic tasks
        - ✅ Natural settings
        
        ---
        #### **3. Temporal Validity**
        
        **Question:** Do results apply to other time periods?
        
        **Threats:**
        - Historical context changes
        - Technology evolves
        - Cultural norms shift
        
        **Example:**
        - 1950s conformity studies
        - May not apply to modern individualistic culture
        - Limited temporal validity
        
        **Solutions:**
        - ✅ Replicate over time
        - ✅ Consider historical context
        - ✅ Update periodically
        
        ---
        ### **Internal vs External Validity Trade-off**
        
        | Design | Internal Validity | External Validity |
        |--------|-------------------|-------------------|
        | Lab Experiment | ⭐⭐⭐⭐⭐ High | ⭐⭐ Low |
        | Field Experiment | ⭐⭐⭐⭐ Good | ⭐⭐⭐⭐ Good |
        | Quasi-Experiment | ⭐⭐⭐ Moderate | ⭐⭐⭐⭐ Good |
        | Observational | ⭐⭐ Low | ⭐⭐⭐⭐⭐ High |
        
        **The Dilemma:**
        - More control → Better causation → Less realistic
        - Less control → Worse causation → More realistic
        """)
    
    with st.expander("⚡ QUASI-EXPERIMENTAL DESIGNS", expanded=True):
        st.markdown("""
        ### When True Experiments Aren't Possible
        
        **Quasi-Experimental** = Looks like experiment, but lacks random assignment
        
        **When to Use:**
        - ❌ Can't randomly assign (ethics, practicality)
        - ❌ Groups already exist (schools, hospitals, companies)
        - ❌ Real-world constraints
        
        ---
        #### **Design 1: Non-Equivalent Control Group**
        
        **Structure:**
        ```
        Experimental Group:  O₁  →  X  →  O₂
        Control Group:       O₃  →  -  →  O₄
        
        (No random assignment - groups already exist)
        ```
        
        **Example:** School Intervention
        - School A gets new curriculum (can't randomly assign schools)
        - School B continues old curriculum
        - Compare outcomes
        
        **Weakness:** Schools may differ in many ways (SES, resources, teacher quality)
        
        **Strengthen With:**
        - ✅ Match schools on key variables
        - ✅ Statistical controls (ANCOVA)
        - ✅ Multiple comparison schools
        
        ---
        #### **Design 2: Time Series Design**
        
        **Structure:**
        ```
        O₁  O₂  O₃  O₄  X  O₅  O₆  O₇  O₈
        
        Multiple measurements before and after treatment
        ```
        
        **Example:** Policy Impact
        - Measure crime rates monthly for 2 years
        - New policing policy implemented
        - Continue measuring for 2 years
        - Look for change in trend
        
        **Strengths:**
        - ✅ Can see trends before intervention
        - ✅ Controls for history (gradual vs. sudden change)
        - ✅ No control group needed
        
        ---
        #### **Design 3: Regression Discontinuity**
        
        **When:** Treatment assigned based on cutoff score
        
        **Example:**
        - Scholarship given to students scoring ≥ 80
        - Compare students just above (81) vs. just below (79) cutoff
        - Very similar students, different treatment
        
        **Strength:** Near-random assignment at cutoff
        
        ---
        ### **Quasi vs. True Experiments**
        
        | Feature | True Experiment | Quasi-Experiment |
        | Random Assignment | ✅ Yes | ❌ No |
        | Causation | ✅ Strong | ⚠️ Weaker |
        | Internal Validity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
        | Practicality | ⭐⭐ | ⭐⭐⭐⭐⭐ |
        | Real-world Use | ⭐⭐ | ⭐⭐⭐⭐⭐ |
        """)


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
        A literature review is NOT just a summary of papers. It's a critical analysis that serves multiple purposes:
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Primary Purposes:**
            
            | Purpose | Description | Example |
            |---------|-------------|---------|
            | **Establish Context** | Show where your research fits | "Previous studies focused on X, but ignored Y" |
            | **Identify Gaps** | Find what hasn't been studied | "No research examines Z in developing countries" |
            | **Avoid Duplication** | Ensure originality | "This exact study was done in 2015, but..." |
            | **Learn Methods** | Discover appropriate designs | "Most studies use surveys; I'll use experiments" |
            | **Build Framework** | Identify guiding theories | "Social Cognitive Theory will guide this study" |
            | **Identify Variables** | Discover key relationships | "Age, income, and education affect adoption" |
            | **Justify Research** | Show why study is needed | "Given these gaps, my research is necessary" |
            """)
        
        with col2:
            st.markdown("""
            **📚 Detailed Example: Literature Review for "AI in Education"**
            
            **Context:** "AI in education has grown rapidly since 2015, with 500+ papers published."
            
            **What's Known:**
            - AI tutoring systems improve learning outcomes (Smith, 2020)
            - Personalized learning increases engagement (Jones, 2021)
            - Teachers have concerns about AI replacing them (Lee, 2022)
            
            **Gaps Identified:**
            - ❌ Most studies in developed countries only
            - ❌ Limited research on rural schools
            - ❌ No studies on teacher training for AI tools
            - ❌ Contradictory findings on student motivation
            
            **Your Research:**
            "This study addresses the gap by examining AI adoption in rural Indian schools, 
            focusing on teacher training needs and student motivation."
            
            **Justification:**
            "Given the digital divide and unique challenges of rural education, 
            understanding AI implementation in this context is crucial for equitable education."
            """)

    with st.expander("🔍 Step-by-Step Literature Review Process", expanded=True):
        st.markdown("""
        ### Complete Literature Review Workflow
        
        Follow this systematic approach for a comprehensive literature review:
        """)
        
        st.markdown("""
        #### **Step 1: Define Scope** 🎯
        
        **What to Do:**
        - Formulate specific research questions
        - Identify key concepts and terms
        - Set boundaries (timeframe, geography, population)
        - Decide on inclusion/exclusion criteria
        
        **Example:**
        - **Topic:** "Impact of social media on mental health"
        - **Research Question:** "How does Instagram use affect anxiety in college students?"
        - **Key Concepts:** Social media, Instagram, anxiety, mental health, college students
        - **Boundaries:** 
          - Timeframe: 2015-2024 (last 10 years)
          - Population: College students aged 18-25
          - Geography: English-language studies, any country
          - Exclude: Other social media platforms, other age groups
        
        ---
        
        #### **Step 2: Search Databases** 🔎
        
        **Major Academic Databases:**
        """)
        
        st.markdown("""
        | Database | Best For | Coverage | Access | Key Features |
        |----------|----------|----------|--------|--------------|
        | **Google Scholar** | Broad search, free access | All disciplines | Free | Simple interface, comprehensive |
        | **Scopus** | Citation analysis, metrics | Science, tech, medicine, social sciences | Subscription | Advanced metrics, author profiles |
        | **Web of Science** | High-quality journals, citations | Science, social sciences, humanities | Subscription | Citation tracking, impact factors |
        | **PubMed** | Medical and health sciences | Medicine, biology, health | Free | MeSH terms, clinical trials |
        | **IEEE Xplore** | Engineering and technology | Computer science, engineering | Subscription | Standards, conference papers |
        | **JSTOR** | Humanities and social sciences | History, literature, sociology | Subscription | Historical archives |
        | **ScienceDirect** | Elsevier journals | All sciences | Subscription | Full-text access |
        | **ERIC** | Education research | Education, teaching | Free | Thesaurus, lesson plans |
        """)
        
        st.markdown("""
        **Search Strategy:**
        
        1. **Start Broad:** Google Scholar for overview
        2. **Go Specific:** Scopus/WoS for peer-reviewed articles
        3. **Check Citations:** Follow references in key papers
        4. **Use Alerts:** Set up email alerts for new papers
        
        ---
        
        #### **Step 3: Master Boolean Operators** 🔧
        
        **Boolean operators are the KEY to effective searching. Master these!**
        """)
        
        st.markdown("""
        | Operator | Function | Example | Results |
        |----------|----------|---------|---------|
        | **AND** | Both terms must appear | `social media AND anxiety` | Papers with BOTH terms |
        | **OR** | Either term can appear | `Instagram OR Facebook` | Papers with EITHER term |
        | **NOT** | Exclude term | `social media NOT Twitter` | Papers about social media EXCEPT Twitter |
        | **" "** | Exact phrase | `"mental health"` | Exact phrase only |
        | **( )** | Group terms | `(Instagram OR Facebook) AND anxiety` | Grouped logic |
        | **\*** | Wildcard | `adolescen*` | adolescent, adolescents, adolescence |
        """)
        
        st.markdown("""
        **🎯 20+ Boolean Operator Examples:**
        
        **Basic Examples:**
        1. `machine learning AND education` → Papers about ML in education
        2. `smartphone OR "mobile phone" OR cellphone` → Any term for mobile devices
        3. `cancer NOT "breast cancer"` → All cancers except breast
        4. `"climate change"` → Exact phrase only
        5. `teach*` → teach, teacher, teaching, teachers
        
        **Intermediate Examples:**
        6. `(AI OR "artificial intelligence") AND healthcare` → AI in healthcare
        7. `diabetes AND (treatment OR therapy OR intervention)` → Diabetes treatments
        8. `"social media" AND (anxiety OR depression OR stress)` → Social media mental health
        9. `COVID-19 NOT vaccine` → COVID research excluding vaccines
        10. `child* AND obesity` → Children/childhood obesity
        
        **Advanced Examples:**
        11. `("machine learning" OR "deep learning" OR "neural network") AND (medical OR healthcare OR clinical)` 
            → AI in medicine
        
        12. `(smartphone OR "mobile phone") AND (addiction OR "problematic use") AND (adolescen* OR teen* OR youth)`
            → Phone addiction in young people
        
        13. `"online learning" AND (effectiveness OR "learning outcomes" OR performance) AND (pandemic OR COVID-19)`
            → Online learning during pandemic
        
        14. `(renewable AND energy) AND (solar OR wind OR hydro) NOT nuclear`
            → Renewable energy excluding nuclear
        
        15. `"climate change" AND (agriculture OR farming) AND (India OR "South Asia")`
            → Climate impact on agriculture in India
        
        **Field-Specific Examples:**
        
        **Medicine:**
        16. `(diabetes OR "diabetes mellitus") AND (metformin OR insulin) AND "randomized controlled trial"`
        
        **Psychology:**
        17. `(CBT OR "cognitive behavioral therapy") AND (anxiety OR depression) AND effectiveness`
        
        **Education:**
        18. `("active learning" OR "flipped classroom") AND ("student engagement" OR motivation) AND "higher education"`
        
        **Engineering:**
        19. `("Internet of Things" OR IoT) AND (security OR privacy) AND (healthcare OR medical)`
        
        **Business:**
        20. `("employee satisfaction" OR "job satisfaction") AND (turnover OR retention) AND IT`
        
        **Complex Multi-Field Example:**
        21. `(("artificial intelligence" OR AI OR "machine learning") AND (education OR learning OR teaching)) 
            AND (effectiveness OR outcomes OR performance) 
            AND (2020 OR 2021 OR 2022 OR 2023 OR 2024)
            NOT "higher education"`
            → Recent AI in K-12 education effectiveness studies
        
        **💡 Pro Tips:**
        - Use OR for synonyms: `(smartphone OR "mobile phone" OR cellphone)`
        - Use AND to narrow: `AI AND education AND "developing countries"`
        - Use NOT to exclude: `cancer NOT "breast cancer"`
        - Use quotes for phrases: `"machine learning"` not `machine learning`
        - Use wildcards: `teach*` finds teach, teacher, teaching, teachers
        - Combine with parentheses: `(A OR B) AND (C OR D)`
        
        ---
        
        #### **Step 4: Evaluate Sources** ✅
        
        **Quality Criteria:**
        """)
        
        st.markdown("""
        | Criterion | Questions to Ask | Red Flags | Green Flags |
        |-----------|------------------|-----------|-------------|
        | **Relevance** | Does it address my research question? | Off-topic, tangential | Directly relevant |
        | **Recency** | Is it current? (usually last 5-10 years) | Outdated (unless seminal) | Recent publications |
        | **Peer Review** | Is it published in peer-reviewed journal? | Blog posts, Wikipedia | Peer-reviewed journals |
        | **Citations** | Is it cited by others? How many times? | Zero citations after 2+ years | Highly cited |
        | **Author Credentials** | Are authors experts in the field? | Unknown authors | Recognized experts |
        | **Journal Quality** | Is journal reputable? (Check Impact Factor) | Predatory journals | High-impact journals |
        | **Methodology** | Is research method sound? | Poor design, small sample | Rigorous methodology |
        | **Funding** | Who funded the research? | Conflicts of interest | Independent funding |
        """)
        
        st.markdown("""
        **Prioritization:**
        1. **Tier 1:** Recent (last 3 years), high-impact journals, highly cited
        2. **Tier 2:** Older but seminal works, moderate-impact journals
        3. **Tier 3:** Gray literature, reports, theses (use sparingly)
        
        ---
        
        #### **Step 5: Organize Literature** 📊
        
        **Reference Management Tools:**
        """)
        
        st.markdown("""
        | Tool | Pros | Cons | Cost | Best For |
        |------|------|------|------|----------|
        | **Zotero** | Free, open-source, browser integration | Learning curve | Free | Budget-conscious researchers |
        | **Mendeley** | Free, PDF annotation, social features | Owned by Elsevier | Free | Collaborative research |
        | **EndNote** | Powerful, widely used in academia | Expensive, complex | Paid | Institutional users |
        | **RefWorks** | Cloud-based, institutional access | Requires subscription | Paid | University students |
        | **Paperpile** | Google Docs integration, clean interface | Subscription required | Paid | Google Workspace users |
        """)
        
        st.markdown("""
        **Organization Strategies:**
        
        **1. By Theme:**
        - Folder: "AI in Education"
          - Subfolder: "Learning Outcomes"
          - Subfolder: "Teacher Attitudes"
          - Subfolder: "Implementation Challenges"
        
        **2. By Methodology:**
        - Quantitative Studies
        - Qualitative Studies
        - Mixed Methods
        - Reviews
        
        **3. By Chronology:**
        - 2020-2024
        - 2015-2019
        - Before 2015 (Seminal Works)
        
        **Literature Matrix Template:**
        """)
        
        st.markdown("""
        | Author (Year) | Research Question | Method | Sample | Key Findings | Limitations | Relevance to My Study |
        |---------------|-------------------|--------|--------|--------------|-------------|----------------------|
        | Smith (2020) | Does AI improve learning? | Experiment | 200 students | 15% improvement | Small sample | Supports my hypothesis |
        | Jones (2021) | Teacher attitudes to AI | Survey | 500 teachers | 60% positive | Self-report bias | Informs my survey design |
        | Lee (2022) | AI in rural schools | Case study | 5 schools | Implementation challenges | Limited generalizability | Directly relevant to my context |
        """)
        
        st.markdown("""
        ---
        
        #### **Step 6: Synthesize and Write** ✍️
        
        **Don't Just Summarize — Synthesize!**
        
        ❌ **Bad (Summary):**
        "Smith (2020) found that AI improves learning. Jones (2021) found teachers like AI. Lee (2022) found students are motivated."
        
        ✅ **Good (Synthesis):**
        "Research consistently shows positive impacts of AI in education. Learning outcomes improve by 10-20% (Smith, 2020; Chen, 2021), 
        teachers report increased efficiency (Jones, 2021), and students show higher motivation (Lee, 2022). However, these studies 
        focus primarily on developed countries, leaving a gap in understanding AI's impact in resource-constrained settings."
        
        **Organization Patterns:**
        
        1. **Thematic:** Group by topics (most common)
           - Theme 1: Learning Outcomes
           - Theme 2: Teacher Training
           - Theme 3: Implementation Challenges
        
        2. **Chronological:** Historical development
           - Early AI in Education (1960s-1990s)
           - Modern AI Tutors (2000-2015)
           - Current Trends (2015-present)
        
        3. **Methodological:** Group by research approach
           - Experimental Studies
           - Survey Research
           - Qualitative Case Studies
        
        **Writing Tips:**
        - Use transition phrases: "Similarly...", "In contrast...", "Building on this..."
        - Show relationships: "While Smith found X, Jones found Y, suggesting..."
        - Identify patterns: "A consistent finding across studies is..."
        - Highlight gaps: "Despite extensive research on X, little is known about Y..."
        - Be critical: "However, these studies suffer from small sample sizes..."
        """)

    with st.expander("🔬 Advanced Literature Search Techniques", expanded=True):
        st.markdown("""
        ### Pro Tips for Efficient Literature Search
        
        **1. Citation Chaining** 🔗
        - **Forward Citation:** Who cited this paper? (Use Google Scholar "Cited by")
        - **Backward Citation:** What did this paper cite? (Check references)
        
        **Example:**
        - Find seminal paper: Smith (2015) on AI in education
        - Backward: Read the 50 papers Smith cited
        - Forward: Read the 200 papers that cited Smith
        - Result: Comprehensive coverage of the field
        
        **2. Snowball Sampling** ❄️
        - Start with 1-2 key papers
        - Read their references
        - Read papers that cited them
        - Repeat until saturation (no new themes)
        
        **3. Use Review Papers** 📖
        - Search for "systematic review" or "meta-analysis"
        - These summarize 50-100 studies
        - Excellent starting point
        - Check their reference lists
        
        **4. Set Up Alerts** 🔔
        - Google Scholar: Create alerts for keywords
        - Journal websites: Subscribe to new issue alerts
        - ResearchGate: Follow researchers
        - Get notified when new relevant papers publish
        
        **5. Use Advanced Search Features** 🔍
        
        **Google Scholar Advanced Search:**
        - "with all of the words": AND logic
        - "with the exact phrase": " " quotes
        - "with at least one of the words": OR logic
        - "without the words": NOT logic
        - "where my words occur": in title, anywhere
        - "Return articles dated between": time filter
        
        **6. Check Grey Literature** 📄
        - Theses and dissertations (ProQuest)
        - Conference proceedings
        - Government reports
        - White papers
        - Technical reports
        - Working papers
        
        **7. Use Citation Metrics** 📊
        - Sort by "Cited by" in Google Scholar
        - Highly cited = influential papers
        - But don't ignore recent papers (haven't had time to accumulate citations)
        
        **8. Language and Translation** 🌍
        - Most databases are English-dominant
        - Use Google Translate for non-English abstracts
        - Consider including non-English studies if relevant
        - Mention language limitations in your review
        """)

    with st.expander("🎯 Research Problem Identification", expanded=True):
        st.markdown("""
        ### How to Identify a Good Research Problem
        
        A research problem is the foundation of your entire study. Here's how to find and refine one:
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Sources of Research Problems:**
            
            | Source | Description | Example |
            |--------|-------------|---------|
            | **Personal Experience** | Observations from your work/life | "I noticed students struggle with online learning" |
            | **Theory Gaps** | Theory doesn't explain new phenomena | "Existing motivation theories don't explain gig economy workers" |
            | **Literature Gaps** | "No study has examined..." | "No research on AI in rural Indian schools" |
            | **Practical Problems** | Organizations need solutions | "Company wants to reduce employee turnover" |
            | **Technological Changes** | New tools enable new research | "ChatGPT enables new studies on AI writing assistance" |
            | **Conflicting Findings** | Studies disagree | "Some studies show X, others show Y — why?" |
            | **Policy Needs** | Government/institutions need evidence | "Government needs data on electric vehicle adoption" |
            | **Emerging Trends** | New phenomena to understand | "Rise of remote work during pandemic" |
            """)
        
        with col2:
            st.markdown("""
            **Characteristics of a GOOD Research Problem:**
            
            ✅ **CLEAR and SPECIFIC**
            - ❌ Bad: "Study social media"
            - ✅ Good: "Impact of Instagram use on anxiety in college students"
            
            ✅ **RESEARCHABLE** (Can gather data)
            - ❌ Bad: "Is God real?" (philosophical, not empirical)
            - ✅ Good: "Do religious beliefs correlate with life satisfaction?"
            
            ✅ **SIGNIFICANT** (Contributes to knowledge)
            - ❌ Bad: "Do students prefer blue or red pens?" (trivial)
            - ✅ Good: "Does pen color affect memory retention?" (if theory suggests it might)
            
            ✅ **FEASIBLE** (Resources available)
            - ❌ Bad: "Global survey of all internet users" (impossible)
            - ✅ Good: "Survey of 500 university students in Delhi"
            
            ✅ **ORIGINAL** (Not already solved)
            - ❌ Bad: "Does smoking cause cancer?" (well-established)
            - ✅ Good: "Does vaping cause cancer?" (emerging question)
            
            ✅ **ETHICAL** (Doesn't harm participants)
            - ❌ Bad: "Induce depression to study effects"
            - ✅ Good: "Survey people with existing depression"
            """)
        
        st.markdown("""
        ---
        ### 🔄 From Broad Interest to Specific Problem
        
        **Example Evolution:**
        
        | Stage | Statement | Issue |
        |-------|-----------|-------|
        | **1. Too Broad** | "I'm interested in education" | Not a research problem |
        | **2. Narrowing** | "I want to study online education" | Still too broad |
        | **3. More Specific** | "I want to study effectiveness of online education" | Better, but vague |
        | **4. Focused** | "Does online learning affect student performance?" | Good, but needs context |
        | **5. Research Problem** | "How does online learning affect academic performance of engineering students in Indian universities compared to traditional classroom learning?" | ✅ Specific, researchable, significant |
        
        ---
        ### 🎯 Problem Statement Template
        
        **Formula:**
        > "This study examines [WHAT] among [WHO] in [WHERE] to [WHY/PURPOSE]."
        
        **Examples:**
        
        1. **Business:** "This study examines the factors affecting employee retention among IT professionals in Bangalore to help companies reduce turnover costs."
        
        2. **Education:** "This study examines the impact of gamification on student engagement among high school students in rural Maharashtra to improve learning outcomes."
        
        3. **Health:** "This study examines the relationship between smartphone use and sleep quality among college students in Delhi to inform health interventions."
        
        4. **Engineering:** "This study examines the effectiveness of solar panels in reducing electricity costs among residential users in Rajasthan to promote renewable energy adoption."
        
        5. **Social Science:** "This study examines the impact of social media on political participation among young voters in urban India to understand democratic engagement."
        
        ---
        ### ⚠️ Common Mistakes to Avoid
        
        | Mistake | Example | Fix |
        |---------|---------|-----|
        | **Too Broad** | "Study of climate change" | "Impact of climate change on rice yield in Punjab" |
        | **Not Researchable** | "What is the meaning of life?" | "How do people find meaning in life after trauma?" |
        | **Already Solved** | "Does exercise improve health?" | "Does HIIT improve health more than moderate exercise?" |
        | **No Gap** | Repeating existing study exactly | Add new context, population, or variable |
        | **Not Significant** | "Do students prefer morning or evening classes?" | Only significant if linked to learning outcomes |
        | **Unfeasible** | "Survey all doctors in India" | "Survey 300 doctors in Delhi hospitals" |
        | **Unethical** | "Expose children to violence" | "Survey children exposed to violence" |
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
