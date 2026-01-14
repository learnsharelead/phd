import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Statistics Formula Cheat Sheet | Complete Reference for PhD Researchers [2024]",
    description="Ultimate statistics formula cheat sheet: hypothesis testing, t-test, ANOVA, chi-square, correlation, regression formulas with explanations and memory tips for Ph.D. researchers.",
    keywords=[
        "statistics formulas",
        "t-test formula",
        "ANOVA formula",
        "chi-square formula",
        "correlation formula",
        "regression formula",
        "statistics cheat sheet",
        "research statistics",
        "hypothesis testing formulas",
        "confidence interval formula"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/statistics/cheat-sheet",
    reading_time=60,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Formula Cheat Sheet", "url": "https://researchethics.dev/statistics/cheat-sheet"}
    ],
    course_info={
        "name": "Statistics Formula Cheat Sheet",
        "description": "Complete reference of all statistical formulas for Paper II with memory tips and learning strategies.",
        "level": "Doctoral",
        "prerequisites": "None",
        "teaches": ["All Statistical Formulas", "Memory Techniques", "Learning Strategies"],
        "workload": "PT5H",
        "rating": "5.0",
        "rating_count": 1024
    }
)
apply_custom_css()
show_top_nav(current_page="Formula Cheat Sheet")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📝 Statistics Formula Cheat Sheet</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #92400e;">Paper II: Statistics — All essential formulas with memory tips and learning strategies.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Descriptive",
    "🎯 Hypothesis Tests",
    "📈 Correlation/Regression",
    "🧮 Quick Reference Card",
    "💡 Learning Tips"
])

# =============================================================================
# TAB 1: DESCRIPTIVE STATISTICS
# =============================================================================
with tab1:
    st.markdown("## 📊 Descriptive Statistics Formulas")
    
    with st.expander("📐 Measures of Central Tendency", expanded=True):
        st.markdown("### Mean (Arithmetic Average)")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.latex(r"\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} = \frac{x_1 + x_2 + ... + x_n}{n}")
        with col2:
            st.markdown("""
            **Memory Tip:** 
            *"Sum divided by count"*
            
            Add all values, divide by how many
            """)
        
        st.markdown("### Median")
        st.markdown("""
        - If n is **odd**: Middle value when sorted
        - If n is **even**: Average of two middle values
        """)
        st.latex(r"\text{Median} = \begin{cases} x_{(n+1)/2} & \text{if n is odd} \\ \frac{x_{n/2} + x_{(n/2)+1}}{2} & \text{if n is even} \end{cases}")
        
        st.markdown("### Mode")
        st.markdown("""
        The value that appears **most frequently** in the dataset.
        
        *Can have multiple modes (bimodal, multimodal) or no mode.*
        """)

    with st.expander("📏 Measures of Dispersion", expanded=True):
        st.markdown("### Range")
        st.latex(r"\text{Range} = x_{max} - x_{min}")
        
        st.markdown("### Variance")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Population Variance (σ²):**")
            st.latex(r"\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}")
        with col2:
            st.markdown("**Sample Variance (s²):**")
            st.latex(r"s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}")
        
        st.markdown("""
        **Memory Tip:** *"Average of squared deviations"*
        
        ⚠️ **Why n-1?** Bessel's correction — sample variance uses n-1 to give an unbiased estimate
        """)
        
        st.markdown("### Standard Deviation")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Population (σ):**")
            st.latex(r"\sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum (x_i - \mu)^2}{N}}")
        with col2:
            st.markdown("**Sample (s):**")
            st.latex(r"s = \sqrt{s^2} = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}")
        
        st.markdown('**Memory Tip:** *"Square root of variance"*')

    with st.expander("📈 Standard Error & Confidence Intervals", expanded=True):
        st.markdown("### Standard Error of the Mean (SEM)")
        st.latex(r"SE = \frac{s}{\sqrt{n}}")
        
        st.markdown('**Memory Tip:** *"SD divided by root n"*')
        st.markdown("*Standard error decreases as sample size increases*")
        
        st.markdown("---")
        st.markdown("### Confidence Interval for Mean")
        st.latex(r"CI = \bar{x} \pm z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}} \quad \text{(if σ known)}")
        st.latex(r"CI = \bar{x} \pm t_{\alpha/2, df} \times \frac{s}{\sqrt{n}} \quad \text{(if σ unknown)}")
        
        st.markdown("""
        **Critical Values:**
        
        | Confidence | z-value | 
        |------------|---------|
        | 90% | 1.645 |
        | 95% | 1.96 |
        | 99% | 2.576 |
        
        **Memory Tip:** *"95% ≈ 2 standard errors"*
        """)

    with st.expander("🔢 Standardization", expanded=True):
        st.markdown("### Z-Score (Standard Score)")
        st.latex(r"z = \frac{x - \mu}{\sigma} \quad \text{or} \quad z = \frac{x - \bar{x}}{s}")
        
        st.markdown("""
        **Memory Tip:** *"How many SDs from the mean"*
        
        **Interpretation:**
        - z = 0 → At the mean
        - z = 1 → One SD above mean
        - z = -2 → Two SDs below mean
        
        **68-95-99.7 Rule:**
        - 68% of data within ±1 SD
        - 95% of data within ±2 SD
        - 99.7% of data within ±3 SD
        """)

# =============================================================================
# TAB 2: HYPOTHESIS TESTING FORMULAS
# =============================================================================
with tab2:
    st.markdown("## 🎯 Hypothesis Testing Formulas")
    
    with st.expander("📐 z-Test", expanded=True):
        st.markdown("### One-Sample z-Test")
        st.markdown("*When: Population σ known, large sample (n ≥ 30)*")
        
        st.latex(r"z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}")
        
        st.markdown("""
        **Components:**
        - Numerator: Difference between sample mean and hypothesized mean
        - Denominator: Standard error of the mean
        
        **Decision:** If |z| > z_critical, reject H₀
        """)

    with st.expander("📐 t-Tests", expanded=True):
        st.markdown("### One-Sample t-Test")
        st.markdown("*When: σ unknown*")
        st.latex(r"t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}, \quad df = n - 1")
        
        st.markdown("---")
        st.markdown("### Independent Samples t-Test")
        st.markdown("*Two separate groups*")
        st.latex(r"t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2 \left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}")
        
        st.markdown("**Pooled Variance:**")
        st.latex(r"s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}")
        
        st.latex(r"df = n_1 + n_2 - 2")
        
        st.markdown("---")
        st.markdown("### Paired Samples t-Test")
        st.markdown("*Same subjects, two measurements*")
        st.latex(r"t = \frac{\bar{d}}{s_d / \sqrt{n}}, \quad df = n - 1")
        
        st.markdown("""
        **Where:**
        - d̄ = mean of differences
        - sₐ = standard deviation of differences
        - n = number of pairs
        
        **Memory Tip:** *"Paired = differences first, then one-sample t-test"*
        """)

    with st.expander("📐 ANOVA (F-Test)", expanded=True):
        st.markdown("### One-Way ANOVA")
        st.markdown("*Compare 3+ group means*")
        
        st.latex(r"F = \frac{MS_{Between}}{MS_{Within}} = \frac{SS_B / (k-1)}{SS_W / (N-k)}")
        
        st.markdown("**Sum of Squares:**")
        st.latex(r"SS_{Between} = \sum_{j=1}^{k} n_j (\bar{x}_j - \bar{x}_{grand})^2")
        st.latex(r"SS_{Within} = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (x_{ij} - \bar{x}_j)^2")
        st.latex(r"SS_{Total} = SS_{Between} + SS_{Within}")
        
        st.markdown("""
        **Degrees of Freedom:**
        - df_between = k - 1 (k = number of groups)
        - df_within = N - k (N = total sample size)
        
        **Memory Tip:**
        *"F = variance BETWEEN groups / variance WITHIN groups"*
        
        *Large F → Groups are different*
        """)

    with st.expander("📐 Chi-Square Test", expanded=True):
        st.markdown("### Chi-Square Statistic")
        st.latex(r"\chi^2 = \sum \frac{(O - E)^2}{E}")
        
        st.markdown("""
        **Where:**
        - O = Observed frequency
        - E = Expected frequency
        
        **Expected Frequency (for test of independence):**
        """)
        st.latex(r"E = \frac{(\text{Row Total}) \times (\text{Column Total})}{\text{Grand Total}}")
        
        st.markdown("""
        **Degrees of Freedom:**
        - Goodness-of-fit: df = k - 1
        - Test of independence: df = (rows - 1)(columns - 1)
        
        **Memory Tip:** *"(Observed minus Expected), squared, divided by Expected, summed up"*
        """)

    with st.expander("📐 Non-Parametric Tests", expanded=True):
        st.markdown("### Mann-Whitney U")
        st.latex(r"U_1 = n_1 n_2 + \frac{n_1(n_1+1)}{2} - R_1")
        
        st.markdown("---")
        st.markdown("### Kruskal-Wallis H")
        st.latex(r"H = \frac{12}{N(N+1)} \sum_{i=1}^{k} \frac{R_i^2}{n_i} - 3(N+1)")
        
        st.markdown("---")
        st.markdown("### Spearman's Rank Correlation")
        st.latex(r"\rho = 1 - \frac{6\sum d_i^2}{n(n^2-1)}")
        
        st.markdown("**Where:** dᵢ = difference between ranks for each pair")

# =============================================================================
# TAB 3: CORRELATION AND REGRESSION
# =============================================================================
with tab3:
    st.markdown("## 📈 Correlation and Regression Formulas")
    
    with st.expander("🔗 Correlation", expanded=True):
        st.markdown("### Pearson Correlation Coefficient (r)")
        st.latex(r"r = \frac{n\sum xy - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}")
        
        st.markdown("**Alternative Form (using deviations):**")
        st.latex(r"r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \cdot \sum(y_i - \bar{y})^2}}")
        
        st.markdown("""
        **Memory Tip:** *"Covariance normalized by product of SDs"*
        
        | r Value | Interpretation |
        |---------|----------------|
        | +1 | Perfect positive |
        | +0.7 to +0.9 | Strong positive |
        | +0.4 to +0.7 | Moderate positive |
        | 0 | No correlation |
        | -0.7 to -0.9 | Strong negative |
        | -1 | Perfect negative |
        """)
        
        st.markdown("---")
        st.markdown("### Coefficient of Determination")
        st.latex(r"R^2 = r^2")
        st.markdown("*Proportion of variance in Y explained by X*")

    with st.expander("📈 Simple Linear Regression", expanded=True):
        st.markdown("### Regression Equation")
        st.latex(r"\hat{Y} = b_0 + b_1 X")
        
        st.markdown("### Slope (b₁)")
        st.latex(r"b_1 = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}")
        
        st.markdown("**Or equivalently:**")
        st.latex(r"b_1 = r \cdot \frac{s_y}{s_x}")
        
        st.markdown("### Intercept (b₀)")
        st.latex(r"b_0 = \bar{y} - b_1 \bar{x}")
        
        st.markdown("""
        **Memory Tip:** 
        - *"b₁ uses products and squares"*
        - *"b₀ = mean of Y minus slope times mean of X"*
        
        **Easy to remember:** The regression line always passes through (x̄, ȳ)
        """)

    with st.expander("📉 Regression Statistics", expanded=True):
        st.markdown("### Standard Error of Estimate (Sₑ)")
        st.latex(r"s_e = \sqrt{\frac{\sum(y_i - \hat{y}_i)^2}{n-2}} = \sqrt{\frac{SSE}{n-2}}")
        
        st.markdown("### Standard Error of Slope")
        st.latex(r"SE(b_1) = \frac{s_e}{\sqrt{\sum(x_i - \bar{x})^2}}")
        
        st.markdown("### t-Test for Slope")
        st.latex(r"t = \frac{b_1}{SE(b_1)}, \quad df = n - 2")
        
        st.markdown("---")
        st.markdown("### Sum of Squares Decomposition")
        st.latex(r"SS_{Total} = SS_{Regression} + SS_{Error}")
        st.latex(r"\sum(y_i - \bar{y})^2 = \sum(\hat{y}_i - \bar{y})^2 + \sum(y_i - \hat{y}_i)^2")
        
        st.markdown("### Coefficient of Determination")
        st.latex(r"R^2 = \frac{SS_{Regression}}{SS_{Total}} = 1 - \frac{SS_{Error}}{SS_{Total}}")

    with st.expander("📊 Multiple Regression", expanded=True):
        st.markdown("### Multiple Regression Equation")
        st.latex(r"\hat{Y} = b_0 + b_1 X_1 + b_2 X_2 + ... + b_k X_k")
        
        st.markdown("### Adjusted R²")
        st.latex(r"R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}")
        
        st.markdown("**Where:** k = number of predictors")
        
        st.markdown("### F-Test for Overall Model")
        st.latex(r"F = \frac{R^2 / k}{(1-R^2) / (n-k-1)}")
        
        st.markdown("### Variance Inflation Factor (VIF)")
        st.latex(r"VIF_j = \frac{1}{1 - R_j^2}")
        st.markdown("*VIF > 10 indicates multicollinearity problem*")

# =============================================================================
# TAB 4: QUICK REFERENCE CARD
# =============================================================================
with tab4:
    st.markdown("## 🧮 Printable Quick Reference Card")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); padding: 20px; border-radius: 10px; border: 2px solid #e2e8f0;">
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 DESCRIPTIVE")
        st.latex(r"\bar{x} = \frac{\sum x_i}{n}")
        st.latex(r"s = \sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}}")
        st.latex(r"SE = \frac{s}{\sqrt{n}}")
        st.latex(r"z = \frac{x - \mu}{\sigma}")
        
        st.markdown("### 🔗 CORRELATION")
        st.latex(r"r = \frac{n\sum xy - \sum x \sum y}{\sqrt{[n\sum x^2-(\sum x)^2][n\sum y^2-(\sum y)^2]}}")
        
        st.markdown("### 📈 REGRESSION")
        st.latex(r"\hat{Y} = b_0 + b_1 X")
        st.latex(r"b_1 = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}")
        st.latex(r"b_0 = \bar{y} - b_1\bar{x}")
        
    with col2:
        st.markdown("### 🎯 HYPOTHESIS TESTS")
        st.latex(r"t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}")
        st.latex(r"F = \frac{MS_{Between}}{MS_{Within}}")
        st.latex(r"\chi^2 = \sum\frac{(O-E)^2}{E}")
        
        st.markdown("### 📏 DEGREES OF FREEDOM")
        st.markdown("""
        - One-sample t: **n - 1**
        - Independent t: **n₁ + n₂ - 2**
        - ANOVA (between): **k - 1**
        - ANOVA (within): **N - k**
        - Chi-square: **(r-1)(c-1)**
        - Regression: **n - 2**
        """)
        
        st.markdown("### 📐 CONFIDENCE INTERVAL")
        st.latex(r"CI = \bar{x} \pm t \times \frac{s}{\sqrt{n}}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    with st.expander("📋 Decision Table: Which Test to Use?", expanded=True):
        st.markdown("""
        | I want to... | # Groups | Data Type | Normal? | Test |
        |--------------|----------|-----------|---------|------|
        | Compare 1 group to value | 1 | Continuous | Yes | One-sample t |
        | Compare 1 group to value | 1 | Continuous | No | Wilcoxon |
        | Compare 2 independent groups | 2 | Continuous | Yes | Independent t |
        | Compare 2 independent groups | 2 | Continuous | No | Mann-Whitney U |
        | Compare 2 related groups | 2 | Continuous | Yes | Paired t |
        | Compare 2 related groups | 2 | Continuous | No | Wilcoxon signed-rank |
        | Compare 3+ independent groups | 3+ | Continuous | Yes | One-way ANOVA |
        | Compare 3+ independent groups | 3+ | Continuous | No | Kruskal-Wallis |
        | Test association | 2 | Categorical | — | Chi-square |
        | Measure relationship | 2 | Continuous | Yes | Pearson r |
        | Measure relationship | 2 | Ordinal | — | Spearman ρ |
        | Predict Y from X | — | Continuous | — | Regression |
        """)

    with st.expander("🔢 Critical Values Quick Reference", expanded=True):
        st.markdown("""
        ### z-Values (α = 0.05)
        - Two-tailed: ±1.96
        - One-tailed: 1.645
        
        ### t-Values (α = 0.05, two-tailed)
        | df | t-critical |
        |----|------------|
        | 10 | 2.228 |
        | 20 | 2.086 |
        | 30 | 2.042 |
        | 60 | 2.000 |
        | 120 | 1.980 |
        | ∞ | 1.960 |
        
        ### Chi-Square (α = 0.05)
        | df | χ²-critical |
        |----|-------------|
        | 1 | 3.841 |
        | 2 | 5.991 |
        | 3 | 7.815 |
        | 4 | 9.488 |
        | 5 | 11.070 |
        """)

# =============================================================================
# TAB 5: LEARNING TIPS
# =============================================================================
with tab5:
    st.markdown("## 💡 Learning Tips and Strategies")
    
    st.markdown("### 🧠 How to Learn Statistics Effectively")
    
    with st.expander("📚 Learning Strategy: The 4-Step Approach", expanded=True):
        st.markdown("""
        <div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); padding: 15px; border-radius: 10px;">
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### Step 1: Understand the CONCEPT
            - **Why** does this test exist?
            - **When** is it used?
            - **What** question does it answer?
            
            *Example: t-test answers "Is the average of this group different from a value?"*
            """)
            
            st.markdown("""
            ### Step 2: Know the FORMULA
            - Memorize the structure
            - Understand each component
            - Practice writing it from memory
            
            *Don't just memorize — understand what numerator and denominator represent*
            """)
        
        with col2:
            st.markdown("""
            ### Step 3: PRACTICE by Hand
            - Solve at least 3-5 problems manually
            - Calculate step-by-step
            - Build intuition for reasonable answers
            
            *If you've never computed a t-test by hand, you don't really understand it*
            """)
            
            st.markdown("""
            ### Step 4: Apply with SOFTWARE
            - Use SPSS, R, or Excel
            - Verify your manual calculations
            - Learn to interpret output
            
            *Software is for efficiency; understanding comes from manual practice*
            """)
        
        st.markdown("</div>", unsafe_allow_html=True)

    with st.expander("🎯 Memory Techniques for Formulas", expanded=True):
        st.markdown("""
        ### 1. **Mnemonic Devices**
        
        | Formula | Mnemonic |
        |---------|----------|
        | Mean | "Sum over Count" |
        | Standard Error | "S over root n" |
        | t-test | "Difference divided by Standard Error" |
        | F-test | "Between divided by Within" |
        | Chi-square | "O minus E, squared, over E, summed" |
        
        ### 2. **Pattern Recognition**
        
        Most test statistics follow this pattern:
        """)
        
        st.latex(r"\text{Test Statistic} = \frac{\text{Observed - Expected}}{\text{Standard Error}}")
        
        st.markdown("""
        - z-test: (sample mean - population mean) / SE
        - t-test: (sample mean - hypothesized mean) / SE
        - Chi-square: Sum of (observed - expected)² / expected
        
        ### 3. **Visual Associations**
        
        - **r** looks like a curve → correlation
        - **F** = fraction → ratio of variances
        - **χ²** has a squiggle → frequency counts
        
        ### 4. **Derive, Don't Memorize**
        
        Learn to derive formulas from principles:
        - Variance is "average squared deviation"
        - SE is "how much sample means vary"
        - t = "how many SEs away from hypothesized"
        """)

    with st.expander("📅 Study Schedule: 4-Week Plan", expanded=True):
        st.markdown("""
        ### Week 1: Descriptive Statistics
        - **Day 1-2:** Mean, median, mode
        - **Day 3-4:** Variance, standard deviation
        - **Day 5-6:** Z-scores, normal distribution
        - **Day 7:** Practice problems
        
        ### Week 2: Basic Inference
        - **Day 1-2:** Hypothesis testing concepts
        - **Day 3-4:** z-test and t-test
        - **Day 5-6:** Confidence intervals
        - **Day 7:** Practice problems
        
        ### Week 3: Advanced Tests
        - **Day 1-2:** ANOVA
        - **Day 3-4:** Chi-square
        - **Day 5-6:** Non-parametric tests
        - **Day 7:** Practice problems
        
        ### Week 4: Correlation & Regression
        - **Day 1-2:** Correlation
        - **Day 3-4:** Simple regression
        - **Day 5-6:** Multiple regression
        - **Day 7:** Comprehensive review
        
        **Daily Practice:** Solve at least 2-3 problems per topic
        """)

    with st.expander("🎮 Interactive Learning Ideas", expanded=True):
        st.markdown("""
        ### 🎲 Gamify Your Learning
        
        1. **Flash Cards**
           - Front: Formula name
           - Back: Formula + when to use
           - Use apps like Anki for spaced repetition
        
        2. **Quiz Yourself**
           - Cover formulas and try to write them
           - Time yourself solving problems
           - Set goals (e.g., complete 5 problems in 10 minutes)
        
        3. **Teach Others**
           - Explain concepts to friends
           - Create YouTube-style explanations
           - Teaching reinforces your understanding
        
        4. **Real Data Projects**
           - Analyze your own data
           - Use Kaggle datasets
           - Make statistics personally relevant
        
        ### 📺 Recommended Video Channels
        
        | Channel | Best For |
        |---------|----------|
        | **StatQuest** | Intuitive explanations |
        | **Khan Academy** | Comprehensive coverage |
        | **3Blue1Brown** | Visual math intuition |
        | **Crash Course Statistics** | Quick overviews |
        
        ### 📖 Practice Problem Sources
        
        - Textbook end-of-chapter problems
        - Online problem generators
        - Past exam papers
        - Research papers (replicate analyses)
        """)

    with st.expander("❌ Common Mistakes to Avoid", expanded=True):
        st.markdown("""
        ### Statistical Errors
        
        | Mistake | Why It's Wrong | Correct Approach |
        |---------|----------------|------------------|
        | Using t-test for 3+ groups | Inflates Type I error | Use ANOVA |
        | Not checking assumptions | Results may be invalid | Always check normality, homogeneity |
        | Confusing statistical vs practical significance | p < 0.05 ≠ important | Report effect sizes |
        | Ignoring sample size | Small n = unstable estimates | Conduct power analysis |
        | Multiple testing without correction | Inflates false positives | Use Bonferroni or FDR |
        
        ### Formula Errors
        
        | Mistake | Correct |
        |---------|---------|
        | Using σ when you have s | t-test uses s (sample SD) |
        | Forgetting to square in chi-square | Formula is (O-E)²/E |
        | Wrong df for t-test | Independent = n₁+n₂-2, paired = n-1 |
        | Dividing by n instead of n-1 | Sample variance uses n-1 |
        
        ### Interpretation Errors
        
        - **Wrong:** "p = 0.03 means 3% chance null is true"
        - **Right:** "p = 0.03 means 3% chance of seeing this result IF null is true"
        
        - **Wrong:** "Correlation of 0.7 means 70% relationship"
        - **Right:** "r = 0.7 means R² = 0.49, so 49% of variance is shared"
        
        - **Wrong:** "Correlation means causation"
        - **Right:** "Correlation shows association, not causation"
        """)

    # Final Tips Card
    st.markdown("""
    <div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 20px; border-radius: 10px; margin-top: 15px; border: 1px solid #86efac;">
        <h3 style="color: #166534; margin: 0 0 15px 0 !important;">🌟 Top 10 Tips for Statistics Success</h3>
        <ol style="margin: 0; padding-left: 25px; color: #166534;">
            <li><b>Understand before memorizing</b> — know the "why"</li>
            <li><b>Practice by hand</b> — builds deep understanding</li>
            <li><b>Draw pictures</b> — visualize distributions and relationships</li>
            <li><b>Start simple</b> — master basics before advanced topics</li>
            <li><b>Connect concepts</b> — see how tests relate to each other</li>
            <li><b>Use real data</b> — abstract concepts become concrete</li>
            <li><b>Check assumptions</b> — always before running tests</li>
            <li><b>Report effect sizes</b> — not just p-values</li>
            <li><b>Learn software too</b> — be efficient with SPSS, R, or Python</li>
            <li><b>Ask "so what?"</b> — interpret results meaningfully</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# Footer
show_footer()
