import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Statistical Foundations for Research | Hypothesis Testing, t-test, ANOVA, Chi-Square [2024]",
    description="Master statistical foundations for Ph.D. research: hypothesis design, parametric & non-parametric tests, z-test, t-test, ANOVA, Mann-Whitney U, Kruskal-Wallis, Chi-square with formulas and examples.",
    keywords=[
        "hypothesis testing",
        "null hypothesis",
        "t-test",
        "ANOVA",
        "chi-square test",
        "Mann-Whitney U test",
        "Kruskal-Wallis test",
        "parametric tests",
        "non-parametric tests",
        "degrees of freedom",
        "confidence interval",
        "z-test",
        "statistical significance",
        "p-value",
        "research statistics"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/statistics/foundations",
    reading_time=120,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Statistical Foundations", "url": "https://researchethics.dev/statistics/foundations"}
    ],
    course_info={
        "name": "Statistical Foundations for Research - Paper II Unit I",
        "description": "Comprehensive coverage of statistical foundations including hypothesis testing, parametric and non-parametric tests for Ph.D. research.",
        "level": "Doctoral",
        "prerequisites": "Basic mathematics",
        "teaches": ["Hypothesis Testing", "t-test", "ANOVA", "Chi-Square", "Non-parametric Tests"],
        "workload": "PT20H",
        "rating": "4.9",
        "rating_count": 723
    }
)
apply_custom_css()
show_top_nav(current_page="Statistical Foundations")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📐 Unit I: Statistical Foundations</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #1e40af;">Paper II: Statistics and Computer Applications — Building blocks of research data analysis.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Hypothesis Design",
    "📊 Parametric Tests",
    "📈 Non-Parametric Tests",
    "🔢 Chi-Square",
    "📋 Quick Reference"
])

# =============================================================================
# TAB 1: HYPOTHESIS DESIGN
# =============================================================================
with tab1:
    st.markdown("## 🎯 Chapter 1: Hypothesis Design")
    
    st.markdown("### 1.1 What is a Hypothesis?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Hypothesis</b> is a tentative statement about the relationship between two or more variables. It's a specific, testable prediction about what you expect to happen in your study.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Court Trial</h4>
            <p style="margin: 0 !important; font-size: 13px;">Think of hypothesis testing like a <b>court trial</b>. The defendant (null hypothesis) is innocent until proven guilty. You need sufficient evidence to reject innocence.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("⚖️ Null and Alternative Hypotheses", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">H₀: Null Hypothesis</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Statement of "no effect" or "no difference"<br>
                <b>Example:</b> "There is no difference in test scores between Group A and Group B"<br>
                <b>Role:</b> The hypothesis we try to reject
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fef2f2 0%, #fecaca 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">H₁ or Hₐ: Alternative Hypothesis</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>What:</b> Statement that there IS an effect or difference<br>
                <b>Example:</b> "Group A has higher scores than Group B"<br>
                <b>Role:</b> What we accept if we reject H₀
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **Types of Alternative Hypotheses:**
        
        | Type | Symbol | Example | When to Use |
        |------|--------|---------|-------------|
        | **Two-tailed** | H₁: μ₁ ≠ μ₂ | Scores are different | When direction is unknown |
        | **One-tailed (Right)** | H₁: μ₁ > μ₂ | Treatment increases scores | When you predict increase |
        | **One-tailed (Left)** | H₁: μ₁ < μ₂ | Treatment decreases time | When you predict decrease |
        """)

    with st.expander("🎚️ Degrees of Freedom (df)", expanded=True):
        col_def, col_ex = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
                <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Degrees of Freedom (df)</b> is the number of values in a calculation that are free to vary. It represents the amount of independent information available to estimate a parameter.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_ex:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">💡 Analogy: Seating at a Table</h4>
                <p style="margin: 0 !important; font-size: 13px;">If 4 people must sit at a table with 4 chairs, 3 can choose freely, but the 4th has no choice. df = 4 - 1 = 3.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **Common Degrees of Freedom Formulas:**
        
        | Test | Degrees of Freedom |
        |------|-------------------|
        | One-sample t-test | df = n - 1 |
        | Two-sample t-test (equal variance) | df = n₁ + n₂ - 2 |
        | Paired t-test | df = n - 1 (n = pairs) |
        | Chi-square test | df = (rows - 1) × (columns - 1) |
        | One-way ANOVA (between) | df = k - 1 (k = groups) |
        | One-way ANOVA (within) | df = N - k |
        """)

    with st.expander("📏 Confidence Intervals", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Confidence Interval (CI)</b> is a range of values that likely contains the true population parameter with a specified level of confidence (usually 95%).</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"\text{CI} = \bar{x} \pm z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}")
        
        st.markdown("""
        **Where:**
        - x̄ = sample mean
        - z_α/2 = critical z-value (1.96 for 95% CI)
        - σ = standard deviation
        - n = sample size
        
        **Interpretation:**
        > "We are 95% confident that the true population mean lies between [lower, upper]"
        
        **Common Confidence Levels:**
        | Confidence Level | z-value |
        |-----------------|---------|
        | 90% | 1.645 |
        | 95% | 1.96 |
        | 99% | 2.576 |
        """)

    with st.expander("📊 Type I and Type II Errors", expanded=False):
        st.markdown("""
        | Error Type | Description | Probability | Analogy |
        |------------|-------------|-------------|---------|
        | **Type I (α)** | Rejecting H₀ when it's true | α (usually 0.05) | Convicting an innocent person |
        | **Type II (β)** | Failing to reject H₀ when it's false | β | Letting a guilty person go free |
        
        **Power = 1 - β** (probability of correctly rejecting a false H₀)
        """)
        
        st.graphviz_chart("""
        digraph {
            rankdir=LR; 
            node [fontname="Arial", fontsize=11, shape=box, style="rounded,filled"];
            
            decision [label="Your Decision", fillcolor="#dbeafe", shape=ellipse];
            
            reject [label="Reject H₀", fillcolor="#fecaca"];
            accept [label="Fail to Reject H₀", fillcolor="#dcfce7"];
            
            type1 [label="Type I Error\\n(False Positive)\\nα = 0.05", fillcolor="#fca5a5"];
            correct1 [label="Correct!\\n(True Positive)", fillcolor="#86efac"];
            
            type2 [label="Type II Error\\n(False Negative)\\nβ", fillcolor="#fdba74"];
            correct2 [label="Correct!\\n(True Negative)", fillcolor="#86efac"];
            
            decision -> reject;
            decision -> accept;
        }
        """)

# =============================================================================
# TAB 2: PARAMETRIC TESTS
# =============================================================================
with tab2:
    st.markdown("## 📊 Chapter 2: Parametric Tests")
    
    st.markdown("""
    <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb; margin-bottom: 15px;">
        <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 What are Parametric Tests?</h4>
        <p style="margin: 0 !important; font-size: 13px;"><b>Parametric tests</b> make assumptions about population parameters (e.g., normal distribution, equal variances). They are more powerful but require assumptions to be met.</p>
    </div>
    """, unsafe_allow_html=True)

    # z-test
    st.markdown("### 2.1 z-Test")
    
    with st.expander("📐 z-Test", expanded=True):
        col_def, col_use = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a;">
                <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>z-Test</b> is used to compare sample mean to population mean when population standard deviation (σ) is known AND sample size is large (n ≥ 30).</p>
            </div>
            """, unsafe_allow_html=True)
        with col_use:
            st.markdown("""
            **When to Use:**
            - Population σ is known
            - n ≥ 30 (large sample)
            - Data approximately normal
            
            **Types:**
            - One-sample z-test
            - Two-sample z-test
            - z-test for proportions
            """)
        
        st.markdown("**Formula (One-sample z-test):**")
        st.latex(r"z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}")
        
        st.markdown("""
        **Where:**
        - x̄ = sample mean
        - μ₀ = hypothesized population mean
        - σ = population standard deviation
        - n = sample size
        
        **Decision Rule:** If |z| > z_critical (1.96 for α=0.05, two-tailed), reject H₀
        """)

    # t-test
    st.markdown("### 2.2 t-Test")
    
    with st.expander("📐 t-Test (Student's t-Test)", expanded=True):
        col_def, col_analogy = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
                <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>t-Test</b> compares means when population σ is unknown (using sample s instead). Used for small samples or when σ is not known.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_analogy:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">💡 Analogy</h4>
                <p style="margin: 0 !important; font-size: 13px;">z-test is like measuring with a ruler you know is accurate. t-test is like measuring with a ruler where even the ruler has some uncertainty.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("**Types of t-Tests:**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">One-Sample t-Test</h4>
                <p style="margin: 0 !important; font-size: 12px;">Compares sample mean to known value</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">Independent t-Test</h4>
                <p style="margin: 0 !important; font-size: 12px;">Compares means of two separate groups</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); padding: 12px; border-radius: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">Paired t-Test</h4>
                <p style="margin: 0 !important; font-size: 12px;">Compares two measurements on same subjects</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("**Formulas:**")
        
        st.markdown("*One-Sample t-Test:*")
        st.latex(r"t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}, \quad df = n - 1")
        
        st.markdown("*Independent Samples t-Test (pooled):*")
        st.latex(r"t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \quad s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}")
        
        st.markdown("*Paired t-Test:*")
        st.latex(r"t = \frac{\bar{d}}{s_d / \sqrt{n}}, \quad \text{where } d = \text{differences}")

    # ANOVA
    st.markdown("### 2.3 ANOVA (Analysis of Variance)")
    
    with st.expander("📐 ANOVA", expanded=True):
        col_def, col_analogy = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #fff7ed; padding: 14px; border-radius: 8px; border-left: 4px solid #f97316;">
                <h4 style="color: #ea580c; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>ANOVA</b> (Analysis of Variance) tests whether there are significant differences between the means of three or more groups.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_analogy:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">💡 Analogy</h4>
                <p style="margin: 0 !important; font-size: 13px;">ANOVA is like checking if different fertilizers produce different plant heights. It tells you IF there's a difference, but not WHICH specific fertilizers differ.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        **Why not multiple t-tests?**
        - Multiple comparisons inflate Type I error
        - With 5 groups, you'd need 10 comparisons
        - ANOVA controls overall error rate
        """)
        
        st.markdown("**ANOVA Table:**")
        st.markdown("""
        | Source | Sum of Squares | df | Mean Square | F |
        |--------|---------------|----|--------------|----|
        | Between Groups | SS_B | k - 1 | MS_B = SS_B/(k-1) | MS_B/MS_W |
        | Within Groups | SS_W | N - k | MS_W = SS_W/(N-k) | |
        | Total | SS_T | N - 1 | | |
        """)
        
        st.markdown("**F-Statistic:**")
        st.latex(r"F = \frac{MS_{Between}}{MS_{Within}} = \frac{\text{Variance between groups}}{\text{Variance within groups}}")
        
        st.markdown("""
        **Interpretation:**
        - Large F → Groups are different
        - F ≈ 1 → Groups are similar
        - If p < α (0.05), reject H₀ (at least one group differs)
        
        **Post-hoc Tests (after significant ANOVA):**
        - Tukey's HSD
        - Bonferroni correction
        - Scheffé's test
        """)

# =============================================================================
# TAB 3: NON-PARAMETRIC TESTS
# =============================================================================
with tab3:
    st.markdown("## 📈 Chapter 3: Non-Parametric Tests")
    
    st.markdown("""
    <div style="background: #faf5ff; padding: 14px; border-radius: 8px; border-left: 4px solid #7c3aed; margin-bottom: 15px;">
        <h4 style="color: #6d28d9; margin: 0 0 8px 0 !important;">📖 What are Non-Parametric Tests?</h4>
        <p style="margin: 0 !important; font-size: 13px;"><b>Non-parametric tests</b> (distribution-free tests) don't assume normal distribution. Use when: data is ordinal, distribution is skewed, sample is small, or assumptions are violated.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 Parametric vs Non-Parametric", expanded=True):
        st.markdown("""
        | Parametric Test | Non-Parametric Equivalent | Use Non-Parametric When |
        |-----------------|---------------------------|-------------------------|
        | One-sample t-test | Wilcoxon Signed-Rank | Data not normal |
        | Independent t-test | Mann-Whitney U | Ordinal data or non-normal |
        | Paired t-test | Wilcoxon Signed-Rank (paired) | Ordinal differences |
        | One-way ANOVA | Kruskal-Wallis | 3+ groups, non-normal |
        | Pearson correlation | Spearman's rho | Ordinal or non-linear |
        """)

    # Kolmogorov-Smirnov Test
    st.markdown("### 3.1 Kolmogorov-Smirnov Test")
    
    with st.expander("📐 Kolmogorov-Smirnov (K-S) Test", expanded=True):
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb; margin-bottom: 10px;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Kolmogorov-Smirnov Test</b> compares the cumulative distribution function (CDF) of a sample with a reference distribution (usually normal) to test for goodness of fit.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Purpose:** Test if data follows a specific distribution (commonly used to test normality)
        
        **Hypotheses:**
        - H₀: Sample comes from the specified distribution
        - H₁: Sample does not come from the specified distribution
        """)
        
        st.latex(r"D = \max |F_n(x) - F(x)|")
        
        st.markdown("""
        **Where:**
        - Fₙ(x) = empirical (sample) CDF
        - F(x) = theoretical CDF
        - D = maximum absolute difference
        
        **Decision:** If D > D_critical, reject H₀
        """)

    # Run Test
    with st.expander("🏃 Run Test (Wald-Wolfowitz)", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Run Test</b> tests whether a sequence of data is random. A "run" is a sequence of identical symbols (e.g., + + + or - - -).</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Example:** Sequence + + - - - + - + + +
        - Run 1: + +
        - Run 2: - - -
        - Run 3: +
        - Run 4: -
        - Run 5: + + +
        - **Total runs = 5**
        
        **Test Statistic:**
        """)
        st.latex(r"z = \frac{R - \mu_R}{\sigma_R}")
        
        st.markdown("""
        Where:
        - R = observed number of runs
        - μᵣ = expected runs = (2n₁n₂)/(n₁+n₂) + 1
        - σᵣ = standard deviation of runs
        
        **Interpretation:**
        - Too few runs → Clustering (pattern)
        - Too many runs → Systematic alternation
        """)

    # Mann-Whitney U Test
    st.markdown("### 3.2 Mann-Whitney U Test")
    
    with st.expander("📐 Mann-Whitney U Test", expanded=True):
        col_def, col_analogy = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #fff7ed; padding: 14px; border-radius: 8px; border-left: 4px solid #f97316;">
                <h4 style="color: #ea580c; margin: 0 0 8px 0 !important;">📖 Definition</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>Mann-Whitney U Test</b> is the non-parametric equivalent of the independent samples t-test. It compares two independent groups using ranks.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_analogy:
            st.markdown("""
            <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <h4 style="color: #b45309; margin: 0 0 8px 0 !important;">💡 When to Use</h4>
                <p style="margin: 0 !important; font-size: 13px;">Use when comparing two groups but data is ordinal, not normal, or has extreme outliers.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("**Calculation Steps:**")
        st.markdown("""
        1. Combine all scores and rank them (1 = smallest)
        2. Sum ranks for each group (R₁, R₂)
        3. Calculate U for each group
        """)
        
        st.latex(r"U_1 = n_1 n_2 + \frac{n_1(n_1+1)}{2} - R_1")
        st.latex(r"U_2 = n_1 n_2 + \frac{n_2(n_2+1)}{2} - R_2")
        
        st.markdown("**Note:** Use the smaller U value; compare to critical value from U-table")

    # Kruskal-Wallis Test
    st.markdown("### 3.3 Kruskal-Wallis Test")
    
    with st.expander("📐 Kruskal-Wallis H Test", expanded=True):
        st.markdown("""
        <div style="background: #faf5ff; padding: 14px; border-radius: 8px; border-left: 4px solid #7c3aed; margin-bottom: 10px;">
            <h4 style="color: #6d28d9; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Kruskal-Wallis Test</b> is the non-parametric equivalent of one-way ANOVA. It compares three or more independent groups using ranks.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**H Statistic:**")
        st.latex(r"H = \frac{12}{N(N+1)} \sum_{i=1}^{k} \frac{R_i^2}{n_i} - 3(N+1)")
        
        st.markdown("""
        **Where:**
        - N = total sample size
        - k = number of groups
        - nᵢ = size of group i
        - Rᵢ = sum of ranks in group i
        
        **Distribution:** H follows chi-square distribution with df = k - 1
        
        **Post-hoc:** If significant, use Dunn's test for pairwise comparisons
        """)

# =============================================================================
# TAB 4: CHI-SQUARE TEST
# =============================================================================
with tab4:
    st.markdown("## 🔢 Chapter 4: Chi-Square (χ²) Test")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Chi-Square (χ²) Test</b> is used to analyze categorical (frequency) data. It tests whether observed frequencies differ significantly from expected frequencies.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Dice Fairness</h4>
            <p style="margin: 0 !important; font-size: 13px;">Testing if a die is fair: Expected = each face 1/6 of time. Chi-square tests if your observed rolls match this expectation.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📊 Types of Chi-Square Tests", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">Goodness-of-Fit Test</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Purpose:</b> Does sample match expected distribution?<br>
                <b>Example:</b> Are colors equally preferred?<br>
                <b>df:</b> k - 1 (k = categories)
                </p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 12px; border-radius: 8px; margin-bottom: 8px;">
                <h4 style="margin: 0 0 5px 0 !important;">Test of Independence</h4>
                <p style="margin: 0 !important; font-size: 13px;">
                <b>Purpose:</b> Are two categorical variables related?<br>
                <b>Example:</b> Is gender related to product preference?<br>
                <b>df:</b> (rows-1) × (columns-1)
                </p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("🧮 Chi-Square Formula", expanded=True):
        st.latex(r"\chi^2 = \sum \frac{(O - E)^2}{E}")
        
        st.markdown("""
        **Where:**
        - O = Observed frequency
        - E = Expected frequency
        
        **For Test of Independence:**
        """)
        st.latex(r"E_{ij} = \frac{(\text{Row Total}_i) \times (\text{Column Total}_j)}{\text{Grand Total}}")
        
        st.markdown("""
        **Example Calculation:**
        
        |  | Prefer A | Prefer B | Total |
        |--|----------|----------|-------|
        | Male | 30 | 20 | 50 |
        | Female | 25 | 35 | 60 |
        | Total | 55 | 55 | 110 |
        
        Expected for Male-A: (50 × 55) / 110 = 25
        
        χ² contribution: (30-25)²/25 = 1.0
        
        (Calculate for all cells and sum)
        """)

    with st.expander("⚠️ Assumptions and Limitations", expanded=False):
        st.markdown("""
        **Assumptions:**
        1. Data is categorical (counts/frequencies)
        2. Observations are independent
        3. Expected frequency ≥ 5 in each cell (if not, use Fisher's exact test)
        4. Mutually exclusive categories
        
        **Effect Size:** Cramér's V or Phi (φ) for strength of association
        """)
        
        st.latex(r"\phi = \sqrt{\frac{\chi^2}{n}} \quad \text{(for 2×2 tables)}")

# =============================================================================
# TAB 5: QUICK REFERENCE
# =============================================================================
with tab5:
    st.markdown("## 📋 Quick Reference: Choosing the Right Test")
    
    with st.expander("🔍 Test Selection Flowchart", expanded=True):
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=10, shape=box, style="rounded,filled"];
            
            start [label="What type of data?", fillcolor="#dbeafe", shape=diamond];
            
            cat [label="Categorical\\n(Counts)", fillcolor="#fef3c7"];
            cont [label="Continuous\\n(Measurements)", fillcolor="#dcfce7"];
            
            chisq [label="Chi-Square Test", fillcolor="#fed7aa"];
            
            normal [label="Data Normal?", fillcolor="#f3e8ff", shape=diamond];
            
            yes [label="Parametric Tests", fillcolor="#86efac"];
            no [label="Non-Parametric Tests", fillcolor="#fca5a5"];
            
            groups [label="How many groups?", fillcolor="#dbeafe", shape=diamond];
            
            one [label="1 group:\\nOne-sample t-test", fillcolor="#bfdbfe"];
            two [label="2 groups:\\nt-test", fillcolor="#bfdbfe"];
            more [label="3+ groups:\\nANOVA", fillcolor="#bfdbfe"];
            
            start -> cat -> chisq;
            start -> cont -> normal;
            normal -> yes [label="Yes"];
            normal -> no [label="No"];
            yes -> groups;
            groups -> one [label="1"];
            groups -> two [label="2"];
            groups -> more [label="3+"];
        }
        """)

    with st.expander("📊 Complete Test Summary Table", expanded=True):
        st.markdown("""
        | Objective | Parametric | Non-Parametric |
        |-----------|------------|----------------|
        | Compare 1 group to value | One-sample t-test | Wilcoxon Signed-Rank |
        | Compare 2 independent groups | Independent t-test | Mann-Whitney U |
        | Compare 2 related groups | Paired t-test | Wilcoxon Signed-Rank |
        | Compare 3+ independent groups | One-way ANOVA | Kruskal-Wallis |
        | Compare 3+ related groups | Repeated Measures ANOVA | Friedman Test |
        | Association (2 continuous) | Pearson r | Spearman ρ |
        | Association (2 categorical) | — | Chi-Square |
        | Test normality | — | K-S Test, Shapiro-Wilk |
        | Test randomness | — | Run Test |
        """)

    with st.expander("📝 Key Formulas Summary", expanded=True):
        st.markdown("**Central Tendency & Variability:**")
        st.latex(r"\bar{x} = \frac{\sum x_i}{n}, \quad s = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n-1}}")
        
        st.markdown("**Standard Error of Mean:**")
        st.latex(r"SE = \frac{s}{\sqrt{n}}")
        
        st.markdown("**z-score:**")
        st.latex(r"z = \frac{x - \mu}{\sigma}")
        
        st.markdown("**t-statistic:**")
        st.latex(r"t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}")
        
        st.markdown("**F-statistic (ANOVA):**")
        st.latex(r"F = \frac{MS_{Between}}{MS_{Within}}")
        
        st.markdown("**Chi-Square:**")
        st.latex(r"\chi^2 = \sum \frac{(O-E)^2}{E}")

# Footer
show_footer()
