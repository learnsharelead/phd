import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# SEO & Styles
inject_seo_meta(
    title="Excel for Statistical Analysis | Complete Tutorial with Examples [2024]",
    description="Master statistical analysis in Excel: descriptive statistics, t-tests, ANOVA, correlation, regression. Step-by-step tutorials with Data Analysis ToolPak.",
    keywords=[
        "excel statistics",
        "data analysis toolpak",
        "excel t-test",
        "excel anova",
        "excel correlation",
        "statistical analysis excel",
        "excel formulas statistics",
        "excel data analysis"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/software/excel",
    reading_time=45
)
apply_custom_css()
show_top_nav(current_page="Excel Tutorial")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">💻 Excel for Statistical Analysis</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #1e40af;">Complete tutorial from basics to advanced statistical tests</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Basics",
    "📈 Descriptive Stats",
    "🧪 t-Tests",
    "📉 ANOVA & Regression",
    "💡 Tips & Tricks"
])

# =============================================================================
# TAB 1: EXCEL BASICS
# =============================================================================
with tab1:
    st.markdown("## 📊 Excel Basics for Research")
    
    with st.expander("🎯 Setting Up Excel for Statistics", expanded=True):
        st.markdown("""
        ### Step 1: Enable Data Analysis ToolPak
        
        **What is it?** Excel's built-in statistical analysis add-in
        
        **How to Enable:**
        
        1. **File** → **Options** → **Add-ins**
        2. At bottom, select **Excel Add-ins** → Click **Go**
        3. Check ✅ **Analysis ToolPak**
        4. Click **OK**
        
        **Verify Installation:**
        - Go to **Data** tab
        - You should see **Data Analysis** button on the right
        
        **If you don't see it:**
        - Mac users: **Tools** → **Excel Add-ins** → Check Analysis ToolPak
        - Some versions: May need to install from Microsoft website
        
        ---
        ### Step 2: Data Entry Best Practices
        
        **Golden Rules:**
        
        1. **First Row = Headers**
           ```
           | StudentID | PreTest | PostTest | Group |
           |-----------|---------|----------|-------|
           | 1         | 65      | 82       | Exp   |
           | 2         | 70      | 75       | Ctrl  |
           ```
        
        2. **One Variable Per Column**
           - ✅ Good: Separate columns for PreTest, PostTest
           - ❌ Bad: Mixing different variables in one column
        
        3. **No Empty Rows/Columns**
           - Keep data continuous
           - Excel treats empty cells as missing data
        
        4. **Consistent Data Types**
           - Numbers as numbers (not text)
           - Dates as dates
           - Categories as text
        
        5. **No Merged Cells**
           - Breaks formulas and analysis
        
        ---
        ### Step 3: Essential Excel Functions
        
        | Function | Purpose | Example |
        |----------|---------|---------|
        | `=AVERAGE(A2:A50)` | Mean | Average test score |
        | `=MEDIAN(A2:A50)` | Median | Middle value |
        | `=STDEV.S(A2:A50)` | Sample SD | Variability |
        | `=STDEV.P(A2:A50)` | Population SD | For entire population |
        | `=COUNT(A2:A50)` | Count numbers | Sample size |
        | `=MIN(A2:A50)` | Minimum | Lowest score |
        | `=MAX(A2:A50)` | Maximum | Highest score |
        | `=QUARTILE(A2:A50, 1)` | Q1 | 25th percentile |
        | `=QUARTILE(A2:A50, 3)` | Q3 | 75th percentile |
        
        **Pro Tip:** Use `STDEV.S` for sample data (most research), `STDEV.P` only if you have the entire population.
        """)
    
    with st.expander("📋 Example Dataset Setup", expanded=True):
        st.markdown("""
        ### Practice Dataset: Student Performance Study
        
        **Scenario:** Testing if a new teaching method improves test scores
        
        **Data Structure:**
        ```
        | StudentID | Gender | PreTest | PostTest | Method    | Attendance |
        |-----------|--------|---------|----------|-----------|------------|
        | 1         | M      | 65      | 82       | Active    | 95         |
        | 2         | F      | 70      | 75       | Active    | 88         |
        | 3         | M      | 68      | 85       | Active    | 92         |
        | 4         | F      | 72      | 78       | Active    | 90         |
        | 5         | M      | 64      | 70       | Traditional| 85        |
        | 6         | F      | 66      | 72       | Traditional| 87        |
        | 7         | M      | 69      | 74       | Traditional| 89        |
        | 8         | F      | 71      | 76       | Traditional| 91        |
        ```
        
        **How to Enter:**
        1. Type headers in Row 1
        2. Enter data starting Row 2
        3. Format numbers as **Number** (not General)
        4. Save as `.xlsx` file
        
        **Download Practice Data:**
        - Create this in Excel and save
        - We'll use it for all examples below
        """)

# =============================================================================
# TAB 2: DESCRIPTIVE STATISTICS
# =============================================================================
with tab2:
    st.markdown("## 📈 Descriptive Statistics in Excel")
    
    with st.expander("📊 Method 1: Using Formulas", expanded=True):
        st.markdown("""
        ### Complete Descriptive Statistics
        
        **Example: Analyzing PreTest Scores**
        
        Assuming PreTest scores are in cells `C2:C50`
        
        | Statistic | Formula | Result |
        |-----------|---------|--------|
        | **Mean** | `=AVERAGE(C2:C50)` | 68.5 |
        | **Median** | `=MEDIAN(C2:C50)` | 69.0 |
        | **Mode** | `=MODE.SNGL(C2:C50)` | 70 |
        | **Standard Deviation** | `=STDEV.S(C2:C50)` | 5.2 |
        | **Variance** | `=VAR.S(C2:C50)` | 27.04 |
        | **Minimum** | `=MIN(C2:C50)` | 58 |
        | **Maximum** | `=MAX(C2:C50)` | 78 |
        | **Range** | `=MAX(C2:C50)-MIN(C2:C50)` | 20 |
        | **Count** | `=COUNT(C2:C50)` | 49 |
        | **Q1 (25th percentile)** | `=QUARTILE(C2:C50, 1)` | 65 |
        | **Q3 (75th percentile)** | `=QUARTILE(C2:C50, 3)` | 72 |
        | **IQR** | `=QUARTILE(C2:C50,3)-QUARTILE(C2:C50,1)` | 7 |
        | **Skewness** | `=SKEW(C2:C50)` | 0.15 |
        | **Kurtosis** | `=KURT(C2:C50)` | -0.32 |
        
        **How to Create a Summary Table:**
        
        1. Create labels in Column F:
           ```
           F1: Statistic
           F2: Mean
           F3: Median
           F4: SD
           ...
           ```
        
        2. Enter formulas in Column G:
           ```
           G2: =AVERAGE(C2:C50)
           G3: =MEDIAN(C2:C50)
           G4: =STDEV.S(C2:C50)
           ...
           ```
        
        3. Format numbers: Right-click → Format Cells → Number → 2 decimal places
        """)
    
    with st.expander("📊 Method 2: Data Analysis ToolPak", expanded=True):
        st.markdown("""
        ### Using Descriptive Statistics Tool
        
        **Step-by-Step:**
        
        1. **Data** tab → **Data Analysis** → **Descriptive Statistics** → **OK**
        
        2. **Input Range:** Select your data (e.g., `C2:C50`)
           - ✅ Check "Labels in First Row" if you included header
        
        3. **Output Options:**
           - Select "Output Range" and click a cell (e.g., `F1`)
           - OR select "New Worksheet"
        
        4. **Check these boxes:**
           - ✅ Summary Statistics
           - ✅ Confidence Level for Mean (95%)
           - ✅ Kth Largest (1) - gives maximum
           - ✅ Kth Smallest (1) - gives minimum
        
        5. Click **OK**
        
        **Output You'll Get:**
        ```
        PreTest
        
        Mean                    68.5
        Standard Error          0.74
        Median                  69
        Mode                    70
        Standard Deviation      5.2
        Sample Variance         27.04
        Kurtosis               -0.32
        Skewness                0.15
        Range                   20
        Minimum                 58
        Maximum                 78
        Sum                     3356.5
        Count                   49
        Confidence Level(95.0%) 1.49
        ```
        
        **Interpretation:**
        - **Mean = 68.5**: Average score
        - **SD = 5.2**: Typical deviation from mean
        - **Confidence Interval**: 68.5 ± 1.49 = [67.01, 69.99]
        - **Skewness = 0.15**: Nearly symmetric (close to 0)
        - **Kurtosis = -0.32**: Slightly flatter than normal
        """)

# =============================================================================
# TAB 3: t-TESTS
# =============================================================================
with tab3:
    st.markdown("## 🧪 t-Tests in Excel")
    
    with st.expander("📋 One-Sample t-Test", expanded=True):
        st.markdown("""
        ### Testing Against a Known Value
        
        **Example:** Is average PreTest score different from 70?
        
        **Method 1: Using Formula**
        
        ```excel
        // Assuming PreTest scores in C2:C50
        
        // Step 1: Calculate sample statistics
        Mean:    =AVERAGE(C2:C50)           // Result: 68.5
        SD:      =STDEV.S(C2:C50)           // Result: 5.2
        N:       =COUNT(C2:C50)             // Result: 49
        
        // Step 2: Calculate t-statistic
        t = (Mean - 70) / (SD / SQRT(N))
        =( AVERAGE(C2:C50) - 70 ) / ( STDEV.S(C2:C50) / SQRT(COUNT(C2:C50)) )
        // Result: -2.02
        
        // Step 3: Calculate p-value (two-tailed)
        df = N - 1 = 48
        =T.DIST.2T(ABS(t-statistic), df)
        =T.DIST.2T(2.02, 48)
        // Result: 0.049
        
        // Step 4: Decision
        p = 0.049 < 0.05 → Significant
        ```
        
        **Interpretation:**
        "The mean PreTest score (M = 68.5, SD = 5.2) was significantly different from 70, 
        t(48) = -2.02, p = .049."
        
        ---
        **Method 2: Using Data Analysis ToolPak**
        
        Unfortunately, Excel's ToolPak doesn't have one-sample t-test. Use formulas above.
        """)
    
    with st.expander("📋 Independent Samples t-Test", expanded=True):
        st.markdown("""
        ### Comparing Two Groups
        
        **Example:** Do Active and Traditional methods differ in PostTest scores?
        
        **Data Setup:**
        - Active Learning scores: `D2:D25` (24 students)
        - Traditional scores: `D26:D50` (25 students)
        
        **Step-by-Step:**
        
        1. **Data** → **Data Analysis** → **t-Test: Two-Sample Assuming Equal Variances**
        
        2. **Variable 1 Range:** `D2:D25` (Active Learning)
        
        3. **Variable 2 Range:** `D26:D50` (Traditional)
        
        4. **Hypothesized Mean Difference:** `0`
        
        5. **Alpha:** `0.05`
        
        6. **Output Range:** Click a cell (e.g., `F1`)
        
        7. Click **OK**
        
        **Output:**
        ```
        t-Test: Two-Sample Assuming Equal Variances
                                    Variable 1  Variable 2
        Mean                        82.5        73.2
        Variance                    45.3        52.1
        Observations                24          25
        Pooled Variance             48.76
        Hypothesized Mean Diff      0
        df                          47
        t Stat                      4.68
        P(T<=t) one-tail            0.000015
        t Critical one-tail         1.678
        P(T<=t) two-tail            0.00003
        t Critical two-tail         2.012
        ```
        
        **Interpretation:**
        - **t(47) = 4.68, p < .001**
        - Active Learning (M = 82.5) significantly higher than Traditional (M = 73.2)
        - Difference = 9.3 points
        - Effect size d = (82.5 - 73.2) / √48.76 = 1.33 (very large)
        
        **APA Format:**
        "Active learning (M = 82.5, SD = 6.7) resulted in significantly higher scores than 
        traditional instruction (M = 73.2, SD = 7.2), t(47) = 4.68, p < .001, d = 1.33."
        
        ---
        **When to Use "Unequal Variances":**
        
        First, test for equal variances:
        ```excel
        =F.TEST(D2:D25, D26:D50)
        ```
        - If p > 0.05: Use "Equal Variances"
        - If p < 0.05: Use "Unequal Variances" (Welch's t-test)
        """)
    
    with st.expander("📋 Paired Samples t-Test", expanded=True):
        st.markdown("""
        ### Before-After Comparison
        
        **Example:** Did students improve from PreTest to PostTest?
        
        **Data Setup:**
        - PreTest scores: `C2:C50`
        - PostTest scores: `D2:D50`
        - Same students in both columns
        
        **Step-by-Step:**
        
        1. **Data** → **Data Analysis** → **t-Test: Paired Two Sample for Means**
        
        2. **Variable 1 Range:** `D2:D50` (PostTest)
        
        3. **Variable 2 Range:** `C2:C50` (PreTest)
        
        4. **Hypothesized Mean Difference:** `0`
        
        5. **Alpha:** `0.05`
        
        6. Click **OK**
        
        **Output:**
        ```
        t-Test: Paired Two Sample for Means
                                PostTest    PreTest
        Mean                    78.5        68.5
        Variance                48.2        27.0
        Observations            49          49
        Pearson Correlation     0.68
        Hypothesized Mean Diff  0
        df                      48
        t Stat                  12.45
        P(T<=t) one-tail        <0.000001
        t Critical one-tail     1.677
        P(T<=t) two-tail        <0.000001
        t Critical two-tail     2.011
        ```
        
        **Interpretation:**
        - Mean improvement = 78.5 - 68.5 = 10 points
        - t(48) = 12.45, p < .001
        - Highly significant improvement
        
        **Calculate Effect Size (Cohen's d):**
        ```excel
        // SD of differences
        =STDEV.S(D2:D50 - C2:C50)  // Assuming you created difference column
        // If SD_diff = 5.6
        d = 10 / 5.6 = 1.79 (very large effect)
        ```
        """)

# =============================================================================
# TAB 4: ANOVA & REGRESSION
# =============================================================================
with tab4:
    st.markdown("## 📉 ANOVA and Regression in Excel")
    
    with st.expander("📊 One-Way ANOVA", expanded=True):
        st.markdown("""
        ### Comparing 3+ Groups
        
        **Example:** Compare test scores across three teaching methods
        
        **Data Setup:**
        ```
        | Method A | Method B | Method C |
        |----------|----------|----------|
        | 75       | 85       | 70       |
        | 78       | 88       | 73       |
        | 72       | 82       | 68       |
        | 80       | 90       | 75       |
        | 76       | 87       | 71       |
        ```
        
        **Step-by-Step:**
        
        1. **Data** → **Data Analysis** → **ANOVA: Single Factor**
        
        2. **Input Range:** Select all data including headers (e.g., `A1:C6`)
           - ✅ Check "Labels in First Row"
        
        3. **Alpha:** `0.05`
        
        4. **Output Range:** Click a cell
        
        5. Click **OK**
        
        **Output:**
        ```
        ANOVA: Single Factor
        
        SUMMARY
        Groups      Count   Sum     Average   Variance
        Method A    5       381     76.2      9.7
        Method B    5       432     86.4      9.3
        Method C    5       357     71.4      8.8
        
        ANOVA
        Source of Variation  SS      df    MS      F       P-value   F crit
        Between Groups       636.4   2     318.2   34.55   <0.001    3.89
        Within Groups        110.8   12    9.23
        Total                747.2   14
        ```
        
        **Interpretation:**
        - F(2, 12) = 34.55, p < .001
        - Significant difference among methods
        - η² = 636.4 / 747.2 = 0.85 (very large effect)
        
        **Post-hoc Tests:**
        Excel doesn't do post-hoc automatically. Use t-tests with Bonferroni correction:
        - For 3 groups: 3 comparisons
        - Adjusted alpha = 0.05 / 3 = 0.017
        - Compare each pair with t-test, use p < 0.017
        """)
    
    with st.expander("📈 Correlation", expanded=True):
        st.markdown("""
        ### Measuring Relationship Between Variables
        
        **Example:** Relationship between Attendance and PostTest scores
        
        **Method 1: Using CORREL Function**
        ```excel
        =CORREL(F2:F50, D2:D50)
        // Where F = Attendance, D = PostTest
        // Result: r = 0.68
        ```
        
        **Method 2: Data Analysis ToolPak**
        
        1. **Data** → **Data Analysis** → **Correlation**
        
        2. **Input Range:** Select both columns (e.g., `D1:F50`)
           - ✅ Check "Labels in First Row"
        
        3. Click **OK**
        
        **Output:**
        ```
                    PostTest  Attendance
        PostTest    1
        Attendance  0.68      1
        ```
        
        **Interpretation:**
        - r = 0.68 (strong positive correlation)
        - Higher attendance → Higher scores
        - r² = 0.46 (46% of variance explained)
        
        **Significance Test:**
        ```excel
        // Calculate t-statistic
        n = 49
        t = r * SQRT(n-2) / SQRT(1-r²)
        t = 0.68 * SQRT(47) / SQRT(1-0.68²)
        t = 6.32
        
        // p-value
        =T.DIST.2T(6.32, 47)
        p < 0.001 (significant)
        ```
        """)
    
    with st.expander("📉 Linear Regression", expanded=True):
        st.markdown("""
        ### Predicting One Variable from Another
        
        **Example:** Predict PostTest from Attendance
        
        **Step-by-Step:**
        
        1. **Data** → **Data Analysis** → **Regression**
        
        2. **Input Y Range:** `D1:D50` (PostTest - dependent variable)
        
        3. **Input X Range:** `F1:F50` (Attendance - independent variable)
           - ✅ Check "Labels"
        
        4. **Output Options:**
           - ✅ Confidence Level: 95%
           - ✅ Residuals (optional, for checking assumptions)
        
        5. Click **OK**
        
        **Output:**
        ```
        SUMMARY OUTPUT
        
        Regression Statistics
        Multiple R          0.68
        R Square            0.46
        Adjusted R Square   0.45
        Standard Error      4.85
        Observations        49
        
        ANOVA
                    df      SS        MS        F       Significance F
        Regression  1       938.5     938.5     39.9    <0.001
        Residual    47      1105.2    23.5
        Total       48      2043.7
        
        Coefficients
                    Coeff   Std Error   t Stat   P-value   Lower 95%   Upper 95%
        Intercept   32.5    8.2         3.96     <0.001    16.0        49.0
        Attendance  0.52    0.08        6.32     <0.001    0.35        0.69
        ```
        
        **Regression Equation:**
        ```
        PostTest = 32.5 + 0.52 × Attendance
        ```
        
        **Interpretation:**
        - For every 1% increase in attendance, PostTest increases by 0.52 points
        - R² = 0.46: Attendance explains 46% of variance in PostTest
        - F(1, 47) = 39.9, p < .001 (model is significant)
        
        **Making Predictions:**
        ```excel
        // Predict score for 90% attendance
        =32.5 + 0.52 * 90
        = 79.3 points
        ```
        """)

# =============================================================================
# TAB 5: TIPS & TRICKS
# =============================================================================
with tab5:
    st.markdown("## 💡 Excel Tips & Tricks")
    
    with st.expander("⚡ Quick Tips", expanded=True):
        st.markdown("""
        ### Time-Saving Shortcuts
        
        **Keyboard Shortcuts:**
        - `Ctrl + ;` - Insert today's date
        - `Ctrl + Shift + ;` - Insert current time
        - `Ctrl + D` - Fill down
        - `Ctrl + R` - Fill right
        - `Alt + =` - AutoSum
        - `F4` - Repeat last action
        - `Ctrl + Home` - Go to cell A1
        - `Ctrl + End` - Go to last used cell
        
        **Formula Tips:**
        1. **Absolute References:** Use `$` to lock cells
           - `$A$1` - Locks both row and column
           - `$A1` - Locks column only
           - `A$1` - Locks row only
        
        2. **Array Formulas:** Press `Ctrl + Shift + Enter`
           - Calculates across multiple cells at once
        
        3. **Named Ranges:** Select range → Name Box → Type name
           - Use `PreTest` instead of `C2:C50`
        
        ---
        ### Common Errors & Solutions
        
        | Error | Meaning | Solution |
        |-------|---------|----------|
        | `#DIV/0!` | Division by zero | Check denominator isn't zero |
        | `#VALUE!` | Wrong data type | Check for text in number cells |
        | `#REF!` | Invalid cell reference | Cell was deleted, fix reference |
        | `#NAME?` | Excel doesn't recognize formula | Check spelling, install ToolPak |
        | `#N/A` | Value not available | Check VLOOKUP range |
        | `#NUM!` | Invalid numeric value | Check for negative in SQRT, etc. |
        
        ---
        ### Best Practices
        
        1. **Always Save Backups**
           - Save as `.xlsx` (not `.xls`)
           - Keep original data separate from analysis
        
        2. **Document Your Work**
           - Add comments to cells (Right-click → Insert Comment)
           - Create a "Notes" sheet explaining analysis
        
        3. **Check Assumptions**
           - Normality: Create histogram, check skewness
           - Equal variances: Use F-test
           - Outliers: Use boxplot or Z-scores
        
        4. **Validate Results**
           - Cross-check with online calculators
           - Verify formulas with simple known data
           - Check if results make sense
        """)
    
    with st.expander("📊 Creating Professional Charts", expanded=True):
        st.markdown("""
        ### Visualization Best Practices
        
        **1. Histogram (for distribution)**
        - Select data → Insert → Charts → Histogram
        - Right-click bars → Format → Adjust bin width
        - Add axis labels and title
        
        **2. Boxplot (for comparing groups)**
        - Insert → Charts → Box and Whisker
        - Shows median, quartiles, outliers
        
        **3. Scatter Plot (for correlation)**
        - Select two variables → Insert → Scatter
        - Add trendline: Right-click points → Add Trendline
        - Display equation and R²
        
        **4. Bar Chart (for group means)**
        - Calculate means for each group
        - Insert → Bar Chart
        - Add error bars (SD or SE)
        
        **Chart Formatting Tips:**
        - Remove gridlines for cleaner look
        - Use colorblind-friendly colors
        - Make axis labels large and readable
        - Always include units
        - Add data labels if few data points
        """)

show_footer()
