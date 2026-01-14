import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Research Ethics Case Studies | Fraud Cases from India & Worldwide [2024]",
    description="Learn from real-world research misconduct cases: famous fraud scandals from India and abroad, ethical dilemmas, retractions, and lessons learned. Essential for Ph.D. researchers.",
    keywords=[
        "research fraud cases",
        "scientific misconduct examples",
        "plagiarism cases India",
        "retracted papers",
        "Hwang Woo-suk",
        "Piero Anversa",
        "Jan Hendrik Schön",
        "research ethics violations",
        "fabrication cases",
        "ethical dilemmas research",
        "scientific scandal",
        "retraction watch",
        "academic fraud India"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/case-studies",
    reading_time=90,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Case Studies", "url": "https://researchethics.dev/case-studies"}
    ],
    course_info={
        "name": "Research Ethics Case Studies Module",
        "description": "In-depth analysis of research misconduct cases from India and worldwide, ethical dilemmas, and lessons for researchers.",
        "level": "Doctoral",
        "prerequisites": "Understanding of research integrity concepts",
        "teaches": ["Case Analysis", "Ethical Decision Making", "Misconduct Recognition", "Lessons from Fraud"],
        "workload": "PT10H",
        "rating": "4.9",
        "rating_count": 521
    },
    faq_items=[
        {
            "question": "What is the biggest research fraud case ever?",
            "answer": "One of the largest is the Piero Anversa cardiac stem cell case, resulting in 31+ retractions and $10+ million repaid to NIH. The Hwang Woo-suk stem cell fraud in South Korea is another landmark case."
        },
        {
            "question": "What happens when a paper is retracted?",
            "answer": "The paper is marked with a retraction notice explaining why. It remains in databases but with 'RETRACTED' labels. Citations should stop, though the paper may still be cited erroneously."
        }
    ]
)
apply_custom_css()
show_top_nav(current_page="Case Studies")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📋 Module 4: Real-World Case Studies</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #c2410c;">Learning from mistakes — fraud cases, ethical dilemmas, and lessons for researchers.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🌍 International Cases",
    "🇮🇳 Cases from India",
    "🤔 Ethical Dilemmas",
    "📚 Lessons Learned"
])

# =============================================================================
# TAB 1: INTERNATIONAL CASES
# =============================================================================
with tab1:
    st.markdown("## 🌍 Chapter 1: Notable International Misconduct Cases")
    
    st.markdown("""
    <div style="background: #fef2f2; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444; margin-bottom: 15px;">
        <h4 style="color: #dc2626; margin: 0 0 8px 0 !important;">⚠️ Why Study These Cases?</h4>
        <p style="margin: 0 !important; font-size: 13px;">These cases represent spectacular failures of research integrity. By understanding what went wrong and why, we can build better safeguards and recognize warning signs.</p>
    </div>
    """, unsafe_allow_html=True)

    # Case 1: Hwang Woo-suk
    with st.expander("🧬 Case 1: Hwang Woo-suk (South Korea) — Stem Cell Fraud", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **The Rise:**
            - 2004-2005: Claimed to create human embryonic stem cells through cloning
            - Celebrated as a national hero in South Korea
            - Published in *Science* (prestigious journal)
            - Funded with millions in government grants
            
            **The Fall:**
            - 2005: Whistleblowers and journalists questioned data
            - Investigation revealed: **Data fabricated, photos doctored**
            - None of the claimed stem cell lines were actually cloned
            - Eggs were obtained unethically from lab members
            
            **The Misconduct:**
            - **Fabrication**: No successful cloning occurred
            - **Falsification**: Images manipulated
            - **Ethical Violations**: Coerced egg donations
            """)
        with col2:
            st.markdown("""
            <div style="background: #fef2f2; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📊 Impact</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Papers Retracted:</b> 2 in Science<br>
                <b>Conviction:</b> Embezzlement, bioethics violations<br>
                <b>Sentence:</b> 2 years suspended<br>
                <b>Career:</b> Barred, then controversial return
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **🎯 Key Lessons:**
        1. Even prestigious journals can publish fraudulent work
        2. National pride can blind oversight
        3. Whistleblowers are essential
        4. Independent replication is crucial
        """)

    # Case 2: Jan Hendrik Schön
    with st.expander("⚡ Case 2: Jan Hendrik Schön (Germany/Bell Labs) — Physics Fabrication", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **The Rise:**
            - Early 2000s: Prolific physicist at Bell Labs
            - Claimed breakthroughs in superconductivity, transistors
            - Published ~average of 1 paper every 8 days
            - Published in Nature, Science, Physical Review Letters
            
            **The Fall:**
            - 2002: Other scientists noticed identical graphs in unrelated papers
            - Investigation found: **Same data reused across studies**
            - Experiments could not be replicated
            - Data was "too perfect" — statistically impossible
            
            **The Misconduct:**
            - **Fabrication**: Made up experimental results
            - **Falsification**: Reused graphs, manipulated data
            - Possibly 16 papers affected
            """)
        with col2:
            st.markdown("""
            <div style="background: #fff7ed; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📊 Impact</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Papers Retracted:</b> 28+<br>
                <b>PhD Revoked:</b> 2004 (University of Konstanz)<br>
                <b>Career:</b> Ended in academia<br>
                <b>Nobel Speculation:</b> Was considered a candidate
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **🎯 Key Lessons:**
        1. Prolific output can be a red flag
        2. Data should never be "too perfect"
        3. Co-authors share responsibility
        4. Replication is essential for major claims
        """)

    # Case 3: Piero Anversa
    with st.expander("❤️ Case 3: Piero Anversa (USA) — Cardiac Stem Cell Fraud", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **The Rise:**
            - 2001-2015: Claimed heart could regenerate via c-kit+ stem cells
            - Harvard Medical School professor
            - Hugely influential: changed cardiac research direction
            - Over $50 million in NIH funding
            
            **The Fall:**
            - 2014: First retraction (Circulation)
            - Other labs couldn't replicate findings
            - 2018: Brigham and Women's Hospital investigation
            - Found: **Data fabrication and falsification**
            
            **The Misconduct:**
            - **Fabrication**: Created false data
            - **Falsification**: Manipulated experiments
            - Caused research community to pursue dead ends
            """)
        with col2:
            st.markdown("""
            <div style="background: #fef2f2; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📊 Impact</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Papers Retracted:</b> 31+<br>
                <b>Repayment:</b> $10 million+ to NIH<br>
                <b>Settlement:</b> Hospital paid $10M<br>
                <b>Damage:</b> Entire field misled for years
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **🎯 Key Lessons:**
        1. Even senior, respected scientists can fabricate
        2. Replication failures should prompt investigation
        3. Financial impacts can be enormous
        4. Entire research directions can be corrupted
        """)

    # Case 4: Diederik Stapel
    with st.expander("🧠 Case 4: Diederik Stapel (Netherlands) — Psychology Fraud", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **The Rise:**
            - Social psychology professor at Tilburg University
            - Dean of the social science faculty
            - Published attention-grabbing studies
            - Famous study: Messy environments cause discrimination
            
            **The Fall:**
            - 2011: Junior researchers reported suspicions
            - Investigation found: **Fabricated data in 55+ papers**
            - Made up entire experiments
            - Never collected data for many studies
            
            **The Misconduct:**
            - **Complete Fabrication**: Entire datasets invented
            - Affected 10+ PhD students' dissertations
            - Some PhDs were revoked
            """)
        with col2:
            st.markdown("""
            <div style="background: #fff7ed; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📊 Impact</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Papers Retracted:</b> 58<br>
                <b>PhD Theses Affected:</b> 10+<br>
                <b>Career:</b> Terminated, banned<br>
                <b>Book:</b> Wrote memoir "Derailment"
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **🎯 Key Lessons:**
        1. Junior researchers can be whistleblowers
        2. Fabrication affects student careers
        3. Psychology's "replication crisis" exposed weaknesses
        4. Solo data collection is a risk factor
        """)

    # Case 5: Andrew Wakefield
    with st.expander("💉 Case 5: Andrew Wakefield (UK) — Vaccine-Autism Fraud", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **The Claim:**
            - 1998 *Lancet* paper suggested MMR vaccine linked to autism
            - Based on 12 children (tiny sample)
            - Triggered global anti-vaccine movement
            
            **The Fall:**
            - 2004: Investigative journalism (Brian Deer) uncovered issues
            - 2010: Paper fully retracted by *Lancet*
            - Found: **Data manipulated, ethical violations, undisclosed conflicts**
            
            **The Misconduct:**
            - **Falsification**: Medical records didn't match paper claims
            - **Conflict of Interest**: Paid by lawyers suing vaccine makers
            - **Ethical Violations**: Unethical procedures on children
            """)
        with col2:
            st.markdown("""
            <div style="background: #fef2f2; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📊 Impact</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>Paper Retracted:</b> 2010<br>
                <b>Medical License:</b> Revoked<br>
                <b>Public Health:</b> Vaccine hesitancy, disease outbreaks<br>
                <b>Status:</b> Still promotes anti-vaccine views
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **🎯 Key Lessons:**
        1. Fraudulent research can have massive public health consequences
        2. Conflicts of interest must be disclosed
        3. Small studies with big claims need scrutiny
        4. Retraction doesn't undo public damage
        """)

# =============================================================================
# TAB 2: CASES FROM INDIA
# =============================================================================
with tab2:
    st.markdown("## 🇮🇳 Chapter 2: Cases from India")
    
    st.markdown("""
    <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb; margin-bottom: 15px;">
        <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📊 India's Research Integrity Landscape</h4>
        <p style="margin: 0 !important; font-size: 13px;">India has seen growing awareness of research integrity issues. The UGC-CARE list, mandatory plagiarism checking, and institutional ethics committees are positive developments.</p>
    </div>
    """, unsafe_allow_html=True)

    # Case 1: Patent Fraud
    with st.expander("🧬 Case 1: High-Profile Plagiarism Cases in Academia", expanded=True):
        st.markdown("""
        **Context:**
        - Multiple cases of PhD thesis plagiarism discovered
        - Vice-Chancellors and senior academics implicated
        - Many cases involve copying large sections from published work
        
        **Notable Patterns:**
        - Theses copied from books or other theses
        - Lack of proper supervision
        - Inadequate plagiarism checking systems (now improving)
        
        **Consequences:**
        - PhD degrees revoked in several cases
        - Faculty positions terminated
        - Legal battles over degrees
        
        **Response:**
        - UGC mandated plagiarism checking for all theses
        - Maximum 10% similarity threshold for PhD
        - Institutional subscription to Turnitin/Urkund
        """)
        
        st.warning("**Note:** Specific names are withheld to focus on systemic lessons rather than individual blame.")

    # Case 2: Predatory Publishing
    with st.expander("📰 Case 2: Mass Publication in Predatory Journals", expanded=True):
        st.markdown("""
        **The Problem:**
        - Thousands of Indian academics published in predatory journals
        - "Publish or perish" pressure without guidance
        - Lack of awareness about legitimate vs. predatory venues
        - API (Academic Performance Indicator) requirements exploited
        
        **Scale:**
        - India was identified as the top source country for predatory journal submissions
        - Some researchers published 10+ papers/year in questionable venues
        - Financial loss to researchers paying APCs to fake journals
        
        **Response:**
        - UGC-CARE list established (2019)
        - Only CARE-listed journals count for API
        - White list approach vs. black list
        - Institutions now verify journal legitimacy
        
        **🎯 Lessons:**
        - Quantity metrics create perverse incentives
        - Researchers need training on journal selection
        - Institutional verification systems are essential
        """)

    # Case 3: Data Fabrication
    with st.expander("🔬 Case 3: Data Fabrication in Clinical Trials", expanded=True):
        st.markdown("""
        **Context:**
        - Several cases of clinical trial data fabrication discovered
        - Issues with informed consent documentation
        - Post-marketing surveillance data problems
        
        **Categories of Issues:**
        | Issue | Description |
        |-------|-------------|
        | Fabricated patient data | Inventing trial participants |
        | Informed consent violations | Forged signatures, inadequate disclosure |
        | Selective reporting | Publishing only positive results |
        | GCP violations | Not following Good Clinical Practice |
        
        **Regulatory Response:**
        - CDSCO (Central Drugs Standard Control Organisation) strengthened oversight
        - Clinical trial registry made mandatory
        - Ethics committee requirements enhanced
        - Compensation requirements for trial participants
        
        **🎯 Lessons:**
        - Clinical research needs robust oversight
        - Patient safety must be paramount
        - Registration and transparency are essential
        """)

    # Case 4: Image Manipulation
    with st.expander("🖼️ Case 4: Image Manipulation Cases", expanded=True):
        st.markdown("""
        **The Issue:**
        - Western blots, gels, and microscopy images manipulated
        - Same images appearing in multiple papers
        - Splicing, duplication, and contrast manipulation
        
        **Detection:**
        - Detected by watchdog sites like PubPeer
        - Forensic image analysis tools
        - Reader reports to journals
        
        **Institutional Responses:**
        - IITs and NITs have faced retractions
        - Some institutions now require raw data submission
        - Image integrity checks during review
        
        **Scale:**
        - India ranks among countries with higher retraction rates
        - Most retractions are for plagiarism and data issues
        
        **🎯 Lessons:**
        - Keep raw data and lab notebooks
        - Document all image processing
        - Understand what manipulation is acceptable vs. not
        """)

    # Case 5: Self-Citation and Citation Manipulation
    with st.expander("🔗 Case 5: Citation Manipulation Networks", expanded=True):
        st.markdown("""
        **The Problem:**
        - Citation cartels: Groups agreeing to cite each other
        - Excessive self-citation to inflate h-index
        - Coercive citation (reviewers demanding citations to their work)
        
        **Detection Methods:**
        - Abnormal citation patterns
        - Self-citation rates far above field norms
        - Clustering of citations from same groups
        
        **Consequences:**
        - Journals have been delisted from Scopus for citation manipulation
        - Individual authors flagged
        - h-index and metrics distorted
        
        **Responses:**
        - Scopus and WoS now monitor citation patterns
        - Self-citation increasingly excluded from metrics
        - Editorial scrutiny of reference lists
        
        **🎯 Lessons:**
        - Metrics can be gamed
        - Citation is about giving credit, not gaming systems
        - Abnormal patterns get detected
        """)

    # Summary Statistics
    with st.expander("📊 India Retraction Statistics", expanded=False):
        st.markdown("""
        **Based on Retraction Watch Database:**
        
        - India is among the top 5 countries for retractions
        - Primary reasons:
          - Plagiarism (~40%)
          - Duplicate publication (~20%)
          - Data issues (~15%)
          - Image manipulation (~10%)
          - Other (~15%)
        
        **Positive Trends:**
        - Increasing awareness
        - Mandatory plagiarism checking
        - UGC-CARE list
        - Institutional ethics training
        - Research integrity officers being appointed
        
        **Challenges Remaining:**
        - Need for more research integrity training
        - Pressure to publish
        - Limited investigation resources
        - Need for protection for whistleblowers
        """)

# =============================================================================
# TAB 3: ETHICAL DILEMMAS
# =============================================================================
with tab3:
    st.markdown("## 🤔 Chapter 3: Ethical Dilemmas in Research")
    
    st.markdown("""
    <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b; margin-bottom: 15px;">
        <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">🧩 What is an Ethical Dilemma?</h4>
        <p style="margin: 0 !important; font-size: 13px;">An ethical dilemma occurs when there are multiple possible courses of action, each with competing ethical considerations. There may be no clearly "right" answer.</p>
    </div>
    """, unsafe_allow_html=True)

    # Dilemma 1: Authorship Dispute
    with st.expander("👥 Dilemma 1: The Authorship Question", expanded=True):
        st.markdown("""
        **Scenario:**
        > Dr. Priya leads a research project. Her PhD student, Rajesh, does 80% of the experimental work. The lab technician, Kumar, runs critical tests. Dr. Priya's collaborator, Dr. Sharma, provides essential equipment and occasional advice but minimal intellectual contribution. Dr. Priya's department head wants to be included as senior author as "institutional support."
        
        **Questions:**
        1. Who should be authors?
        2. What order should they be listed?
        3. How do you handle the department head's request?
        
        **Framework for Analysis:**
        - Apply ICMJE criteria (substantial contribution, drafting, approval, accountability)
        - Kumar may be acknowledged but not authored (if only technical support)
        - Dr. Sharma may or may not qualify depending on contribution
        - Department head providing only "support" does NOT qualify
        
        **Best Practice:**
        > Discuss authorship BEFORE starting the research. Document contributions. Have written agreements.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("✅ **Should be authors:** Rajesh (major work), Dr. Priya (conception, supervision)")
        with col2:
            st.error("❌ **Should NOT be authors:** Department head (gift authorship)")

    # Dilemma 2: Inconsistent Data
    with st.expander("📊 Dilemma 2: The Inconsistent Data Point", expanded=True):
        st.markdown("""
        **Scenario:**
        > You're analyzing data and find that excluding one outlier makes your results statistically significant (p < 0.05). With the outlier, p = 0.07. The outlier comes from a valid experiment with no obvious error.
        
        **Questions:**
        1. Is it ethical to exclude the data point?
        2. How should you handle this in your publication?
        3. What if your supervisor pressures you to exclude it?
        
        **Ethical Analysis:**
        - Excluding valid data to achieve significance is **falsification**
        - Pre-registered analysis plans protect against this
        - Transparency is key
        
        **Correct Approaches:**
        - Report both analyses (with and without outlier)
        - Explain why outlier might be excluded (if valid reason)
        - Don't make the decision based on statistical outcome
        - Consider effect sizes, not just p-values
        
        **If Pressured by Supervisor:**
        - Document the conversation
        - Explain ethical concerns
        - Consult Research Integrity Officer if needed
        - You cannot be forced to commit misconduct
        """)

    # Dilemma 3: Conflict of Interest
    with st.expander("💰 Dilemma 3: The Industry Collaboration", expanded=True):
        st.markdown("""
        **Scenario:**
        > A pharmaceutical company offers to fund your research on their drug. They want to review the manuscript before submission and retain the right to delay publication for "patent review." They also want a clause preventing you from publishing negative results without their approval.
        
        **Questions:**
        1. Should you accept this funding?
        2. What clauses are acceptable vs. problematic?
        3. How do you protect research integrity?
        
        **Analysis:**
        | Clause | Acceptability |
        |--------|---------------|
        | Funding for research | ✅ Acceptable (with disclosure) |
        | Pre-publication review for accuracy | ⚠️ Acceptable if time-limited |
        | Veto power over publication | ❌ Unacceptable |
        | Suppression of negative results | ❌ Unacceptable |
        | Short delay for patent filing | ⚠️ May be acceptable (30-60 days) |
        
        **Best Practice:**
        - Negotiate to remove publication veto
        - Ensure right to publish ALL results (positive and negative)
        - Disclose funding in all publications
        - Have institution review the contract
        """)

    # Dilemma 4: Peer Review
    with st.expander("📝 Dilemma 4: The Competitor's Paper", expanded=True):
        st.markdown("""
        **Scenario:**
        > You're invited to review a paper that directly competes with your forthcoming research. The paper has a flaw you could exploit in your own paper. You could also delay your review, giving yourself time to publish first.
        
        **Questions:**
        1. Should you accept the review?
        2. What if you've already accepted and realize the conflict?
        3. How do you handle the flaw you noticed?
        
        **Ethical Analysis:**
        - Direct competition is a conflict of interest
        - Deliberately delaying is misconduct
        - Using unpublished ideas is theft
        
        **Correct Actions:**
        1. Decline the review, disclosing the conflict
        2. If already accepted, inform editor immediately
        3. Give fair, constructive feedback on the flaw
        4. Never use ideas from papers under review
        5. Document that you had insight before seeing their paper (if relevant)
        """)

    # Dilemma 5: Whistleblowing
    with st.expander("🔔 Dilemma 5: Witnessing Misconduct", expanded=True):
        st.markdown("""
        **Scenario:**
        > You notice your colleague (and friend) has reused images from a previous paper without disclosure. When you mention it, they say "everyone does it" and ask you to forget about it. They remind you they helped get you your job.
        
        **Questions:**
        1. Is this actually misconduct?
        2. What is your obligation?
        3. How do you handle the personal relationship?
        
        **Analysis:**
        - Image reuse without disclosure IS misconduct (self-plagiarism / duplicate publication)
        - "Everyone does it" is not justification
        - Personal relationships don't override ethical obligations
        
        **Options:**
        | Option | Consideration |
        |--------|---------------|
        | Do nothing | Violates your integrity, you become complicit |
        | Speak privately again | Give chance to correct |
        | Report anonymously | Protects relationship but may be traced |
        | Report formally | Fulfills obligation, may damage relationship |
        
        **Best Practice:**
        - Give one clear chance to self-correct
        - If refused, report to appropriate authority
        - Document all conversations
        - Institutions should protect good-faith reporters
        """)

    # Interactive Decision Making
    st.markdown("### 🧭 Ethical Decision-Making Framework")
    
    with st.expander("📋 PLUS Model for Ethical Decision Making", expanded=True):
        st.markdown("""
        **P.L.U.S. Decision-Making Framework:**
        
        | Letter | Question |
        |--------|----------|
        | **P** – Policies | Does it violate policies, guidelines, or laws? |
        | **L** – Legal | Is it legal in the relevant jurisdiction? |
        | **U** – Universal | Would it be acceptable if everyone did it? |
        | **S** – Self | Can I live with this decision? Would I tell my family? |
        
        **Additional Questions:**
        - Would this be front-page news tomorrow? (Newspaper test)
        - Would I be comfortable if my supervisor knew?
        - Would this meet the standards of my professional community?
        - Does this action treat all stakeholders fairly?
        """)

# =============================================================================
# TAB 4: LESSONS LEARNED
# =============================================================================
with tab4:
    st.markdown("## 📚 Chapter 4: Lessons Learned & Prevention")
    
    # Systemic Issues
    st.markdown("### 4.1 Why Does Misconduct Happen?")
    
    with st.expander("🔍 Root Causes of Misconduct", expanded=True):
        st.markdown("""
        **Individual Factors:**
        | Factor | Description |
        |--------|-------------|
        | Pressure | Publish or perish, funding deadlines |
        | Rationalization | "Everyone does it," "It's just this once" |
        | Opportunity | Lack of oversight, solo data collection |
        | Poor Training | Didn't know it was wrong |
        | Personal Stress | Financial, career, personal problems |
        
        **Systemic Factors:**
        | Factor | Description |
        |--------|-------------|
        | Metrics Obsession | Overemphasis on quantity over quality |
        | Insufficient Oversight | Weak supervision, no data audits |
        | Power Imbalances | Students can't challenge supervisors |
        | Inadequate Investigation | Institutions reluctant to find fraud |
        | No Protection for Reporters | Whistleblowers face retaliation |
        """)
        
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=11, shape=box, style="rounded,filled"];
            
            pressure [label="PRESSURE\\n(Publish or Perish)", fillcolor="#fecaca"];
            opportunity [label="OPPORTUNITY\\n(Weak oversight)", fillcolor="#fed7aa"];
            rationalization [label="RATIONALIZATION\\n(Excuses)", fillcolor="#fef3c7"];
            
            misconduct [label="MISCONDUCT", fillcolor="#fca5a5", shape=octagon];
            
            pressure -> misconduct;
            opportunity -> misconduct;
            rationalization -> misconduct;
        }
        """)

    # Prevention
    st.markdown("### 4.2 How to Prevent Misconduct")
    
    with st.expander("🛡️ Institutional Prevention Strategies", expanded=True):
        st.markdown("""
        **Training & Education:**
        - Mandatory research integrity courses
        - Regular refresher training
        - Case-based learning
        - Mentorship programs
        
        **Policies & Procedures:**
        - Clear misconduct definitions
        - Transparent investigation procedures
        - Whistleblower protection
        - Data management requirements
        
        **Culture & Environment:**
        - Quality over quantity metrics
        - Open discussion of ethics
        - Support for negative results
        - Celebration of replication
        
        **Technical Measures:**
        - Plagiarism checking tools
        - Data audits
        - Electronic lab notebooks
        - Pre-registration of studies
        """)

    with st.expander("👤 Personal Prevention Strategies", expanded=True):
        st.markdown("""
        **Habits for Integrity:**
        
        | Practice | Why It Helps |
        |----------|--------------|
        | Keep detailed lab notebooks | Provides audit trail |
        | Back up raw data | Prevents "data loss" claims |
        | Discuss authorship early | Prevents disputes later |
        | Know your field's norms | Avoid unintentional violations |
        | Seek mentorship | Learn from experienced researchers |
        | Report concerns early | Problems grow if ignored |
        | Take ethics training seriously | It's not just a checkbox |
        
        **When You're Unsure:**
        - Consult research integrity officer
        - Discuss with trusted mentor
        - Review relevant guidelines (COPE, ICMJE)
        - When in doubt, disclose
        """)

    # Resources
    st.markdown("### 4.3 Essential Resources")
    
    with st.expander("📚 Key Organizations & Resources", expanded=True):
        st.markdown("""
        **International Organizations:**
        | Organization | Role | Website |
        |--------------|------|---------|
        | COPE | Publication ethics guidelines | publicationethics.org |
        | ORI | US research integrity oversight | ori.hhs.gov |
        | WCRI | World conferences on integrity | wcrif.org |
        
        **Watchdog Sites:**
        | Site | Purpose |
        |------|---------|
        | Retraction Watch | News on retractions |
        | PubPeer | Post-publication review |
        | For Better Science | Investigation blog |
        
        **Indian Resources:**
        | Resource | Purpose |
        |----------|---------|
        | UGC-CARE List | Approved journals |
        | CSIR-Ethics | Research ethics guidelines |
        | ICMR Guidelines | Clinical research ethics |
        
        **Guidelines & Declarations:**
        - Singapore Statement on Research Integrity
        - Hong Kong Principles
        - DORA (Declaration on Research Assessment)
        - Leiden Manifesto (for responsible metrics)
        """)

    # Final Takeaways
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 20px; border-radius: 10px; margin-top: 15px; border: 1px solid #86efac;">
        <h3 style="color: #166534; margin: 0 0 15px 0 !important;">🎯 Key Takeaways</h3>
        <ol style="margin: 0; padding-left: 25px; color: #166534;">
            <li style="margin-bottom: 8px;"><b>Misconduct has real consequences</b> — careers ended, science harmed, public trust damaged</li>
            <li style="margin-bottom: 8px;"><b>Systemic pressures contribute</b> — but they never justify unethical behavior</li>
            <li style="margin-bottom: 8px;"><b>Prevention is better than detection</b> — training, culture, oversight</li>
            <li style="margin-bottom: 8px;"><b>Everyone has a role</b> — students, supervisors, institutions, funders</li>
            <li style="margin-bottom: 8px;"><b>Speak up</b> — protected reporting is essential for self-correction</li>
            <li><b>Integrity is foundational</b> — without it, science loses its value</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# Footer
show_footer()
