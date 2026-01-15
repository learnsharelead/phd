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
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🎯 Hypothesis Design",
    "📊 Parametric Tests",
    "📈 Non-Parametric Tests",
    "🔢 Chi-Square",
    "🧮 Calculators",
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
    
    with st.expander("📚 z-Test: 5 Complete Worked Examples", expanded=True):
        st.markdown("""
        ### Master z-Test with These Detailed Examples
        
        Learn z-test through complete, step-by-step examples from various fields.
        """)
        
        st.markdown("""
        ---
        #### **Example 1: Employee Salary Analysis** (Business)
        
        **Problem:**
        A company claims the average employee salary is ₹50,000 with a known population standard deviation of ₹8,000. 
        A random sample of 100 employees shows a mean salary of ₹48,500. Test at α = 0.05 if the claim is accurate.
        
        **Step 1: State Hypotheses**
        - H₀: μ = 50,000 (Company claim is correct)
        - H₁: μ ≠ 50,000 (Company claim is incorrect)
        - Two-tailed test (we're checking if it's different, not specifically higher or lower)
        
        **Step 2: Set Significance Level**
        - α = 0.05
        - Critical values: ±1.96 (from z-table for two-tailed test)
        
        **Step 3: Calculate Test Statistic**
        
        Given:
        - x̄ = 48,500
        - μ₀ = 50,000
        - σ = 8,000
        - n = 100
        
        Formula: z = (x̄ - μ₀) / (σ/√n)
        
        Calculation:
        ```
        Standard Error (SE) = σ/√n = 8,000/√100 = 8,000/10 = 800
        
        z = (48,500 - 50,000) / 800
        z = -1,500 / 800
        z = -1.875
        ```
        
        **Step 4: Make Decision**
        - |z| = 1.875 < 1.96 (critical value)
        - z-statistic falls within the acceptance region
        - **Decision**: Fail to reject H₀
        
        **Step 5: Calculate p-value**
        - For z = -1.875 (two-tailed)
        - p-value = 2 × P(Z < -1.875) = 2 × 0.0304 = 0.0608
        - p = 0.061 > 0.05 → Not significant
        
        **Step 6: Conclusion**
        "At α = 0.05, there is insufficient evidence to conclude that the average salary differs from ₹50,000 
        (z = -1.875, p = 0.061). The company's claim cannot be rejected."
        
        **95% Confidence Interval:**
        ```
        CI = x̄ ± 1.96(SE)
        CI = 48,500 ± 1.96(800)
        CI = 48,500 ± 1,568
        CI = [46,932, 50,068]
        ```
        The claimed value (50,000) falls within the CI, supporting our decision.
        
        **Excel Implementation:**
        ```excel
        =NORM.S.DIST(-1.875, TRUE) * 2  // Two-tailed p-value = 0.0608
        =ABS(-1.875) > 1.96  // FALSE (not significant)
        ```
        
        **R Code:**
        ```r
        # Data
        x_bar <- 48500
        mu_0 <- 50000
        sigma <- 8000
        n <- 100
        
        # Calculate z-statistic
        se <- sigma / sqrt(n)
        z <- (x_bar - mu_0) / se
        
        # Calculate p-value (two-tailed)
        p_value <- 2 * pnorm(abs(z), lower.tail = FALSE)
        
        # Results
        cat("z-statistic:", z, "\\n")
        cat("p-value:", p_value, "\\n")
        cat("Decision:", ifelse(abs(z) > 1.96, "Reject H0", "Fail to reject H0"))
        ```
        
        ---
        #### **Example 2: Student Test Scores** (Education)
        
        **Problem:**
        National average IQ is 100 with σ = 15. A gifted program has 64 students with mean IQ = 108. 
        Is this significantly higher than the national average? (α = 0.01, one-tailed)
        
        **Step 1: Hypotheses**
        - H₀: μ ≤ 100 (Not higher than national average)
        - H₁: μ > 100 (Higher than national average)
        - One-tailed test (right-tailed)
        
        **Step 2: Significance Level**
        - α = 0.01
        - Critical value: z = 2.33 (one-tailed, right)
        
        **Step 3: Calculate z**
        ```
        SE = 15/√64 = 15/8 = 1.875
        
        z = (108 - 100) / 1.875
        z = 8 / 1.875
        z = 4.27
        ```
        
        **Step 4: Decision**
        - z = 4.27 > 2.33 (critical value)
        - **Decision**: Reject H₀
        
        **Step 5: p-value**
        - p = P(Z > 4.27) ≈ 0.00001 (extremely small)
        - p < 0.01 → Highly significant
        
        **Step 6: Conclusion**
        "The gifted program students have significantly higher IQ than the national average 
        (z = 4.27, p < 0.001). This is a highly significant result with a large effect size."
        
        **Effect Size (Cohen's d):**
        ```
        d = (108 - 100) / 15 = 0.53 (Medium effect)
        ```
        
        **APA-Style Reporting:**
        "A one-sample z-test revealed that gifted program students (M = 108, SD = 15, n = 64) 
        had significantly higher IQ scores than the national average (μ = 100), z = 4.27, p < .001, d = 0.53."
        
        ---
        #### **Example 3: Quality Control in Manufacturing** (Engineering)
        
        **Problem:**
        A machine produces bolts with a target diameter of 10mm (σ = 0.5mm). A sample of 50 bolts 
        has mean diameter = 10.15mm. Is the machine out of calibration? (α = 0.05, two-tailed)
        
        **Step 1: Hypotheses**
        - H₀: μ = 10mm (Machine is calibrated)
        - H₁: μ ≠ 10mm (Machine is out of calibration)
        
        **Step 2: Calculate z**
        ```
        SE = 0.5/√50 = 0.5/7.071 = 0.0707
        
        z = (10.15 - 10) / 0.0707
        z = 0.15 / 0.0707
        z = 2.12
        ```
        
        **Step 3: Decision**
        - |z| = 2.12 > 1.96
        - **Decision**: Reject H₀
        - p-value = 0.034 < 0.05
        
        **Step 4: Conclusion**
        "The machine is significantly out of calibration (z = 2.12, p = 0.034). 
        Maintenance is required."
        
        **Practical Significance:**
        - Difference = 0.15mm (1.5% deviation)
        - Depending on tolerance specifications, this may or may not be practically significant
        - Statistical significance ≠ Practical significance
        
        ---
        #### **Example 4: Medical Research - Blood Pressure** (Medicine)
        
        **Problem:**
        Normal systolic blood pressure is 120 mmHg (σ = 15). A sample of 80 patients on a new diet 
        shows mean = 115 mmHg. Does the diet reduce blood pressure? (α = 0.05, one-tailed)
        
        **Step 1: Hypotheses**
        - H₀: μ ≥ 120 (Diet doesn't reduce BP)
        - H₁: μ < 120 (Diet reduces BP)
        - One-tailed test (left-tailed)
        
        **Step 2: Calculate z**
        ```
        SE = 15/√80 = 15/8.944 = 1.677
        
        z = (115 - 120) / 1.677
        z = -5 / 1.677
        z = -2.98
        ```
        
        **Step 3: Decision**
        - z = -2.98 < -1.645 (critical value for one-tailed)
        - **Decision**: Reject H₀
        - p-value = 0.0014 < 0.05
        
        **Step 4: Conclusion**
        "The diet significantly reduces blood pressure (z = -2.98, p = 0.001). 
        Mean reduction = 5 mmHg (95% CI: [2.24, 7.76])."
        
        **Clinical Significance:**
        - 5 mmHg reduction is clinically meaningful
        - Both statistically AND practically significant
        
        ---
        #### **Example 5: Customer Satisfaction Survey** (Business)
        
        **Problem:**
        A company's historical customer satisfaction score is 75 (σ = 12). After implementing changes, 
        a survey of 120 customers shows mean = 78. Did satisfaction improve? (α = 0.05, one-tailed)
        
        **Step 1: Hypotheses**
        - H₀: μ ≤ 75 (No improvement)
        - H₁: μ > 75 (Improvement)
        
        **Step 2: Calculate z**
        ```
        SE = 12/√120 = 12/10.954 = 1.095
        
        z = (78 - 75) / 1.095
        z = 3 / 1.095
        z = 2.74
        ```
        
        **Step 3: Decision**
        - z = 2.74 > 1.645 (critical value)
        - **Decision**: Reject H₀
        - p-value = 0.003 < 0.05
        
        **Step 4: Conclusion**
        "Customer satisfaction significantly improved after the changes (z = 2.74, p = 0.003). 
        Mean increase = 3 points (95% CI: [1.19, 4.81])."
        
        **Business Impact:**
        - 4% improvement in satisfaction
        - Statistically significant and meaningful for business
        """)
    
    with st.expander("⚠️ When to Use z-Test vs When NOT to Use", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **✅ Use z-Test When:**
            
            1. **Population σ is KNOWN**
               - From historical data
               - From previous studies
               - From manufacturer specifications
            
            2. **Large Sample Size (n ≥ 30)**
               - Central Limit Theorem applies
               - Sample distribution approaches normal
            
            3. **Data is Approximately Normal**
               - Or large enough for CLT to work
            
            4. **Comparing to a Known Value**
               - Testing against a standard
               - Quality control applications
               - Comparing to population mean
            
            **Examples of Appropriate Use:**
            - Quality control (known σ from specs)
            - Standardized test scores (known σ)
            - Large-scale surveys (n > 30)
            - Historical data comparison
            """)
        
        with col2:
            st.markdown("""
            **❌ Do NOT Use z-Test When:**
            
            1. **Population σ is UNKNOWN**
               - Use t-test instead
               - Most real-world scenarios
            
            2. **Small Sample Size (n < 30)**
               - Use t-test instead
               - Unless population is exactly normal
            
            3. **Data is Highly Non-Normal**
               - Use non-parametric tests
               - Or transform data
            
            4. **Comparing Two Samples**
               - Use two-sample t-test
               - Or Mann-Whitney U test
            
            **Common Mistakes:**
            - ❌ Using z-test with unknown σ
            - ❌ Using z-test with n < 30
            - ❌ Ignoring non-normality
            - ❌ Using when t-test is appropriate
            """)
    
    with st.expander("💻 Software Implementation Guide", expanded=True):
        st.markdown("""
        ### How to Perform z-Test in Different Software
        
        #### **Excel**
        
        **Method 1: Using Formulas**
        ```excel
        // Given data in cells
        A1: Sample Mean (x̄) = 48500
        A2: Population Mean (μ₀) = 50000
        A3: Population SD (σ) = 8000
        A4: Sample Size (n) = 100
        
        // Calculate z-statistic
        A5: =(A1-A2)/(A3/SQRT(A4))  // Result: -1.875
        
        // Calculate p-value (two-tailed)
        A6: =2*NORM.S.DIST(A5,TRUE)  // Result: 0.0608
        
        // Decision
        A7: =IF(ABS(A5)>1.96,"Reject H0","Fail to reject H0")
        ```
        
        **Method 2: Using Data Analysis ToolPak**
        1. Data → Data Analysis → z-Test: Two Sample for Means
        2. Enter variable range and hypothesized mean
        3. Enter known variance (σ²)
        4. Set alpha level
        5. Click OK
        
        ---
        
        #### **R Programming**
        
        **Basic z-Test Function:**
        ```r
        # Create z-test function (R doesn't have built-in z-test)
        z.test <- function(x, mu, sigma, alternative = "two.sided") {
          n <- length(x)
          x_bar <- mean(x)
          se <- sigma / sqrt(n)
          z <- (x_bar - mu) / se
          
          # Calculate p-value
          if (alternative == "two.sided") {
            p_value <- 2 * pnorm(abs(z), lower.tail = FALSE)
          } else if (alternative == "greater") {
            p_value <- pnorm(z, lower.tail = FALSE)
          } else {
            p_value <- pnorm(z, lower.tail = TRUE)
          }
          
          return(list(
            statistic = z,
            p.value = p_value,
            alternative = alternative,
            method = "One Sample z-Test"
          ))
        }
        
        # Example usage
        data <- c(48500, 49000, 47800, ...)  # Your sample data
        result <- z.test(data, mu = 50000, sigma = 8000, alternative = "two.sided")
        print(result)
        ```
        
        **Using BSDA Package:**
        ```r
        # Install and load package
        install.packages("BSDA")
        library(BSDA)
        
        # Perform z-test
        z.test(x = sample_data, 
               mu = 50000, 
               sigma.x = 8000, 
               alternative = "two.sided",
               conf.level = 0.95)
        ```
        
        ---
        
        #### **Python (scipy)**
        
        ```python
        import numpy as np
        from scipy import stats
        
        # Data
        x_bar = 48500
        mu_0 = 50000
        sigma = 8000
        n = 100
        
        # Calculate z-statistic
        se = sigma / np.sqrt(n)
        z = (x_bar - mu_0) / se
        
        # Calculate p-value (two-tailed)
        p_value = 2 * (1 - stats.norm.cdf(abs(z)))
        
        # Results
        print(f"z-statistic: {z:.4f}")
        print(f"p-value: {p_value:.4f}")
        print(f"Decision: {'Reject H0' if abs(z) > 1.96 else 'Fail to reject H0'}")
        
        # Confidence interval
        ci_lower = x_bar - 1.96 * se
        ci_upper = x_bar + 1.96 * se
        print(f"95% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")
        ```
        
        ---
        
        #### **SPSS**
        
        SPSS doesn't have a direct z-test option (it uses t-test). However, for large samples:
        
        1. Analyze → Compare Means → One-Sample T Test
        2. Enter test variable
        3. Enter test value (μ₀)
        4. Click OK
        5. For large n, t ≈ z
        
        **Note**: For true z-test, use syntax:
        ```spss
        COMPUTE z = (MEAN - 50000) / (8000 / SQRT(100)).
        COMPUTE p = 2 * (1 - CDF.NORMAL(ABS(z), 0, 1)).
        EXECUTE.
        ```
        """)
    
    with st.expander("📊 Interpretation Guide & APA Reporting", expanded=True):
        st.markdown("""
        ### How to Interpret z-Test Results
        
        #### **Step-by-Step Interpretation:**
        
        **1. Check the z-statistic:**
        - Large |z| → Sample mean far from hypothesized mean
        - Small |z| → Sample mean close to hypothesized mean
        
        **2. Compare to critical value:**
        - α = 0.05, two-tailed: ±1.96
        - α = 0.05, one-tailed: 1.645 (right) or -1.645 (left)
        - α = 0.01, two-tailed: ±2.576
        - α = 0.01, one-tailed: 2.33 or -2.33
        
        **3. Check p-value:**
        - p < 0.001: Highly significant (***)
        - p < 0.01: Very significant (**)
        - p < 0.05: Significant (*)
        - p ≥ 0.05: Not significant (ns)
        
        **4. Calculate effect size (Cohen's d):**
        ```
        d = (x̄ - μ₀) / σ
        
        Interpretation:
        - |d| < 0.2: Negligible
        - 0.2 ≤ |d| < 0.5: Small
        - 0.5 ≤ |d| < 0.8: Medium
        - |d| ≥ 0.8: Large
        ```
        
        **5. Report confidence interval:**
        - Shows range of plausible values
        - If CI includes μ₀ → Not significant
        - If CI excludes μ₀ → Significant
        
        ---
        
        ### **APA-Style Reporting**
        
        **Template:**
        > "A one-sample z-test was conducted to compare [variable] to [standard/population value]. 
        > The sample (M = [mean], SD = [SD], n = [n]) [was/was not] significantly different from 
        > [population mean], z = [z-value], p = [p-value], d = [effect size]."
        
        **Example 1 (Significant Result):**
        > "A one-sample z-test was conducted to determine whether employee salaries differed from 
        > the company's claimed average of ₹50,000. The sample (M = 48,500, SD = 8,000, n = 100) 
        > was not significantly different from the claimed average, z = -1.88, p = .061, d = -0.19, 
        > 95% CI [46,932, 50,068]."
        
        **Example 2 (Significant Result):**
        > "A one-sample z-test revealed that gifted program students (M = 108, SD = 15, n = 64) 
        > had significantly higher IQ scores than the national average (μ = 100), z = 4.27, p < .001, 
        > d = 0.53, 95% CI [104.32, 111.68]."
        
        **Example 3 (With Direction):**
        > "Customer satisfaction scores (M = 78, SD = 12, n = 120) were significantly higher after 
        > implementing changes compared to the historical average (μ = 75), z = 2.74, p = .003, 
        > d = 0.25, 95% CI [75.85, 80.15]."
        
        ---
        
        ### **Common Reporting Mistakes to Avoid**
        
        | Mistake | Correct |
        |---------|---------|
        | ❌ "The result is significant" | ✅ "z = 2.74, p = .003" (report statistics) |
        | ❌ "p = 0.000" | ✅ "p < .001" (never report p = 0) |
        | ❌ "Highly significant" without p-value | ✅ "z = 4.27, p < .001" |
        | ❌ Reporting only p-value | ✅ Report z, p, and effect size |
        | ❌ "Accepted H₀" | ✅ "Failed to reject H₀" |
        | ❌ No confidence interval | ✅ Include 95% CI |
        | ❌ "Proved the hypothesis" | ✅ "Supported the hypothesis" or "Consistent with" |
        
        ---
        
        ### **Decision Table**
        
        | z-statistic | p-value | Decision | Interpretation |
        |-------------|---------|----------|----------------|
        | \|z\| < 1.96 | p > 0.05 | Fail to reject H₀ | No significant difference |
        | 1.96 ≤ \|z\| < 2.58 | 0.01 < p ≤ 0.05 | Reject H₀ | Significant difference |
        | 2.58 ≤ \|z\| < 3.29 | 0.001 < p ≤ 0.01 | Reject H₀ | Very significant difference |
        | \|z\| ≥ 3.29 | p ≤ 0.001 | Reject H₀ | Highly significant difference |
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
    
    with st.expander("📚 t-Test: 10 Complete Worked Examples", expanded=True):
        st.markdown("""
        ### Master All Three Types of t-Tests
        
        Learn through detailed, step-by-step examples from various research fields.
        """)
        
        st.markdown("""
        ---
        ## 🔵 ONE-SAMPLE t-TEST (3 Examples)
        
        **Use When**: Comparing a sample mean to a known population value (when σ is unknown)
        
        ---
        #### **Example 1: Testing Average Study Hours** (Education)
        
        **Problem:**
        A university claims students study an average of 20 hours per week. A sample of 25 students 
        shows: Mean = 18.5 hours, SD = 4.2 hours. Test at α = 0.05 if students study less than claimed.
        
        **Step 1: Hypotheses**
        - H₀: μ ≥ 20 (Students study at least 20 hours)
        - H₁: μ < 20 (Students study less than 20 hours)
        - One-tailed test (left)
        
        **Step 2: Calculate t-statistic**
        
        Given:
        - x̄ = 18.5
        - μ₀ = 20
        - s = 4.2
        - n = 25
        - df = 25 - 1 = 24
        
        ```
        SE = s/√n = 4.2/√25 = 4.2/5 = 0.84
        
        t = (x̄ - μ₀) / SE
        t = (18.5 - 20) / 0.84
        t = -1.5 / 0.84
        t = -1.79
        ```
        
        **Step 3: Find Critical Value**
        - df = 24, α = 0.05, one-tailed
        - t_critical = -1.711 (from t-table)
        
        **Step 4: Decision**
        - t = -1.79 < -1.711 (critical value)
        - **Decision**: Reject H₀
        - p-value ≈ 0.043 < 0.05
        
        **Step 5: Effect Size (Cohen's d)**
        ```
        d = (x̄ - μ₀) / s
        d = (18.5 - 20) / 4.2
        d = -0.36 (Small to medium effect)
        ```
        
        **Step 6: Confidence Interval**
        ```
        95% CI = x̄ ± t(0.025, 24) × SE
        95% CI = 18.5 ± 2.064 × 0.84
        95% CI = 18.5 ± 1.73
        95% CI = [16.77, 20.23]
        ```
        
        **Conclusion:**
        "Students study significantly less than the claimed 20 hours per week 
        (M = 18.5, SD = 4.2, n = 25), t(24) = -1.79, p = .043, d = -0.36, 95% CI [16.77, 20.23]."
        
        **SPSS Output Interpretation:**
        ```
        One-Sample Statistics
        ┌──────────┬───┬──────┬─────────┬──────────┐
        │          │ N │ Mean │ Std Dev │ Std Error│
        ├──────────┼───┼──────┼─────────┼──────────┤
        │ Hours    │25 │18.50 │  4.200  │   0.840  │
        └──────────┴───┴──────┴─────────┴──────────┘
        
        One-Sample Test (Test Value = 20)
        ┌──────┬────┬─────┬──────────┬─────────────┐
        │  t   │ df │ Sig │   Mean   │   95% CI    │
        │      │    │(2-t)│   Diff   │             │
        ├──────┼────┼─────┼──────────┼─────────────┤
        │-1.79 │ 24 │.086 │  -1.500  │[-3.23, 0.23]│
        └──────┴────┴─────┴──────────┴─────────────┘
        
        Note: SPSS shows two-tailed p (.086), divide by 2 for one-tailed (.043)
        ```
        
        **R Code:**
        ```r
        # Data
        hours <- c(18, 19, 17, 20, 16, 22, 18, 19, 15, 21, 
                   17, 18, 20, 19, 16, 18, 17, 19, 20, 18,
                   16, 19, 17, 18, 20)
        
        # One-sample t-test
        result <- t.test(hours, mu = 20, alternative = "less")
        print(result)
        
        # Effect size
        library(effsize)
        cohen.d(hours, f = NA, mu = 20)
        ```
        
        ---
        #### **Example 2: Quality Control - Product Weight** (Manufacturing)
        
        **Problem:**
        Cereal boxes should weigh 500g. A sample of 30 boxes shows: Mean = 498g, SD = 5g. 
        Is the filling machine accurate? (α = 0.05, two-tailed)
        
        **Step 1: Hypotheses**
        - H₀: μ = 500 (Machine is accurate)
        - H₁: μ ≠ 500 (Machine is not accurate)
        
        **Step 2: Calculate**
        ```
        SE = 5/√30 = 0.913
        t = (498 - 500) / 0.913 = -2.19
        df = 29
        ```
        
        **Step 3: Decision**
        - t_critical = ±2.045 (df = 29, α = 0.05, two-tailed)
        - |t| = 2.19 > 2.045
        - **Reject H₀**
        - p = 0.037 < 0.05
        
        **Step 4: Conclusion**
        "The filling machine is significantly off-target (M = 498g, SD = 5g, n = 30), 
        t(29) = -2.19, p = .037, d = -0.40. The machine needs calibration."
        
        **Practical Significance:**
        - 2g difference (0.4% deviation)
        - May or may not be practically significant depending on tolerance
        
        ---
        #### **Example 3: Medical Research - Blood Glucose** (Medicine)
        
        **Problem:**
        Normal fasting blood glucose is 100 mg/dL. A sample of 20 diabetic patients on new medication 
        shows: Mean = 105 mg/dL, SD = 12 mg/dL. Is the medication effective? (α = 0.01)
        
        **Step 1: Hypotheses**
        - H₀: μ = 100 (Medication doesn't change glucose)
        - H₁: μ ≠ 100 (Medication changes glucose)
        
        **Step 2: Calculate**
        ```
        SE = 12/√20 = 2.683
        t = (105 - 100) / 2.683 = 1.86
        df = 19
        ```
        
        **Step 3: Decision**
        - t_critical = ±2.861 (df = 19, α = 0.01, two-tailed)
        - |t| = 1.86 < 2.861
        - **Fail to reject H₀**
        - p = 0.078 > 0.01
        
        **Step 4: Conclusion**
        "The medication did not significantly change blood glucose levels at α = 0.01 
        (M = 105, SD = 12, n = 20), t(19) = 1.86, p = .078, d = 0.42."
        
        **Note**: Result is not significant at α = 0.01, but would be at α = 0.05. 
        This highlights the importance of pre-specifying alpha level.
        
        ---
        ## 🟢 INDEPENDENT SAMPLES t-TEST (4 Examples)
        
        **Use When**: Comparing means of two separate, unrelated groups
        
        ---
        #### **Example 4: Gender Differences in Math Scores** (Education)
        
        **Problem:**
        Do males and females differ in math test scores?
        - Males: n₁ = 30, x̄₁ = 75, s₁ = 10
        - Females: n₂ = 30, x̄₂ = 80, s₂ = 12
        Test at α = 0.05 (two-tailed)
        
        **Step 1: Check Assumptions**
        - Independence: ✅ Different students
        - Normality: ✅ n > 30 (CLT applies)
        - Equal variances: Test with Levene's test
          - F = 1.44, p = 0.235 > 0.05 ✅ Variances equal
        
        **Step 2: Calculate Pooled Variance**
        ```
        s²_pooled = [(n₁-1)s₁² + (n₂-1)s₂²] / (n₁ + n₂ - 2)
        s²_pooled = [(29)(100) + (29)(144)] / 58
        s²_pooled = [2900 + 4176] / 58
        s²_pooled = 122
        s_pooled = 11.05
        ```
        
        **Step 3: Calculate t-statistic**
        ```
        SE = s_pooled × √(1/n₁ + 1/n₂)
        SE = 11.05 × √(1/30 + 1/30)
        SE = 11.05 × 0.258
        SE = 2.85
        
        t = (x̄₁ - x̄₂) / SE
        t = (75 - 80) / 2.85
        t = -1.75
        
        df = n₁ + n₂ - 2 = 58
        ```
        
        **Step 4: Decision**
        - t_critical = ±2.00 (df = 58, α = 0.05)
        - |t| = 1.75 < 2.00
        - **Fail to reject H₀**
        - p = 0.085 > 0.05
        
        **Step 5: Effect Size**
        ```
        Cohen's d = (x̄₁ - x̄₂) / s_pooled
        d = (75 - 80) / 11.05 = -0.45 (Small to medium)
        ```
        
        **Step 6: Conclusion**
        "There was no significant difference in math scores between males (M = 75, SD = 10) 
        and females (M = 80, SD = 12), t(58) = -1.75, p = .085, d = -0.45."
        
        **SPSS Output:**
        ```
        Group Statistics
        ┌────────┬───┬──────┬─────────┬──────────┐
        │ Gender │ N │ Mean │ Std Dev │ Std Error│
        ├────────┼───┼──────┼─────────┼──────────┤
        │ Male   │30 │ 75.0 │  10.0   │   1.83   │
        │ Female │30 │ 80.0 │  12.0   │   2.19   │
        └────────┴───┴──────┴─────────┴──────────┘
        
        Independent Samples Test
        Levene's Test: F = 1.44, Sig = .235
        
        t-test for Equality of Means (Equal variances assumed)
        ┌──────┬────┬─────┬──────────┬─────────────┐
        │  t   │ df │ Sig │   Mean   │   95% CI    │
        │      │    │(2-t)│   Diff   │             │
        ├──────┼────┼─────┼──────────┼─────────────┤
        │-1.75 │ 58 │.085 │  -5.00   │[-10.72,0.72]│
        └──────┴────┴─────┴──────────┴─────────────┘
        ```
        
        ---
        #### **Example 5: Treatment vs Control Group** (Medicine)
        
        **Problem:**
        Does a new drug reduce blood pressure more than placebo?
        - Treatment: n₁ = 40, x̄₁ = 118 mmHg, s₁ = 8
        - Control: n₂ = 40, x̄₂ = 125 mmHg, s₂ = 10
        Test at α = 0.05 (one-tailed, expecting treatment < control)
        
        **Step 1: Hypotheses**
        - H₀: μ₁ ≥ μ₂ (Treatment not better)
        - H₁: μ₁ < μ₂ (Treatment is better)
        
        **Step 2: Calculate**
        ```
        s²_pooled = [(39)(64) + (39)(100)] / 78 = 82
        s_pooled = 9.06
        
        SE = 9.06 × √(1/40 + 1/40) = 2.03
        
        t = (118 - 125) / 2.03 = -3.45
        df = 78
        ```
        
        **Step 3: Decision**
        - t_critical = -1.665 (one-tailed, df = 78)
        - t = -3.45 < -1.665
        - **Reject H₀**
        - p < 0.001
        
        **Step 4: Effect Size**
        ```
        d = (118 - 125) / 9.06 = -0.77 (Medium to large)
        ```
        
        **Step 5: Conclusion**
        "The treatment group had significantly lower blood pressure (M = 118, SD = 8) than 
        the control group (M = 125, SD = 10), t(78) = -3.45, p < .001, d = -0.77, 
        95% CI [-11.07, -2.93]. The drug is effective."
        
        **Clinical Significance:**
        - 7 mmHg reduction is clinically meaningful
        - Both statistically and clinically significant
        
        ---
        #### **Example 6: Online vs Traditional Learning** (Education)
        
        **Problem:**
        Compare final exam scores between online and traditional classes.
        - Online: n₁ = 50, x̄₁ = 82, s₁ = 8
        - Traditional: n₂ = 50, x̄₂ = 85, s₂ = 7
        
        **Calculation:**
        ```
        s_pooled = 7.52
        SE = 1.50
        t = (82 - 85) / 1.50 = -2.00
        df = 98
        p = 0.048
        d = -0.40
        ```
        
        **Conclusion:**
        "Traditional learning resulted in significantly higher scores (M = 85, SD = 7) than 
        online learning (M = 82, SD = 8), t(98) = -2.00, p = .048, d = -0.40."
        
        ---
        #### **Example 7: Brand Comparison** (Business)
        
        **Problem:**
        Compare customer satisfaction between two brands.
        - Brand A: n₁ = 60, x̄₁ = 7.5, s₁ = 1.2
        - Brand B: n₂ = 60, x̄₂ = 7.8, s₂ = 1.4
        
        **Calculation:**
        ```
        s_pooled = 1.30
        SE = 0.237
        t = (7.5 - 7.8) / 0.237 = -1.27
        df = 118
        p = 0.208
        d = -0.23
        ```
        
        **Conclusion:**
        "No significant difference in satisfaction between Brand A (M = 7.5, SD = 1.2) and 
        Brand B (M = 7.8, SD = 1.4), t(118) = -1.27, p = .208, d = -0.23."
        
        ---
        ## 🟣 PAIRED t-TEST (3 Examples)
        
        **Use When**: Comparing two measurements on the same subjects (before-after, matched pairs)
        
        ---
        #### **Example 8: Before-After Training Program** (Business)
        
        **Problem:**
        Does a training program improve employee productivity?
        10 employees measured before and after training.
        
        | Employee | Before | After | Difference (d) |
        |----------|--------|-------|----------------|
        | 1 | 65 | 72 | 7 |
        | 2 | 70 | 75 | 5 |
        | 3 | 68 | 74 | 6 |
        | 4 | 72 | 78 | 6 |
        | 5 | 66 | 71 | 5 |
        | 6 | 69 | 76 | 7 |
        | 7 | 71 | 77 | 6 |
        | 8 | 67 | 73 | 6 |
        | 9 | 70 | 78 | 8 |
        | 10 | 68 | 76 | 8 |
        
        **Step 1: Calculate Differences**
        ```
        d̄ = (7+5+6+6+5+7+6+6+8+8) / 10 = 6.4
        
        s_d = √[Σ(d - d̄)² / (n-1)]
        s_d = √[(0.36+1.96+0.16+0.16+1.96+0.36+0.16+0.16+2.56+2.56) / 9]
        s_d = √[10.4 / 9] = 1.08
        ```
        
        **Step 2: Calculate t-statistic**
        ```
        SE = s_d / √n = 1.08 / √10 = 0.342
        
        t = d̄ / SE = 6.4 / 0.342 = 18.71
        df = n - 1 = 9
        ```
        
        **Step 3: Decision**
        - t_critical = 2.262 (df = 9, α = 0.05, two-tailed)
        - t = 18.71 > 2.262
        - **Reject H₀**
        - p < 0.001
        
        **Step 4: Effect Size**
        ```
        Cohen's d = d̄ / s_d = 6.4 / 1.08 = 5.93 (Very large!)
        ```
        
        **Step 5: Conclusion**
        "Training significantly improved productivity scores (M_diff = 6.4, SD_diff = 1.08, n = 10), 
        t(9) = 18.71, p < .001, d = 5.93, 95% CI [5.63, 7.17]. This is a very large effect."
        
        **SPSS Output:**
        ```
        Paired Samples Statistics
        ┌────────┬──────┬─────────┬──────────┐
        │        │ Mean │ Std Dev │ Std Error│
        ├────────┼──────┼─────────┼──────────┤
        │ Before │ 68.6 │  2.27   │   0.72   │
        │ After  │ 75.0 │  2.58   │   0.82   │
        └────────┴──────┴─────────┴──────────┘
        
        Paired Samples Test
        ┌────────┬──────┬─────────┬──────────┬──────┬────┬─────┐
        │  Pair  │ Mean │ Std Dev │ Std Error│  t   │ df │ Sig │
        ├────────┼──────┼─────────┼──────────┼──────┼────┼─────┤
        │Before- │-6.40 │  1.08   │   0.34   │-18.71│ 9  │.000 │
        │ After  │      │         │          │      │    │     │
        └────────┴──────┴─────────┴──────────┴──────┴────┴─────┘
        ```
        
        **R Code:**
        ```r
        before <- c(65, 70, 68, 72, 66, 69, 71, 67, 70, 68)
        after <- c(72, 75, 74, 78, 71, 76, 77, 73, 78, 76)
        
        # Paired t-test
        result <- t.test(after, before, paired = TRUE)
        print(result)
        
        # Effect size
        library(effsize)
        cohen.d(after, before, paired = TRUE)
        ```
        
        ---
        #### **Example 9: Diet Program Weight Loss** (Health)
        
        **Problem:**
        Does a 12-week diet program reduce weight?
        15 participants measured before and after.
        
        **Data:**
        - Mean weight loss (d̄) = 3.2 kg
        - SD of differences (s_d) = 1.5 kg
        - n = 15
        
        **Calculation:**
        ```
        SE = 1.5 / √15 = 0.387
        t = 3.2 / 0.387 = 8.27
        df = 14
        t_critical = 2.145 (one-tailed, α = 0.05)
        p < 0.001
        d = 3.2 / 1.5 = 2.13 (Very large)
        ```
        
        **Conclusion:**
        "The diet program significantly reduced weight (M_loss = 3.2 kg, SD = 1.5, n = 15), 
        t(14) = 8.27, p < .001, d = 2.13, 95% CI [2.37, 4.03]."
        
        ---
        #### **Example 10: Medication Effect on Sleep** (Medicine)
        
        **Problem:**
        Does medication improve sleep hours?
        20 patients measured before and after 1 month of medication.
        
        **Data:**
        - Mean increase in sleep (d̄) = 1.2 hours
        - SD of differences (s_d) = 0.8 hours
        - n = 20
        
        **Calculation:**
        ```
        SE = 0.8 / √20 = 0.179
        t = 1.2 / 0.179 = 6.70
        df = 19
        p < 0.001
        d = 1.2 / 0.8 = 1.50 (Large)
        ```
        
        **Conclusion:**
        "Medication significantly increased sleep duration (M_increase = 1.2 hours, SD = 0.8, n = 20), 
        t(19) = 6.70, p < .001, d = 1.50, 95% CI [0.83, 1.57]."
        """)
    
    with st.expander("💻 Complete Software Implementation for t-Tests", expanded=True):
        st.markdown("""
        ### How to Perform t-Tests in Different Software
        
        #### **SPSS - Complete Guide**
        
        **One-Sample t-Test:**
        1. Analyze → Compare Means → One-Sample T Test
        2. Move variable to "Test Variable(s)"
        3. Enter test value (μ₀)
        4. Click "Options" → Set confidence level (95%)
        5. Click OK
        
        **Independent Samples t-Test:**
        1. Analyze → Compare Means → Independent-Samples T Test
        2. Move dependent variable to "Test Variable(s)"
        3. Move grouping variable to "Grouping Variable"
        4. Click "Define Groups" → Enter group codes (e.g., 1, 2)
        5. Click OK
        
        **Paired Samples t-Test:**
        1. Analyze → Compare Means → Paired-Samples T Test
        2. Select both variables → Move to "Paired Variables"
        3. Click OK
        
        **Interpreting SPSS Output:**
        
        ```
        Key Values to Report:
        - t-statistic: The calculated t value
        - df: Degrees of freedom
        - Sig. (2-tailed): p-value
        - Mean Difference: Difference between means
        - 95% CI: Confidence interval for difference
        
        For Independent t-test:
        - Check Levene's Test first:
          - If Sig > 0.05: Use "Equal variances assumed" row
          - If Sig < 0.05: Use "Equal variances not assumed" row
        ```
        
        ---
        
        #### **R Programming**
        
        **One-Sample t-Test:**
        ```r
        # Data
        data <- c(18, 19, 17, 20, 16, 22, 18, 19, 15, 21)
        
        # One-sample t-test
        t.test(data, mu = 20, alternative = "two.sided")
        
        # One-tailed (less than)
        t.test(data, mu = 20, alternative = "less")
        
        # One-tailed (greater than)
        t.test(data, mu = 20, alternative = "greater")
        ```
        
        **Independent Samples t-Test:**
        ```r
        # Data
        group1 <- c(75, 78, 72, 80, 76, 74, 77, 79, 73, 75)
        group2 <- c(80, 82, 78, 85, 81, 79, 83, 84, 77, 80)
        
        # Independent t-test (equal variances)
        t.test(group1, group2, var.equal = TRUE)
        
        # Welch's t-test (unequal variances)
        t.test(group1, group2, var.equal = FALSE)
        
        # Test for equal variances first
        var.test(group1, group2)  # F-test
        ```
        
        **Paired Samples t-Test:**
        ```r
        # Data
        before <- c(65, 70, 68, 72, 66, 69, 71, 67, 70, 68)
        after <- c(72, 75, 74, 78, 71, 76, 77, 73, 78, 76)
        
        # Paired t-test
        t.test(after, before, paired = TRUE)
        
        # Or with differences
        diff <- after - before
        t.test(diff, mu = 0)
        ```
        
        **Effect Size (Cohen's d):**
        ```r
        # Install package
        install.packages("effsize")
        library(effsize)
        
        # For independent samples
        cohen.d(group1, group2)
        
        # For paired samples
        cohen.d(after, before, paired = TRUE)
        ```
        
        ---
        
        #### **Excel**
        
        **Using Data Analysis ToolPak:**
        
        1. Data → Data Analysis → t-Test
        2. Choose type:
           - t-Test: Paired Two Sample for Means
           - t-Test: Two-Sample Assuming Equal Variances
           - t-Test: Two-Sample Assuming Unequal Variances
        3. Enter variable ranges
        4. Enter hypothesized mean difference (usually 0)
        5. Set alpha (0.05)
        6. Click OK
        
        **Using Formulas:**
        ```excel
        // One-sample t-test
        =T.TEST(range, hypothesized_mean, tails, type)
        // Example: =T.TEST(A1:A25, 20, 2, 1)
        // tails: 1 = one-tailed, 2 = two-tailed
        // type: 1 = paired, 2 = equal variance, 3 = unequal variance
        
        // Calculate t-statistic manually
        =(AVERAGE(A1:A25) - 20) / (STDEV.S(A1:A25) / SQRT(COUNT(A1:A25)))
        
        // Calculate p-value
        =T.DIST.2T(ABS(t_statistic), df)  // Two-tailed
        =T.DIST.RT(t_statistic, df)       // One-tailed (right)
        ```
        
        ---
        
        #### **Python (scipy)**
        
        ```python
        import numpy as np
        from scipy import stats
        
        # One-sample t-test
        data = [18, 19, 17, 20, 16, 22, 18, 19, 15, 21]
        t_stat, p_value = stats.ttest_1samp(data, 20)
        print(f"t = {t_stat:.3f}, p = {p_value:.3f}")
        
        # Independent samples t-test
        group1 = [75, 78, 72, 80, 76, 74, 77, 79, 73, 75]
        group2 = [80, 82, 78, 85, 81, 79, 83, 84, 77, 80]
        t_stat, p_value = stats.ttest_ind(group1, group2)
        print(f"t = {t_stat:.3f}, p = {p_value:.3f}")
        
        # Paired samples t-test
        before = [65, 70, 68, 72, 66, 69, 71, 67, 70, 68]
        after = [72, 75, 74, 78, 71, 76, 77, 73, 78, 76]
        t_stat, p_value = stats.ttest_rel(after, before)
        print(f"t = {t_stat:.3f}, p = {p_value:.3f}")
        
        # Effect size (Cohen's d)
        def cohens_d(group1, group2):
            n1, n2 = len(group1), len(group2)
            var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
            pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
            return (np.mean(group1) - np.mean(group2)) / pooled_std
        
        d = cohens_d(group1, group2)
        print(f"Cohen's d = {d:.3f}")
        ```
        """)
    
    with st.expander("📊 APA-Style Reporting Guide for t-Tests", expanded=True):
        st.markdown("""
        ### Complete APA Reporting Templates
        
        #### **One-Sample t-Test**
        
        **Template:**
        > "A one-sample t-test was conducted to compare [variable] to [test value]. 
        > [Sample description] (M = [mean], SD = [SD], n = [n]) [was/was not] significantly 
        > different from [test value], t([df]) = [t-value], p = [p-value], d = [effect size], 
        > 95% CI [[lower], [upper]]."
        
        **Example:**
        > "A one-sample t-test was conducted to determine whether students' study hours differed 
        > from the claimed 20 hours per week. Students (M = 18.5, SD = 4.2, n = 25) studied 
        > significantly less than 20 hours, t(24) = -1.79, p = .043, d = -0.36, 95% CI [16.77, 20.23]."
        
        ---
        
        #### **Independent Samples t-Test**
        
        **Template:**
        > "An independent samples t-test was conducted to compare [variable] between [group 1] and 
        > [group 2]. [Assumption checks]. [Group 1] (M = [mean], SD = [SD], n = [n]) [did/did not] 
        > differ significantly from [Group 2] (M = [mean], SD = [SD], n = [n]), t([df]) = [t-value], 
        > p = [p-value], d = [effect size], 95% CI [[lower], [upper]]."
        
        **Example:**
        > "An independent samples t-test was conducted to compare math scores between males and females. 
        > Levene's test indicated equal variances (F = 1.44, p = .235). Males (M = 75, SD = 10, n = 30) 
        > did not differ significantly from females (M = 80, SD = 12, n = 30), t(58) = -1.75, p = .085, 
        > d = -0.45, 95% CI [-10.72, 0.72]."
        
        ---
        
        #### **Paired Samples t-Test**
        
        **Template:**
        > "A paired samples t-test was conducted to evaluate the impact of [intervention] on [variable]. 
        > There was a statistically significant [increase/decrease] from [Time 1] (M = [mean], SD = [SD]) 
        > to [Time 2] (M = [mean], SD = [SD]), t([df]) = [t-value], p = [p-value], d = [effect size], 
        > 95% CI [[lower], [upper]]."
        
        **Example:**
        > "A paired samples t-test was conducted to evaluate the impact of a training program on employee 
        > productivity. There was a statistically significant increase from pre-training (M = 68.6, SD = 2.27) 
        > to post-training (M = 75.0, SD = 2.58), t(9) = 18.71, p < .001, d = 5.93, 95% CI [5.63, 7.17]."
        
        ---
        
        ### **Reporting Checklist**
        
        ✅ **Always Include:**
        - [ ] Type of t-test used
        - [ ] Descriptive statistics (M, SD, n) for each group
        - [ ] t-statistic with degrees of freedom: t(df)
        - [ ] Exact p-value (or p < .001 if very small)
        - [ ] Effect size (Cohen's d)
        - [ ] 95% confidence interval
        - [ ] Direction of effect (which group higher/lower)
        
        ✅ **For Independent t-Test, Also Include:**
        - [ ] Levene's test results (F, p)
        - [ ] Which variance assumption used
        
        ✅ **For Paired t-Test, Also Include:**
        - [ ] Mean difference and SD of differences
        - [ ] Both time points described
        
        ---
        
        ### **Effect Size Interpretation**
        
        | Cohen's d | Interpretation | Example |
        |-----------|----------------|---------|
        | \|d\| < 0.2 | Negligible | Practically no difference |
        | 0.2 ≤ \|d\| < 0.5 | Small | Noticeable but small |
        | 0.5 ≤ \|d\| < 0.8 | Medium | Moderate difference |
        | \|d\| ≥ 0.8 | Large | Substantial difference |
        | \|d\| ≥ 1.2 | Very large | Very substantial |
        
        ---
        
        ### **Common Reporting Mistakes**
        
        | Mistake | Correct |
        |---------|---------|
        | ❌ "The groups were significantly different" | ✅ "t(58) = -1.75, p = .085" (report statistics) |
        | ❌ "p = 0.000" | ✅ "p < .001" (never report p = 0) |
        | ❌ Only reporting p-value | ✅ Report t, df, p, d, and CI |
        | ❌ "Accepted the null hypothesis" | ✅ "Failed to reject the null hypothesis" |
        | ❌ No effect size | ✅ Always include Cohen's d |
        | ❌ "Proved there's no difference" | ✅ "No significant difference was found" |
        | ❌ Ignoring assumptions | ✅ Report Levene's test for independent t-test |
        """)


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
    
    with st.expander("📚 ANOVA: 3 Complete Worked Examples", expanded=True):
        st.markdown("""
        ### One-Way ANOVA - Complete Tutorial
        
        Master ANOVA through detailed, step-by-step examples.
        
        ---
        #### **Example 1: Comparing Three Diets** (Health)
        
        **Problem:**
        Compare weight loss (kg) across three diet plans after 8 weeks.
        - Diet A: 5, 6, 4, 7, 5, 6 (n₁ = 6)
        - Diet B: 8, 9, 7, 10, 8, 9 (n₂ = 6)
        - Diet C: 3, 4, 2, 5, 3, 4 (n₃ = 6)
        
        **Step 1: Calculate Group Means**
        ```
        x̄₁ (Diet A) = (5+6+4+7+5+6)/6 = 5.5 kg
        x̄₂ (Diet B) = (8+9+7+10+8+9)/6 = 8.5 kg
        x̄₃ (Diet C) = (3+4+2+5+3+4)/6 = 3.5 kg
        
        Grand Mean (x̄) = (5.5+8.5+3.5)/3 = 5.83 kg
        ```
        
        **Step 2: Calculate Sum of Squares**
        
        **Between Groups (SS_B):**
        ```
        SS_B = Σnᵢ(x̄ᵢ - x̄)²
        SS_B = 6(5.5-5.83)² + 6(8.5-5.83)² + 6(3.5-5.83)²
        SS_B = 6(0.11) + 6(7.13) + 6(5.43)
        SS_B = 0.66 + 42.78 + 32.58
        SS_B = 76.02
        ```
        
        **Within Groups (SS_W):**
        ```
        Diet A: (5-5.5)² + (6-5.5)² + (4-5.5)² + (7-5.5)² + (5-5.5)² + (6-5.5)²
              = 0.25 + 0.25 + 2.25 + 2.25 + 0.25 + 0.25 = 5.5
        
        Diet B: (8-8.5)² + (9-8.5)² + (7-8.5)² + (10-8.5)² + (8-8.5)² + (9-8.5)²
              = 0.25 + 0.25 + 2.25 + 2.25 + 0.25 + 0.25 = 5.5
        
        Diet C: (3-3.5)² + (4-3.5)² + (2-3.5)² + (5-3.5)² + (3-3.5)² + (4-3.5)²
              = 0.25 + 0.25 + 2.25 + 2.25 + 0.25 + 0.25 = 5.5
        
        SS_W = 5.5 + 5.5 + 5.5 = 16.5
        ```
        
        **Total (SS_T):**
        ```
        SS_T = SS_B + SS_W = 76.02 + 16.5 = 92.52
        ```
        
        **Step 3: Calculate Degrees of Freedom**
        ```
        df_between = k - 1 = 3 - 1 = 2
        df_within = N - k = 18 - 3 = 15
        df_total = N - 1 = 18 - 1 = 17
        ```
        
        **Step 4: Calculate Mean Squares**
        ```
        MS_B = SS_B / df_between = 76.02 / 2 = 38.01
        MS_W = SS_W / df_within = 16.5 / 15 = 1.10
        ```
        
        **Step 5: Calculate F-statistic**
        ```
        F = MS_B / MS_W = 38.01 / 1.10 = 34.55
        ```
        
        **Step 6: Decision**
        ```
        F_critical (df₁=2, df₂=15, α=0.05) = 3.68
        F = 34.55 > 3.68 → Reject H₀
        p < 0.001
        ```
        
        **Step 7: Effect Size (Eta-squared, η²)**
        ```
        η² = SS_B / SS_T = 76.02 / 92.52 = 0.82
        
        Interpretation: 82% of variance in weight loss is explained by diet type (Very large effect)
        
        η² interpretation:
        - 0.01: Small
        - 0.06: Medium
        - 0.14: Large
        ```
        
        **Step 8: Post-hoc Tests (Tukey's HSD)**
        ```
        HSD = q × √(MS_W / n)
        q (k=3, df=15, α=0.05) = 3.67
        
        HSD = 3.67 × √(1.10 / 6) = 3.67 × 0.428 = 1.57
        
        Pairwise Comparisons:
        |x̄₁ - x̄₂| = |5.5 - 8.5| = 3.0 > 1.57 → Significant
        |x̄₁ - x̄₃| = |5.5 - 3.5| = 2.0 > 1.57 → Significant
        |x̄₂ - x̄₃| = |8.5 - 3.5| = 5.0 > 1.57 → Significant
        
        All three diets differ significantly from each other.
        Diet B > Diet A > Diet C
        ```
        
        **ANOVA Table:**
        ```
        ┌────────────┬──────┬────┬──────┬───────┬─────────┐
        │ Source     │  SS  │ df │  MS  │   F   │    p    │
        ├────────────┼──────┼────┼──────┼───────┼─────────┤
        │ Between    │76.02 │ 2  │38.01 │ 34.55 │ < .001  │
        │ Within     │16.50 │ 15 │ 1.10 │       │         │
        │ Total      │92.52 │ 17 │      │       │         │
        └────────────┴──────┴────┴──────┴───────┴─────────┘
        ```
        
        **Conclusion:**
        "There was a significant difference in weight loss across the three diets, 
        F(2, 15) = 34.55, p < .001, η² = 0.82. Post-hoc comparisons using Tukey's HSD 
        indicated that Diet B (M = 8.5 kg, SD = 1.05) resulted in significantly more 
        weight loss than both Diet A (M = 5.5 kg, SD = 0.96, p < .001) and Diet C 
        (M = 3.5 kg, SD = 0.96, p < .001). Diet A also produced significantly more 
        weight loss than Diet C (p < .001)."
        
        **SPSS Output:**
        ```
        Descriptives
        ┌──────┬───┬──────┬─────────┬──────────┐
        │ Diet │ N │ Mean │ Std Dev │ Std Error│
        ├──────┼───┼──────┼─────────┼──────────┤
        │  A   │ 6 │ 5.50 │  0.96   │   0.39   │
        │  B   │ 6 │ 8.50 │  1.05   │   0.43   │
        │  C   │ 6 │ 3.50 │  0.96   │   0.39   │
        │Total │18 │ 5.83 │  2.35   │   0.55   │
        └──────┴───┴──────┴─────────┴──────────┘
        
        ANOVA
        ┌────────────┬──────┬────┬──────┬───────┬─────┐
        │            │  SS  │ df │  MS  │   F   │ Sig │
        ├────────────┼──────┼────┼──────┼───────┼─────┤
        │Between Grps│76.02 │ 2  │38.01 │ 34.55 │.000 │
        │Within Grps │16.50 │ 15 │ 1.10 │       │     │
        │Total       │92.52 │ 17 │      │       │     │
        └────────────┴──────┴────┴──────┴───────┴─────┘
        
        Post Hoc Tests (Tukey HSD)
        ┌──────────┬──────────┬──────────┬─────┐
        │  (I)     │   (J)    │   Mean   │ Sig │
        │  Diet    │   Diet   │   Diff   │     │
        ├──────────┼──────────┼──────────┼─────┤
        │    A     │    B     │  -3.00*  │.000 │
        │    A     │    C     │   2.00*  │.001 │
        │    B     │    C     │   5.00*  │.000 │
        └──────────┴──────────┴──────────┴─────┘
        * The mean difference is significant at the 0.05 level.
        ```
        
        **R Code:**
        ```r
        # Data
        weight_loss <- c(5,6,4,7,5,6, 8,9,7,10,8,9, 3,4,2,5,3,4)
        diet <- factor(rep(c("A","B","C"), each=6))
        
        # One-way ANOVA
        model <- aov(weight_loss ~ diet)
        summary(model)
        
        # Effect size
        library(effectsize)
        eta_squared(model)
        
        # Post-hoc Tukey's HSD
        TukeyHSD(model)
        
        # Visualize
        boxplot(weight_loss ~ diet, main="Weight Loss by Diet",
                xlab="Diet", ylab="Weight Loss (kg)")
        ```
        
        ---
        #### **Example 2: Teaching Methods** (Education)
        
        **Problem:**
        Compare test scores across four teaching methods.
        - Method 1: 75, 78, 72, 80, 76 (n=5)
        - Method 2: 85, 88, 82, 90, 87 (n=5)
        - Method 3: 70, 73, 68, 75, 71 (n=5)
        - Method 4: 80, 83, 78, 85, 82 (n=5)
        
        **Quick Calculation:**
        ```
        Means: x̄₁=76.2, x̄₂=86.4, x̄₃=71.4, x̄₄=81.6
        Grand Mean: 78.9
        
        SS_B = 5[(76.2-78.9)² + (86.4-78.9)² + (71.4-78.9)² + (81.6-78.9)²]
             = 5[7.29 + 56.25 + 56.25 + 7.29] = 636.4
        
        SS_W = 74 (calculated from individual deviations)
        
        MS_B = 636.4/3 = 212.13
        MS_W = 74/16 = 4.625
        
        F = 212.13/4.625 = 45.87
        p < 0.001
        η² = 0.90 (Very large)
        ```
        
        **Conclusion:**
        "Teaching method significantly affected test scores, F(3, 16) = 45.87, p < .001, η² = 0.90."
        
        ---
        #### **Example 3: Drug Effectiveness** (Medicine)
        
        **Problem:**
        Compare pain reduction across three drugs.
        - Drug A: 6, 7, 5, 8, 6, 7 (n=6)
        - Drug B: 4, 5, 3, 6, 4, 5 (n=6)
        - Drug C: 8, 9, 7, 10, 8, 9 (n=6)
        
        **Calculation:**
        ```
        Means: x̄₁=6.5, x̄₂=4.5, x̄₃=8.5
        
        F = 48.00, df=(2,15)
        p < 0.001
        η² = 0.86
        
        Post-hoc: Drug C > Drug A > Drug B (all p < 0.001)
        ```
        
        **Conclusion:**
        "Drug type significantly affected pain reduction, F(2, 15) = 48.00, p < .001, η² = 0.86. 
        Drug C was most effective."
        
        ---
        ### **Software Implementation**
        
        **SPSS:**
        ```
        1. Analyze → Compare Means → One-Way ANOVA
        2. Move dependent variable to "Dependent List"
        3. Move grouping variable to "Factor"
        4. Click "Post Hoc" → Select "Tukey" → Continue
        5. Click "Options" → Check "Descriptive" and "Homogeneity of variance test"
        6. Click OK
        ```
        
        **R:**
        ```r
        # One-way ANOVA
        model <- aov(outcome ~ group, data = mydata)
        summary(model)
        
        # Check assumptions
        # 1. Normality
        shapiro.test(residuals(model))
        
        # 2. Homogeneity of variance
        library(car)
        leveneTest(outcome ~ group, data = mydata)
        
        # Effect size
        library(effectsize)
        eta_squared(model)
        omega_squared(model)
        
        # Post-hoc tests
        TukeyHSD(model)
        
        # Or Bonferroni
        pairwise.t.test(mydata$outcome, mydata$group, p.adjust.method = "bonferroni")
        ```
        
        **Python:**
        ```python
        from scipy import stats
        import pandas as pd
        from statsmodels.stats.multicomp import pairwise_tukeyhsd
        
        # One-way ANOVA
        f_stat, p_value = stats.f_oneway(group1, group2, group3)
        
        # Post-hoc Tukey HSD
        data = pd.DataFrame({'value': values, 'group': groups})
        tukey = pairwise_tukeyhsd(data['value'], data['group'])
        print(tukey)
        ```
        
        ---
        ### **APA-Style Reporting**
        
        **Template:**
        > "A one-way ANOVA was conducted to compare [variable] across [k] groups. 
        > There was a statistically significant difference, F([df₁], [df₂]) = [F-value], 
        > p = [p-value], η² = [effect size]. Post-hoc comparisons using [test name] 
        > indicated that [specific findings]."
        
        **Complete Example:**
        > "A one-way ANOVA was conducted to compare weight loss across three diet plans. 
        > There was a statistically significant difference in weight loss between the diets, 
        > F(2, 15) = 34.55, p < .001, η² = 0.82. Post-hoc comparisons using Tukey's HSD test 
        > indicated that the mean weight loss for Diet B (M = 8.5 kg, SD = 1.05) was 
        > significantly greater than both Diet A (M = 5.5 kg, SD = 0.96, p < .001) and 
        > Diet C (M = 3.5 kg, SD = 0.96, p < .001). Diet A also resulted in significantly 
        > more weight loss than Diet C (p < .001)."
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
    
    with st.expander("📚 K-S Test: Complete Tutorial with Examples", expanded=True):
        st.markdown("""
        ### Kolmogorov-Smirnov Test - Deep Dive
        
        The K-S test is one of the most important tests for checking if your data follows a specific distribution.
        
        ---
        #### **When to Use K-S Test**
        
        ✅ **Use K-S Test When:**
        - Testing if data follows normal distribution (before using parametric tests)
        - Comparing sample distribution to any theoretical distribution
        - Continuous data (not categorical)
        - Any sample size (works well even with small n)
        
        ❌ **Do NOT Use When:**
        - Data is discrete/categorical (use Chi-square instead)
        - Testing normality with small samples (Shapiro-Wilk is better for n < 50)
        - Parameters are estimated from data (reduces power)
        
        ---
        #### **Example 1: Testing Normality of Exam Scores** (Education)
        
        **Problem:**
        A teacher has exam scores from 30 students. Before using a t-test, she wants to check if 
        scores are normally distributed.
        
        **Data (sorted):**
        ```
        45, 52, 58, 61, 63, 65, 67, 68, 70, 72, 
        73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 
        84, 85, 86, 87, 88, 89, 90, 92, 94, 96
        ```
        
        **Step 1: Calculate Sample Statistics**
        ```
        Mean (x̄) = 76.5
        SD (s) = 12.3
        n = 30
        ```
        
        **Step 2: For Each Data Point, Calculate:**
        - Empirical CDF: F_n(x) = (number of values ≤ x) / n
        - Theoretical CDF: F(x) = P(Z ≤ (x - μ)/σ) using normal distribution
        - Absolute difference: |F_n(x) - F(x)|
        
        **Step 3: Find Maximum Difference (D)**
        ```
        For x = 70:
        F_n(70) = 9/30 = 0.300
        F(70) = P(Z ≤ (70-76.5)/12.3) = P(Z ≤ -0.53) = 0.298
        |Difference| = |0.300 - 0.298| = 0.002
        
        ... (calculate for all points)
        
        Maximum D = 0.089 (found at x = 80)
        ```
        
        **Step 4: Find Critical Value**
        - For n = 30, α = 0.05
        - D_critical = 1.36/√n = 1.36/√30 = 0.248
        
        **Step 5: Decision**
        - D = 0.089 < 0.248 (critical value)
        - **Fail to reject H₀**
        - p-value = 0.82 > 0.05
        
        **Conclusion:**
        "The exam scores do not significantly deviate from normal distribution 
        (D = 0.089, p = .82). It is appropriate to use parametric tests."
        
        **SPSS Output:**
        ```
        Tests of Normality
        ┌────────────┬─────────────────────────┬─────────────────────────┐
        │            │ Kolmogorov-Smirnov      │ Shapiro-Wilk            │
        │            ├──────┬────┬─────────────┼──────┬────┬─────────────┤
        │            │Stat  │ df │    Sig.     │Stat  │ df │    Sig.     │
        ├────────────┼──────┼────┼─────────────┼──────┼────┼─────────────┤
        │ ExamScores │.089  │ 30 │    .820     │.976  │ 30 │    .715     │
        └────────────┴──────┴────┴─────────────┴──────┴────┴─────────────┘
        
        Note: If Sig. > 0.05, data is normally distributed
        ```
        
        **R Code:**
        ```r
        # Data
        scores <- c(45, 52, 58, 61, 63, 65, 67, 68, 70, 72, 
                    73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 
                    84, 85, 86, 87, 88, 89, 90, 92, 94, 96)
        
        # K-S test for normality
        ks.test(scores, "pnorm", mean = mean(scores), sd = sd(scores))
        
        # Better: Use Shapiro-Wilk for normality
        shapiro.test(scores)
        
        # Visualize
        qqnorm(scores)
        qqline(scores, col = "red")
        ```
        
        ---
        #### **Example 2: Comparing Two Samples** (Quality Control)
        
        **Problem:**
        A factory produces widgets on two machines. Are the weight distributions the same?
        - Machine A: n₁ = 25 widgets
        - Machine B: n₂ = 25 widgets
        
        **Two-Sample K-S Test:**
        
        **Hypotheses:**
        - H₀: Both samples come from the same distribution
        - H₁: Samples come from different distributions
        
        **Data:**
        ```
        Machine A: 98, 99, 100, 101, 102, ... (Mean = 100.2, SD = 2.1)
        Machine B: 99, 100, 101, 102, 103, ... (Mean = 101.5, SD = 2.3)
        ```
        
        **Calculation:**
        ```
        D = max |F_A(x) - F_B(x)| = 0.32
        
        Critical value for n₁ = n₂ = 25, α = 0.05:
        D_critical = 1.36 × √[(n₁ + n₂)/(n₁ × n₂)]
        D_critical = 1.36 × √(50/625) = 0.384
        ```
        
        **Decision:**
        - D = 0.32 < 0.384
        - **Fail to reject H₀**
        - p = 0.12 > 0.05
        
        **Conclusion:**
        "No significant difference in weight distributions between machines 
        (D = 0.32, p = .12)."
        
        **R Code:**
        ```r
        # Two-sample K-S test
        machine_a <- c(98, 99, 100, 101, 102, ...)
        machine_b <- c(99, 100, 101, 102, 103, ...)
        
        ks.test(machine_a, machine_b)
        ```
        
        ---
        #### **Example 3: Testing for Uniform Distribution** (Statistics)
        
        **Problem:**
        A random number generator should produce uniform distribution [0, 1]. 
        Test with 50 generated numbers.
        
        **Data:**
        ```
        0.12, 0.23, 0.34, 0.45, 0.56, ... (50 numbers)
        ```
        
        **Test:**
        ```
        H₀: Data follows uniform distribution U(0,1)
        H₁: Data does not follow uniform distribution
        
        D = 0.095
        D_critical = 1.36/√50 = 0.192
        
        D < D_critical → Fail to reject H₀
        p = 0.78
        ```
        
        **Conclusion:**
        "The random number generator produces values consistent with uniform distribution 
        (D = 0.095, p = .78)."
        
        **R Code:**
        ```r
        # Test for uniform distribution
        random_nums <- runif(50)  # Generate 50 random numbers
        ks.test(random_nums, "punif", 0, 1)
        ```
        
        ---
        ### **K-S Test vs Shapiro-Wilk Test**
        
        | Feature | K-S Test | Shapiro-Wilk |
        |---------|----------|--------------|
        | **Purpose** | Test any distribution | Test normality only |
        | **Power** | Lower for normality | Higher for normality |
        | **Sample Size** | Better for n > 50 | Better for n < 50 |
        | **Sensitivity** | Sensitive to middle | Sensitive to tails |
        | **Recommendation** | Use for large samples or non-normal distributions | Use for testing normality with small samples |
        
        **Best Practice:**
        - For normality testing with n < 50: Use **Shapiro-Wilk**
        - For normality testing with n > 50: Use **K-S** or **Anderson-Darling**
        - For comparing to other distributions: Use **K-S**
        
        ---
        ### **Interpretation Guide**
        
        **p-value Interpretation:**
        - p > 0.05: Data is consistent with the specified distribution (fail to reject H₀)
        - p ≤ 0.05: Data significantly deviates from the specified distribution (reject H₀)
        
        **D-statistic Interpretation:**
        - D close to 0: Good fit
        - D close to 1: Poor fit
        - Typical values: 0.05 - 0.20 for good fit
        
        **Common Mistakes:**
        - ❌ Using K-S when parameters are estimated from data (reduces power)
        - ❌ Using K-S for small samples when testing normality (use Shapiro-Wilk)
        - ❌ Ignoring visual inspection (always plot Q-Q plot)
        - ❌ Over-relying on p-value (also check histogram and Q-Q plot)
        
        ---
        ### **Software Implementation**
        
        **SPSS:**
        ```
        1. Analyze → Descriptive Statistics → Explore
        2. Move variable to "Dependent List"
        3. Click "Plots" → Check "Normality plots with tests"
        4. Click Continue → OK
        
        Output shows both K-S and Shapiro-Wilk tests
        ```
        
        **R:**
        ```r
        # One-sample K-S test (normality)
        ks.test(data, "pnorm", mean(data), sd(data))
        
        # Two-sample K-S test
        ks.test(sample1, sample2)
        
        # Test for other distributions
        ks.test(data, "punif", 0, 1)  # Uniform
        ks.test(data, "pexp", 1/mean(data))  # Exponential
        ```
        
        **Python:**
        ```python
        from scipy import stats
        
        # One-sample K-S test
        stats.kstest(data, 'norm', args=(mean, std))
        
        # Two-sample K-S test
        stats.ks_2samp(sample1, sample2)
        ```
        
        ---
        ### **APA-Style Reporting**
        
        **Template:**
        > "A Kolmogorov-Smirnov test was conducted to assess the normality of [variable]. 
        > The test was [significant/not significant], D([n]) = [D-value], p = [p-value], 
        > indicating that the data [does/does not] significantly deviate from normal distribution."
        
        **Example:**
        > "A Kolmogorov-Smirnov test was conducted to assess the normality of exam scores. 
        > The test was not significant, D(30) = 0.089, p = .82, indicating that the data 
        > does not significantly deviate from normal distribution. Therefore, parametric 
        > tests are appropriate for this dataset."
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
    
    with st.expander("📚 Run Test: Complete Tutorial with Examples", expanded=True):
        st.markdown("""
        ### Run Test - Testing for Randomness
        
        The Run Test checks if a sequence is random or has patterns.
        
        ---
        #### **When to Use Run Test**
        
        ✅ **Use Run Test When:**
        - Testing if a sequence is random
        - Checking quality control processes
        - Detecting patterns in time series
        - Validating random number generators
        - Testing coin flip fairness
        
        ❌ **Do NOT Use When:**
        - Data is not sequential
        - Sample size is very small (n < 10)
        
        ---
        #### **Example 1: Coin Flip Randomness** (Statistics)
        
        **Problem:**
        A coin is flipped 20 times. Is the sequence random?
        
        **Data:**
        ```
        H T T H H H T H T T H T H H T T T H H T
        ```
        
        **Step 1: Convert to Binary**
        ```
        Above median (H) = +
        Below median (T) = -
        
        Sequence: + - - + + + - + - - + - + + - - - + + -
        ```
        
        **Step 2: Count Runs**
        ```
        Run 1: +           (1 element)
        Run 2: - -         (2 elements)
        Run 3: + + +       (3 elements)
        Run 4: -           (1 element)
        Run 5: +           (1 element)
        Run 6: - -         (2 elements)
        Run 7: +           (1 element)
        Run 8: -           (1 element)
        Run 9: + +         (2 elements)
        Run 10: - - -      (3 elements)
        Run 11: + +        (2 elements)
        Run 12: -          (1 element)
        
        Total runs (R) = 12
        n₁ = 10 (number of H)
        n₂ = 10 (number of T)
        ```
        
        **Step 3: Calculate Expected Runs**
        ```
        μᵣ = (2n₁n₂)/(n₁+n₂) + 1
        μᵣ = (2 × 10 × 10)/(10+10) + 1
        μᵣ = 200/20 + 1 = 11
        
        σᵣ = √[(2n₁n₂(2n₁n₂ - n₁ - n₂)) / ((n₁+n₂)²(n₁+n₂-1))]
        σᵣ = √[(200(200-20)) / (400 × 19)]
        σᵣ = √[36000/7600] = 2.17
        ```
        
        **Step 4: Calculate z-statistic**
        ```
        z = (R - μᵣ) / σᵣ
        z = (12 - 11) / 2.17
        z = 0.46
        ```
        
        **Step 5: Decision**
        ```
        Critical values: ±1.96 (α = 0.05, two-tailed)
        |z| = 0.46 < 1.96
        Fail to reject H₀
        p = 0.65 > 0.05
        ```
        
        **Conclusion:**
        "The coin flip sequence is random (R = 12, z = 0.46, p = .65). 
        No evidence of pattern or bias."
        
        **R Code:**
        ```r
        # Install package
        library(randtests)
        
        # Data
        flips <- c(1,0,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0)
        
        # Run test
        runs.test(flips)
        ```
        
        ---
        #### **Example 2: Quality Control - Defective Products** (Manufacturing)
        
        **Problem:**
        A production line produces 30 items. D = defective, G = good. 
        Is the defect pattern random?
        
        **Data:**
        ```
        G G D G G G D D G G G G D G G D G G G G 
        D D G G G D G G G G
        
        n₁ = 7 (defective)
        n₂ = 23 (good)
        ```
        
        **Count Runs:**
        ```
        Run 1: G G         (2 good)
        Run 2: D           (1 defective)
        Run 3: G G G       (3 good)
        Run 4: D D         (2 defective)
        Run 5: G G G G     (4 good)
        Run 6: D           (1 defective)
        Run 7: G G         (2 good)
        Run 8: D           (1 defective)
        Run 9: G G G G     (4 good)
        Run 10: D D        (2 defective)
        Run 11: G G G      (3 good)
        Run 12: D          (1 defective)
        Run 13: G G G G    (4 good)
        
        Total runs (R) = 13
        ```
        
        **Calculate:**
        ```
        μᵣ = (2 × 7 × 23)/(7+23) + 1 = 11.77
        σᵣ = 2.28
        
        z = (13 - 11.77) / 2.28 = 0.54
        
        |z| = 0.54 < 1.96
        p = 0.59
        ```
        
        **Conclusion:**
        "Defects occur randomly (R = 13, z = 0.54, p = .59). 
        No systematic pattern detected."
        
        ---
        #### **Example 3: Stock Price Movements** (Finance)
        
        **Problem:**
        Stock prices for 25 days: Are up/down movements random?
        
        **Data:**
        ```
        + + - + - - - + + + - + - - + + - - - + + + - - +
        
        n₁ = 13 (up days)
        n₂ = 12 (down days)
        R = 16 runs
        ```
        
        **Calculate:**
        ```
        μᵣ = (2 × 13 × 12)/(13+12) + 1 = 13.48
        σᵣ = 2.45
        
        z = (16 - 13.48) / 2.45 = 1.03
        
        |z| = 1.03 < 1.96
        p = 0.30
        ```
        
        **Conclusion:**
        "Stock movements are random (R = 16, z = 1.03, p = .30). 
        No trend detected."
        
        ---
        ### **Interpretation Guide**
        
        **z-statistic Interpretation:**
        
        | z-value | Runs | Interpretation | Meaning |
        |---------|------|----------------|---------|
        | z < -1.96 | Too few | **Clustering** | Values tend to group together |
        | -1.96 ≤ z ≤ 1.96 | Expected | **Random** | No pattern detected |
        | z > 1.96 | Too many | **Alternating** | Values alternate too regularly |
        
        **Examples:**
        - **Too few runs (clustering):** + + + + + - - - - - (only 2 runs)
          - Indicates trend or persistence
          - Quality control: defects come in batches
          
        - **Too many runs (alternating):** + - + - + - + - + - (10 runs)
          - Indicates systematic alternation
          - Quality control: machine switching between states
        
        ---
        ### **Software Implementation**
        
        **SPSS:**
        ```
        1. Analyze → Nonparametric Tests → Legacy Dialogs → Runs
        2. Move variable to "Test Variable List"
        3. Choose cut point:
           - Median (default)
           - Mean
           - Mode
           - Custom value
        4. Click OK
        
        Output shows:
        - Number of runs
        - Test value (cut point)
        - Cases < test value
        - Cases >= test value
        - Z-statistic
        - Asymp. Sig. (2-tailed)
        ```
        
        **R:**
        ```r
        # Install package
        install.packages("randtests")
        library(randtests)
        
        # Binary data (0s and 1s)
        data <- c(1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,0,1)
        runs.test(data)
        
        # Continuous data (test above/below median)
        continuous_data <- c(23, 45, 12, 67, 34, 56, 78, 23, 45, 67)
        runs.test(continuous_data)
        ```
        
        **Python:**
        ```python
        from statsmodels.sandbox.stats.runs import runstest_1samp
        
        # Data
        data = [1,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,0,1]
        
        # Run test
        z_stat, p_value = runstest_1samp(data)
        print(f"z = {z_stat:.3f}, p = {p_value:.3f}")
        ```
        
        ---
        ### **APA-Style Reporting**
        
        **Template:**
        > "A runs test was conducted to assess the randomness of [sequence]. 
        > The test [was/was not] significant (R = [runs], z = [z-value], p = [p-value]), 
        > indicating that the sequence [is/is not] random."
        
        **Example:**
        > "A runs test was conducted to assess the randomness of coin flip outcomes. 
        > The test was not significant (R = 12, z = 0.46, p = .65), indicating that 
        > the sequence is random and shows no evidence of pattern or bias."
        
        ---
        ### **Common Applications**
        
        1. **Quality Control:**
           - Detecting machine malfunctions
           - Identifying batch effects
           - Monitoring process stability
        
        2. **Finance:**
           - Testing market efficiency
           - Detecting trends in stock prices
           - Validating trading strategies
        
        3. **Sports:**
           - Testing if winning/losing streaks are random
           - Analyzing player performance patterns
        
        4. **Research:**
           - Validating random assignment
           - Testing randomness of residuals
           - Checking random number generators
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
    
    with st.expander("📚 Mann-Whitney U Test: Complete Tutorial", expanded=True):
        st.markdown("""
        ### Mann-Whitney U Test - Comparing Two Independent Groups
        
        The non-parametric alternative to independent samples t-test.
        
        ---
        #### **When to Use Mann-Whitney U Test**
        
        ✅ **Use Mann-Whitney U When:**
        - Data is ordinal (ranks, ratings, Likert scales)
        - Data is not normally distributed
        - Extreme outliers present
        - Small sample sizes
        - Comparing two independent groups
        
        ❌ **Use t-test Instead When:**
        - Data is normally distributed
        - Large sample sizes (n > 30 per group)
        - No extreme outliers
        
        ---
        #### **Example 1: Customer Satisfaction Ratings** (Business)
        
        **Problem:**
        Compare customer satisfaction (1-10 scale) between two stores.
        - Store A: 7, 8, 6, 9, 7, 8, 10, 7
        - Store B: 5, 6, 4, 7, 5, 6, 5
        
        **Step 1: Combine and Rank**
        ```
        Combined data (sorted): 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 10
        
        Value | Store | Rank
        ------|-------|------
          4   |   B   |  1
          5   |   B   |  2.5 (tied: average of 2,3,4)
          5   |   B   |  2.5
          5   |   B   |  2.5
          6   |   A   |  6 (tied: average of 5,6,7)
          6   |   B   |  6
          6   |   B   |  6
          7   |   A   |  9.5 (tied: average of 8,9,10,11)
          7   |   A   |  9.5
          7   |   B   |  9.5
          7   |   A   |  9.5
          8   |   A   |  13 (tied: average of 12,13)
          8   |   A   |  13
          9   |   A   |  14
         10   |   A   |  15
        ```
        
        **Step 2: Sum Ranks**
        ```
        Store A ranks: 6 + 9.5 + 9.5 + 9.5 + 13 + 13 + 14 + 15 = 90
        Store B ranks: 1 + 2.5 + 2.5 + 2.5 + 6 + 6 + 9.5 = 30
        
        n₁ = 8 (Store A)
        n₂ = 7 (Store B)
        R₁ = 90
        R₂ = 30
        ```
        
        **Step 3: Calculate U Statistics**
        ```
        U₁ = n₁n₂ + n₁(n₁+1)/2 - R₁
        U₁ = (8)(7) + 8(9)/2 - 90
        U₁ = 56 + 36 - 90 = 2
        
        U₂ = n₁n₂ + n₂(n₂+1)/2 - R₂
        U₂ = (8)(7) + 7(8)/2 - 30
        U₂ = 56 + 28 - 30 = 54
        
        Check: U₁ + U₂ = 2 + 54 = 56 = n₁n₂ ✓
        ```
        
        **Step 4: Decision**
        ```
        Use smaller U = 2
        Critical value (n₁=8, n₂=7, α=0.05, two-tailed) = 8
        
        U = 2 < 8 → Reject H₀
        p < 0.05
        ```
        
        **Step 5: Effect Size**
        ```
        Convert to z-score for large samples:
        z = (U - μᵤ) / σᵤ
        μᵤ = n₁n₂/2 = 56/2 = 28
        σᵤ = √[n₁n₂(n₁+n₂+1)/12] = √[56(16)/12] = 8.62
        
        z = (2 - 28) / 8.62 = -3.02
        
        Effect size r = |z|/√N = 3.02/√15 = 0.78 (Large)
        ```
        
        **Conclusion:**
        "Store A had significantly higher satisfaction ratings (Mdn = 7.5) than Store B (Mdn = 5), 
        U = 2, z = -3.02, p = .003, r = 0.78."
        
        **SPSS Output:**
        ```
        Ranks
        ┌───────┬─────┬───┬──────────┐
        │ Store │  N  │Mean Rank│Sum of Ranks│
        ├───────┼─────┼─────────┼──────────┤
        │   A   │  8  │  11.25  │   90.00  │
        │   B   │  7  │   4.29  │   30.00  │
        │ Total │ 15  │         │          │
        └───────┴─────┴─────────┴──────────┘
        
        Test Statistics
        ┌──────────────────┬────────┐
        │ Mann-Whitney U   │  2.000 │
        │ Wilcoxon W       │ 30.000 │
        │ Z                │ -3.016 │
        │ Asymp. Sig.(2-t) │  .003  │
        └──────────────────┴────────┘
        ```
        
        **R Code:**
        ```r
        store_a <- c(7, 8, 6, 9, 7, 8, 10, 7)
        store_b <- c(5, 6, 4, 7, 5, 6, 5)
        
        # Mann-Whitney U test
        wilcox.test(store_a, store_b, exact = FALSE)
        
        # Effect size
        library(rstatix)
        wilcox_effsize(data.frame(value = c(store_a, store_b),
                                   group = c(rep("A", 8), rep("B", 7))),
                       value ~ group)
        ```
        
        ---
        #### **Example 2: Pain Relief Medication** (Medicine)
        
        **Problem:**
        Compare pain reduction (0-10 scale) between Drug A and Placebo.
        - Drug A (n=12): 8, 7, 9, 6, 8, 7, 9, 8, 7, 8, 9, 7
        - Placebo (n=12): 4, 5, 3, 6, 4, 5, 4, 6, 5, 4, 5, 6
        
        **Calculation:**
        ```
        R₁ (Drug A) = 234
        R₂ (Placebo) = 66
        
        U₁ = 12(12) + 12(13)/2 - 234 = 144 + 78 - 234 = -12 (error, recalculate)
        Actually: U₁ = 6, U₂ = 138
        
        U = 6 < critical value (37)
        p < 0.001
        r = 0.85 (Very large effect)
        ```
        
        **Conclusion:**
        "Drug A produced significantly greater pain relief (Mdn = 8) than placebo (Mdn = 5), 
        U = 6, p < .001, r = 0.85."
        
        ---
        ### **APA-Style Reporting**
        
        **Template:**
        > "A Mann-Whitney U test was conducted to compare [variable] between [group 1] and [group 2]. 
        > [Group 1] (Mdn = [median], n = [n]) [was/was not] significantly different from 
        > [Group 2] (Mdn = [median], n = [n]), U = [U-value], z = [z-value], p = [p-value], r = [effect size]."
        
        **Example:**
        > "A Mann-Whitney U test was conducted to compare customer satisfaction between Store A and Store B. 
        > Store A (Mdn = 7.5, n = 8) had significantly higher satisfaction than Store B (Mdn = 5, n = 7), 
        > U = 2, z = -3.02, p = .003, r = 0.78."
        """)
    
    with st.expander("📚 Kruskal-Wallis Test: Complete Tutorial", expanded=True):
        st.markdown("""
        ### Kruskal-Wallis H Test - Comparing 3+ Independent Groups
        
        The non-parametric alternative to one-way ANOVA.
        
        ---
        #### **When to Use Kruskal-Wallis Test**
        
        ✅ **Use Kruskal-Wallis When:**
        - Comparing 3 or more independent groups
        - Data is ordinal
        - Data is not normally distributed
        - Extreme outliers present
        - Unequal variances
        
        ❌ **Use ANOVA Instead When:**
        - Data is normally distributed
        - Equal variances (Levene's test p > 0.05)
        - Large sample sizes
        
        ---
        #### **Example 1: Teaching Methods Comparison** (Education)
        
        **Problem:**
        Compare exam scores across three teaching methods.
        - Method A: 85, 88, 82, 90, 87, 86
        - Method B: 78, 75, 80, 77, 79, 76
        - Method C: 92, 95, 90, 93, 94, 91
        
        **Step 1: Combine and Rank**
        ```
        All scores sorted: 75, 76, 77, 78, 79, 80, 82, 85, 86, 87, 88, 90, 90, 91, 92, 93, 94, 95
        
        Score | Method | Rank
        ------|--------|------
         75   |   B    |  1
         76   |   B    |  2
         77   |   B    |  3
         78   |   B    |  4
         79   |   B    |  5
         80   |   B    |  6
         82   |   A    |  7
         85   |   A    |  8
         86   |   A    |  9
         87   |   A    |  10
         88   |   A    |  11
         90   |   A    |  12.5 (tied)
         90   |   C    |  12.5
         91   |   C    |  14
         92   |   C    |  15
         93   |   C    |  16
         94   |   C    |  17
         95   |   C    |  18
        ```
        
        **Step 2: Sum Ranks**
        ```
        R₁ (Method A) = 7 + 8 + 9 + 10 + 11 + 12.5 = 57.5
        R₂ (Method B) = 1 + 2 + 3 + 4 + 5 + 6 = 21
        R₃ (Method C) = 12.5 + 14 + 15 + 16 + 17 + 18 = 92.5
        
        n₁ = n₂ = n₃ = 6
        N = 18
        ```
        
        **Step 3: Calculate H Statistic**
        ```
        H = [12/(N(N+1))] × Σ(R²ᵢ/nᵢ) - 3(N+1)
        
        H = [12/(18×19)] × [(57.5²/6) + (21²/6) + (92.5²/6)] - 3(19)
        H = [12/342] × [551.04 + 73.5 + 1425.04] - 57
        H = 0.0351 × 2049.58 - 57
        H = 71.94 - 57
        H = 14.94
        ```
        
        **Step 4: Decision**
        ```
        df = k - 1 = 3 - 1 = 2
        χ²_critical (df=2, α=0.05) = 5.991
        
        H = 14.94 > 5.991 → Reject H₀
        p < 0.001
        ```
        
        **Step 5: Post-hoc Tests (Dunn's Test)**
        ```
        Compare all pairs:
        A vs B: p = 0.032 (significant)
        A vs C: p = 0.018 (significant)
        B vs C: p < 0.001 (significant)
        
        Conclusion: All three methods differ significantly
        Method C > Method A > Method B
        ```
        
        **Conclusion:**
        "There was a significant difference in exam scores across teaching methods, 
        H(2) = 14.94, p < .001. Post-hoc tests revealed Method C (Mdn = 92.5) > 
        Method A (Mdn = 86.5) > Method B (Mdn = 78.5), all p < 0.05."
        
        **SPSS Output:**
        ```
        Ranks
        ┌────────┬───┬──────────┐
        │ Method │ N │Mean Rank │
        ├────────┼───┼──────────┤
        │   A    │ 6 │   9.58   │
        │   B    │ 6 │   3.50   │
        │   C    │ 6 │  15.42   │
        │ Total  │18 │          │
        └────────┴───┴──────────┘
        
        Test Statistics
        ┌──────────────────┬────────┐
        │ Kruskal-Wallis H │ 14.940 │
        │ df               │    2   │
        │ Asymp. Sig.      │  .001  │
        └──────────────────┴────────┘
        ```
        
        **R Code:**
        ```r
        # Data
        scores <- c(85,88,82,90,87,86, 78,75,80,77,79,76, 92,95,90,93,94,91)
        method <- factor(rep(c("A","B","C"), each=6))
        
        # Kruskal-Wallis test
        kruskal.test(scores ~ method)
        
        # Post-hoc Dunn's test
        library(dunn.test)
        dunn.test(scores, method, method="bonferroni")
        ```
        
        ---
        #### **Example 2: Drug Dosage Comparison** (Medicine)
        
        **Problem:**
        Compare recovery time (days) across four drug dosages.
        - Low (n=8): 12, 14, 13, 15, 14, 13, 16, 14
        - Medium (n=8): 10, 11, 9, 12, 10, 11, 10, 12
        - High (n=8): 7, 8, 6, 9, 7, 8, 7, 9
        - Placebo (n=8): 18, 20, 19, 21, 19, 20, 18, 22
        
        **Calculation:**
        ```
        R₁ (Low) = 172
        R₂ (Medium) = 124
        R₃ (High) = 60
        R₄ (Placebo) = 244
        
        N = 32
        H = 24.73
        df = 3
        p < 0.001
        ```
        
        **Post-hoc:**
        ```
        High < Medium < Low < Placebo (all p < 0.05)
        ```
        
        **Conclusion:**
        "Drug dosage significantly affected recovery time, H(3) = 24.73, p < .001. 
        Higher dosages resulted in faster recovery."
        
        ---
        ### **Software Implementation**
        
        **SPSS:**
        ```
        1. Analyze → Nonparametric Tests → Legacy Dialogs → K Independent Samples
        2. Move dependent variable to "Test Variable List"
        3. Move grouping variable to "Grouping Variable"
        4. Click "Define Range" → Enter min and max group codes
        5. Check "Kruskal-Wallis H"
        6. Click OK
        ```
        
        **R:**
        ```r
        # Kruskal-Wallis test
        kruskal.test(outcome ~ group, data = mydata)
        
        # Post-hoc Dunn's test
        library(dunn.test)
        dunn.test(mydata$outcome, mydata$group, method="bonferroni")
        
        # Or use FSA package
        library(FSA)
        dunnTest(outcome ~ group, data = mydata, method="bonferroni")
        ```
        
        **Python:**
        ```python
        from scipy import stats
        import scikit_posthocs as sp
        
        # Kruskal-Wallis test
        h_stat, p_value = stats.kruskal(group1, group2, group3)
        
        # Post-hoc Dunn's test
        sp.posthoc_dunn([group1, group2, group3], p_adjust='bonferroni')
        ```
        
        ---
        ### **APA-Style Reporting**
        
        **Template:**
        > "A Kruskal-Wallis H test was conducted to compare [variable] across [k] groups. 
        > There was a statistically significant difference, H([df]) = [H-value], p = [p-value]. 
        > Post-hoc pairwise comparisons using Dunn's test with Bonferroni correction revealed 
        > [specific differences]."
        
        **Example:**
        > "A Kruskal-Wallis H test was conducted to compare exam scores across three teaching methods. 
        > There was a statistically significant difference, H(2) = 14.94, p < .001. Post-hoc pairwise 
        > comparisons using Dunn's test with Bonferroni correction revealed that Method C (Mdn = 92.5) 
        > produced significantly higher scores than both Method A (Mdn = 86.5, p = .018) and Method B 
        > (Mdn = 78.5, p < .001). Method A also scored significantly higher than Method B (p = .032)."
        
        ---
        ### **Effect Size for Kruskal-Wallis**
        
        **Epsilon-squared (ε²):**
        ```
        ε² = H / (N² - 1) / (N + 1)
        
        Interpretation:
        - ε² < 0.01: Negligible
        - 0.01 ≤ ε² < 0.06: Small
        - 0.06 ≤ ε² < 0.14: Medium
        - ε² ≥ 0.14: Large
        ```
        
        **For Example 1:**
        ```
        ε² = 14.94 / [(18² - 1) / (18 + 1)]
        ε² = 14.94 / 16.79 = 0.89 (Very large)
        ```
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
# TAB 5: CALCULATORS
# =============================================================================
with tab5:
    st.markdown("## 🧮 Statistical Calculators")
    st.markdown("Use these tools to perform quick calculations for your research.")

    calc_tab1, calc_tab2, calc_tab3 = st.tabs(["Sample Size", "t-Test (One Sample)", "Effect Size"])

    # --- Sample Size Calculator ---
    with calc_tab1:
        st.markdown("### 📏 Sample Size Calculator (Cochran's Formula)")
        st.info("Calculate the minimum sample size required to estimate a population proportion with a specific margin of error and confidence level.")
        
        col1, col2 = st.columns(2)
        with col1:
            conf_level = st.selectbox("Confidence Level", [0.90, 0.95, 0.99], index=1, format_func=lambda x: f"{int(x*100)}%")
            margin_error = st.number_input("Margin of Error (e.g., 0.05 for 5%)", min_value=0.01, max_value=0.20, value=0.05, step=0.01)
        with col2:
            p_prop = st.number_input("Est. Population Proportion (p) - keep 0.5 if unknown", min_value=0.1, max_value=0.9, value=0.5, step=0.1)
            pop_size = st.number_input("Population Size (leave 0 if infinite)", min_value=0, value=0)

        if st.button("Calculate Sample Size"):
            # Z-values
            z_map = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
            z = z_map[conf_level]
            
            # Cochran's Formula: n0 = (Z^2 * p * (1-p)) / e^2
            n0 = (z**2 * p_prop * (1 - p_prop)) / (margin_error**2)
            
            # Finite Population Correction
            if pop_size > 0:
                n = n0 / (1 + ((n0 - 1) / pop_size))
            else:
                n = n0
            
            st.success(f"### Recommended Sample Size: {int(n) + 1}")
            st.markdown(f"**Formula Used:** n = (Z² · p(1-p)) / e²")
            if pop_size > 0:
                st.markdown("*Adjusted for finite population.*")

    # --- T-Test Calculator ---
    with calc_tab2:
        st.markdown("### 📐 One-Sample t-Test Calculator")
        st.info("Compare a sample mean to a hypothesized population mean.")
        
        col1, col2 = st.columns(2)
        with col1:
            sample_mean = st.number_input("Sample Mean (x̄)", value=0.0)
            pop_mean = st.number_input("Hypothesized Mean (μ₀)", value=0.0)
        with col2:
            sample_std = st.number_input("Sample Std Dev (s)", min_value=0.0001, value=1.0)
            n_size = st.number_input("Sample Size (n)", min_value=2, value=30)
            
        if st.button("Calculate t-Statistic"):
            import math
            se = sample_std / math.sqrt(n_size)
            t_stat = (sample_mean - pop_mean) / se
            df = n_size - 1
            
            st.markdown("---")
            st.metric("t-Statistic", f"{t_stat:.4f}")
            st.metric("Degrees of Freedom", df)
            
            st.markdown(f"""
            **Interpretation:**
            - If |t| > 2.045 (approx for df=29, α=0.05), result is significant.
            - Check t-table for exact p-value using df={df}.
            """)

    # --- Effect Size Calculator ---
    with calc_tab3:
        st.markdown("### 📊 Cohen's d Calculator")
        st.info("Calculate the effect size between two independent groups.")
        
        c1, c2 = st.columns(2)
        with c1:
            m1 = st.number_input("Mean Group 1", value=10.0)
            s1 = st.number_input("Std Dev Group 1", value=2.0)
            n1 = st.number_input("n Group 1", min_value=2, value=30)
        with c2:
            m2 = st.number_input("Mean Group 2", value=12.0)
            s2 = st.number_input("Std Dev Group 2", value=2.0)
            n2 = st.number_input("n Group 2", min_value=2, value=30)
            
        if st.button("Calculate Cohen's d"):
            import math
            # Pooled SD
            sp = math.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
            d = (m1 - m2) / sp
            
            st.success(f"### Cohen's d: {d:.3f}")
            
            interp = ""
            abs_d = abs(d)
            if abs_d < 0.2: interp = "Negligible"
            elif abs_d < 0.5: interp = "Small"
            elif abs_d < 0.8: interp = "Medium"
            else: interp = "Large"
            
            st.info(f"**Interpretation:** {interp} effect size")

# =============================================================================
# TAB 6: QUICK REFERENCE
# =============================================================================
with tab6:
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
