import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# SEO & Styles
inject_seo_meta(
    title="SPSS for Statistical Analysis | Complete Tutorial with Output Interpretation [2024]",
    description="Master SPSS: descriptive statistics, t-tests, ANOVA, non-parametric tests, regression. Step-by-step tutorials with output interpretation.",
    keywords=[
        "spss tutorial",
        "spss statistics",
        "spss t-test",
        "spss anova",
        "spss output interpretation",
        "statistical analysis spss",
        "spss for research",
        "spss beginners guide"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/software/spss",
    reading_time=60
)
apply_custom_css()
show_top_nav(current_page="SPSS Tutorial")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📊 SPSS for Statistical Analysis</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #166534;">Complete guide from basics to advanced analysis with output interpretation</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🎯 Getting Started",
    "📊 Descriptive Stats",
    "🧪 t-Tests",
    "📈 ANOVA",
    "📉 Non-Parametric",
    "💡 Tips"
])

# =============================================================================
# TAB 1: GETTING STARTED
# =============================================================================
with tab1:
    st.markdown("## 🎯 Getting Started with SPSS")
    
    with st.expander("📋 SPSS Interface Overview", expanded=True):
        st.markdown("""
        ### Understanding SPSS Windows
        
        **1. Data View** (Spreadsheet-like)
        - Where you enter your data
        - Rows = Cases/Participants
        - Columns = Variables
        - Similar to Excel
        
        **2. Variable View** (Define variables)
        - Name: Variable name (no spaces, start with letter)
        - Type: Numeric, String, Date
        - Width: Number of digits
        - Decimals: Decimal places
        - Label: Full description
        - Values: Code labels (e.g., 1=Male, 2=Female)
        - Missing: Define missing value codes
        - Measure: Scale, Ordinal, or Nominal
        
        **3. Output Viewer**
        - Shows all results
        - Can export to Word, PDF, Excel
        
        ---
        ### Data Entry Best Practices
        
        **Step 1: Define Variables (Variable View)**
        
        Example: Student Performance Study
        
        | Name | Type | Label | Values | Measure |
        |------|------|-------|--------|---------|
        | StudentID | Numeric | Student ID Number | None | Scale |
        | Gender | Numeric | Student Gender | 1=Male, 2=Female | Nominal |
        | Group | Numeric | Teaching Method | 1=Active, 2=Traditional | Nominal |
        | PreTest | Numeric | Pretest Score | None | Scale |
        | PostTest | Numeric | Posttest Score | None | Scale |
        | Attendance | Numeric | Attendance Percentage | None | Scale |
        
        **Step 2: Enter Data (Data View)**
        ```
        StudentID  Gender  Group  PreTest  PostTest  Attendance
        1          1       1      65       82        95
        2          2       1      70       75        88
        3          1       2      68       72        85
        ...
        ```
        
        **Important:**
        - Use numeric codes for categories (1, 2, 3) not text
        - Define value labels in Variable View
        - Leave cells blank for missing data (don't use 0 or 999)
        - Save as `.sav` file
        
        ---
        ### Measure Types
        
        | Type | Description | Examples | Statistics Allowed |
        |------|-------------|----------|-------------------|
        | **Scale** | Continuous numbers | Age, Score, Income | Mean, SD, Correlation |
        | **Ordinal** | Ordered categories | Likert scale (1-5) | Median, Mode |
        | **Nominal** | Unordered categories | Gender, Color, Group | Mode, Frequency |
        
        **Critical:** Set correct measure type or SPSS won't allow certain analyses!
        """)
    
    with st.expander("💾 Importing Data", expanded=True):
        st.markdown("""
        ### From Excel to SPSS
        
        **Method 1: Copy-Paste**
        1. In Excel: Select all data (including headers)
        2. Copy (Ctrl+C)
        3. In SPSS Data View: Click cell A1
        4. Paste (Ctrl+V)
        5. SPSS will create variables automatically
        6. Go to Variable View to add labels and value codes
        
        **Method 2: Import**
        1. File → Open → Data
        2. Change file type to "Excel (*.xls, *.xlsx)"
        3. Select your Excel file
        4. ✅ Check "Read variable names from first row"
        5. Click OK
        
        **Method 3: Direct Import**
        1. File → Import Data → Excel
        2. Browse to file
        3. Select worksheet
        4. ✅ Read variable names
        5. Click OK
        
        ---
        ### Saving Your Work
        
        **Data File:**
        - File → Save As → `.sav` format
        - This preserves variable definitions
        
        **Output:**
        - In Output Viewer: File → Export
        - Choose format: Word, PDF, Excel, HTML
        - Select which tables to export
        """)

# =============================================================================
# TAB 2: DESCRIPTIVE STATISTICS
# =============================================================================
with tab2:
    st.markdown("## 📊 Descriptive Statistics in SPSS")
    
    with st.expander("📈 Frequencies and Descriptives", expanded=True):
        st.markdown("""
        ### Method 1: Frequencies (for all variable types)
        
        **Steps:**
        1. **Analyze → Descriptive Statistics → Frequencies**
        2. Move variables to "Variable(s)" box
        3. Click **Statistics** button:
           - ✅ Mean, Median, Mode
           - ✅ Std. Deviation, Variance
           - ✅ Minimum, Maximum, Range
           - ✅ Quartiles
           - ✅ Skewness, Kurtosis
        4. Click **Charts** (optional):
           - Histograms with normal curve
           - Bar charts
        5. Click **OK**
        
        **Output:**
        ```
        Statistics
        PreTest
        N           Valid       49
                    Missing     0
        Mean                    68.50
        Std. Error of Mean      0.74
        Median                  69.00
        Mode                    70
        Std. Deviation          5.20
        Variance                27.04
        Skewness                0.15
        Std. Error of Skewness  0.34
        Kurtosis               -0.32
        Std. Error of Kurtosis  0.67
        Range                   20
        Minimum                 58
        Maximum                 78
        Percentiles    25       65.00
                       50       69.00
                       75       72.00
        ```
        
        **Interpretation:**
        - Mean = 68.5 (average score)
        - SD = 5.2 (typical deviation)
        - Skewness = 0.15 (nearly symmetric, |skew| < 0.5 is good)
        - Kurtosis = -0.32 (slightly flat, acceptable)
        
        ---
        ### Method 2: Descriptives (for scale variables only)
        
        **Steps:**
        1. **Analyze → Descriptive Statistics → Descriptives**
        2. Move scale variables to "Variable(s)"
        3. Click **Options**:
           - ✅ Mean, Sum, Std. Deviation
           - ✅ Minimum, Maximum, Range
           - ✅ S.E. mean
        4. Click **OK**
        
        **When to Use:**
        - Quick summary for multiple variables
        - Only for continuous (scale) variables
        - Doesn't show median or mode
        
        ---
        ### Method 3: Explore (most comprehensive)
        
        **Steps:**
        1. **Analyze → Descriptive Statistics → Explore**
        2. Move variable to "Dependent List"
        3. (Optional) Move grouping variable to "Factor List"
        4. Click **Plots**:
           - ✅ Stem-and-leaf
           - ✅ Histogram
           - ✅ Normality plots with tests
        5. Click **Statistics**:
           - ✅ Descriptives
           - ✅ Outliers
           - ✅ Percentiles
        6. Click **OK**
        
        **Output Includes:**
        - Complete descriptive statistics
        - Boxplot
        - Normality tests (Shapiro-Wilk, Kolmogorov-Smirnov)
        - Q-Q plot
        - Outlier detection
        
        **Best for:**
        - Checking assumptions before analysis
        - Detecting outliers
        - Comparing groups visually
        """)

# =============================================================================
# TAB 3: t-TESTS
# =============================================================================
with tab3:
    st.markdown("## 🧪 t-Tests in SPSS")
    
    with st.expander("📋 One-Sample t-Test", expanded=True):
        st.markdown("""
        ### Testing Against a Known Value
        
        **Example:** Is average PreTest score different from 70?
        
        **Steps:**
        1. **Analyze → Compare Means → One-Sample T Test**
        2. Move "PreTest" to "Test Variable(s)"
        3. Enter **Test Value: 70**
        4. Click **Options**:
           - Confidence Interval: 95%
           - Missing Values: Exclude cases analysis by analysis
        5. Click **OK**
        
        **Output:**
        ```
        One-Sample Statistics
        ┌─────────┬───┬──────┬─────────┬──────────┐
        │         │ N │ Mean │ Std Dev │ Std Error│
        ├─────────┼───┼──────┼─────────┼──────────┤
        │ PreTest │49 │68.50 │  5.20   │   0.74   │
        └─────────┴───┴──────┴─────────┴──────────┘
        
        One-Sample Test (Test Value = 70)
        ┌─────────┬──────┬────┬─────────┬──────────┬─────────────────┐
        │         │  t   │ df │Sig(2-t) │   Mean   │   95% CI of     │
        │         │      │    │         │   Diff   │   Difference    │
        ├─────────┼──────┼────┼─────────┼──────────┼─────────────────┤
        │ PreTest │-2.03 │ 48 │  .049   │  -1.50   │ [-2.99, -0.01]  │
        └─────────┴──────┴────┴─────────┴──────────┴─────────────────┘
        ```
        
        **Interpretation:**
        - t(48) = -2.03, p = .049 < .05 → Significant
        - Mean difference = -1.50 (actual mean is 1.5 points below 70)
        - 95% CI [-2.99, -0.01] doesn't include 0 → Significant
        
        **APA Format:**
        "A one-sample t-test revealed that PreTest scores (M = 68.50, SD = 5.20) 
        were significantly lower than 70, t(48) = -2.03, p = .049."
        """)
    
    with st.expander("📋 Independent Samples t-Test", expanded=True):
        st.markdown("""
        ### Comparing Two Groups
        
        **Example:** Do Active and Traditional groups differ in PostTest?
        
        **Steps:**
        1. **Analyze → Compare Means → Independent-Samples T Test**
        2. Move "PostTest" to "Test Variable(s)"
        3. Move "Group" to "Grouping Variable"
        4. Click **Define Groups**:
           - Group 1: 1 (Active)
           - Group 2: 2 (Traditional)
           - Click Continue
        5. Click **Options**: 95% CI
        6. Click **OK**
        
        **Output:**
        ```
        Group Statistics
        ┌────────────┬───────┬────┬──────┬─────────┬──────────┐
        │            │ Group │ N  │ Mean │ Std Dev │ Std Error│
        ├────────────┼───────┼────┼──────┼─────────┼──────────┤
        │ PostTest   │Active │ 24 │82.50 │  6.73   │   1.37   │
        │            │Trad   │ 25 │73.20 │  7.22   │   1.44   │
        └────────────┴───────┴────┴──────┴─────────┴──────────┘
        
        Independent Samples Test
        
        Levene's Test for Equality of Variances
        ┌──────┬─────┐
        │  F   │ Sig │
        ├──────┼─────┤
        │ 0.18 │.674 │
        └──────┴─────┘
        
        t-test for Equality of Means
        ┌──────┬────┬─────────┬──────────┬─────────────────┐
        │  t   │ df │Sig(2-t) │   Mean   │   95% CI of     │
        │      │    │         │   Diff   │   Difference    │
        ├──────┼────┼─────────┼──────────┼─────────────────┤
        │ 4.68 │ 47 │  .000   │   9.30   │  [5.32, 13.28]  │
        └──────┴────┴─────────┴──────────┴─────────────────┘
        ```
        
        **Step-by-Step Interpretation:**
        
        **1. Check Levene's Test:**
        - F = 0.18, p = .674 > .05
        - Variances are equal ✅
        - Use "Equal variances assumed" row
        
        **2. Check t-test:**
        - t(47) = 4.68, p < .001
        - Highly significant difference
        
        **3. Effect Size (Cohen's d):**
        ```
        Pooled SD = √[(23×6.73² + 24×7.22²)/(24+25-2)] = 6.98
        d = (82.50 - 73.20) / 6.98 = 1.33 (very large)
        ```
        
        **APA Format:**
        "An independent samples t-test revealed that Active Learning (M = 82.50, SD = 6.73) 
        resulted in significantly higher PostTest scores than Traditional instruction 
        (M = 73.20, SD = 7.22), t(47) = 4.68, p < .001, d = 1.33."
        """)
    
    with st.expander("📋 Paired Samples t-Test", expanded=True):
        st.markdown("""
        ### Before-After Comparison
        
        **Example:** Did students improve from PreTest to PostTest?
        
        **Steps:**
        1. **Analyze → Compare Means → Paired-Samples T Test**
        2. Select "PreTest" and "PostTest"
        3. Click arrow to move to "Paired Variables"
        4. Click **Options**: 95% CI
        5. Click **OK**
        
        **Output:**
        ```
        Paired Samples Statistics
        ┌──────────┬──────┬────┬─────────┬──────────┐
        │          │ Mean │ N  │ Std Dev │ Std Error│
        ├──────────┼──────┼────┼─────────┼──────────┤
        │ PreTest  │68.50 │ 49 │  5.20   │   0.74   │
        │ PostTest │78.50 │ 49 │  6.94   │   0.99   │
        └──────────┴──────┴────┴─────────┴──────────┘
        
        Paired Samples Correlations
        ┌──────────────────┬───┬────────┬─────┐
        │                  │ N │Correl  │ Sig │
        ├──────────────────┼───┼────────┼─────┤
        │PreTest-PostTest  │49 │  .680  │.000 │
        └──────────────────┴───┴────────┴─────┘
        
        Paired Samples Test
        ┌────────┬──────┬─────────┬──────────┬──────┬────┬─────────┬─────────────────┐
        │  Pair  │ Mean │ Std Dev │ Std Error│  t   │ df │Sig(2-t) │   95% CI of     │
        │        │ Diff │  Diff   │   Mean   │      │    │         │   Difference    │
        ├────────┼──────┼─────────┼──────────┼──────┼────┼─────────┼─────────────────┤
        │Pre-Post│-10.00│  5.60   │   0.80   │-12.50│ 48 │  .000   │[-11.61, -8.39]  │
        └────────┴──────┴─────────┴──────────┴──────┴────┴─────────┴─────────────────┘
        ```
        
        **Interpretation:**
        - Mean improvement = 10.00 points
        - t(48) = -12.50, p < .001
        - 95% CI [8.39, 11.61] - doesn't include 0
        - Correlation = .680 (moderate positive - students who scored high on PreTest also scored high on PostTest)
        
        **Effect Size:**
        ```
        Cohen's d = Mean Diff / SD Diff = 10.00 / 5.60 = 1.79 (very large)
        ```
        
        **APA Format:**
        "A paired samples t-test revealed a significant improvement from PreTest 
        (M = 68.50, SD = 5.20) to PostTest (M = 78.50, SD = 6.94), t(48) = -12.50, 
        p < .001, d = 1.79."
        """)

# =============================================================================
# TAB 4: ANOVA
# =============================================================================
with tab4:
    st.markdown("## 📈 ANOVA in SPSS")
    
    with st.expander("📊 One-Way ANOVA", expanded=True):
        st.markdown("""
        ### Comparing 3+ Groups
        
        **Example:** Compare PostTest across three teaching methods
        
        **Steps:**
        1. **Analyze → Compare Means → One-Way ANOVA**
        2. Move "PostTest" to "Dependent List"
        3. Move "Method" to "Factor"
        4. Click **Post Hoc**:
           - ✅ Tukey (equal variances)
           - ✅ Games-Howell (unequal variances)
           - Continue
        5. Click **Options**:
           - ✅ Descriptive
           - ✅ Homogeneity of variance test
           - ✅ Means plot
           - Continue
        6. Click **OK**
        
        **Output:**
        ```
        Descriptives
        ┌────────┬────┬──────┬─────────┬──────────┬─────┬─────┐
        │ Method │ N  │ Mean │ Std Dev │ Std Error│ Min │ Max │
        ├────────┼────┼──────┼─────────┼──────────┼─────┼─────┤
        │   A    │ 6  │76.20 │  3.11   │   1.27   │ 72  │ 80  │
        │   B    │ 6  │86.40 │  3.05   │   1.24   │ 82  │ 90  │
        │   C    │ 6  │71.40 │  2.97   │   1.21   │ 68  │ 75  │
        │ Total  │ 18 │78.00 │  6.54   │   1.54   │ 68  │ 90  │
        └────────┴────┴──────┴─────────┴──────────┴─────┴─────┘
        
        Test of Homogeneity of Variances
        ┌──────────┬────┬────┬─────┐
        │Levene St │ df1│ df2│ Sig │
        ├──────────┼────┼────┼─────┤
        │   0.02   │ 2  │ 15 │.981 │
        └──────────┴────┴────┴─────┘
        
        ANOVA
        ┌────────────────┬──────┬────┬──────┬───────┬─────┐
        │ Source         │  SS  │ df │  MS  │   F   │ Sig │
        ├────────────────┼──────┼────┼──────┼───────┼─────┤
        │ Between Groups │636.40│ 2  │318.20│ 34.55 │.000 │
        │ Within Groups  │138.00│ 15 │  9.20│       │     │
        │ Total          │774.40│ 17 │      │       │     │
        └────────────────┴──────┴────┴──────┴───────┴─────┘
        
        Post Hoc Tests - Multiple Comparisons (Tukey HSD)
        ┌────────┬────────┬──────────┬──────────┬─────┬─────────────────┐
        │  (I)   │  (J)   │   Mean   │ Std Error│ Sig │   95% CI        │
        │ Method │ Method │   Diff   │          │     │                 │
        ├────────┼────────┼──────────┼──────────┼─────┼─────────────────┤
        │   A    │   B    │ -10.20*  │   1.75   │.000 │[-14.58, -5.82]  │
        │   A    │   C    │   4.80*  │   1.75   │.032 │[  0.42,  9.18]  │
        │   B    │   C    │  15.00*  │   1.75   │.000 │[ 10.62, 19.38]  │
        └────────┴────────┴──────────┴──────────┴─────┴─────────────────┘
        * The mean difference is significant at the 0.05 level.
        ```
        
        **Step-by-Step Interpretation:**
        
        **1. Check Assumptions:**
        - Levene's test: p = .981 > .05 ✅ Equal variances
        
        **2. Check ANOVA:**
        - F(2, 15) = 34.55, p < .001
        - Significant difference among groups
        
        **3. Effect Size:**
        ```
        η² = SS_Between / SS_Total = 636.40 / 774.40 = 0.82 (very large)
        ```
        
        **4. Post-Hoc Results:**
        - Method B > Method A (p < .001, diff = 10.20)
        - Method A > Method C (p = .032, diff = 4.80)
        - Method B > Method C (p < .001, diff = 15.00)
        - **Ranking:** B > A > C
        
        **APA Format:**
        "A one-way ANOVA revealed a significant effect of teaching method on PostTest scores, 
        F(2, 15) = 34.55, p < .001, η² = 0.82. Post-hoc comparisons using Tukey's HSD indicated 
        that Method B (M = 86.40, SD = 3.05) produced significantly higher scores than both 
        Method A (M = 76.20, SD = 3.11, p < .001) and Method C (M = 71.40, SD = 2.97, p < .001). 
        Method A also scored significantly higher than Method C (p = .032)."
        """)

# =============================================================================
# TAB 5: NON-PARAMETRIC TESTS
# =============================================================================
with tab5:
    st.markdown("## 📉 Non-Parametric Tests in SPSS")
    
    with st.expander("🔬 Mann-Whitney U Test", expanded=True):
        st.markdown("""
        ### Non-Parametric Alternative to Independent t-Test
        
        **When to Use:**
        - Data is ordinal (Likert scales)
        - Data is not normally distributed
        - Small sample sizes
        - Extreme outliers present
        
        **Steps:**
        1. **Analyze → Nonparametric Tests → Legacy Dialogs → 2 Independent Samples**
        2. Move dependent variable to "Test Variable List"
        3. Move grouping variable to "Grouping Variable"
        4. Click **Define Groups**: Enter group codes (e.g., 1, 2)
        5. Test Type: ✅ Mann-Whitney U
        6. Click **OK**
        
        **Output:**
        ```
        Ranks
        ┌───────┬────┬──────────┬─────────────┐
        │ Group │ N  │Mean Rank │ Sum of Ranks│
        ├───────┼────┼──────────┼─────────────┤
        │Active │ 24 │  32.50   │    780.00   │
        │Trad   │ 25 │  17.80   │    445.00   │
        │Total  │ 49 │          │             │
        └───────┴────┴──────────┴─────────────┘
        
        Test Statistics
        ┌──────────────────┬────────┐
        │ Mann-Whitney U   │ 120.00 │
        │ Wilcoxon W       │ 445.00 │
        │ Z                │ -4.12  │
        │ Asymp. Sig.(2-t) │  .000  │
        └──────────────────┴────────┘
        ```
        
        **Interpretation:**
        - U = 120.00, Z = -4.12, p < .001
        - Active group has significantly higher ranks
        - Effect size: r = |Z|/√N = 4.12/√49 = 0.59 (large)
        
        **APA Format:**
        "A Mann-Whitney U test indicated that Active Learning (Mdn = 83, n = 24) 
        produced significantly higher scores than Traditional instruction (Mdn = 72, n = 25), 
        U = 120.00, z = -4.12, p < .001, r = 0.59."
        """)
    
    with st.expander("🔬 Kruskal-Wallis Test", expanded=True):
        st.markdown("""
        ### Non-Parametric Alternative to One-Way ANOVA
        
        **Steps:**
        1. **Analyze → Nonparametric Tests → Legacy Dialogs → K Independent Samples**
        2. Move dependent variable to "Test Variable List"
        3. Move grouping variable to "Grouping Variable"
        4. Click **Define Range**: Enter min and max (e.g., 1, 3)
        5. Test Type: ✅ Kruskal-Wallis H
        6. Click **OK**
        
        **Output:**
        ```
        Ranks
        ┌────────┬────┬──────────┐
        │ Method │ N  │Mean Rank │
        ├────────┼────┼──────────┤
        │   A    │ 6  │   9.50   │
        │   B    │ 6  │  15.50   │
        │   C    │ 6  │   3.50   │
        │ Total  │ 18 │          │
        └────────┴────┴──────────┘
        
        Test Statistics
        ┌──────────────────┬────────┐
        │ Kruskal-Wallis H │ 14.94  │
        │ df               │    2   │
        │ Asymp. Sig.      │  .001  │
        └──────────────────┴────────┘
        ```
        
        **Interpretation:**
        - H(2) = 14.94, p = .001
        - Significant difference among groups
        - Effect size: ε² = H/(N²-1)/(N+1) = 0.89 (very large)
        
        **Post-Hoc:** Use Mann-Whitney U for pairwise comparisons with Bonferroni correction
        """)

# =============================================================================
# TAB 6: TIPS & TRICKS
# =============================================================================
with tab6:
    st.markdown("## 💡 SPSS Tips & Tricks")
    
    with st.expander("⚡ Essential Tips", expanded=True):
        st.markdown("""
        ### Keyboard Shortcuts
        - `Ctrl + T` - Switch between Data View and Variable View
        - `Ctrl + D` - Duplicate selection
        - `Ctrl + F` - Find
        - `Ctrl + G` - Go to case
        - `F5` - Go to variable
        
        ### Syntax (for reproducibility)
        **Why use syntax?**
        - Reproducible analysis
        - Document your steps
        - Run same analysis on new data
        
        **How to save syntax:**
        1. In any dialog box, click **Paste** instead of OK
        2. Syntax window opens with commands
        3. Save as `.sps` file
        4. Run: Click ▶ or Ctrl+R
        
        **Example Syntax:**
        ```spss
        * Independent t-test.
        T-TEST GROUPS=Group(1 2)
          /VARIABLES=PostTest
          /CRITERIA=CI(.95).
        ```
        
        ### Common Errors & Solutions
        
        | Error | Cause | Solution |
        |-------|-------|----------|
        | "Variable not found" | Typo in variable name | Check spelling, case-sensitive |
        | "Insufficient memory" | Large dataset | Close other programs, increase memory |
        | "Cannot compute" | Missing data | Check for blank cells |
        | "Invalid grouping variable" | Wrong measure type | Set to Nominal in Variable View |
        | "No valid cases" | All data missing | Check filters, missing values |
        
        ### Best Practices
        
        1. **Always check assumptions first**
           - Normality: Analyze → Descriptive → Explore
           - Equal variances: Levene's test
           - Outliers: Boxplots
        
        2. **Save often**
           - SPSS can crash
           - Save data (.sav) and output (.spv) separately
        
        3. **Label everything**
           - Variable labels
           - Value labels
           - Output titles
        
        4. **Keep original data**
           - Never overwrite original file
           - Create new variables for transformations
        
        5. **Export results properly**
           - Copy tables to Word: Right-click → Copy → Paste Special → Picture
           - Or: File → Export → Word/Excel
        """)

show_footer()
