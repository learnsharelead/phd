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
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📖 Meaning & Types",
    "🔍 Research Procedures",
    "📚 Literature Survey",
    "🎯 Hypothesis",
    "📋 Classification"
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
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📝 Descriptive Research</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Purpose:</b> Describe characteristics of a phenomenon<br>
                <b>Question:</b> "What is happening?"<br>
                <b>Example:</b> Survey of consumer preferences<br>
                <b>Methods:</b> Surveys, observations, case studies
                </p>
            </div>
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🔬 Analytical Research</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Purpose:</b> Analyze and explain relationships<br>
                <b>Question:</b> "Why is this happening?"<br>
                <b>Example:</b> Analyzing causes of customer churn<br>
                <b>Methods:</b> Statistical analysis, hypothesis testing
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">⚙️ Applied Research</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Purpose:</b> Solve practical problems<br>
                <b>Question:</b> "How can we fix this?"<br>
                <b>Example:</b> Developing a new drug<br>
                <b>Outcome:</b> Solutions, products, policies
                </p>
            </div>
            <div style="background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🎓 Fundamental/Basic Research</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Purpose:</b> Expand knowledge, no immediate application<br>
                <b>Question:</b> "What is the nature of X?"<br>
                <b>Example:</b> Studying quantum mechanics<br>
                <b>Outcome:</b> Theories, principles
                </p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("🔢 Quantitative vs Qualitative Research", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 14px; border-radius: 8px;">
                <h4 style="margin: 0 0 8px 0 !important;">📊 Quantitative Research</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Focus:</b> Numbers, measurements, statistics<br>
                <b>Data:</b> Numerical (scores, counts, ratings)<br>
                <b>Analysis:</b> Statistical tests<br>
                <b>Sample:</b> Large, representative<br>
                <b>Goal:</b> Generalization, prediction<br>
                <b>Questions:</b> How many? How much? What's the relationship?
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 14px; border-radius: 8px;">
                <h4 style="margin: 0 0 8px 0 !important;">📝 Qualitative Research</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Focus:</b> Meanings, experiences, perspectives<br>
                <b>Data:</b> Words, images, observations<br>
                <b>Analysis:</b> Thematic, content analysis<br>
                <b>Sample:</b> Small, purposive<br>
                <b>Goal:</b> Deep understanding<br>
                <b>Questions:</b> Why? How do people experience X?
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        | Aspect | Quantitative | Qualitative |
        |--------|--------------|-------------|
        | **Paradigm** | Positivist | Interpretivist |
        | **Reality** | Objective, measurable | Subjective, constructed |
        | **Researcher Role** | Detached, objective | Immersed, interpretive |
        | **Data Collection** | Surveys, experiments | Interviews, observations |
        | **Output** | Statistics, graphs | Themes, narratives |
        """)

    with st.expander("💡 Conceptual vs Empirical Research", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">💭 Conceptual Research</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Abstract thinking, theorizing<br>
                <b>Data:</b> Existing theories, literature<br>
                <b>Method:</b> Logical analysis, synthesis<br>
                <b>Example:</b> Developing a new theoretical framework
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: #dbeafe; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
                <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">🔬 Empirical Research</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Based on observation, experiment<br>
                <b>Data:</b> Collected from real world<br>
                <b>Method:</b> Systematic observation/measurement<br>
                <b>Example:</b> Testing a drug's effectiveness
                </p>
            </div>
            """, unsafe_allow_html=True)

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

# Footer
show_footer()
