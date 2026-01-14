import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Philosophy, Ethics & Scientific Conduct | Research Ethics Course 2024",
    description="Master the foundations of research ethics: Philosophy, moral judgments, scientific misconduct (FFP), publication ethics, authorship issues, and research integrity. Complete Ph.D. course material.",
    keywords=[
        "research ethics",
        "scientific misconduct",
        "plagiarism",
        "fabrication",
        "falsification",
        "research integrity",
        "publication ethics",
        "authorship ethics",
        "moral philosophy",
        "intellectual honesty",
        "salami slicing",
        "duplicate publication",
        "ethical research",
        "phd ethics course"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/philosophy-ethics",
    reading_time=90,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Philosophy & Ethics", "url": "https://researchethics.dev/philosophy-ethics"}
    ],
    course_info={
        "name": "Philosophy, Ethics and Scientific Conduct Module",
        "description": "Comprehensive coverage of philosophy foundations, ethics, scientific misconduct, publication ethics, and research integrity.",
        "level": "Doctoral",
        "prerequisites": "Basic research experience",
        "teaches": ["Philosophy", "Ethics", "Research Integrity", "Scientific Misconduct", "Publication Ethics", "Authorship"],
        "workload": "PT15H",
        "rating": "4.9",
        "rating_count": 892
    },
    faq_items=[
        {
            "question": "What is the difference between fabrication and falsification?",
            "answer": "Fabrication is making up data or results and recording/reporting them. Falsification is manipulating research materials, equipment, or processes, or changing/omitting data such that the research is not accurately represented."
        },
        {
            "question": "What is self-plagiarism?",
            "answer": "Self-plagiarism occurs when researchers reuse their own previously published work without proper citation. This includes recycling text, data, or ideas from earlier publications without acknowledgment."
        },
        {
            "question": "What is salami slicing in research?",
            "answer": "Salami slicing is the practice of dividing a single research study into multiple publications to artificially inflate publication count, rather than publishing results as one comprehensive paper."
        }
    ]
)
apply_custom_css()
show_top_nav(current_page="Philosophy & Ethics")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📖 Module 1: Philosophy, Ethics & Scientific Conduct</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #1e40af;">From moral foundations to preventing misconduct — building ethical researchers.</p>
</div>
""", unsafe_allow_html=True)

# Tabs for different sections
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏛️ Philosophy", 
    "⚖️ Ethics", 
    "🔬 Research Integrity", 
    "⚠️ Misconduct", 
    "📝 Publication Ethics"
])

# =============================================================================
# TAB 1: INTRODUCTION TO PHILOSOPHY
# =============================================================================
with tab1:
    st.markdown("## 🏛️ Chapter 1: Introduction to Philosophy")
    
    # Section 1.1: Definition
    st.markdown("### 1.1 What is Philosophy?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Philosophy</b> (from Greek <i>philosophia</i> = "love of wisdom") is the systematic study of fundamental questions about existence, knowledge, values, reason, mind, and language.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: The Root System</h4>
            <p style="margin: 0 !important; font-size: 13px;">Philosophy is like the <b>root system of a tree</b>. Just as roots provide foundation and nourishment to branches, philosophy provides foundational thinking for all other disciplines.</p>
        </div>
        """, unsafe_allow_html=True)

    # Nature and Scope
    with st.expander("📚 Nature and Scope of Philosophy", expanded=True):
        st.markdown("""
        **Nature of Philosophy:**
        - **Reflective**: Examines assumptions underlying knowledge and beliefs
        - **Critical**: Questions established ideas and seeks logical justifications
        - **Systematic**: Uses organized methods to explore fundamental questions
        - **Universal**: Applies to all areas of human experience
        
        **Scope of Philosophy:**
        | Area | Questions It Addresses |
        |------|----------------------|
        | Metaphysics | What exists? What is the nature of reality? |
        | Epistemology | What is knowledge? How do we know things? |
        | Ethics | What is right and wrong? How should we act? |
        | Logic | What constitutes valid reasoning? |
        | Aesthetics | What is beauty? What makes art valuable? |
        """)

    # Branches of Philosophy
    with st.expander("🌳 Branches of Philosophy", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🔮 Metaphysics</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Study of:</b> Reality, existence, being<br><b>Questions:</b> Does God exist? What is time?</p>
            </div>
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🧠 Epistemology</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Study of:</b> Knowledge, belief, justification<br><b>Questions:</b> How do we know what we know?</p>
            </div>
            <div style="background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">⚖️ Ethics</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Study of:</b> Morality, right/wrong, virtues<br><b>Questions:</b> What is the good life?</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🔗 Logic</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Study of:</b> Valid reasoning, arguments<br><b>Questions:</b> What makes an argument sound?</p>
            </div>
            <div style="background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🎨 Aesthetics</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Study of:</b> Beauty, art, taste<br><b>Questions:</b> What makes something beautiful?</p>
            </div>
            <div style="background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🏛️ Political Philosophy</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Study of:</b> Government, justice, rights<br><b>Questions:</b> What is a just society?</p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("🖼️ Visual: Philosophy as Foundation of Knowledge", expanded=False):
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=11, shape=box, style="rounded,filled"];
            
            phil [label="PHILOSOPHY\\n(Foundation)", fillcolor="#dbeafe", shape=ellipse];
            
            meta [label="Metaphysics", fillcolor="#f3e8ff"];
            epis [label="Epistemology", fillcolor="#dcfce7"];
            ethics [label="Ethics", fillcolor="#fef3c7"];
            logic [label="Logic", fillcolor="#fed7aa"];
            
            science [label="Natural Sciences", fillcolor="#e0f2fe"];
            social [label="Social Sciences", fillcolor="#fce7f3"];
            research [label="Research Ethics", fillcolor="#d1fae5", shape=doubleoctagon];
            
            phil -> meta; phil -> epis; phil -> ethics; phil -> logic;
            epis -> science; ethics -> social;
            ethics -> research [style=bold, color="#16a34a"];
        }
        """)

# =============================================================================
# TAB 2: ETHICS
# =============================================================================
with tab2:
    st.markdown("## ⚖️ Chapter 2: Ethics and Moral Philosophy")
    
    # Definition
    st.markdown("### 2.1 What is Ethics?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Ethics</b> (or Moral Philosophy) is the branch of philosophy that involves systematizing, defending, and recommending concepts of right and wrong conduct.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: The Compass</h4>
            <p style="margin: 0 !important; font-size: 13px;">Ethics is like an <b>internal compass</b>. Just as a compass guides travelers in the right direction, ethics guides our decisions toward right actions.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📋 Ethics vs. Morals", expanded=True):
        st.markdown("""
        | Aspect | Ethics | Morals |
        |--------|--------|--------|
        | **Source** | External systems (society, profession, religion) | Internal principles (personal beliefs) |
        | **Scope** | Universal, systematic study | Individual, personal values |
        | **Flexibility** | Consistent within a system | May vary by situation |
        | **Example** | "A doctor must not harm patients" (professional ethics) | "I believe lying is always wrong" (personal morals) |
        """)

    # Moral Philosophy
    with st.expander("🧠 Nature of Moral Judgments and Reactions", expanded=True):
        st.markdown("""
        **Moral Judgment** is the process of determining whether an action is right or wrong based on ethical principles.
        
        **Components of Moral Judgments:**
        1. **Cognitive Element**: Knowledge of ethical principles
        2. **Affective Element**: Emotional response (guilt, pride, empathy)
        3. **Behavioral Element**: Action taken based on judgment
        
        **Types of Ethical Theories:**
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">🎯 Consequentialism</h4>
                <p style="margin: 0 !important; font-size: 12px;"><b>Focus:</b> Outcomes<br><b>Principle:</b> Right action = best consequences<br><b>Example:</b> Utilitarianism</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📜 Deontology</h4>
                <p style="margin: 0 !important; font-size: 12px;"><b>Focus:</b> Duties & Rules<br><b>Principle:</b> Some acts are inherently right/wrong<br><b>Example:</b> Kant's Ethics</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">👤 Virtue Ethics</h4>
                <p style="margin: 0 !important; font-size: 12px;"><b>Focus:</b> Character<br><b>Principle:</b> Develop virtuous character<br><b>Example:</b> Aristotelian Ethics</p>
            </div>
            """, unsafe_allow_html=True)

    # Ethics in Science and Research
    with st.expander("🔬 Ethics with Respect to Science and Research", expanded=True):
        st.markdown("""
        **Why Ethics in Research Matters:**
        - Research affects society, policy, and human welfare
        - Unethical research can cause harm to participants and public trust
        - Scientific knowledge builds on prior work; integrity is essential
        
        **Key Ethical Principles in Research:**
        
        | Principle | Description | Application |
        |-----------|-------------|-------------|
        | **Honesty** | Report truthfully without fabrication | Accurate data reporting |
        | **Objectivity** | Avoid bias in research design and analysis | Peer review, methodology |
        | **Integrity** | Keep promises, act consistently | Following protocols |
        | **Carefulness** | Avoid errors, maintain records | Documentation |
        | **Openness** | Share data, methods, ideas | Open science |
        | **Respect for IP** | Honor copyrights, patents | Proper attribution |
        | **Confidentiality** | Protect sensitive information | Participant privacy |
        | **Responsible Publication** | Avoid waste, duplication | Meaningful contributions |
        | **Respect for Colleagues** | Fair treatment | Collaboration |
        | **Social Responsibility** | Benefit society | Ethical applications |
        """)

# =============================================================================
# TAB 3: RESEARCH INTEGRITY
# =============================================================================
with tab3:
    st.markdown("## 🔬 Chapter 3: Intellectual Honesty & Research Integrity")
    
    st.markdown("### 3.1 Intellectual Honesty")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Intellectual Honesty</b> is the virtue of truthfulness in intellectual endeavors. It means presenting ideas, data, and arguments fairly and accurately, acknowledging limitations and opposing views.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: The Clear Window</h4>
            <p style="margin: 0 !important; font-size: 13px;">Intellectual honesty is like a <b>clear glass window</b>. It allows others to see your work exactly as it is — no distortions, no tinting, no smudges.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("✅ Components of Intellectual Honesty", expanded=True):
        st.markdown("""
        1. **Truthfulness**: Stating facts accurately
        2. **Acknowledgment of Sources**: Giving credit where due
        3. **Recognition of Limitations**: Being aware of what you don't know
        4. **Openness to Criticism**: Welcoming peer review and feedback
        5. **Avoidance of Deception**: No misleading representations
        """)

    st.markdown("### 3.2 Research Integrity")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Research Integrity</b> refers to the active adherence to ethical principles and professional standards essential for responsible research practice.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: The Foundation of a Building</h4>
            <p style="margin: 0 !important; font-size: 13px;">Research integrity is like the <b>foundation of a skyscraper</b>. If compromised, the entire structure (body of scientific knowledge) becomes unstable.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🏗️ Pillars of Research Integrity", expanded=True):
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=11, shape=box, style="rounded,filled"];
            
            ri [label="RESEARCH\\nINTEGRITY", fillcolor="#d1fae5", shape=ellipse, fontsize=12];
            
            honest [label="Honesty\\n(True reporting)", fillcolor="#dbeafe"];
            account [label="Accountability\\n(Take responsibility)", fillcolor="#f3e8ff"];
            prof [label="Professional Courtesy\\n(Fair treatment)", fillcolor="#fef3c7"];
            stew [label="Good Stewardship\\n(Resource management)", fillcolor="#fed7aa"];
            
            ri -> honest; ri -> account; ri -> prof; ri -> stew;
        }
        """)

    with st.expander("📊 Research Integrity Framework (Singapore Statement)", expanded=False):
        st.markdown("""
        The **Singapore Statement on Research Integrity** (2010) provides a global framework:
        
        **Responsibilities:**
        1. Integrity in research conduct
        2. Compliance with regulations
        3. Proper research methods
        4. Accurate research records
        5. Appropriate authorship
        6. Publication acknowledgment
        7. Peer review responsibility
        8. Conflict of interest disclosure
        9. Public communication accuracy
        10. Reporting irresponsible practices
        11. Responding to allegations
        
        **Principles:**
        - Honesty in all aspects of research
        - Accountability in conduct
        - Professional courtesy and fairness
        - Good stewardship of research resources
        """)

# =============================================================================
# TAB 4: SCIENTIFIC MISCONDUCT
# =============================================================================
with tab4:
    st.markdown("## ⚠️ Chapter 4: Scientific Misconduct")
    
    st.markdown("""
    <div style="background: #fef2f2; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444; margin-bottom: 15px;">
        <h4 style="color: #dc2626; margin: 0 0 8px 0 !important;">⚠️ Critical Understanding</h4>
        <p style="margin: 0 !important; font-size: 13px;">Scientific misconduct threatens the foundation of science itself. The three major forms are collectively known as <b>FFP: Fabrication, Falsification, and Plagiarism</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    # FFP Section
    st.markdown("### 4.1 The FFP Triad: Fabrication, Falsification, Plagiarism")
    
    with st.expander("🔴 FABRICATION", expanded=True):
        col_def, col_ex = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #fef2f2; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444;">
                <h4 style="color: #dc2626; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Fabrication</b> is making up data or results and recording or reporting them. It's creating data that never existed.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_ex:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">💡 Analogy: The Counterfeit Note</h4>
                <p style="margin: 0 !important; font-size: 13px;">Fabrication is like printing <b>counterfeit money</b>. It looks real but was never produced legitimately.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **Examples of Fabrication:**
        - Inventing experimental data without conducting experiments
        - Creating fake survey responses
        - Manufacturing participant information
        - Generating synthetic results from non-existent studies
        
        **🔴 Famous Case:** Dr. Hwang Woo-suk (South Korea, 2005) fabricated data claiming to have created human embryonic stem cells through cloning.
        """)

    with st.expander("🟠 FALSIFICATION", expanded=True):
        col_def, col_ex = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #fff7ed; padding: 14px; border-radius: 8px; border-left: 4px solid #f97316;">
                <h4 style="color: #ea580c; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Falsification</b> is manipulating research materials, equipment, or processes, or changing/omitting data such that the research is not accurately represented.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_ex:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">💡 Analogy: Photoshopping Reality</h4>
                <p style="margin: 0 !important; font-size: 13px;">Falsification is like <b>heavily editing a photo</b>. The original existed, but it's been altered to show something different.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **Examples of Falsification:**
        - Removing outliers without justification
        - Adjusting images in ways that misrepresent data
        - Selectively omitting contradictory data points
        - Changing experimental conditions after the fact
        - Manipulating statistical analyses
        
        **🟠 Difference from Fabrication:** In falsification, real data exists but is manipulated. In fabrication, data is completely invented.
        """)

    with st.expander("🟡 PLAGIARISM", expanded=True):
        col_def, col_ex = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #fefce8; padding: 14px; border-radius: 8px; border-left: 4px solid #eab308;">
                <h4 style="color: #ca8a04; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Plagiarism</b> is the appropriation of another person's ideas, processes, results, or words without giving appropriate credit.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_ex:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">💡 Analogy: Wearing Someone's Medal</h4>
                <p style="margin: 0 !important; font-size: 13px;">Plagiarism is like wearing <b>someone else's medal</b> and accepting praise for achievements that aren't yours.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **Types of Plagiarism:**
        
        | Type | Description | Severity |
        |------|-------------|----------|
        | **Direct Plagiarism** | Word-for-word copying without citation | 🔴 Most Severe |
        | **Mosaic Plagiarism** | Mixing copied phrases with original text | 🟠 Severe |
        | **Self-Plagiarism** | Reusing own previously published work | 🟡 Moderate |
        | **Paraphrasing Plagiarism** | Rewording without citation | 🟡 Moderate |
        | **Accidental Plagiarism** | Unintentional missing citations | 🟢 Least Severe |
        """)

    # Redundant Publications
    st.markdown("### 4.2 Redundant Publications")
    
    with st.expander("📄 Duplicate and Overlapping Publications", expanded=True):
        st.markdown("""
        <div style="background: #fef2f2; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444; margin-bottom: 10px;">
            <h4 style="color: #dc2626; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Duplicate Publication</b> is publishing the same study in multiple journals without disclosure. <b>Overlapping Publication</b> involves substantial content overlap between publications.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Problems with Duplicate/Overlapping Publications:**
        - Distorts the scientific record
        - Wastes peer review resources
        - May inflate effect sizes in meta-analyses
        - Violates journal copyright agreements
        - Constitutes publication misconduct
        """)

    with st.expander("🔪 Salami Slicing", expanded=True):
        col_def, col_analogy = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #fff7ed; padding: 14px; border-radius: 8px; border-left: 4px solid #f97316;">
                <h4 style="color: #ea580c; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Salami Slicing</b> is the practice of dividing one study into multiple publications (the "least publishable units") to artificially increase publication count.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_analogy:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">💡 Analogy: Slicing a Salami</h4>
                <p style="margin: 0 !important; font-size: 13px;">Like slicing a <b>single salami into many thin pieces</b> to make it seem like you have more food, researchers slice one study into many papers.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **Red Flags for Salami Slicing:**
        - Same methodology across multiple papers
        - Same dataset used repeatedly
        - Papers could logically be combined
        - Similar introduction/discussion sections
        """)

    with st.expander("📊 Selective Reporting and Misrepresentation of Data", expanded=True):
        st.markdown("""
        **Selective Reporting** involves choosing to report only results that support a hypothesis while hiding contradictory findings.
        
        **Forms of Data Misrepresentation:**
        
        | Type | Description |
        |------|-------------|
        | **Cherry Picking** | Selecting favorable data points |
        | **P-Hacking** | Manipulating analysis to achieve statistical significance |
        | **HARKing** | Hypothesizing After Results are Known |
        | **Outcome Switching** | Changing primary/secondary outcomes post-hoc |
        | **Spin** | Presenting negative results as positive |
        | **Image Manipulation** | Altering figures/images inappropriately |
        """)

# =============================================================================
# TAB 5: PUBLICATION ETHICS
# =============================================================================
with tab5:
    st.markdown("## 📝 Chapter 5: Publication Misconduct & Ethics")
    
    st.markdown("### 5.1 What is Publication Misconduct?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Publication Misconduct</b> encompasses any ethical violation related to the publication of research, including authorship fraud, submission fraud, and reviewer misconduct.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Breaking Traffic Rules</h4>
            <p style="margin: 0 !important; font-size: 13px;">Publication ethics are like <b>traffic rules</b>. Breaking them might seem to get you ahead faster, but it endangers everyone and eventually catches up with you.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🔴 Problems Leading to Unethical Behavior", expanded=True):
        st.markdown("""
        **Systemic Pressures:**
        - "Publish or Perish" culture
        - Competition for funding and positions
        - Pressure to meet quotas
        - Career advancement tied to publications
        
        **Individual Factors:**
        - Lack of ethics training
        - Poor mentorship
        - Financial pressures
        - Cultural differences in understanding plagiarism
        
        **Institutional Gaps:**
        - Weak oversight mechanisms
        - Inadequate investigation procedures
        - Lack of clear policies
        - Insufficient resources for ethics training
        """)

    with st.expander("📋 Types of Publication Misconduct", expanded=True):
        st.markdown("""
        | Type | Description | Example |
        |------|-------------|---------|
        | **Authorship Fraud** | False authorship claims | Ghost/Guest authorship |
        | **Citation Manipulation** | Artificially inflating citations | Coercive citation |
        | **Submission Fraud** | Simultaneous submission without disclosure | Double submission |
        | **Reviewer Misconduct** | Conflicts of interest, stealing ideas | Reviewer plagiarism |
        | **Data Fraud** | FFP as discussed earlier | Fabrication |
        | **Peer Review Fraud** | Fake reviewer accounts | Paper mills |
        """)

    # Authorship and Contributorship
    st.markdown("### 5.2 Authorship and Contributorship")
    
    with st.expander("👥 ICMJE Authorship Criteria", expanded=True):
        st.markdown("""
        The **International Committee of Medical Journal Editors (ICMJE)** defines authorship criteria:
        
        **All FOUR criteria must be met:**
        
        1. ✅ **Substantial contributions** to conception/design, OR acquisition/analysis/interpretation of data
        2. ✅ **Drafting** the work OR revising it critically for important intellectual content
        3. ✅ **Final approval** of the version to be published
        4. ✅ **Agreement to be accountable** for all aspects of the work
        
        **Types of Problematic Authorship:**
        
        | Type | Description | Why It's Wrong |
        |------|-------------|----------------|
        | **Gift Authorship** | Adding names for favor/prestige | No real contribution |
        | **Guest Authorship** | Adding senior person's name automatically | No contribution, just status |
        | **Ghost Authorship** | Excluding contributors | Denies credit |
        | **Honorary Authorship** | Senior person automatically included | No meaningful contribution |
        """)

    with st.expander("👤 CRediT: Contributor Roles Taxonomy", expanded=False):
        st.markdown("""
        **CRediT** (Contributor Roles Taxonomy) defines 14 specific roles:
        
        | Role | Description |
        |------|-------------|
        | Conceptualization | Ideas, formulation of research goals |
        | Methodology | Development of methodology |
        | Software | Programming, software development |
        | Validation | Verification of results |
        | Formal Analysis | Statistical analysis |
        | Investigation | Conducting research, data collection |
        | Resources | Provision of materials, equipment |
        | Data Curation | Data management |
        | Writing - Original Draft | Initial writing |
        | Writing - Review & Editing | Critical review |
        | Visualization | Data presentation |
        | Supervision | Oversight of project |
        | Project Administration | Management |
        | Funding Acquisition | Financial support |
        """)

    # Identification and Handling
    st.markdown("### 5.3 Identification of Publication Misconduct")
    
    with st.expander("🔍 How Misconduct is Detected", expanded=True):
        st.markdown("""
        **Detection Methods:**
        
        1. **Peer Review**: Reviewers may notice inconsistencies
        2. **Post-Publication Scrutiny**: Readers and other researchers
        3. **Plagiarism Software**: Turnitin, iThenticate, etc.
        4. **Image Analysis**: Forensic image detection
        5. **Statistical Analysis**: Detecting improbable results
        6. **Whistleblowers**: Internal reporting
        7. **Data Audits**: Verification of raw data
        """)

    with st.expander("📞 Complaints and Appeals Process", expanded=True):
        st.markdown("""
        **Standard Process (COPE Guidelines):**
        
        1. **Allegation Received** → Initial screening
        2. **Preliminary Assessment** → Is there substance?
        3. **Investigation** → Gather evidence, interview parties
        4. **Finding** → Misconduct confirmed or not
        5. **Action** → Correction, retraction, notification
        6. **Appeal** → Opportunity to contest decision
        
        **Key Principles:**
        - Confidentiality until proven
        - Fair hearing for accused
        - Proportionate response
        - Protection for whistleblowers
        - Documentation of process
        
        **COPE (Committee on Publication Ethics)** provides flowcharts for handling various misconduct scenarios.
        """)

    with st.expander("⚖️ Violation of Publication Ethics - Consequences", expanded=True):
        st.markdown("""
        **Consequences for Authors:**
        - Retraction of paper
        - Ban from journal
        - Notification to institution
        - Loss of funding
        - Career damage
        - Legal action (in severe cases)
        
        **Consequences for Institutions:**
        - Reputational damage
        - Loss of research funding
        - Regulatory sanctions
        - Required policy changes
        
        **Consequences for Science:**
        - Wasted research resources following false leads
        - Erosion of public trust
        - Potential harm if clinical research is compromised
        """)

# Footer
show_footer()
