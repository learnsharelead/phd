import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Online Tools & Publication Policy | SHERPA/RoMEO, Turnitin, Predatory Journals [2024]",
    description="Master online research tools: SHERPA/RoMEO for self-archiving, Turnitin/Urkund for plagiarism detection, identifying predatory journals, and understanding Open Access publishing policies.",
    keywords=[
        "SHERPA RoMEO",
        "Turnitin",
        "Urkund",
        "plagiarism detection",
        "predatory journals",
        "open access publishing",
        "self-archiving",
        "copyright policy",
        "author rights",
        "publication ethics",
        "conflict of interest",
        "iThenticate",
        "predatory publishers",
        "beall's list"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/online-tools",
    reading_time=75,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Online Tools", "url": "https://researchethics.dev/online-tools"}
    ],
    course_info={
        "name": "Online Tools and Publication Policy Module",
        "description": "Comprehensive guide to Open Access, SHERPA/RoMEO, predatory journal detection, plagiarism software, and publication policy compliance.",
        "level": "Doctoral",
        "prerequisites": "Basic research experience",
        "teaches": ["Open Access Publishing", "SHERPA/RoMEO", "Plagiarism Detection", "Predatory Journal Identification", "Conflict of Interest"],
        "workload": "PT12H",
        "rating": "4.8",
        "rating_count": 634
    },
    faq_items=[
        {
            "question": "What is SHERPA/RoMEO?",
            "answer": "SHERPA/RoMEO is an online service that aggregates publisher copyright and self-archiving policies. It helps authors understand what version of their paper they can archive and where."
        },
        {
            "question": "How do I identify a predatory journal?",
            "answer": "Look for warning signs: aggressive solicitation emails, no rigorous peer review, lack of transparency, no indexed in major databases, missing ISSN, fake impact factors, and unrealistically fast publication times."
        },
        {
            "question": "What is Turnitin?",
            "answer": "Turnitin is a plagiarism detection service that compares submitted work against a database of academic papers, websites, and student submissions to identify text similarity."
        }
    ]
)
apply_custom_css()
show_top_nav(current_page="Online Tools")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">🔧 Module 3: Online Tools, Ethics & Publication Policy</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #7c3aed;">From Open Access to plagiarism detection — mastering the tools of ethical publishing.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔓 Open Access",
    "📜 SHERPA/RoMEO",
    "🔍 Plagiarism Tools",
    "⚠️ Predatory Journals",
    "⚖️ Ethics Issues"
])

# =============================================================================
# TAB 1: OPEN ACCESS PUBLISHING
# =============================================================================
with tab1:
    st.markdown("## 🔓 Chapter 1: Open Access Publishing")
    
    st.markdown("### 1.1 What is Open Access?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Open Access (OA)</b> is the practice of making research publications freely available online so that anyone can read, download, copy, and distribute them without financial, legal, or technical barriers.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Free Highway vs. Toll Road</h4>
            <p style="margin: 0 !important; font-size: 13px;">Open Access is like a <b>free public highway</b> compared to a toll road. Everyone can travel on it without paying each time they want access.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🗓️ Open Access Initiatives & History", expanded=True):
        st.markdown("""
        **Key Milestones:**
        
        | Year | Initiative | Significance |
        |------|------------|--------------|
        | 2001 | Budapest Open Access Initiative | Defined OA, coined the term |
        | 2003 | Bethesda Statement | Extended definition, emphasized reuse |
        | 2003 | Berlin Declaration | Institutional commitments to OA |
        | 2012 | RCUK OA Policy | UK funders mandate OA |
        | 2013 | US OSTP Memo | US government mandates for federally funded research |
        | 2018 | Plan S | European funder coalition mandating OA |
        | 2022 | US Nelson Memo | All US federally funded research must be OA by 2026 |
        
        **The BBB Definition** (Budapest-Bethesda-Berlin):
        Open Access means free online access with the right to read, download, copy, distribute, print, search, and link.
        """)

    # Types of OA
    with st.expander("🎨 Types of Open Access (Color Coding)", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fef9c3 0%, #fef08a 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 2px solid #eab308;">
                <h4 style="margin: 0 0 5px 0 !important;">🟡 Gold OA</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Published in OA journal<br>
                <b>Cost:</b> Author pays APC (Article Processing Charge)<br>
                <b>Example:</b> PLOS ONE, BMC journals<br>
                <b>Rights:</b> Usually CC-BY license
                </p>
            </div>
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #86efac 100%); padding: 12px; border-radius: 8px; border: 2px solid #22c55e;">
                <h4 style="margin: 0 0 5px 0 !important;">🟢 Green OA</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Self-archiving in repository<br>
                <b>Cost:</b> Free<br>
                <b>Where:</b> Institutional repository, PubMed Central<br>
                <b>Version:</b> Usually preprint or accepted manuscript
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fdf4ff 0%, #f5d0fe 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px; border: 2px solid #d946ef;">
                <h4 style="margin: 0 0 5px 0 !important;">💜 Hybrid OA</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> OA article in subscription journal<br>
                <b>Cost:</b> Author pays APC for individual article<br>
                <b>Issue:</b> "Double dipping" controversy<br>
                <b>Example:</b> Nature, Cell
                </p>
            </div>
            <div style="background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%); padding: 12px; border-radius: 8px; border: 2px solid #ef4444;">
                <h4 style="margin: 0 0 5px 0 !important;">🔴 Bronze OA</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Free to read but no license<br>
                <b>Issue:</b> Publisher may remove access<br>
                <b>Rights:</b> May not allow reuse<br>
                <b>Stability:</b> Uncertain
                </p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("⚖️ Creative Commons Licenses", expanded=False):
        st.markdown("""
        **CC Licenses for Open Access:**
        
        | License | Abbreviation | Permissions |
        |---------|--------------|-------------|
        | Attribution | CC BY | Most open: use, share, adapt with credit |
        | Attribution-ShareAlike | CC BY-SA | Derivatives must use same license |
        | Attribution-NonCommercial | CC BY-NC | No commercial use |
        | Attribution-NoDerivatives | CC BY-ND | No adaptations |
        | Attribution-NC-SA | CC BY-NC-SA | Non-commercial + same license |
        | Attribution-NC-ND | CC BY-NC-ND | Most restrictive |
        
        **Plan S Requirement:** CC BY preferred for funded research
        """)

# =============================================================================
# TAB 2: SHERPA/RoMEO
# =============================================================================
with tab2:
    st.markdown("## 📜 Chapter 2: SHERPA/RoMEO")
    
    st.markdown("### 2.1 What is SHERPA/RoMEO?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>SHERPA/RoMEO</b> is an online resource that aggregates and analyzes publisher open access policies from around the world. It helps researchers understand their self-archiving rights.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: The Copyright GPS</h4>
            <p style="margin: 0 !important; font-size: 13px;">SHERPA/RoMEO is like a <b>GPS for copyright navigation</b>. It tells you where you can go (archive) and which routes (versions) are permitted.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🔍 How to Use SHERPA/RoMEO", expanded=True):
        st.markdown("""
        **Access:** [v2.sherpa.ac.uk/romeo](https://v2.sherpa.ac.uk/romeo/)
        
        **Step-by-Step:**
        1. Go to SHERPA/RoMEO website
        2. Search by journal name, ISSN, or publisher
        3. Review the policy summary
        4. Check which version you can archive
        5. Note any embargo periods
        6. Identify allowed repositories
        
        **Key Information Provided:**
        - Journal open access policies
        - Self-archiving permissions
        - Embargo periods
        - License requirements
        - Repository restrictions
        """)

    with st.expander("📄 Understanding Article Versions", expanded=True):
        st.markdown("""
        **Three Key Versions:**
        
        | Version | Also Called | Description |
        |---------|-------------|-------------|
        | **Submitted** | Preprint, Author's Original | Version before peer review |
        | **Accepted** | Postprint, Author's Manuscript | After peer review, before publisher formatting |
        | **Published** | Version of Record (VoR) | Final published version with publisher formatting |
        """)
        
        st.graphviz_chart("""
        digraph {
            rankdir=LR; 
            node [fontname="Arial", fontsize=11, shape=box, style="rounded,filled"];
            
            sub [label="Submitted\\n(Preprint)", fillcolor="#fef3c7"];
            review [label="Peer Review", fillcolor="#f0fdf4", shape=ellipse];
            acc [label="Accepted\\n(Postprint)", fillcolor="#dbeafe"];
            pub [label="Published\\n(VoR)", fillcolor="#d1fae5"];
            
            sub -> review -> acc -> pub;
        }
        """)
        
        st.markdown("""
        **Typical Permissions (varies by publisher):**
        - ✅ Preprint: Usually can be archived anywhere
        - ⚠️ Accepted: Often allowed with embargo (6-12 months)
        - ❌ Published: Usually cannot be self-archived without permission
        """)

    with st.expander("🔒 Understanding Embargo Periods", expanded=False):
        st.markdown("""
        **What is an Embargo?**
        
        An embargo is a period during which you cannot publicly share your accepted manuscript. Publishers use embargoes to protect subscription revenue.
        
        **Common Embargo Periods:**
        | Field | Typical Embargo |
        |-------|-----------------|
        | STM (Science/Tech/Medicine) | 6-12 months |
        | Social Sciences | 12-24 months |
        | Humanities | 12-24 months |
        
        **Note:** Many funders (NIH, Wellcome, Plan S) now require zero or short embargoes.
        """)

# =============================================================================
# TAB 3: PLAGIARISM DETECTION TOOLS
# =============================================================================
with tab3:
    st.markdown("## 🔍 Chapter 3: Plagiarism Detection Software")
    
    st.markdown("### 3.1 Why Use Plagiarism Detection?")
    
    with st.expander("🎯 Purpose of Plagiarism Software", expanded=True):
        st.markdown("""
        **Detection software helps to:**
        - Identify unintentional plagiarism
        - Verify proper citation
        - Maintain academic integrity
        - Meet journal requirements
        - Train researchers on proper attribution
        
        **⚠️ Important Note:**
        - These tools detect **text similarity**, not plagiarism itself
        - Human judgment is required to interpret results
        - High similarity ≠ Plagiarism (e.g., quoted text, methodology)
        - Low similarity ≠ No plagiarism (e.g., paraphrased ideas without citation)
        """)

    # Turnitin
    st.markdown("### 3.2 Turnitin")
    
    with st.expander("📋 Turnitin Overview", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb; margin-bottom: 10px;">
                <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Turnitin</b> is a commercial plagiarism detection service that compares submitted work against its database of academic papers, websites, and student submissions.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **Key Features:**
            - Massive database (70B+ web pages, 1B+ student papers)
            - Originality reports with similarity scores
            - Highlights matching text
            - Links to sources
            - AI writing detection (new)
            
            **Who Uses It:**
            - Universities for student submissions
            - Publishers for manuscript screening
            - Researchers for self-checking
            """)
        with col2:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">💰 Access</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Type:</b> Subscription<br>
                <b>Cost:</b> Institution pays<br>
                <b>iThenticate:</b> For publishers<br>
                <b>URL:</b> turnitin.com
                </p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("📊 Understanding Similarity Reports", expanded=True):
        st.markdown("""
        **Similarity Score Colors (Turnitin):**
        
        | Color | Percentage | Interpretation |
        |-------|------------|----------------|
        | 🔵 Blue | 0% | No matching text |
        | 🟢 Green | 1-24% | Low similarity |
        | 🟡 Yellow | 25-49% | Moderate similarity |
        | 🟠 Orange | 50-74% | High similarity |
        | 🔴 Red | 75-100% | Very high similarity |
        
        **What Counts as Matching Text:**
        - Direct quotes (should be in quotation marks)
        - Common phrases
        - Bibliography entries
        - Standard methodology descriptions
        - Your own previously submitted work
        
        **⚠️ Critical Point:**
        - A 20% similarity score isn't automatically "acceptable"
        - A 5% match might be problematic if it's a key idea
        - Context matters more than percentage
        """)

    # Urkund (Ouriginal)
    st.markdown("### 3.3 Urkund (now Ouriginal)")
    
    with st.expander("📋 Urkund Overview", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Urkund</b> (rebranded as Ouriginal, now part of Turnitin) is a plagiarism detection service popular in Europe and India.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Key Features:**
        - Searches web, published documents, student papers
        - Used by UGC/universities in India
        - Real-time checking during drafting
        - Supports multiple file formats
        - Provides detailed match reports
        
        **How It Differs from Turnitin:**
        - Different database focus
        - Widely used in Nordic countries, India
        - Integration with various LMS platforms
        """)

    # Open Source Tools
    with st.expander("🆓 Open Source Plagiarism Tools", expanded=True):
        st.markdown("""
        **Free/Open Source Options:**
        
        | Tool | Features | Access |
        |------|----------|--------|
        | **Copyscape** | Web-based, limited free checks | copyscape.com |
        | **PlagScan** | Academic focus | plagscan.com |
        | **Duplichecker** | Free, limited | duplichecker.com |
        | **Quetext** | DeepSearch technology | quetext.com |
        | **SmallSEOTools** | Multiple tools | smallseotools.com |
        | **Grammarly** | Basic plagiarism check | grammarly.com |
        
        **Limitations of Free Tools:**
        - Smaller databases
        - May miss academic sources
        - Less detailed reports
        - Word/check limits
        
        **Best Practice:**
        Use institutional tools (Turnitin/Urkund) for final checks; use free tools for initial drafts.
        """)

# =============================================================================
# TAB 4: PREDATORY JOURNALS
# =============================================================================
with tab4:
    st.markdown("## ⚠️ Chapter 4: Identifying Predatory Publications")
    
    st.markdown("### 4.1 What are Predatory Journals?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #fef2f2; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444;">
            <h4 style="color: #dc2626; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Predatory Journals</b> are publications that exploit the open-access model by charging authors fees while providing little or no legitimate peer review, editing, or indexing services.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Diploma Mill</h4>
            <p style="margin: 0 !important; font-size: 13px;">Predatory journals are like <b>diploma mills</b> in education. They take your money and give you something that looks legitimate but has no real value.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🚩 Red Flags: How to Identify Predatory Journals", expanded=True):
        st.markdown("""
        **Warning Signs:**
        
        | Category | Red Flags |
        |----------|-----------|
        | **Solicitation** | Aggressive email invitations, flattery |
        | **Website** | Poor design, spelling errors, copied content |
        | **Peer Review** | Promises very fast review (days), no revision rounds |
        | **Fees** | Hidden or unclear APCs, demanded after acceptance |
        | **Indexing** | Claims to be in Scopus/WoS but isn't, fake metrics |
        | **Editorial Board** | Fake names, unverifiable affiliations, no experts |
        | **Contact** | Generic email (Gmail, Yahoo), no physical address |
        | **ISSN** | Missing, invalid, or multiple ISSNs |
        | **Scope** | Extremely broad ("accepts all sciences") |
        | **Archives** | No or very limited back issues |
        
        **🔴 Major Red Flags:**
        - "Guaranteed acceptance"
        - No retraction policy
        - Can't find archived articles in databases
        - Payment required before peer review complete
        """)

    with st.expander("🔍 SPPU Tool for Predatory Journal Detection", expanded=True):
        st.markdown("""
        **UGC-CARE List (India):**
        
        The University Grants Commission maintains a "**Consortium for Academic and Research Ethics (CARE)**" list of approved journals.
        
        **How to Check:**
        1. Visit [UGC-CARE Portal](https://ugccare.unipune.ac.in/)
        2. Search for journal by title or ISSN
        3. If listed → Legitimate (for Indian academic purposes)
        4. If not listed → Requires further investigation
        
        **SPPU (Savitribai Phule Pune University) Contributions:**
        - Developed tools for predatory journal detection
        - Maintains database of suspicious journals
        - Provides guidelines for researchers
        
        **Other Verification Tools:**
        | Resource | Purpose |
        |----------|---------|
        | DOAJ | Legitimate OA journals |
        | Scopus Source List | Scopus-indexed journals |
        | Master Journal List (WoS) | WoS-indexed journals |
        | Think.Check.Submit | Verification checklist |
        """)

    with st.expander("✅ Think. Check. Submit.", expanded=True):
        st.markdown("""
        **Think. Check. Submit.** is an international initiative helping researchers identify trusted journals.
        
        **The Checklist:**
        
        **THINK:**
        - Do you or colleagues know the journal?
        - Can you easily discover the latest papers?
        
        **CHECK:**
        - ✅ Can you identify and contact the publisher?
        - ✅ Is the journal clear about peer review?
        - ✅ Are articles indexed in databases you use?
        - ✅ Is it clear what fees you'll pay?
        - ✅ Do you recognize the editorial board?
        - ✅ Is the publisher a member of COPE, DOAJ, OASPA?
        
        **SUBMIT:**
        - Only if all checks pass!
        
        **Website:** [thinkchecksubmit.org](https://thinkchecksubmit.org)
        """)

    with st.expander("⚖️ Consequences of Publishing in Predatory Journals", expanded=False):
        st.markdown("""
        **For Researchers:**
        - Paper may not count for promotion/tenure
        - Damage to reputation
        - Work may never be indexed/discoverable
        - Wasted research funds
        - Potential for paper to be ignored by community
        
        **For Science:**
        - Pollutes literature with unreviewed work
        - Undermines trust in research
        - May include fraudulent or poor-quality studies
        
        **Institutional Responses:**
        - Many institutions now check against predatory lists
        - Papers in predatory journals may be excluded from evaluation
        - Some require declaration of journal verification
        """)

# =============================================================================
# TAB 5: ETHICAL ISSUES
# =============================================================================
with tab5:
    st.markdown("## ⚖️ Chapter 5: Subject-Specific Ethical Issues")
    
    # FFP Revisited
    st.markdown("### 5.1 FFP Across Disciplines")
    
    with st.expander("🔬 Discipline-Specific FFP Issues", expanded=True):
        st.markdown("""
        | Discipline | Common FFP Issues |
        |------------|-------------------|
        | **Biomedical** | Image manipulation, data fabrication, animal ethics |
        | **Clinical** | Informed consent, patient confidentiality, trial registration |
        | **Social Sciences** | Interview fabrication, survey data manipulation |
        | **Engineering** | Safety data falsification, performance fabrication |
        | **Humanities** | Text plagiarism, idea appropriation |
        | **Computer Science** | Code plagiarism, benchmark manipulation |
        
        **Image Manipulation (Biomedical):**
        - Adjusting brightness/contrast (acceptable with disclosure)
        - Splicing parts of different images (unacceptable)
        - Removing or adding features (unacceptable)
        - Journals now use forensic image analysis software
        """)

    # Conflicts of Interest
    st.markdown("### 5.2 Conflicts of Interest")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Conflict of Interest (COI)</b> occurs when personal, financial, or professional interests could compromise (or appear to compromise) judgment, objectivity, or integrity in research or publication.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Referee's Conflict</h4>
            <p style="margin: 0 !important; font-size: 13px;">A referee whose child plays on one team has a <b>conflict of interest</b>. Even if impartial, the appearance of bias undermines trust.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("💰 Types of Conflicts of Interest", expanded=True):
        st.markdown("""
        | Type | Examples |
        |------|----------|
        | **Financial** | Stock ownership, consulting fees, honoraria, research funding |
        | **Personal** | Family relationships, personal rivalries, romantic relationships |
        | **Academic** | Competition for grants/positions, collaboration history |
        | **Institutional** | Employer interests, patent interests |
        | **Ideological** | Strong beliefs that may bias interpretation |
        
        **Disclosure Requirements:**
        - Authors must declare all potential COIs to journals
        - Reviewers must disclose COIs to editors
        - Editors recuse from decisions involving COIs
        - Funding sources must be acknowledged
        
        **Sample Disclosure Statement:**
        > "Author X has received consulting fees from Company Y. Author Z declares no conflicts of interest. This research was funded by Grant ABC."
        """)

    with st.expander("📋 Managing Conflicts of Interest", expanded=False):
        st.markdown("""
        **COI Management Strategies:**
        
        1. **Disclosure** – Transparency about potential conflicts
        2. **Recusal** – Stepping back from decisions
        3. **Oversight** – Independent monitoring
        4. **Divestiture** – Giving up conflicting interests
        
        **Who Should Declare?**
        - All authors (typically at submission)
        - Reviewers (to editors)
        - Editors (to journal)
        - Grant applicants (to funders)
        
        **Time Period:**
        - Usually 36 months (3 years) of potential conflicts
        - Some journals require lifetime disclosure for certain interests
        """)

    # Complaints and Appeals
    st.markdown("### 5.3 Complaints and Appeals")
    
    with st.expander("📞 How to Report Misconduct", expanded=True):
        st.markdown("""
        **Reporting Channels:**
        
        | Level | Report To |
        |-------|-----------|
        | **Institutional** | Research Integrity Officer, Ethics Committee |
        | **Journal** | Editor-in-Chief |
        | **Publisher** | Publisher ethics team |
        | **External** | ORI (US), UKRIO (UK), relevant bodies |
        
        **What to Include:**
        - Specific allegation with evidence
        - Publication details
        - Your relationship to the work
        - Any prior communications
        
        **COPE (Committee on Publication Ethics) Process:**
        1. Receive allegation
        2. Preliminary assessment
        3. Contact accused (confidentially)
        4. Investigation if warranted
        5. Decision on action
        6. Right to appeal
        """)

    with st.expander("⚖️ Appeals Process", expanded=False):
        st.markdown("""
        **If You Disagree with a Decision:**
        
        1. **Request Clarification** – Ask for detailed reasoning
        2. **Provide New Evidence** – If available
        3. **Formal Appeal** – Written response to decision
        4. **Escalation** – To publisher, COPE, or ombudsman
        
        **Grounds for Appeal:**
        - Procedural irregularities
        - New evidence
        - Misinterpretation of evidence
        - Disproportionate sanction
        
        **Whistleblower Protections:**
        - Reports should be confidential
        - Retaliation prohibited
        - Good-faith allegations protected
        - Many institutions have formal policies
        """)

    # Summary Card
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 15px; border-radius: 10px; margin-top: 15px; border: 1px solid #86efac;">
        <h4 style="color: #166534; margin: 0 0 10px 0 !important;">🎯 Key Takeaways</h4>
        <ul style="margin: 0; padding-left: 20px;">
            <li>Always use SHERPA/RoMEO to check self-archiving policies</li>
            <li>Use plagiarism tools to catch unintentional similarity</li>
            <li>Verify journals through DOAJ, Scopus, WoS before submitting</li>
            <li>Disclose ALL conflicts of interest</li>
            <li>Know your institution's misconduct reporting procedures</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
show_footer()
