import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Measurement, Scaling & Sampling | Validity, Reliability, Cronbach Alpha [2024]",
    description="Master measurement concepts: validity, reliability, Cronbach's Alpha, measurement scales (nominal, ordinal, interval, ratio), Likert scales, and sampling methods for Ph.D. research.",
    keywords=[
        "validity and reliability",
        "Cronbach alpha",
        "measurement scales",
        "Likert scale",
        "sampling methods",
        "probability sampling",
        "non-probability sampling",
        "nominal ordinal interval ratio",
        "questionnaire validation",
        "random sampling"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/methodology/measurement",
    reading_time=90,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Measurement & Sampling", "url": "https://researchethics.dev/methodology/measurement"}
    ],
    course_info={
        "name": "Measurement, Scaling & Sampling - Paper I Unit III",
        "description": "Comprehensive guide to measurement concepts, scaling techniques, and sampling methods for research.",
        "level": "Doctoral",
        "prerequisites": "Research Design",
        "teaches": ["Validity", "Reliability", "Cronbach Alpha", "Measurement Scales", "Sampling"],
        "workload": "PT18H",
        "rating": "4.9",
        "rating_count": 834
    }
)
apply_custom_css()
show_top_nav(current_page="Measurement & Sampling")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📏 Unit III: Measurement, Scaling & Sampling</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #7c3aed;">Paper I: Research Methodology — Ensuring precision in measurement.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "✅ Validity & Reliability",
    "📊 Measurement Scales",
    "⚖️ Scaling Techniques",
    "🎯 Sampling Methods"
])

# =============================================================================
# TAB 1: VALIDITY AND RELIABILITY
# =============================================================================
with tab1:
    st.markdown("## ✅ Chapter 1: Validity and Reliability")
    
    st.markdown("### 1.1 Understanding Validity")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Validity</b> is the degree to which an instrument measures what it is intended to measure. A valid test actually captures the concept you're trying to study.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Archery Target</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Validity = hitting the right target.</b> If you're trying to measure intelligence but your test measures memory, you've hit the wrong target — invalid.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🎯 Types of Validity", expanded=True):
        st.markdown("""
        | Type | Question | How to Assess |
        |------|----------|---------------|
        | **Face Validity** | Does it look like it measures what it should? | Expert judgment |
        | **Content Validity** | Does it cover all aspects of the concept? | Expert review of items |
        | **Construct Validity** | Does it measure the theoretical construct? | Factor analysis, correlations |
        | **Criterion Validity** | Does it correlate with other measures of the same thing? | Correlation with criterion |
        | **Predictive Validity** | Does it predict future outcomes? | Correlation with future performance |
        | **Concurrent Validity** | Does it correlate with current criteria? | Correlation with existing measures |
        | **Convergent Validity** | Does it correlate with similar constructs? | High correlation with related measures |
        | **Discriminant Validity** | Does it NOT correlate with unrelated constructs? | Low correlation with unrelated measures |
        """)
        
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=10, shape=box, style="rounded,filled"];
            
            validity [label="VALIDITY", fillcolor="#dbeafe", shape=ellipse];
            
            internal [label="Internal Validity\\n(Within study)", fillcolor="#dcfce7"];
            external [label="External Validity\\n(Generalization)", fillcolor="#fef3c7"];
            construct [label="Construct Validity\\n(Theoretical)", fillcolor="#f3e8ff"];
            
            content [label="Content", fillcolor="#bbf7d0", fontsize=9];
            face [label="Face", fillcolor="#bbf7d0", fontsize=9];
            criterion [label="Criterion", fillcolor="#fde68a", fontsize=9];
            convergent [label="Convergent", fillcolor="#e9d5ff", fontsize=9];
            discriminant [label="Discriminant", fillcolor="#e9d5ff", fontsize=9];
            
            validity -> internal; validity -> external; validity -> construct;
            internal -> content; internal -> face;
            external -> criterion;
            construct -> convergent; construct -> discriminant;
        }
        """)

    st.markdown("### 1.2 Understanding Reliability")
    
    col_def2, col_analogy2 = st.columns(2)
    with col_def2:
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Reliability</b> is the degree to which an instrument produces consistent, stable results. A reliable test gives the same results under consistent conditions.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy2:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Bathroom Scale</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Reliability = consistency.</b> If a scale shows 70kg, then 65kg, then 72kg on three immediate tries — it's unreliable, even if the average is correct.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🔄 Types of Reliability", expanded=True):
        st.markdown("""
        | Type | Description | How to Assess |
        |------|-------------|---------------|
        | **Test-Retest** | Same results over time | Administer twice, correlate |
        | **Parallel Forms** | Equivalent versions give same results | Two versions, correlate |
        | **Internal Consistency** | Items measure same construct | Cronbach's Alpha, Split-half |
        | **Inter-rater** | Different observers agree | Multiple raters, calculate agreement |
        """)

    with st.expander("📊 Cronbach's Alpha", expanded=True):
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb; margin-bottom: 10px;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Cronbach's Alpha (α)</b> is a measure of internal consistency — how closely related a set of items are as a group. It ranges from 0 to 1.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Formula:**")
        st.latex(r"\alpha = \frac{k}{k-1} \left(1 - \frac{\sum_{i=1}^{k} \sigma_{i}^{2}}{\sigma_{total}^{2}}\right)")
        
        st.markdown("""
        **Where:**
        - k = number of items
        - σᵢ² = variance of item i
        - σ²_total = variance of total scores
        
        **Interpretation:**
        
        | Alpha Value | Internal Consistency |
        |-------------|---------------------|
        | α ≥ 0.90 | Excellent |
        | 0.80 ≤ α < 0.90 | Good |
        | 0.70 ≤ α < 0.80 | Acceptable |
        | 0.60 ≤ α < 0.70 | Questionable |
        | 0.50 ≤ α < 0.60 | Poor |
        | α < 0.50 | Unacceptable |
        
        **Note:** For exploratory research, α ≥ 0.60 may be acceptable. For established scales, aim for α ≥ 0.70.
        """)

    with st.expander("⚖️ Validity vs Reliability", expanded=True):
        st.markdown("""
        <div style="background: #fef2f2; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444; margin-bottom: 10px;">
            <h4 style="color: #dc2626; margin: 0 0 8px 0 !important;">⚠️ Key Insight</h4>
            <p style="margin: 0 !important; font-size: 13px;">A test can be <b>reliable but not valid</b> (consistent but wrong target). A test <b>cannot be valid without being reliable</b> (if inconsistent, it can't be accurate).</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        | | Valid | Not Valid |
        |--|-------|-----------|
        | **Reliable** | ✅ Ideal (accurate & consistent) | ⚠️ Consistently wrong |
        | **Not Reliable** | ❌ Impossible | ❌ Random noise |
        
        **Archery Analogy:**
        - Reliable + Valid = All arrows in bullseye
        - Reliable + Invalid = All arrows clustered, but off-center
        - Unreliable = Arrows scattered randomly
        """)

# =============================================================================
# TAB 2: MEASUREMENT SCALES
# =============================================================================
with tab2:
    st.markdown("## 📊 Chapter 2: Measurement Scales")
    
    st.markdown("### 2.1 Levels of Measurement")
    
    with st.expander("📏 The Four Levels of Measurement", expanded=True):
        st.markdown("""
        | Level | Properties | Examples | Allowed Operations |
        |-------|------------|----------|-------------------|
        | **Nominal** | Categories only | Gender, Religion, Color | Mode, Frequency |
        | **Ordinal** | Categories + Order | Rankings, Satisfaction (High/Med/Low) | Median, Percentiles |
        | **Interval** | Order + Equal intervals | Temperature (°C), IQ, Calendar year | Mean, SD, Correlation |
        | **Ratio** | Interval + True zero | Height, Weight, Age, Income | All + Ratios |
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: #eff6ff; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📝 Nominal Scale</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>What:</b> Names or labels, no order<br>
                <b>Example:</b> Male=1, Female=2<br>
                <b>Analysis:</b> Chi-square, mode<br>
                <b>Analogy:</b> Jersey numbers — just labels
                </p>
            </div>
            <div style="background: #f0fdf4; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📊 Ordinal Scale</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>What:</b> Ranked categories<br>
                <b>Example:</b> 1st, 2nd, 3rd place<br>
                <b>Analysis:</b> Median, Mann-Whitney<br>
                <b>Analogy:</b> Race positions — order matters, gaps unknown
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: #fef3c7; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">📈 Interval Scale</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>What:</b> Equal intervals, no true zero<br>
                <b>Example:</b> Temperature in Celsius<br>
                <b>Analysis:</b> Mean, t-test, ANOVA<br>
                <b>Analogy:</b> 20°-10°=10° same as 30°-20°, but 0°C isn't "no heat"
                </p>
            </div>
            <div style="background: #faf5ff; padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">⚖️ Ratio Scale</h4>
                <p style="margin: 0 !important; font-size: 12px;">
                <b>What:</b> Equal intervals + true zero<br>
                <b>Example:</b> Weight, Height, Income<br>
                <b>Analysis:</b> All statistical operations<br>
                <b>Analogy:</b> 0kg means no weight; 100kg is twice 50kg
                </p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("🎯 Memory Trick: NOIR", expanded=True):
        st.markdown("""
        Remember **NOIR** (French for "black"):
        
        - **N**ominal — **N**ames
        - **O**rdinal — **O**rder
        - **I**nterval — **I**ntervals equal
        - **R**atio — **R**atios meaningful
        
        **Increasing sophistication:** Nominal → Ordinal → Interval → Ratio
        
        - Each level has all properties of previous levels plus more
        - Higher level = more statistical options
        """)

# =============================================================================
# TAB 3: SCALING TECHNIQUES
# =============================================================================
with tab3:
    st.markdown("## ⚖️ Chapter 3: Scaling Techniques")
    
    st.markdown("### 3.1 What is Scaling?")
    
    col_def, col_purpose = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Scaling</b> is the process of measuring qualitative concepts (attitudes, perceptions) by assigning numbers according to rules, creating a meaningful scale.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_purpose:
        st.markdown("""
        **Purpose:**
        - Quantify abstract concepts
        - Enable statistical analysis
        - Compare across respondents
        - Track changes over time
        - Standardize measurement
        """)

    with st.expander("📊 Likert Scale", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Rensis Likert Scale</h4>
            <p style="margin: 0 !important; font-size: 13px;">Most popular scaling technique. Measures degree of agreement/disagreement with statements.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Example:** "I am satisfied with my job."
        
        | 1 | 2 | 3 | 4 | 5 |
        |---|---|---|---|---|
        | Strongly Disagree | Disagree | Neutral | Agree | Strongly Agree |
        
        **Variations:**
        - 5-point (most common)
        - 7-point (more granularity)
        - 4-point (forced choice, no neutral)
        - 10-point (fine discrimination)
        
        **Best Practices:**
        - Use consistent anchors
        - Include negatively-worded items (reverse scoring)
        - Label all points, not just endpoints
        - Consider forced choice (even number) vs. neutral option
        """)

    with st.expander("📋 Other Scaling Techniques", expanded=True):
        st.markdown("""
        | Technique | Description | Example |
        |-----------|-------------|---------|
        | **Semantic Differential** | Rate between opposite adjectives | Good ——— Bad |
        | **Thurstone Scale** | Items with assigned values | Equal-appearing intervals |
        | **Guttman Scale** | Cumulative scale | If agree with 3, also agree with 1,2 |
        | **Stapel Scale** | Unipolar, +5 to -5 | Rate how well word describes |
        | **Visual Analog Scale** | Mark on continuous line | Pain scale 0-100mm |
        | **Constant Sum** | Divide points among options | Allocate 100 points among features |
        | **Ranking** | Order preferences | Rank 1st, 2nd, 3rd |
        
        **Semantic Differential Example:**
        
        | Negative | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Positive |
        |----------|---|---|---|---|---|---|---|----------|
        | Slow | o | o | o | o | o | o | o | Fast |
        | Difficult | o | o | o | o | o | o | o | Easy |
        """)

    with st.expander("🔧 Questionnaire Validation Process", expanded=True):
        st.markdown("""
        **Steps to Validate a Questionnaire:**
        
        1. **Literature Review** — Ground items in theory
        2. **Item Generation** — Draft more items than needed
        3. **Expert Review** — Content validity check
        4. **Pilot Test** — Small sample trial
        5. **Exploratory Factor Analysis (EFA)** — Identify dimensions
        6. **Item Refinement** — Remove poor items
        7. **Confirmatory Factor Analysis (CFA)** — Confirm structure
        8. **Reliability Analysis** — Calculate Cronbach's Alpha
        9. **Validity Testing** — Convergent, discriminant validity
        """)

# =============================================================================
# TAB 4: SAMPLING METHODS
# =============================================================================
with tab4:
    st.markdown("## 🎯 Chapter 4: Sampling Methods")
    
    st.markdown("### 4.1 Basic Concepts")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Key Terms</h4>
            <p style="margin: 0 !important; font-size: 13px;">
            <b>Population:</b> Entire group of interest<br>
            <b>Sample:</b> Subset selected for study<br>
            <b>Sampling Frame:</b> List from which sample is drawn<br>
            <b>Sampling Error:</b> Difference between sample and population
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Soup Tasting</h4>
            <p style="margin: 0 !important; font-size: 13px;">You don't need to drink the whole pot to know if soup is good — one well-mixed spoonful tells you. That spoonful is your <b>sample</b>.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🎲 Probability Sampling", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Probability Sampling:</b> Every member of the population has a known, non-zero chance of being selected. Allows statistical generalization.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        | Type | Description | Best For | How |
        |------|-------------|----------|-----|
        | **Simple Random** | Each has equal chance | Homogeneous populations | Lottery, random numbers |
        | **Stratified** | Divide into groups, random from each | Heterogeneous with known subgroups | Proportional or equal allocation |
        | **Systematic** | Every kth member | When list is available | List → select every 10th, etc. |
        | **Cluster** | Randomly select groups, study all in selected | Geographically dispersed | Random villages → all households |
        | **Multi-stage** | Combine methods | Large, complex populations | Clusters → Strata → Random |
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Simple Random Sampling:**
            - Every member has equal probability
            - Use: Random number generator
            - Most basic probability method
            
            **Systematic Sampling:**
            - Select every kth element
            - k = Population size / Sample size
            - Easier than simple random
            """)
        with col2:
            st.markdown("""
            **Stratified Sampling:**
            - Divide population into strata
            - Sample from each stratum
            - Ensures representation
            
            **Cluster Sampling:**
            - Sample groups, not individuals
            - More practical, less precise
            - Good when no individual list
            """)

    with st.expander("🎯 Non-Probability Sampling", expanded=True):
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b; margin-bottom: 10px;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Non-Probability Sampling:</b> Selection based on subjective judgment. Cannot calculate sampling error or generalize statistically.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        | Type | Description | Best For |
        |------|-------------|----------|
        | **Convenience** | Whoever is available | Preliminary research, pilot studies |
        | **Purposive/Judgment** | Researcher selects based on criteria | Expert interviews, case studies |
        | **Quota** | Non-random selection meeting quotas | Surveys when stratified not possible |
        | **Snowball** | Referrals from initial participants | Hidden populations (drug users, etc.) |
        | **Volunteer** | Self-selected participants | When volunteers ethical requirement |
        """)

    with st.expander("📊 Sample Size Determination", expanded=True):
        st.markdown("""
        **Factors Affecting Sample Size:**
        
        | Factor | Effect |
        |--------|--------|
        | **Population size** | Larger population → may need larger sample |
        | **Desired precision** | More precision → larger sample |
        | **Confidence level** | Higher confidence → larger sample |
        | **Population variability** | More variability → larger sample |
        | **Resources** | Budget/time constraints |
        
        **Sample Size Formula (for proportions):**
        """)
        
        st.latex(r"n = \frac{Z^2 \times p \times (1-p)}{e^2}")
        
        st.markdown("""
        **Where:**
        - n = sample size
        - Z = Z-value for confidence level (1.96 for 95%)
        - p = expected proportion (use 0.5 if unknown)
        - e = margin of error (e.g., 0.05 for ±5%)
        
        **Quick Reference:**
        
        | Confidence | Margin of Error | p=0.5 | Sample Size |
        |------------|-----------------|-------|-------------|
        | 95% | ±5% | 0.5 | 385 |
        | 95% | ±3% | 0.5 | 1,067 |
        | 99% | ±5% | 0.5 | 666 |
        """)

    with st.expander("⚖️ Probability vs Non-Probability", expanded=True):
        st.markdown("""
        | Aspect | Probability | Non-Probability |
        |--------|-------------|-----------------|
        | **Selection** | Random | Subjective |
        | **Generalizability** | High | Limited |
        | **Sampling error** | Calculable | Unknown |
        | **Cost** | Higher | Lower |
        | **Feasibility** | Needs sampling frame | Easier |
        | **Use** | Quantitative research | Qualitative, exploratory |
        
        **When to Use Probability:**
        - Want to generalize to population
        - Need statistical precision
        - Have sampling frame available
        
        **When to Use Non-Probability:**
        - Exploratory/pilot research
        - Hard-to-reach populations
        - Budget/time constraints
        - Qualitative research
        """)

# Footer
show_footer()
