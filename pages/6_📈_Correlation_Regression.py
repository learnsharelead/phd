import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Correlation & Regression Analysis | Curve Fitting, Least Squares, Multiple Regression [2024]",
    description="Master correlation and regression for research: Pearson correlation, linear regression, least squares method, Gauss-Markov theorem, multiple regression with formulas and examples.",
    keywords=[
        "correlation analysis",
        "regression analysis",
        "linear regression",
        "least squares method",
        "curve fitting",
        "Gauss-Markov theorem",
        "multiple regression",
        "Pearson correlation",
        "coefficient of determination",
        "R squared",
        "regression assumptions",
        "prediction intervals"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/statistics/regression",
    reading_time=100,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Correlation & Regression", "url": "https://researchethics.dev/statistics/regression"}
    ],
    course_info={
        "name": "Correlation and Regression Analysis - Paper II Unit II",
        "description": "Comprehensive coverage of correlation, regression analysis, curve fitting, and multiple regression for research data analysis.",
        "level": "Doctoral",
        "prerequisites": "Statistical Foundations",
        "teaches": ["Correlation", "Linear Regression", "Multiple Regression", "Curve Fitting", "Gauss-Markov Theorem"],
        "workload": "PT15H",
        "rating": "4.8",
        "rating_count": 612
    }
)
apply_custom_css()
show_top_nav(current_page="Correlation & Regression")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📈 Unit II: Correlation & Regression</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #166534;">Paper II: Statistics and Computer Applications — Understanding relationships in data.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Charts & Tables",
    "🔗 Correlation",
    "📈 Linear Regression",
    "📉 Multiple Regression",
    "📝 Formulas"
])

# =============================================================================
# TAB 1: CHARTS AND TABLES
# =============================================================================
with tab1:
    st.markdown("## 📊 Chapter 1: Charts and Tables")
    
    st.markdown("### 1.1 Data Visualization Fundamentals")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Purpose</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Data Visualization</b> transforms raw data into visual representations that reveal patterns, trends, and relationships that might not be apparent in tabular form.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Map vs Directions</h4>
            <p style="margin: 0 !important; font-size: 13px;">A table is like written directions; a chart is like a map. The map shows relationships at a glance.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📊 Types of Charts", expanded=True):
        st.markdown("""
        | Chart Type | Best For | Example Use |
        |------------|----------|-------------|
        | **Bar Chart** | Comparing categories | Sales by region |
        | **Histogram** | Distribution of continuous data | Age distribution |
        | **Line Chart** | Trends over time | Stock prices |
        | **Scatter Plot** | Relationship between 2 variables | Height vs Weight |
        | **Pie Chart** | Parts of a whole | Market share |
        | **Box Plot** | Distribution summary | Comparing groups |
        | **Heatmap** | Patterns in matrix data | Correlation matrix |
        """)

    with st.expander("📋 Frequency Tables", expanded=True):
        st.markdown("""
        **A frequency table organizes data into classes and shows counts.**
        
        **Components:**
        - Class intervals (bins)
        - Frequency (f) - count in each class
        - Relative frequency (f/n) - proportion
        - Cumulative frequency - running total
        
        **Example:**
        | Test Score | Frequency | Relative Freq | Cumulative |
        |------------|-----------|---------------|------------|
        | 50-59 | 5 | 0.10 | 5 |
        | 60-69 | 12 | 0.24 | 17 |
        | 70-79 | 18 | 0.36 | 35 |
        | 80-89 | 10 | 0.20 | 45 |
        | 90-100 | 5 | 0.10 | 50 |
        | **Total** | **50** | **1.00** | |
        """)

    with st.expander("🎯 Chart Selection Guide", expanded=False):
        st.graphviz_chart("""
        digraph {
            rankdir=TB; 
            node [fontname="Arial", fontsize=10, shape=box, style="rounded,filled"];
            
            start [label="What do you want to show?", fillcolor="#dbeafe", shape=diamond];
            
            comp [label="Comparison", fillcolor="#fef3c7"];
            dist [label="Distribution", fillcolor="#dcfce7"];
            rel [label="Relationship", fillcolor="#f3e8ff"];
            trend [label="Trend over time", fillcolor="#fed7aa"];
            
            bar [label="Bar Chart", fillcolor="#bfdbfe"];
            hist [label="Histogram\\nBox Plot", fillcolor="#bbf7d0"];
            scatter [label="Scatter Plot", fillcolor="#e9d5ff"];
            line [label="Line Chart", fillcolor="#fdba74"];
            
            start -> comp -> bar;
            start -> dist -> hist;
            start -> rel -> scatter;
            start -> trend -> line;
        }
        """)

# =============================================================================
# TAB 2: CORRELATION ANALYSIS
# =============================================================================
with tab2:
    st.markdown("## 🔗 Chapter 2: Correlation Analysis")
    
    st.markdown("### 2.1 What is Correlation?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Correlation</b> measures the strength and direction of the linear relationship between two variables. It ranges from -1 to +1.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Dancing Partners</h4>
            <p style="margin: 0 !important; font-size: 13px;">Correlation is like how well two dancers move together. r = +1 means perfect sync; r = -1 means opposite movement; r = 0 means no coordination.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📐 Pearson Correlation Coefficient (r)", expanded=True):
        st.markdown("**Formula:**")
        st.latex(r"r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2}}")
        
        st.markdown("**Or equivalently:**")
        st.latex(r"r = \frac{n\sum xy - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}")
        
        st.markdown("""
        **Interpretation:**
        
        | r Value | Strength | Direction |
        |---------|----------|-----------|
        | +0.9 to +1.0 | Very strong | Positive |
        | +0.7 to +0.9 | Strong | Positive |
        | +0.5 to +0.7 | Moderate | Positive |
        | +0.3 to +0.5 | Weak | Positive |
        | 0 to ±0.3 | Negligible | — |
        | -0.3 to -0.5 | Weak | Negative |
        | -0.5 to -0.7 | Moderate | Negative |
        | -0.7 to -0.9 | Strong | Negative |
        | -0.9 to -1.0 | Very strong | Negative |
        """)

    with st.expander("📊 Coefficient of Determination (R²)", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>R² (R-squared)</b> indicates the proportion of variance in the dependent variable that is predictable from the independent variable.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"R^2 = r^2 = \frac{SS_{Regression}}{SS_{Total}}")
        
        st.markdown("""
        **Example:** If r = 0.8, then R² = 0.64
        
        **Interpretation:** 64% of the variance in Y can be explained by X
        
        **Adjusted R² (for multiple regression):**
        """)
        st.latex(r"R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}")
        
        st.markdown("Where k = number of predictors")

    with st.expander("⚠️ Correlation ≠ Causation", expanded=True):
        st.markdown("""
        <div style="background: #fef2f2; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444; margin-bottom: 10px;">
            <h4 style="color: #dc2626; margin: 0 0 8px 0 !important;">⚠️ Critical Warning</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Correlation does NOT imply causation!</b> Two variables can be correlated without one causing the other.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Possible Explanations for Correlation:**
        1. **X causes Y** (direct causation)
        2. **Y causes X** (reverse causation)
        3. **Third variable Z causes both** (confounding)
        4. **Pure coincidence** (spurious correlation)
        
        **Famous Example:** Ice cream sales correlate with drowning deaths 🍦💀
        - Ice cream doesn't cause drowning!
        - Confounding variable: **Hot weather** → More swimming & more ice cream
        """)

    with st.expander("📈 Spearman's Rank Correlation", expanded=False):
        st.markdown("""
        **Use when:** Data is ordinal OR relationship is monotonic but not linear
        
        **Formula:**
        """)
        st.latex(r"\rho = 1 - \frac{6\sum d_i^2}{n(n^2-1)}")
        
        st.markdown("""
        **Where:** dᵢ = difference between ranks of pair i
        
        **Process:**
        1. Rank both variables separately
        2. Calculate rank differences
        3. Apply formula
        """)

# =============================================================================
# TAB 3: LINEAR REGRESSION
# =============================================================================
with tab3:
    st.markdown("## 📈 Chapter 3: Linear Regression")
    
    st.markdown("### 3.1 What is Regression?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Regression Analysis</b> is a statistical method for modeling the relationship between a dependent variable (Y) and one or more independent variables (X). It's used for prediction and understanding relationships.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Line of Best Fit</h4>
            <p style="margin: 0 !important; font-size: 13px;">Regression is like drawing the "best possible straight line" through a scatter of points — the line that minimizes the total distance to all points.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📐 Simple Linear Regression Model", expanded=True):
        st.markdown("**The Model:**")
        st.latex(r"Y = \beta_0 + \beta_1 X + \epsilon")
        
        st.markdown("""
        **Where:**
        - Y = Dependent variable (response)
        - X = Independent variable (predictor)
        - β₀ = Y-intercept (value of Y when X = 0)
        - β₁ = Slope (change in Y for one-unit change in X)
        - ε = Error term (random variation)
        
        **Fitted Line:**
        """)
        st.latex(r"\hat{Y} = b_0 + b_1 X")
        
        st.markdown("Where b₀ and b₁ are sample estimates of β₀ and β₁")

    # Least Squares Method
    st.markdown("### 3.2 Least Squares Method")
    
    with st.expander("📉 The Least Squares Principle", expanded=True):
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a; margin-bottom: 10px;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Least Squares Method</b> finds the line that minimizes the sum of squared residuals (differences between observed and predicted values).</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Objective:** Minimize")
        st.latex(r"\sum_{i=1}^{n} e_i^2 = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} (y_i - b_0 - b_1 x_i)^2")
        
        st.markdown("**Solution (Normal Equations):**")
        st.latex(r"b_1 = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2} = \frac{S_{xy}}{S_{xx}}")
        
        st.latex(r"b_0 = \bar{y} - b_1 \bar{x}")
        
        st.markdown("""
        **Why Squared?**
        - Treats positive and negative errors equally
        - Larger errors are penalized more
        - Mathematically convenient (differentiable)
        """)

    # Curve Fitting
    with st.expander("📊 Curve Fitting", expanded=True):
        st.markdown("""
        **When the relationship is not linear, we can fit curves:**
        
        | Relationship | Model | Transformation |
        |--------------|-------|----------------|
        | Linear | Y = a + bX | None |
        | Polynomial | Y = a + bX + cX² | Add X² term |
        | Exponential | Y = ab^X | log(Y) = log(a) + X·log(b) |
        | Logarithmic | Y = a + b·log(X) | Use log(X) |
        | Power | Y = aX^b | log(Y) = log(a) + b·log(X) |
        
        **Note:** Can often linearize non-linear relationships using transformations, then apply least squares.
        """)

    # Classical Assumptions
    st.markdown("### 3.3 Classical Assumptions of Linear Regression")
    
    with st.expander("📋 The CLRM Assumptions", expanded=True):
        st.markdown("""
        **Classical Linear Regression Model (CLRM) Assumptions:**
        
        | # | Assumption | Description | If Violated |
        |---|------------|--------------|-------------|
        | 1 | **Linearity** | Relationship is linear | Use non-linear models |
        | 2 | **Independence** | Errors are independent | Autocorrelation issues |
        | 3 | **Homoscedasticity** | Constant error variance | Heteroscedasticity |
        | 4 | **Normality** | Errors are normally distributed | Affects inference |
        | 5 | **No Multicollinearity** | Predictors not highly correlated | Unstable estimates |
        | 6 | **Exogeneity** | E(ε|X) = 0 | Biased estimates |
        """)
        
        st.markdown("**Checking Assumptions:**")
        st.markdown("""
        1. **Linearity:** Scatter plot, residual plot
        2. **Independence:** Durbin-Watson test
        3. **Homoscedasticity:** Residuals vs fitted plot
        4. **Normality:** Q-Q plot, Shapiro-Wilk test
        5. **Multicollinearity:** VIF (Variance Inflation Factor)
        """)

    # Gauss-Markov Theorem
    st.markdown("### 3.4 Gauss-Markov Theorem")
    
    with st.expander("🏆 Gauss-Markov Theorem", expanded=True):
        st.markdown("""
        <div style="background: #fff7ed; padding: 14px; border-radius: 8px; border-left: 4px solid #f97316; margin-bottom: 10px;">
            <h4 style="color: #ea580c; margin: 0 0 8px 0 !important;">📖 The Theorem</h4>
            <p style="margin: 0 !important; font-size: 13px;">Under the CLRM assumptions (1-5 above, except normality), the <b>Ordinary Least Squares (OLS) estimators are BLUE</b> — Best Linear Unbiased Estimators.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **BLUE = Best Linear Unbiased Estimator**
        
        | Property | Meaning |
        |----------|---------|
        | **Best** | Minimum variance among all linear unbiased estimators |
        | **Linear** | Estimator is a linear function of Y values |
        | **Unbiased** | E(b) = β (expected value equals true parameter) |
        | **Estimator** | Calculated from sample data |
        
        **Significance:** This theorem guarantees that if assumptions hold, OLS gives the most efficient (precise) estimates possible among linear unbiased estimators.
        """)

    # Estimation and Prediction
    with st.expander("🔮 Estimation and Prediction", expanded=True):
        st.markdown("""
        **Point Prediction:**
        """)
        st.latex(r"\hat{y}_0 = b_0 + b_1 x_0")
        
        st.markdown("""
        **Confidence Interval for Mean Response:**
        """)
        st.latex(r"\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot s_e \sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}")
        
        st.markdown("""
        **Prediction Interval for Individual Response:**
        """)
        st.latex(r"\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot s_e \sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}")
        
        st.markdown("""
        **Where:**
        - sₑ = Standard error of estimate = √(SSE/(n-2))
        - SSE = Sum of Squared Errors
        - Sₓₓ = Σ(xᵢ - x̄)²
        
        **Key Difference:** Prediction intervals are wider because they account for individual variation, not just mean variation.
        """)

# =============================================================================
# TAB 4: MULTIPLE REGRESSION
# =============================================================================
with tab4:
    st.markdown("## 📉 Chapter 4: Multiple Regression Analysis")
    
    st.markdown("### 4.1 What is Multiple Regression?")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Definition</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Multiple Regression</b> extends simple regression to include two or more independent variables to predict a single dependent variable.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: Recipe with Multiple Ingredients</h4>
            <p style="margin: 0 !important; font-size: 13px;">Simple regression is like predicting taste from only sugar amount. Multiple regression considers sugar, salt, spice, and more — a complete recipe.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📐 The Multiple Regression Model", expanded=True):
        st.markdown("**The Model:**")
        st.latex(r"Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_k X_k + \epsilon")
        
        st.markdown("**Matrix Notation:**")
        st.latex(r"\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}")
        
        st.markdown("""
        **Where:**
        - Y = Dependent variable (n × 1)
        - X = Design matrix of predictors (n × (k+1))
        - β = Vector of coefficients ((k+1) × 1)
        - ε = Vector of errors (n × 1)
        
        **OLS Solution:**
        """)
        st.latex(r"\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}")

    with st.expander("📊 Interpreting Coefficients", expanded=True):
        st.markdown("""
        **Example Model:**
        > Salary = 30,000 + 5,000(Education) + 2,000(Experience) + 10,000(Manager)
        
        **Interpretation:**
        
        | Coefficient | Meaning |
        |-------------|---------|
        | β₀ = 30,000 | Baseline salary (0 education, 0 experience, not manager) |
        | β₁ = 5,000 | Each year of education adds $5,000, *holding other variables constant* |
        | β₂ = 2,000 | Each year of experience adds $2,000, *controlling for education and manager status* |
        | β₃ = 10,000 | Being a manager adds $10,000, *all else equal* |
        
        **Key Phrase:** "Holding all other variables constant" (ceteris paribus)
        """)

    with st.expander("📋 Model Evaluation", expanded=True):
        st.markdown("""
        **Key Statistics:**
        
        | Statistic | Formula | Interpretation |
        |-----------|---------|----------------|
        | **R²** | 1 - SSE/SST | Proportion of variance explained |
        | **Adjusted R²** | 1 - [(1-R²)(n-1)]/(n-k-1) | Penalizes for adding predictors |
        | **F-statistic** | (SSR/k) / (SSE/(n-k-1)) | Overall model significance |
        | **t-statistic** | b/SE(b) | Individual coefficient significance |
        | **Standard Error** | √(MSE×(X'X)⁻¹ᵢᵢ) | Precision of coefficient estimate |
        
        **Model Selection Criteria:**
        - AIC (Akaike Information Criterion) - Lower is better
        - BIC (Bayesian Information Criterion) - Lower is better
        - Adjusted R² - Higher is better
        """)

    with st.expander("⚠️ Multicollinearity", expanded=True):
        st.markdown("""
        <div style="background: #fef2f2; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444; margin-bottom: 10px;">
            <h4 style="color: #dc2626; margin: 0 0 8px 0 !important;">⚠️ Problem</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Multicollinearity</b> occurs when independent variables are highly correlated with each other. This makes individual coefficient estimates unreliable.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Detection:**
        - Correlation matrix: r > 0.8 between predictors
        - VIF (Variance Inflation Factor): VIF > 10 is problematic
        """)
        
        st.latex(r"VIF_j = \frac{1}{1 - R_j^2}")
        
        st.markdown("""
        **Solutions:**
        1. Remove one of the correlated variables
        2. Combine variables (e.g., create index)
        3. Use regularization (Ridge, Lasso)
        4. Principal Component Regression
        """)

# =============================================================================
# TAB 5: FORMULAS SUMMARY
# =============================================================================
with tab5:
    st.markdown("## 📝 Chapter 5: Key Formulas Summary")
    
    with st.expander("📊 Correlation Formulas", expanded=True):
        st.markdown("**Pearson Correlation Coefficient:**")
        st.latex(r"r = \frac{n\sum xy - \sum x \sum y}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}")
        
        st.markdown("**Coefficient of Determination:**")
        st.latex(r"R^2 = r^2")
        
        st.markdown("**Spearman's Rank Correlation:**")
        st.latex(r"\rho = 1 - \frac{6\sum d_i^2}{n(n^2-1)}")

    with st.expander("📈 Simple Linear Regression", expanded=True):
        st.markdown("**Regression Line:**")
        st.latex(r"\hat{Y} = b_0 + b_1 X")
        
        st.markdown("**Slope:**")
        st.latex(r"b_1 = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}")
        
        st.markdown("**Intercept:**")
        st.latex(r"b_0 = \bar{y} - b_1 \bar{x}")
        
        st.markdown("**Standard Error of Estimate:**")
        st.latex(r"s_e = \sqrt{\frac{\sum(y_i - \hat{y}_i)^2}{n-2}} = \sqrt{\frac{SSE}{n-2}}")
        
        st.markdown("**Standard Error of Slope:**")
        st.latex(r"SE(b_1) = \frac{s_e}{\sqrt{S_{xx}}} = \frac{s_e}{\sqrt{\sum(x_i - \bar{x})^2}}")

    with st.expander("📉 Multiple Regression", expanded=True):
        st.markdown("**Model:**")
        st.latex(r"Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_k X_k + \epsilon")
        
        st.markdown("**OLS Estimates (Matrix Form):**")
        st.latex(r"\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}")
        
        st.markdown("**Adjusted R²:**")
        st.latex(r"R^2_{adj} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}")
        
        st.markdown("**F-Statistic:**")
        st.latex(r"F = \frac{R^2/k}{(1-R^2)/(n-k-1)}")
        
        st.markdown("**VIF:**")
        st.latex(r"VIF_j = \frac{1}{1 - R_j^2}")

    with st.expander("🔮 Prediction Intervals", expanded=True):
        st.markdown("**Confidence Interval for Mean:**")
        st.latex(r"\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot s_e \sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}")
        
        st.markdown("**Prediction Interval for Individual:**")
        st.latex(r"\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot s_e \sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}")

    with st.expander("📐 ANOVA for Regression", expanded=True):
        st.markdown("""
        | Source | SS | df | MS | F |
        |--------|----|----|----|----|
        | Regression | SSR = Σ(ŷᵢ - ȳ)² | k | MSR = SSR/k | MSR/MSE |
        | Error | SSE = Σ(yᵢ - ŷᵢ)² | n-k-1 | MSE = SSE/(n-k-1) | |
        | Total | SST = Σ(yᵢ - ȳ)² | n-1 | | |
        
        **Relationship:** SST = SSR + SSE
        """)
        
        st.latex(r"R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}")

# Footer
show_footer()
