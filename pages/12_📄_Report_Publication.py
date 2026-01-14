import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Research Report Writing & Publication | Structure, Citations, Impact Factor [2024]",
    description="Master research report writing: report structure, citation styles, journal publication process, research metrics (Impact Factor, h-index, SNIP, SJR) for Ph.D. researchers.",
    keywords=[
        "research report writing",
        "research paper structure",
        "journal publication",
        "impact factor",
        "h-index",
        "citation metrics",
        "primary secondary data",
        "APA citation",
        "IEEE citation",
        "research ethics"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/methodology/publication",
    reading_time=80,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Report & Publication", "url": "https://researchethics.dev/methodology/publication"}
    ],
    course_info={
        "name": "Research Report & Publication - Paper I Unit IV",
        "description": "Complete guide to research report writing, publication process, and research metrics.",
        "level": "Doctoral",
        "prerequisites": "Measurement & Sampling",
        "teaches": ["Report Writing", "Publication Process", "Research Metrics", "Citations"],
        "workload": "PT15H",
        "rating": "4.9",
        "rating_count": 912
    }
)
apply_custom_css()
show_top_nav(current_page="Report & Publication")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📄 Unit IV: Research Report & Publication</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #c2410c;">Paper I: Research Methodology — Communicating your research to the world.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Data Types",
    "📝 Report Writing",
    "📚 Publication Process",
    "📈 Research Metrics",
    "⚖️ Ethics & Plagiarism"
])

# =============================================================================
# TAB 1: PRIMARY AND SECONDARY DATA
# =============================================================================
with tab1:
    st.markdown("## 📊 Chapter 1: Primary and Secondary Data")
    
    st.markdown("### 1.1 Types of Data")
    
    with st.expander("📋 Primary vs Secondary Data", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
                <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📊 Primary Data</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Data collected firsthand for your specific research<br><br>
                <b>Sources:</b><br>
                • Surveys/Questionnaires<br>
                • Interviews<br>
                • Experiments<br>
                • Observations<br>
                • Focus groups<br><br>
                <b>Pros:</b> Specific to research, current, controlled<br>
                <b>Cons:</b> Time-consuming, expensive
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a;">
                <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📚 Secondary Data</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Data already collected by others<br><br>
                <b>Sources:</b><br>
                • Census data<br>
                • Government reports<br>
                • Published research<br>
                • Company records<br>
                • Databases<br><br>
                <b>Pros:</b> Quick, inexpensive, large scale<br>
                <b>Cons:</b> May not fit needs, outdated
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        | Aspect | Primary Data | Secondary Data |
        |--------|--------------|----------------|
        | **Collection** | By researcher | By others |
        | **Purpose** | Specific to study | General/other purposes |
        | **Cost** | High | Low |
        | **Time** | Long | Short |
        | **Control** | Full | None |
        | **Currency** | Current | May be outdated |
        """)

    with st.expander("🎯 Sampling Techniques Recap", expanded=True):
        st.markdown("""
        **Probability Sampling Methods:**
        
        | Method | How It Works | When to Use |
        |--------|--------------|-------------|
        | **Simple Random** | Each has equal probability | Homogeneous population |
        | **Stratified Random** | Divide into groups, random from each | Known subgroups |
        | **Systematic** | Every kth element | Available list |
        | **Cluster** | Randomly select groups | Geographically dispersed |
        
        **Non-Probability Sampling:**
        
        | Method | How It Works | When to Use |
        |--------|--------------|-------------|
        | **Convenience** | Whoever is available | Pilot studies |
        | **Purposive** | Select based on criteria | Expert interviews |
        | **Snowball** | Referrals from participants | Hidden populations |
        | **Quota** | Non-random meeting quotas | Field surveys |
        """)

# =============================================================================
# TAB 2: RESEARCH REPORT WRITING
# =============================================================================
with tab2:
    st.markdown("## 📝 Chapter 2: Research Report Writing")
    
    st.markdown("### 2.1 Structure of Research Report")
    
    with st.expander("📋 Standard Report Structure", expanded=True):
        st.markdown("""
        | Section | Content | Approximate % |
        |---------|---------|---------------|
        | **Title Page** | Title, author, affiliation, date | — |
        | **Abstract** | Summary (150-300 words) | 1-2% |
        | **Introduction** | Background, problem, objectives | 10-15% |
        | **Literature Review** | Previous research, gaps | 15-25% |
        | **Methodology** | Design, sample, instruments, analysis | 15-20% |
        | **Results** | Findings (tables, figures) | 20-25% |
        | **Discussion** | Interpretation, implications | 15-20% |
        | **Conclusion** | Summary, limitations, future research | 5-10% |
        | **References** | Cited works | — |
        | **Appendices** | Questionnaires, data, etc. | — |
        """)
        
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=10, shape=box, style="rounded,filled"];
            
            title [label="Title Page", fillcolor="#dbeafe"];
            abstract [label="Abstract", fillcolor="#dcfce7"];
            intro [label="Introduction", fillcolor="#fef3c7"];
            lit [label="Literature Review", fillcolor="#f3e8ff"];
            method [label="Methodology", fillcolor="#fed7aa"];
            results [label="Results", fillcolor="#fecaca"];
            discuss [label="Discussion", fillcolor="#e0e7ff"];
            conclude [label="Conclusion", fillcolor="#d1fae5"];
            refs [label="References", fillcolor="#f3f4f6"];
            
            title -> abstract -> intro -> lit -> method -> results -> discuss -> conclude -> refs;
        }
        """)

    with st.expander("✍️ Writing Tips by Section", expanded=True):
        st.markdown("""
        ### Abstract
        - Write LAST (after completing paper)
        - Include: Purpose, Methods, Key findings, Conclusions
        - Stand-alone summary
        - Keywords below abstract
        
        ### Introduction
        - Start broad, narrow to specific
        - State problem clearly
        - Justify importance ("So what?")
        - End with objectives/hypotheses
        
        ### Literature Review
        - Not just summary — synthesize and critique
        - Organize thematically or chronologically
        - Identify gaps your research fills
        - Use recent, relevant sources
        
        ### Methodology
        - Be reproducible — another researcher should replicate
        - Justify choices (why this design? this sample?)
        - Include: Design, population, sampling, instruments, procedure, analysis
        
        ### Results
        - Present findings, NOT interpretations
        - Use tables and figures effectively
        - Start with descriptive statistics
        - Address each hypothesis/objective
        
        ### Discussion
        - Interpret results — what do they mean?
        - Compare with previous studies
        - Explain unexpected findings
        - Acknowledge limitations
        
        ### Conclusion
        - Summarize key findings
        - State contributions to knowledge
        - Suggest practical implications
        - Recommend future research
        """)

    with st.expander("📊 Tables and Figures", expanded=True):
        st.markdown("""
        **Tables vs Figures:**
        
        | Use Tables When | Use Figures When |
        |-----------------|------------------|
        | Precise values needed | Patterns/trends important |
        | Comparisons across categories | Relationships to visualize |
        | Many numbers to report | Quick overview needed |
        
        **Table Best Practices:**
        - Number tables sequentially (Table 1, 2, 3...)
        - Title above table
        - Clear column/row headers
        - Notes below for abbreviations
        - Don't duplicate data in text
        
        **Figure Best Practices:**
        - Number figures sequentially
        - Caption below figure
        - High resolution
        - Clear labels and legends
        - Consistent style throughout
        """)

    with st.expander("📚 Citation Styles", expanded=True):
        st.markdown("""
        | Style | Field | Example (In-text) |
        |-------|-------|-------------------|
        | **APA** | Social Sciences | (Smith, 2020) |
        | **MLA** | Humanities | (Smith 45) |
        | **Chicago** | History | (Smith 2020, 45) |
        | **Harvard** | Business | (Smith 2020) |
        | **IEEE** | Engineering | [1] |
        | **Vancouver** | Medical | (1) or superscript¹ |
        
        **APA 7th Edition Example:**
        
        **Book:**
        Smith, J. D. (2020). *Research methods*. Publisher.
        
        **Journal Article:**
        Smith, J. D., & Jones, M. (2020). Title of article. *Journal Name*, *12*(3), 45-67. https://doi.org/...
        
        **Website:**
        Smith, J. D. (2020, January 15). *Title of page*. Site Name. https://www.example.com
        """)

# =============================================================================
# TAB 3: JOURNAL PUBLICATION PROCESS
# =============================================================================
with tab3:
    st.markdown("## 📚 Chapter 3: Journal Publication Process")
    
    st.markdown("### 3.1 Publication Process Flow")
    
    with st.expander("📋 Step-by-Step Publication Process", expanded=True):
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=10, shape=box, style="rounded,filled"];
            
            write [label="1. Write Manuscript", fillcolor="#dbeafe"];
            choose [label="2. Choose Journal", fillcolor="#dcfce7"];
            format [label="3. Format per Guidelines", fillcolor="#fef3c7"];
            submit [label="4. Submit", fillcolor="#f3e8ff"];
            review [label="5. Peer Review", fillcolor="#fed7aa"];
            decision [label="6. Editorial Decision", fillcolor="#fecaca", shape=diamond];
            revise [label="7. Revise", fillcolor="#e0e7ff"];
            accept [label="8. Accepted", fillcolor="#d1fae5"];
            publish [label="9. Published", fillcolor="#86efac"];
            
            write -> choose -> format -> submit -> review -> decision;
            decision -> accept [label="Accept"];
            decision -> revise [label="Revise"];
            decision -> write [label="Reject", style=dashed];
            revise -> review;
            accept -> publish;
        }
        """)
        
        st.markdown("""
        | Stage | Duration | What Happens |
        |-------|----------|--------------|
        | Submission | 1 day | Upload manuscript, cover letter |
        | Initial Screening | 1-2 weeks | Editor checks fit, quality |
        | Peer Review | 1-3 months | Expert reviewers evaluate |
        | Decision | 1 week | Accept/Revise/Reject |
        | Revision | 2-4 weeks | Author addresses comments |
        | Re-review | 2-4 weeks | May need second round |
        | Acceptance | 1 week | Final decision |
        | Production | 1-2 months | Copyediting, proofs |
        | Publication | Variable | Online first or issue |
        """)

    with st.expander("🎯 Choosing the Right Journal", expanded=True):
        st.markdown("""
        **Criteria for Journal Selection:**
        
        | Factor | Consideration |
        |--------|---------------|
        | **Scope** | Does your topic fit the journal? |
        | **Impact Factor** | Appropriate for your career stage? |
        | **Audience** | Who do you want to reach? |
        | **Indexing** | Scopus, Web of Science, PubMed? |
        | **Turnaround** | How fast is peer review? |
        | **Cost** | Open Access fees (APCs)? |
        | **Reputation** | Avoid predatory journals! |
        
        **Red Flags (Predatory Journals):**
        - ❌ Spam emails inviting submission
        - ❌ Very fast peer review (days)
        - ❌ No clear editorial board
        - ❌ Not indexed in major databases
        - ❌ Poor language/website quality
        - ❌ Pressure to publish quickly
        
        **Verification Resources:**
        - DOAJ (Directory of Open Access Journals)
        - UGC-CARE List (India)
        - Think. Check. Submit.
        - Journal Citation Reports (JCR)
        """)

    with st.expander("📝 Peer Review Process", expanded=True):
        st.markdown("""
        **Types of Peer Review:**
        
        | Type | Author knows reviewer | Reviewer knows author |
        |------|----------------------|----------------------|
        | **Single-blind** | No | Yes |
        | **Double-blind** | No | No |
        | **Open** | Yes | Yes |
        | **Triple-blind** | No (Editor also blind) | No |
        
        **Typical Decisions:**
        
        | Decision | Meaning | Action |
        |----------|---------|--------|
        | **Accept** | Publish as is | Celebrate! |
        | **Minor Revisions** | Small changes needed | Quick revision, resubmit |
        | **Major Revisions** | Significant changes | Substantial revision |
        | **Reject & Resubmit** | Extensive changes | New submission |
        | **Reject** | Not suitable | Submit elsewhere |
        
        **Responding to Reviews:**
        - Be thorough and respectful
        - Address every comment
        - Provide point-by-point response
        - Highlight changes in manuscript
        - If you disagree, justify politely
        """)

# =============================================================================
# TAB 4: RESEARCH METRICS
# =============================================================================
with tab4:
    st.markdown("## 📈 Chapter 4: Research Metrics")
    
    st.markdown("### 4.1 Journal Metrics")
    
    with st.expander("📊 Impact Factor", expanded=True):
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb; margin-bottom: 10px;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Impact Factor (IF)</b> is the average number of citations received in a year by articles published in the previous two years.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Formula:**")
        st.latex(r"IF_{2024} = \frac{\text{Citations in 2024 to articles from 2022-2023}}{\text{Citable items in 2022-2023}}")
        
        st.markdown("""
        **Example:**
        - Journal X published 100 articles in 2022-2023
        - These received 250 citations in 2024
        - IF = 250/100 = 2.5
        
        **Interpretation:**
        - IF > 10: Very high impact
        - IF 3-10: Good impact
        - IF 1-3: Moderate impact
        - IF < 1: Low impact
        
        **Limitations:**
        - Favors review articles
        - Field-dependent
        - Can be manipulated
        - Doesn't measure article quality
        """)

    with st.expander("📊 Other Journal Metrics", expanded=True):
        st.markdown("""
        | Metric | Source | Description |
        |--------|--------|-------------|
        | **CiteScore** | Scopus | Citations/publications over 4 years |
        | **SJR** | Scopus | Prestige-weighted citations |
        | **SNIP** | Scopus | Normalized for field differences |
        | **IPP** | Scopus | Impact per Publication (3 years) |
        | **Eigenfactor** | Web of Science | Network-based importance |
        | **Article Influence** | Web of Science | Per-article Eigenfactor |
        
        **SJR (SCImago Journal Rank):**
        - Citations from high-prestige journals count more
        - Like PageRank for journals
        - Normalized by field
        
        **SNIP (Source Normalized Impact per Paper):**
        - Accounts for citation potential in field
        - Good for comparing across disciplines
        """)

    st.markdown("### 4.2 Author Metrics")
    
    with st.expander("👤 h-index and Related Metrics", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 h-index (Hirsch Index)</h4>
            <p style="margin: 0 !important; font-size: 13px;">An author has h-index <b>h</b> if they have published <b>h</b> papers that each have at least <b>h</b> citations.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Example:**
        - Author has papers with citations: 25, 18, 12, 10, 8, 5, 3, 1
        - h = 5 (5 papers with ≥5 citations each)
        
        **Related Metrics:**
        
        | Metric | Definition |
        |--------|------------|
        | **h-index** | h papers with ≥h citations |
        | **g-index** | Top g papers have ≥g² total citations |
        | **i10-index** | Papers with ≥10 citations |
        
        **Interpretation (varies by field):**
        - h > 40: Outstanding researcher
        - h = 20-40: Established researcher
        - h = 10-20: Active researcher
        - h < 10: Early career
        """)

    with st.expander("📊 Metric Databases", expanded=True):
        st.markdown("""
        | Database | Journal Metrics | Author Metrics |
        |----------|-----------------|----------------|
        | **Web of Science** | Impact Factor, Eigenfactor | h-index |
        | **Scopus** | CiteScore, SJR, SNIP | h-index |
        | **Google Scholar** | — | h-index, i10-index |
        
        **Note:** Different databases may give different h-index values due to coverage differences.
        """)

# =============================================================================
# TAB 5: ETHICS AND PLAGIARISM
# =============================================================================
with tab5:
    st.markdown("## ⚖️ Chapter 5: Research Ethics and Plagiarism")
    
    st.markdown("### 5.1 Research Ethics")
    
    with st.expander("📋 Ethical Principles in Research", expanded=True):
        st.markdown("""
        | Principle | Description |
        |-----------|-------------|
        | **Honesty** | Report methods and findings truthfully |
        | **Objectivity** | Avoid bias in design, analysis, interpretation |
        | **Integrity** | Keep promises, act with sincerity |
        | **Carefulness** | Avoid errors, thoroughly review work |
        | **Openness** | Share data, methods, results |
        | **Respect for IP** | Cite sources, respect patents |
        | **Confidentiality** | Protect participant data |
        | **Responsible Publication** | Avoid redundancy, misconduct |
        | **Respect for Colleagues** | Fair treatment, mentorship |
        | **Social Responsibility** | Consider societal impact |
        """)

    with st.expander("🚫 Types of Research Misconduct (FFP)", expanded=True):
        st.markdown("""
        <div style="background: #fef2f2; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444; margin-bottom: 10px;">
            <h4 style="color: #dc2626; margin: 0 0 8px 0 !important;">⚠️ The Big Three (FFP)</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            **Fabrication**
            - Making up data
            - Inventing results
            - Creating fake experiments
            """)
        with col2:
            st.markdown("""
            **Falsification**
            - Manipulating data
            - Altering images
            - Omitting inconvenient results
            """)
        with col3:
            st.markdown("""
            **Plagiarism**
            - Copying without credit
            - Self-plagiarism
            - Ghost writing
            """)

    with st.expander("📝 Understanding Plagiarism", expanded=True):
        st.markdown("""
        **Types of Plagiarism:**
        
        | Type | Description |
        |------|-------------|
        | **Copy-Paste** | Direct copying without quotes/citation |
        | **Paraphrasing** | Rewording without citation |
        | **Mosaic/Patchwork** | Mixing multiple sources |
        | **Self-Plagiarism** | Reusing own previous work |
        | **Ghost Authorship** | Not crediting true author |
        | **Citation Manipulation** | Citing work not consulted |
        
        **How to Avoid Plagiarism:**
        - ✅ Always cite sources
        - ✅ Use quotation marks for direct quotes
        - ✅ Paraphrase AND cite (paraphrasing alone isn't enough)
        - ✅ Keep track of all sources while researching
        - ✅ Use plagiarism detection tools before submission
        - ✅ Understand what needs citation (not common knowledge)
        
        **Plagiarism Detection Tools:**
        - Turnitin
        - Urkund/Ouriginal
        - iThenticate
        - Grammarly (basic)
        - DupliChecker (free)
        """)

    with st.expander("📚 References for This Course", expanded=True):
        st.markdown("""
        **Core Textbook:**
        - **C.R. Kothari** – *Research Methodology: Methods and Techniques* (New Age International)
        
        **Supplementary Resources:**
        - *Step-by-Step Guide for Beginners* (Pearson)
        - ACM Digital Library
        - IEEE Xplore
        - Elsevier ScienceDirect
        - Springer Nature
        
        **Research Ethics Resources:**
        - COPE (Committee on Publication Ethics)
        - ORI (Office of Research Integrity)
        - ICMJE Guidelines
        - Singapore Statement on Research Integrity
        """)

# Footer
show_footer()
