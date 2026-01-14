import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Research Metrics & Databases | Impact Factor, h-index, Scopus, Web of Science [2024]",
    description="Master research metrics including Impact Factor, h-index, g-index, CiteScore, and navigate databases like Scopus, Web of Science, PubMed. Complete guide for Ph.D. researchers.",
    keywords=[
        "impact factor",
        "h-index",
        "g-index",
        "i10-index",
        "scopus",
        "web of science",
        "pubmed",
        "citescore",
        "journal citation reports",
        "SCI journals",
        "ESCI",
        "SNIP",
        "SJR",
        "eigenfactor",
        "altmetrics",
        "research databases",
        "citation databases"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/research-metrics",
    reading_time=90,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Research Metrics", "url": "https://researchethics.dev/research-metrics"}
    ],
    course_info={
        "name": "Research Metrics and Databases Module",
        "description": "Comprehensive coverage of journal metrics, author metrics, citation databases, and research discovery tools.",
        "level": "Doctoral",
        "prerequisites": "Basic research experience",
        "teaches": ["Impact Factor", "h-index", "Scopus", "Web of Science", "Citation Analysis", "Research Databases"],
        "workload": "PT15H",
        "rating": "4.9",
        "rating_count": 756
    },
    faq_items=[
        {
            "question": "What is Impact Factor and how is it calculated?",
            "answer": "Impact Factor (IF) is a measure of the average citation frequency of articles published in a journal. It's calculated by dividing the citations received in a year by the citable items published in the previous two years."
        },
        {
            "question": "What is the difference between SCI and ESCI?",
            "answer": "SCI (Science Citation Index) includes high-impact journals meeting strict criteria. ESCI (Emerging Sources Citation Index) includes promising journals being evaluated for potential SCI inclusion."
        },
        {
            "question": "What is h-index?",
            "answer": "The h-index is an author-level metric where h is the number of papers with at least h citations each. For example, h-index of 10 means 10 papers have each been cited at least 10 times."
        }
    ]
)
apply_custom_css()
show_top_nav(current_page="Research Metrics")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📊 Module 2: Research Metrics & Databases</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #166534;">Understanding how research impact is measured and where to find quality literature.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 Introduction",
    "📰 Journal Metrics",
    "👤 Author Metrics",
    "🗄️ Major Databases",
    "🔓 Open Access",
    "🧮 Calculators"
])

# =============================================================================
# TAB 1: INTRODUCTION TO RESEARCH METRICS
# =============================================================================
with tab1:
    st.markdown("## 📈 Chapter 1: Introduction to Research Metrics")
    
    st.markdown("### 1.1 What are Research Metrics?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Research Metrics</b> (or Bibliometrics) are quantitative measures used to evaluate the impact, quality, and productivity of research, researchers, journals, and institutions.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Report Card for Research</h4>
            <p style="margin: 0 !important; font-size: 13px;">Research metrics are like a <b>report card</b> for scholarly work. Just as grades measure student performance, metrics measure research impact.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("❓ Why Do We Need Research Metrics?", expanded=True):
        st.markdown("""
        **Key Purposes:**
        
        | Purpose | Application |
        |---------|-------------|
        | **Evaluation** | Assess researcher/institution performance |
        | **Funding Decisions** | Allocate research grants |
        | **Career Advancement** | Hiring, tenure, promotions |
        | **Journal Selection** | Choose where to publish |
        | **Benchmarking** | Compare across fields/institutions |
        | **Policy Making** | Research investment decisions |
        
        **⚠️ Important Caveat:**
        No single metric tells the complete story. Metrics should be used thoughtfully, alongside qualitative assessment (as per DORA Declaration).
        """)

    with st.expander("🗂️ Types of Research Metrics", expanded=True):
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=11, shape=box, style="rounded,filled"];
            
            metrics [label="RESEARCH\\nMETRICS", fillcolor="#d1fae5", shape=ellipse, fontsize=12];
            
            journal [label="Journal Metrics\\n(Impact Factor, CiteScore)", fillcolor="#dbeafe"];
            article [label="Article Metrics\\n(Citations, Downloads)", fillcolor="#f3e8ff"];
            author [label="Author Metrics\\n(h-index, i10-index)", fillcolor="#fef3c7"];
            alt [label="Alternative Metrics\\n(Altmetrics)", fillcolor="#fed7aa"];
            
            metrics -> journal; metrics -> article; metrics -> author; metrics -> alt;
        }
        """)

# =============================================================================
# TAB 2: JOURNAL AND ARTICLE METRICS
# =============================================================================
with tab2:
    st.markdown("## 📰 Chapter 2: Journal and Article Metrics")
    
    # Impact Factor
    st.markdown("### 2.1 Impact Factor (IF)")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Impact Factor</b> is the average number of citations received per paper published in a journal during the two preceding years. Calculated and published by Clarivate in the Journal Citation Reports (JCR).</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Restaurant Reviews</h4>
            <p style="margin: 0 !important; font-size: 13px;">IF is like the <b>average rating</b> of a restaurant. A higher rating suggests people generally had a good experience, but doesn't guarantee YOUR meal will be perfect.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🧮 How is Impact Factor Calculated?", expanded=True):
        st.markdown("""
        **Formula:**
        ```
        Impact Factor (Year X) = Citations in Year X to articles from Years X-1 and X-2
                                 ÷ 
                                 Citable items published in Years X-1 and X-2
        ```
        
        **Example:**
        - Journal published **100 articles** in 2022 and **100 articles** in 2023
        - Those 200 articles received **500 citations** in 2024
        - **IF for 2024 = 500 ÷ 200 = 2.5**
        
        **Interpretation:**
        | IF Range | Interpretation |
        |----------|----------------|
        | > 10 | Excellent (top-tier journals) |
        | 5-10 | Very Good |
        | 2-5 | Good |
        | 1-2 | Moderate |
        | < 1 | Low (may still be quality journals) |
        
        ⚠️ **Note:** IF varies significantly by field. A 2.0 IF might be excellent in humanities but low in biomedical sciences.
        """)

    # SCI and ESCI
    with st.expander("🏆 SCI and ESCI", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🥇 SCI (Science Citation Index)</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Premier index of high-impact journals<br>
                <b>Criteria:</b> Impact, influence, timeliness<br>
                <b>Coverage:</b> ~9,500 journals (2024)<br>
                <b>Status:</b> Gold standard for science journals
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🥈 ESCI (Emerging Sources Citation Index)</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Index for emerging quality journals<br>
                <b>Criteria:</b> Meeting basic standards, under review<br>
                <b>Path:</b> May graduate to SCI after evaluation<br>
                <b>Status:</b> Legitimate but less established
                </p>
            </div>
            """, unsafe_allow_html=True)

    # Web of Science and JCR
    with st.expander("🌐 Web of Science & Journal Citation Reports (JCR)", expanded=True):
        st.markdown("""
        **Web of Science (WoS):**
        - Owned by Clarivate Analytics
        - Premier citation database
        - Includes: SCI, SSCI (Social Sciences), A&HCI (Arts & Humanities)
        - Gold standard for academic evaluation
        
        **Journal Citation Reports (JCR):**
        - Annual publication by Clarivate
        - Contains Impact Factors for journals in WoS
        - Released typically in June each year
        - Provides journal rankings by category
        
        **Key JCR Metrics:**
        | Metric | Description |
        |--------|-------------|
        | Impact Factor | 2-year citation average |
        | 5-Year IF | 5-year citation average |
        | Immediacy Index | Citations in publication year |
        | Cited Half-Life | Age of cited articles |
        | Eigenfactor Score | Journal's total influence |
        | Article Influence Score | Per-article influence |
        """)

    # Other Journal Metrics
    st.markdown("### 2.2 Other Journal Metrics")

    with st.expander("📊 CiteScore (Scopus)", expanded=True):
        col_def, col_calc = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
                <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>CiteScore</b> is Scopus's alternative to Impact Factor, measuring average citations per document over a 4-year window.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_calc:
            st.markdown("""
            **Formula:**
            ```
            CiteScore = Citations in Yr X to items from Yrs X, X-1, X-2, X-3
                        ÷
                        Documents published in Yrs X, X-1, X-2, X-3
            ```
            
            **Advantages over IF:**
            - Longer window (4 years vs 2)
            - Counts all document types
            - Free to access
            """)

    with st.expander("📈 SNIP, SJR, and Eigenfactor", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📐 SNIP</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Source Normalized Impact per Paper</b><br>
                Corrects for citation practices in different fields<br>
                A SNIP of 1.0 = average for the field
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📊 SJR</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>SCImago Journal Rank</b><br>
                Weights citations based on source quality<br>
                Like Google PageRank for journals
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🔢 Eigenfactor</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Journal's total influence score</b><br>
                Based on 5-year citations<br>
                Excludes self-citations
                </p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("📄 Article Influence Score", expanded=False):
        st.markdown("""
        **Article Influence Score (AI):**
        - Measures the average influence of a journal's articles over the first five years after publication
        - Normalized so that the mean article has an AI of 1.0
        - Calculated from Eigenfactor score
        - Comparable across disciplines
        
        **Formula:**
        ```
        Article Influence = Eigenfactor Score × 0.01
                           ÷
                           Fraction of articles in journal
        ```
        """)

# =============================================================================
# TAB 3: AUTHOR LEVEL METRICS
# =============================================================================
with tab3:
    st.markdown("## 👤 Chapter 3: Author Level Metrics")
    
    # h-index
    st.markdown("### 3.1 h-index")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>h-index</b> (Hirsch index) is the largest number h such that the researcher has h papers that have each been cited at least h times. Proposed by Jorge Hirsch in 2005.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: YouTube Views</h4>
            <p style="margin: 0 !important; font-size: 13px;">Imagine h-index for YouTubers: h=10 means you have 10 videos with at least 10,000 views each. It measures both <b>quantity</b> (videos) and <b>impact</b> (views).</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🧮 How to Calculate h-index", expanded=True):
        st.markdown("""
        **Step-by-Step:**
        1. List all papers in order of citations (highest to lowest)
        2. Find the point where paper number = citations received
        
        **Example:**
        | Paper # | Citations |
        |---------|-----------|
        | 1 | 45 | ✅ (1 ≤ 45) |
        | 2 | 32 | ✅ (2 ≤ 32) |
        | 3 | 28 | ✅ (3 ≤ 28) |
        | 4 | 15 | ✅ (4 ≤ 15) |
        | 5 | 10 | ✅ (5 ≤ 10) |
        | 6 | 5 | ❌ (6 > 5) |
        | 7 | 3 | ❌ |
        
        **h-index = 5** (five papers with at least 5 citations each)
        """)
        
        st.graphviz_chart("""
        digraph {
            rankdir=LR; 
            node [fontname="Arial", fontsize=11, shape=box, style="rounded,filled"];
            
            papers [label="Papers\\n(sorted by citations)", fillcolor="#dbeafe"];
            compare [label="Compare:\\nPaper # vs Citations", fillcolor="#fef3c7", shape=diamond];
            hindex [label="h-index =\\nLargest value where\\npaper# ≤ citations", fillcolor="#d1fae5"];
            
            papers -> compare -> hindex;
        }
        """)

    # g-index
    with st.expander("📊 g-index", expanded=True):
        col_def, col_calc = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a;">
                <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>g-index</b> addresses h-index limitations by considering highly-cited papers. g is the largest number such that the top g papers have together at least g² citations.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_calc:
            st.markdown("""
            **Why g-index?**
            - h-index ignores very highly cited papers
            - g-index rewards outstanding papers
            - Always ≥ h-index
            
            **Example:**
            If your top 10 papers have 150 total citations:
            - 10² = 100
            - 150 ≥ 100 ✓
            - Check if top 11 papers have ≥ 121 citations
            """)

    # i10-index
    with st.expander("🔟 i10-index", expanded=True):
        col_def, col_usage = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
                <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>i10-index</b> (introduced by Google Scholar) is simply the number of publications with at least 10 citations.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_usage:
            st.markdown("""
            **Properties:**
            - Simple and intuitive
            - Used only by Google Scholar
            - Good for comparing researchers
            - Threshold of 10 is arbitrary but practical
            
            **Example:**
            If you have 8 papers with ≥10 citations:
            **i10-index = 8**
            """)

    # Altmetrics
    with st.expander("🌐 Altmetrics (Alternative Metrics)", expanded=True):
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b; margin-bottom: 10px;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Altmetrics</b> measure the online attention and engagement with research beyond traditional citations, including social media mentions, news coverage, policy documents, and online saves.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **What Altmetrics Track:**
        
        | Source | Examples |
        |--------|----------|
        | **Social Media** | Twitter/X mentions, Facebook shares |
        | **News** | Mainstream and science news coverage |
        | **Blogs** | Science blogs, commentary |
        | **Policy** | Mentions in policy documents |
        | **Reference Managers** | Mendeley saves, CiteULike |
        | **Wikipedia** | Citations in Wikipedia articles |
        | **Video** | YouTube mentions |
        
        **Advantages:**
        - Measures immediate impact
        - Captures broader societal reach
        - Useful for non-journal outputs
        
        **Limitations:**
        - Can be gamed (buying mentions)
        - Doesn't measure quality
        - Varies by field and audience
        """)

    # Comparison Table
    with st.expander("📋 Comparison of Author Metrics", expanded=False):
        st.markdown("""
        | Metric | Measures | Strengths | Weaknesses |
        |--------|----------|-----------|------------|
        | **h-index** | Productivity + Impact | Simple, widely used | Ignores high-citation papers |
        | **g-index** | Emphasizes top papers | Rewards excellence | Less intuitive |
        | **i10-index** | Papers with ≥10 citations | Very simple | Arbitrary threshold |
        | **Altmetrics** | Online attention | Immediate, broad | Quality not measured |
        | **Citation count** | Total citations | Complete picture | Favors older researchers |
        """)

# =============================================================================
# TAB 4: MAJOR DATABASES
# =============================================================================
with tab4:
    st.markdown("## 🗄️ Chapter 4: Research Databases")
    
    st.markdown("### 4.1 Why Use Research Databases?")
    
    with st.expander("📚 Benefits of Research Databases", expanded=True):
        st.markdown("""
        1. **Quality Assurance**: Curated, peer-reviewed content
        2. **Comprehensive Coverage**: Millions of articles
        3. **Advanced Search**: Boolean operators, filters
        4. **Citation Tracking**: Who cited whom
        5. **Export Tools**: Download references
        6. **Alerts**: Stay updated on new research
        7. **Full-Text Access**: Through institutional subscriptions
        """)

    # Major Subscription Databases
    st.markdown("### 4.2 Major Subscription Databases")

    with st.expander("🔬 Scopus", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Scopus** (Elsevier)
            
            | Feature | Details |
            |---------|---------|
            | **Coverage** | 84M+ records, 27,000+ journals |
            | **Fields** | Science, Social Sciences, Arts, Humanities |
            | **Metrics** | CiteScore, SJR, SNIP, h-index |
            | **Unique** | Author & affiliation disambiguation |
            | **Access** | Subscription required |
            | **URL** | [scopus.com](https://www.scopus.com) |
            
            **Best For:** Comprehensive literature searches, citation analysis, author metrics
            """)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🌟 SciVal</h4>
                <p style="margin: 0 !important; font-size: 12px;">Scopus's analytics platform for institutional research performance evaluation.</p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("🌐 Web of Science", expanded=True):
        st.markdown("""
        **Web of Science** (Clarivate Analytics)
        
        | Feature | Details |
        |---------|---------|
        | **Coverage** | 100M+ records, 21,000+ journals |
        | **Indexes** | SCI, SSCI, A&HCI, ESCI, CPCI |
        | **Metrics** | Impact Factor (via JCR), h-index |
        | **Unique** | Cited reference searching |
        | **Access** | Subscription required |
        | **URL** | [webofscience.com](https://www.webofscience.com) |
        
        **Difference from Scopus:**
        - WoS more selective (fewer journals, higher standards)
        - Scopus has broader coverage
        - WoS is the source of Impact Factor
        """)

    with st.expander("🧬 PubMed", expanded=True):
        st.markdown("""
        **PubMed** (National Library of Medicine, USA)
        
        | Feature | Details |
        |---------|---------|
        | **Coverage** | 36M+ records in biomedical literature |
        | **Focus** | Medicine, Life Sciences, Health |
        | **Unique** | MeSH (Medical Subject Headings) |
        | **Access** | FREE! |
        | **URL** | [pubmed.gov](https://pubmed.gov) |
        
        **Related Resources:**
        - **PubMed Central (PMC)**: Free full-text archive
        - **MEDLINE**: The database that PubMed searches
        """)

    with st.expander("📚 Other Major Databases", expanded=True):
        st.markdown("""
        | Database | Focus | Access | Notable Features |
        |----------|-------|--------|------------------|
        | **JSTOR** | Humanities, Social Sciences | Subscription | Historic archive |
        | **IEEE Xplore** | Engineering, Computer Science | Subscription | Technical standards |
        | **ScienceDirect** | STM (Elsevier journals) | Subscription | Full-text access |
        | **ERIC** | Education | Free | Education research |
        | **PsycINFO** | Psychology | Subscription | APA database |
        | **CINAHL** | Nursing, Allied Health | Subscription | Clinical focus |
        | **Academic Search Complete** | Multidisciplinary | Subscription | EBSCO's flagship |
        | **Business Source Complete** | Business | Subscription | Company data |
        | **ABI/INFORM** | Business | Subscription | ProQuest |
        """)

    # Indexing and Citation Databases
    st.markdown("### 4.3 Indexing vs. Citation Databases")

    with st.expander("📑 Understanding the Difference", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📋 Indexing Databases</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Purpose:</b> Catalog and organize literature<br>
                <b>Features:</b> Subject indexing, abstracts<br>
                <b>Examples:</b> MEDLINE, ERIC, PsycINFO<br>
                <b>Use:</b> Finding relevant literature
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🔗 Citation Databases</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Purpose:</b> Track citations between papers<br>
                <b>Features:</b> Citation counts, metrics<br>
                <b>Examples:</b> Web of Science, Scopus<br>
                <b>Use:</b> Impact analysis, finding related work
                </p>
            </div>
            """, unsafe_allow_html=True)

# =============================================================================
# TAB 5: OPEN ACCESS RESOURCES
# =============================================================================
with tab5:
    st.markdown("## 🔓 Chapter 5: Open Access Resources")
    
    st.markdown("### 5.1 What is Open Access?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Open Access (OA)</b> is the practice of providing unrestricted access to peer-reviewed scholarly research. OA removes price and permission barriers.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Public Library</h4>
            <p style="margin: 0 !important; font-size: 13px;">Open Access is like a <b>public library</b> vs. a private bookstore. The library is free for everyone; the bookstore requires payment.</p>
        </div>
        """, unsafe_allow_html=True)

    # OA Databases
    st.markdown("### 5.2 Free Open Access Databases")

    with st.expander("📖 DOAJ - Directory of Open Access Journals", expanded=True):
        st.markdown("""
        **DOAJ** - An index of high-quality, open access, peer-reviewed journals
        
        | Feature | Details |
        |---------|---------|
        | **Coverage** | 20,000+ journals, 9M+ articles |
        | **Quality** | Strict inclusion criteria |
        | **Use** | Identify legitimate OA journals |
        | **URL** | [doaj.org](https://doaj.org) |
        
        **Why DOAJ Matters:**
        - Helps distinguish legitimate OA from predatory journals
        - DOAJ listing indicates quality
        """)

    with st.expander("🔬 PLOS - Public Library of Science", expanded=True):
        st.markdown("""
        **PLOS** - Pioneer in open access scientific publishing
        
        | Journal | Focus |
        |---------|-------|
        | PLOS ONE | Multidisciplinary |
        | PLOS Medicine | Medical research |
        | PLOS Biology | Life sciences |
        | PLOS Genetics | Genetics |
        | PLOS Computational Biology | Comp bio |
        | PLOS Pathogens | Infectious diseases |
        | PLOS Neglected Tropical Diseases | NTDs |
        
        **URL:** [plos.org](https://plos.org)
        """)

    with st.expander("🔍 BASE - Bielefeld Academic Search Engine", expanded=True):
        st.markdown("""
        **BASE** - One of the world's most voluminous search engines for academic web resources
        
        | Feature | Details |
        |---------|---------|
        | **Coverage** | 380M+ documents from 11,000+ sources |
        | **Content** | 60% full-text OA |
        | **Unique** | Searches institutional repositories |
        | **URL** | [base-search.net](https://www.base-search.net) |
        """)

    with st.expander("📚 Other Open Access Resources", expanded=True):
        st.markdown("""
        | Resource | Description | URL |
        |----------|-------------|-----|
        | **Paperity** | Aggregator of OA papers | paperity.org |
        | **CORE** | Open research papers from repositories | core.ac.uk |
        | **EconBiz** | Economics and business research | econbiz.de |
        | **BioMed Central** | OA publisher in STM | biomedcentral.com |
        | **arXiv** | Preprint server (physics, math, CS) | arxiv.org |
        | **PubMed Central** | Biomedical and life sciences | ncbi.nlm.nih.gov/pmc |
        
        **⚠️ Controversial Resources (Use with Caution):**
        
        | Resource | Note |
        |----------|------|
        | **Sci-Hub** | Provides access to paywalled articles (legally gray) |
        | **Library Genesis (LibGen)** | Book/article repository (copyright issues) |
        
        *Note: Using Sci-Hub or LibGen may violate copyright laws in many jurisdictions.*
        """)

    # Summary Table
    st.markdown("### 5.3 Database Selection Guide")
    
    with st.expander("🗺️ Which Database Should You Use?", expanded=True):
        st.markdown("""
        | If you need... | Use... |
        |----------------|--------|
        | Comprehensive citation data | Scopus or Web of Science |
        | Impact Factor | Web of Science (JCR) |
        | Biomedical research | PubMed |
        | Free full-text | PubMed Central, DOAJ |
        | Engineering/CS | IEEE Xplore |
        | Education research | ERIC |
        | Psychology | PsycINFO |
        | Business | ABI/INFORM, Business Source |
        | Humanities | JSTOR, A&HCI |
        | Find OA version | Unpaywall, BASE, CORE |
        | Author metrics | Google Scholar, Scopus |
        """)


# =============================================================================
# TAB 6: CALCULATORS
# =============================================================================
with tab6:
    st.markdown("## 🧮 Metric Calculators")
    st.markdown("Simulate and calculate common research metrics.")

    c1, c2 = st.tabs(["👤 h-index Calculator", "📰 Impact Factor Simulator"])

    # --- h-index Calculator ---
    with c1:
        st.info("Enter the number of citations for each of your papers (comma separated).")
        
        cit_input = st.text_area("Citations per paper (e.g., 50, 45, 12, 11, 10, 5, 2)", value="10, 8, 5, 4, 3")
        
        if st.button("Calculate h-index"):
            try:
                # Parse input
                citations = [int(x.strip()) for x in cit_input.split(",") if x.strip().isdigit()]
                citations.sort(reverse=True)
                
                h_index = 0
                for i, citations_count in enumerate(citations):
                    if citations_count >= i + 1:
                        h_index = i + 1
                    else:
                        break
                
                # g-index calculation
                g_index = 0
                citations_sum = 0
                for i, c in enumerate(citations):
                    citations_sum += c
                    if citations_sum >= (i + 1)**2:
                        g_index = i + 1

                st.success(f"### Your h-index is: {h_index}")
                st.info(f"Your g-index is: {g_index}")
                
                # Visualization
                st.write("**Visual Representation:**")
                chart_data = {"Paper Rank": list(range(1, len(citations)+1)), 
                              "Citations": citations,
                              "h-line": [h_index] * len(citations)}
                st.line_chart(chart_data, x="Paper Rank", y=["Citations", "h-line"])
                
            except Exception as e:
                st.error("Invalid input. Please enter numbers separated by commas.")

    # --- Impact Factor Simulator ---
    with c2:
        st.info("Simulate how Journal Impact Factor is calculated.")
        
        col1, col2 = st.columns(2)
        with col1:
            y1_cites = st.number_input("Citations in 2024 to items published in 2023", value=150)
            y2_cites = st.number_input("Citations in 2024 to items published in 2022", value=200)
        with col2:
            y1_pubs = st.number_input("Citable items published in 2023", value=50)
            y2_pubs = st.number_input("Citable items published in 2022", value=45)
            
        if st.button("Calculate Impact Factor"):
            numerator = y1_cites + y2_cites
            denominator = y1_pubs + y2_pubs
            
            if denominator > 0:
                if_score = numerator / denominator
                st.metric("2024 Impact Factor", f"{if_score:.3f}")
                st.latex(f"IF = \\frac{{{numerator}}}{{{denominator}}} = {if_score:.3f}")
            else:
                st.error("Denominator cannot be zero (must have published items).")

# Footer
show_footer()
