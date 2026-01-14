import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# Expert SEO & Styles
inject_seo_meta(
    title="Computer Applications for Research | Excel, SPSS, R, MATLAB, LaTeX, AMOS [2024]",
    description="Master computer applications for research: Excel for data analysis, SPSS statistical analysis, R programming, MATLAB computation, LaTeX document preparation, ATLAS.ti qualitative analysis, and AMOS SEM.",
    keywords=[
        "Excel data analysis",
        "SPSS tutorial",
        "R programming research",
        "MATLAB statistics",
        "LaTeX academic writing",
        "ATLAS.ti qualitative analysis",
        "AMOS structural equation modeling",
        "statistical software",
        "research software",
        "data analysis tools"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/statistics/computer-applications",
    reading_time=90,
    breadcrumbs=[
        {"name": "Home", "url": "https://researchethics.dev"},
        {"name": "Computer Applications", "url": "https://researchethics.dev/statistics/computer-applications"}
    ],
    course_info={
        "name": "Computer Applications for Research - Paper II Unit III",
        "description": "Practical guide to Excel, SPSS, R, MATLAB, LaTeX, ATLAS.ti, and AMOS for research data analysis and academic writing.",
        "level": "Doctoral",
        "prerequisites": "Basic computer skills",
        "teaches": ["Excel", "SPSS", "R", "MATLAB", "LaTeX", "ATLAS.ti", "AMOS"],
        "workload": "PT20H",
        "rating": "4.9",
        "rating_count": 834
    }
)
apply_custom_css()
show_top_nav(current_page="Computer Applications")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">💻 Unit III: Computer Applications</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #7c3aed;">Paper II: Statistics and Computer Applications — Tools for modern research.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 MS Excel",
    "📈 SPSS",
    "📉 R & MATLAB",
    "📝 LaTeX",
    "🔧 Other Tools"
])

# =============================================================================
# TAB 1: MS EXCEL
# =============================================================================
with tab1:
    st.markdown("## 📊 Chapter 1: MS Excel for Data Analysis")
    
    st.markdown("### 1.1 Why Excel for Research?")
    
    col_def, col_use = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Overview</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>Microsoft Excel</b> is a spreadsheet application widely used for data organization, basic statistical analysis, and visualization. It's accessible and requires no programming knowledge.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_use:
        st.markdown("""
        **Best For:**
        - Data entry and organization
        - Basic descriptive statistics
        - Simple charts and graphs
        - Data cleaning
        - Quick calculations
        
        **Limitations:**
        - Not ideal for complex analysis
        - Limited sample size handling
        - Not well-suited for reproducibility
        """)

    with st.expander("📐 Essential Excel Formulas for Research", expanded=True):
        st.markdown("""
        **Descriptive Statistics:**
        
        | Statistic | Excel Formula | Example |
        |-----------|---------------|---------|
        | Mean | `=AVERAGE(range)` | `=AVERAGE(A1:A100)` |
        | Median | `=MEDIAN(range)` | `=MEDIAN(A1:A100)` |
        | Mode | `=MODE(range)` | `=MODE(A1:A100)` |
        | Standard Deviation (sample) | `=STDEV.S(range)` | `=STDEV.S(A1:A100)` |
        | Standard Deviation (pop) | `=STDEV.P(range)` | `=STDEV.P(A1:A100)` |
        | Variance (sample) | `=VAR.S(range)` | `=VAR.S(A1:A100)` |
        | Count | `=COUNT(range)` | `=COUNT(A1:A100)` |
        | Sum | `=SUM(range)` | `=SUM(A1:A100)` |
        | Minimum | `=MIN(range)` | `=MIN(A1:A100)` |
        | Maximum | `=MAX(range)` | `=MAX(A1:A100)` |
        
        **Statistical Tests:**
        
        | Test | Excel Formula |
        |------|---------------|
        | t-test (independent) | `=T.TEST(array1, array2, tails, type)` |
        | Correlation | `=CORREL(array1, array2)` |
        | Chi-square test | `=CHISQ.TEST(actual_range, expected_range)` |
        | F-test | `=F.TEST(array1, array2)` |
        | Z-test | `=Z.TEST(array, x, sigma)` |
        
        **Regression:**
        
        | Function | Formula |
        |----------|---------|
        | Slope | `=SLOPE(known_y's, known_x's)` |
        | Intercept | `=INTERCEPT(known_y's, known_x's)` |
        | R-squared | `=RSQ(known_y's, known_x's)` |
        | Standard Error | `=STEYX(known_y's, known_x's)` |
        """)

    with st.expander("📊 Data Analysis ToolPak", expanded=True):
        st.markdown("""
        **Enabling Data Analysis ToolPak:**
        1. File → Options → Add-ins
        2. Select "Analysis ToolPak" → Go
        3. Check "Analysis ToolPak" → OK
        4. Access: Data tab → Data Analysis
        
        **Available Tools:**
        
        | Tool | Use For |
        |------|---------|
        | Descriptive Statistics | Complete summary statistics |
        | Correlation | Correlation matrix |
        | Regression | Full regression analysis with ANOVA |
        | t-Test | Two-sample and paired t-tests |
        | ANOVA | One-way and two-way ANOVA |
        | Histogram | Frequency distribution |
        | Moving Average | Time series smoothing |
        | Random Number Generation | Simulation |
        """)

    with st.expander("📈 Creating Charts", expanded=True):
        st.markdown("""
        **Steps to Create a Chart:**
        1. Select your data (including headers)
        2. Insert → Charts → Choose type
        3. Customize using Chart Design tab
        
        **Best Practices:**
        - Always include axis labels and titles
        - Use appropriate chart type for data
        - Avoid 3D charts (distorts perception)
        - Keep it simple and clear
        - Use consistent colors
        
        **Chart Types and Uses:**
        
        | Chart | Best For |
        |-------|----------|
        | Column/Bar | Comparing categories |
        | Line | Trends over time |
        | Scatter | Relationship between variables |
        | Pie | Parts of whole (use sparingly) |
        | Box Plot | Distribution comparison |
        """)

# =============================================================================
# TAB 2: SPSS
# =============================================================================
with tab2:
    st.markdown("## 📈 Chapter 2: SPSS (Statistical Package for Social Sciences)")
    
    st.markdown("### 2.1 Introduction to SPSS")
    
    col_def, col_use = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a;">
            <h4 style="color: #166534; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 Overview</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>SPSS</b> (now IBM SPSS Statistics) is a comprehensive statistical software widely used in social sciences, business, and health research. It offers a point-and-click interface for complex analyses.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_use:
        st.markdown("""
        **Strengths:**
        - User-friendly GUI
        - Comprehensive statistical tests
        - Good for beginners
        - Excellent documentation
        - Widely taught in universities
        
        **Limitations:**
        - Expensive license
        - Less flexible than R/Python
        - Syntax can be cumbersome
        """)

    with st.expander("🖥️ SPSS Interface", expanded=True):
        st.markdown("""
        **Two Main Windows:**
        
        | Window | Purpose |
        |--------|---------|
        | **Data View** | Spreadsheet-like data entry |
        | **Variable View** | Define variable properties |
        
        **Variable View Settings:**
        - **Name:** Variable identifier (no spaces)
        - **Type:** Numeric, String, Date, etc.
        - **Width:** Number of characters
        - **Decimals:** Decimal places
        - **Label:** Descriptive name
        - **Values:** Code labels (e.g., 1=Male, 2=Female)
        - **Missing:** Define missing values
        - **Measure:** Scale, Ordinal, or Nominal
        """)

    with st.expander("📊 Common SPSS Procedures", expanded=True):
        st.markdown("""
        **Menu Navigation:**
        
        | Analysis | Menu Path |
        |----------|-----------|
        | Descriptive Statistics | Analyze → Descriptive Statistics → Descriptives |
        | Frequencies | Analyze → Descriptive Statistics → Frequencies |
        | Cross-tabulation | Analyze → Descriptive Statistics → Crosstabs |
        | Independent t-test | Analyze → Compare Means → Independent-Samples T Test |
        | Paired t-test | Analyze → Compare Means → Paired-Samples T Test |
        | One-way ANOVA | Analyze → Compare Means → One-Way ANOVA |
        | Correlation | Analyze → Correlate → Bivariate |
        | Regression | Analyze → Regression → Linear |
        | Chi-square | Analyze → Descriptive Statistics → Crosstabs → Statistics |
        | Factor Analysis | Analyze → Dimension Reduction → Factor |
        | Reliability | Analyze → Scale → Reliability Analysis |
        """)

    with st.expander("💻 SPSS Syntax Examples", expanded=True):
        st.markdown("""
        **Descriptive Statistics:**
        ```
        DESCRIPTIVES VARIABLES=age income score
          /STATISTICS=MEAN STDDEV MIN MAX.
        ```
        
        **Independent t-test:**
        ```
        T-TEST GROUPS=gender(1 2)
          /VARIABLES=score
          /CRITERIA=CI(.95).
        ```
        
        **Correlation:**
        ```
        CORRELATIONS
          /VARIABLES=var1 var2 var3
          /PRINT=TWOTAIL NOSIG
          /MISSING=PAIRWISE.
        ```
        
        **Linear Regression:**
        ```
        REGRESSION
          /DEPENDENT y
          /METHOD=ENTER x1 x2 x3
          /STATISTICS=COEFF OUTS R ANOVA.
        ```
        
        **💡 Tip:** Save syntax for reproducibility. File → Save As → SPSS Syntax (.sps)
        """)

    with st.expander("📋 Learning Tips for SPSS", expanded=True):
        st.markdown("""
        **Step-by-Step Learning Path:**
        
        1. **Week 1-2:** Data entry and variable definition
        2. **Week 3-4:** Descriptive statistics and frequencies
        3. **Week 5-6:** Correlation and t-tests
        4. **Week 7-8:** ANOVA and regression
        5. **Week 9-10:** Advanced topics (factor analysis, etc.)
        
        **Resources:**
        - IBM SPSS Documentation (free online)
        - Laerd Statistics SPSS tutorials
        - Andy Field - "Discovering Statistics Using IBM SPSS Statistics"
        
        **Best Practices:**
        - Always examine your data first (Descriptives, Histograms)
        - Check assumptions before running tests
        - Save your syntax for reproducibility
        - Use variable labels for clear output
        """)

# =============================================================================
# TAB 3: R & MATLAB
# =============================================================================
with tab3:
    st.markdown("## 📉 Chapter 3: R and MATLAB")
    
    # R Programming
    st.markdown("### 3.1 R for Statistical Computing")
    
    with st.expander("📊 Introduction to R", expanded=True):
        col_def, col_use = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
                <h4 style="color: #1e40af; margin: 0 0 8px 0 !important;">📖 What is R?</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>R</b> is a free, open-source programming language for statistical computing and graphics. It's the gold standard in academia and increasingly popular in industry.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_use:
            st.markdown("""
            **Why Use R:**
            - Free and open source
            - 18,000+ packages
            - Reproducible research (R Markdown)
            - Publication-quality graphics
            - Active community
            
            **Get Started:** Download from [r-project.org](https://www.r-project.org/)
            
            **IDE:** RStudio (free)
            """)

    with st.expander("💻 Essential R Commands", expanded=True):
        st.markdown("""
        **Basic Operations:**
        ```r
        # Assignment
        x <- 5
        y <- c(1, 2, 3, 4, 5)  # Vector
        
        # Basic stats
        mean(y)      # Mean
        sd(y)        # Standard deviation
        median(y)    # Median
        summary(y)   # Summary statistics
        ```
        
        **Reading Data:**
        ```r
        # Read CSV
        data <- read.csv("filename.csv")
        
        # Read Excel
        library(readxl)
        data <- read_excel("filename.xlsx")
        
        # View data
        head(data)    # First 6 rows
        str(data)     # Structure
        names(data)   # Column names
        ```
        
        **Statistical Tests:**
        ```r
        # t-test
        t.test(group1, group2)
        
        # Paired t-test
        t.test(before, after, paired = TRUE)
        
        # Correlation
        cor.test(x, y)
        
        # ANOVA
        aov_result <- aov(score ~ group, data = mydata)
        summary(aov_result)
        
        # Regression
        model <- lm(y ~ x1 + x2, data = mydata)
        summary(model)
        
        # Chi-square
        chisq.test(table(var1, var2))
        ```
        
        **Visualization:**
        ```r
        # Base R
        plot(x, y)
        hist(x)
        boxplot(score ~ group)
        
        # ggplot2 (better graphics)
        library(ggplot2)
        ggplot(data, aes(x = x, y = y)) + 
          geom_point() +
          geom_smooth(method = "lm")
        ```
        """)

    with st.expander("📚 Key R Packages for Research", expanded=True):
        st.markdown("""
        | Package | Purpose | Install |
        |---------|---------|---------|
        | **tidyverse** | Data manipulation & viz | `install.packages("tidyverse")` |
        | **ggplot2** | Advanced graphics | Part of tidyverse |
        | **dplyr** | Data wrangling | Part of tidyverse |
        | **psych** | Psychology statistics | `install.packages("psych")` |
        | **lme4** | Mixed-effects models | `install.packages("lme4")` |
        | **lavaan** | Structural equation modeling | `install.packages("lavaan")` |
        | **car** | Companion to Applied Regression | `install.packages("car")` |
        | **rmarkdown** | Reproducible reports | `install.packages("rmarkdown")` |
        """)

    # MATLAB
    st.markdown("### 3.2 MATLAB")
    
    with st.expander("🔢 Introduction to MATLAB", expanded=True):
        col_def, col_use = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #fff7ed; padding: 14px; border-radius: 8px; border-left: 4px solid #f97316;">
                <h4 style="color: #ea580c; margin: 0 0 8px 0 !important;">📖 What is MATLAB?</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>MATLAB</b> (Matrix Laboratory) is a proprietary language for numerical computing. It excels at matrix operations, signal processing, and engineering applications.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_use:
            st.markdown("""
            **Best For:**
            - Matrix computations
            - Signal/image processing
            - Control systems
            - Engineering simulations
            - Algorithm development
            
            **Note:** MATLAB is commercial software (expensive). Consider GNU Octave as a free alternative.
            """)

    with st.expander("💻 Basic MATLAB Commands", expanded=True):
        st.markdown("""
        **Basic Operations:**
        ```matlab
        % Assignment
        x = 5;
        y = [1 2 3 4 5];  % Row vector
        z = [1; 2; 3];    % Column vector
        A = [1 2; 3 4];   % Matrix
        
        % Basic statistics
        mean(y)
        std(y)
        median(y)
        var(y)
        ```
        
        **Matrix Operations:**
        ```matlab
        A = [1 2; 3 4];
        B = [5 6; 7 8];
        
        A + B      % Addition
        A * B      % Matrix multiplication
        A .* B     % Element-wise multiplication
        A'         % Transpose
        inv(A)     % Inverse
        det(A)     % Determinant
        eig(A)     % Eigenvalues
        ```
        
        **Statistical Functions:**
        ```matlab
        % t-test
        [h, p] = ttest2(group1, group2);
        
        % Correlation
        [R, P] = corrcoef(X, Y);
        
        % Regression
        b = regress(Y, [ones(size(X)) X]);
        % or
        mdl = fitlm(X, Y);
        
        % ANOVA
        [p, tbl, stats] = anova1(data, groups);
        ```
        
        **Plotting:**
        ```matlab
        plot(x, y)
        scatter(x, y)
        histogram(x)
        boxplot(data, groups)
        ```
        """)

    with st.expander("📋 R vs MATLAB Comparison", expanded=True):
        st.markdown("""
        | Feature | R | MATLAB |
        |---------|---|--------|
        | **Cost** | Free | Expensive |
        | **Focus** | Statistics | Engineering/Matrix |
        | **Learning Curve** | Moderate | Moderate |
        | **Graphics** | Excellent (ggplot2) | Good |
        | **Packages** | 18,000+ | Toolboxes (paid) |
        | **Speed** | Fast (with optimization) | Very fast |
        | **Reproducibility** | Excellent (R Markdown) | Good |
        | **Industry Use** | Academia, Data Science | Engineering, Finance |
        
        **Recommendation:** 
        - For statistics/social sciences → **R**
        - For engineering/numerical computing → **MATLAB**
        - For budget-conscious → **R** or **GNU Octave**
        """)

# =============================================================================
# TAB 4: LaTeX
# =============================================================================
with tab4:
    st.markdown("## 📝 Chapter 4: LaTeX for Academic Writing")
    
    st.markdown("### 4.1 Introduction to LaTeX")
    
    col_def, col_analogy = st.columns(2)
    with col_def:
        st.markdown("""
        <div style="background: #eff6ff; padding: 14px; border-radius: 8px; border-left: 4px solid #2563eb;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0 !important; font-size: 14px !important;">📖 What is LaTeX?</h4>
            <p style="margin: 0 !important; font-size: 13px;"><b>LaTeX</b> is a typesetting system for producing professional documents, especially those with complex mathematical formulas. It's the standard for academic publishing in STEM fields.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_analogy:
        st.markdown("""
        <div style="background: #fef3c7; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
            <h4 style="color: #b45309; margin: 0 0 8px 0 !important; font-size: 14px !important;">💡 Analogy: HTML for Documents</h4>
            <p style="margin: 0 !important; font-size: 13px;">LaTeX is like HTML for academic documents. You write code that describes the content and structure, and LaTeX compiles it into a beautifully formatted PDF.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🚀 Getting Started with LaTeX", expanded=True):
        st.markdown("""
        **Options to Use LaTeX:**
        
        | Option | Description | Recommendation |
        |--------|-------------|----------------|
        | **Overleaf** | Online editor, no installation | Best for beginners |
        | **TeXstudio** | Desktop editor | Good for offline work |
        | **VS Code + LaTeX Workshop** | Programmer-friendly | For developers |
        
        **Overleaf:** [overleaf.com](https://www.overleaf.com) (free account available)
        """)

    with st.expander("📄 Basic LaTeX Document Structure", expanded=True):
        st.markdown("""
        ```latex
        \\documentclass{article}  % Document type
        
        % Preamble - packages and settings
        \\usepackage{amsmath}     % Math support
        \\usepackage{graphicx}   % Images
        \\usepackage{hyperref}   % Hyperlinks
        
        \\title{My Research Paper}
        \\author{John Researcher}
        \\date{\\today}
        
        \\begin{document}
        
        \\maketitle              % Generate title
        
        \\begin{abstract}
        This is my abstract...
        \\end{abstract}
        
        \\section{Introduction}
        This is the introduction.
        
        \\section{Methods}
        Description of methods.
        
        \\subsection{Participants}
        Details about participants.
        
        \\section{Results}
        The results show...
        
        \\section{Conclusion}
        In conclusion...
        
        \\end{document}
        ```
        
        **Document Classes:**
        - `article` - For journal articles, short reports
        - `report` - For longer reports with chapters
        - `book` - For books
        - `thesis` - For dissertations (often institution-specific)
        """)

    with st.expander("🔢 Mathematical Equations in LaTeX", expanded=True):
        st.markdown("""
        **Inline Math:** Use single `$...$`
        ```latex
        The mean is $\\bar{x} = \\frac{\\sum x_i}{n}$
        ```
        
        **Display Math:** Use `$$...$$` or `\\[...\\]`
        ```latex
        The regression equation is:
        $$Y = \\beta_0 + \\beta_1 X + \\epsilon$$
        ```
        
        **Common Symbols:**
        
        | Symbol | LaTeX | Result |
        |--------|-------|--------|
        | Mean | `\\bar{x}` | x̄ |
        | Sum | `\\sum` | Σ |
        | Square root | `\\sqrt{x}` | √x |
        | Fraction | `\\frac{a}{b}` | a/b |
        | Greek letters | `\\alpha, \\beta` | α, β |
        | Subscript | `x_i` | xᵢ |
        | Superscript | `x^2` | x² |
        | Hat | `\\hat{y}` | ŷ |
        | Chi-square | `\\chi^2` | χ² |
        
        **Example - t-test formula:**
        ```latex
        $$t = \\frac{\\bar{x} - \\mu_0}{s / \\sqrt{n}}$$
        ```
        """)

    with st.expander("📊 Tables and Figures", expanded=True):
        st.markdown("""
        **Creating a Table:**
        ```latex
        \\begin{table}[h]
        \\centering
        \\caption{Descriptive Statistics}
        \\begin{tabular}{lcc}
        \\hline
        Variable & Mean & SD \\\\
        \\hline
        Age & 25.3 & 4.2 \\\\
        Score & 78.5 & 12.1 \\\\
        \\hline
        \\end{tabular}
        \\end{table}
        ```
        
        **Including Figures:**
        ```latex
        \\begin{figure}[h]
        \\centering
        \\includegraphics[width=0.8\\textwidth]{figure1.png}
        \\caption{Results of the experiment}
        \\label{fig:results}
        \\end{figure}
        ```
        
        **Referencing:** Use `\\label{}` and `\\ref{}`
        ```latex
        As shown in Figure \\ref{fig:results}...
        ```
        """)

    with st.expander("📚 Bibliography Management", expanded=True):
        st.markdown("""
        **Using BibTeX:**
        
        1. Create `.bib` file with references:
        ```bibtex
        @article{smith2023,
          author = {Smith, John and Jones, Mary},
          title = {Research Methods in Statistics},
          journal = {Journal of Research},
          year = {2023},
          volume = {15},
          pages = {123-145}
        }
        ```
        
        2. Cite in document:
        ```latex
        According to \\cite{smith2023}, the method...
        ```
        
        3. Include bibliography:
        ```latex
        \\bibliographystyle{apa}  % or plain, harvard, etc.
        \\bibliography{references}  % your .bib filename
        ```
        
        **Tip:** Use **Zotero** or **Mendeley** to manage references and export to BibTeX
        """)

# =============================================================================
# TAB 5: OTHER TOOLS
# =============================================================================
with tab5:
    st.markdown("## 🔧 Chapter 5: Other Research Tools")
    
    # ATLAS.ti
    st.markdown("### 5.1 ATLAS.ti (Qualitative Data Analysis)")
    
    with st.expander("📝 ATLAS.ti Overview", expanded=True):
        col_def, col_use = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #f0fdf4; padding: 14px; border-radius: 8px; border-left: 4px solid #16a34a;">
                <h4 style="color: #166534; margin: 0 0 8px 0 !important;">📖 What is ATLAS.ti?</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>ATLAS.ti</b> is a Computer-Assisted Qualitative Data Analysis Software (CAQDAS). It helps researchers organize, code, and analyze qualitative data like interviews, documents, images, and videos.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_use:
            st.markdown("""
            **Use For:**
            - Thematic analysis
            - Content analysis
            - Grounded theory
            - Discourse analysis
            - Literature reviews
            
            **Data Types:**
            - Text documents
            - Audio/video
            - Images
            - PDFs
            - Surveys
            """)
        
        st.markdown("""
        **Key Concepts:**
        
        | Term | Definition |
        |------|------------|
        | **Quotation** | Selected segment of data |
        | **Code** | Label assigned to quotation |
        | **Code Group** | Collection of related codes |
        | **Memo** | Researcher's notes and reflections |
        | **Network** | Visual representation of connections |
        
        **Workflow:**
        1. Import documents
        2. Read and highlight quotations
        3. Create and assign codes
        4. Group codes into themes
        5. Write memos
        6. Build networks
        7. Generate reports
        """)

    # AMOS
    st.markdown("### 5.2 AMOS (Structural Equation Modeling)")
    
    with st.expander("📊 AMOS Overview", expanded=True):
        col_def, col_use = st.columns([1, 1])
        with col_def:
            st.markdown("""
            <div style="background: #faf5ff; padding: 14px; border-radius: 8px; border-left: 4px solid #7c3aed;">
                <h4 style="color: #6d28d9; margin: 0 0 8px 0 !important;">📖 What is AMOS?</h4>
                <p style="margin: 0 !important; font-size: 13px;"><b>AMOS</b> (Analysis of Moment Structures) is a structural equation modeling (SEM) software that uses graphical interface to specify, estimate, and test models.</p>
            </div>
            """, unsafe_allow_html=True)
        with col_use:
            st.markdown("""
            **Use For:**
            - Path analysis
            - Confirmatory Factor Analysis (CFA)
            - Structural Equation Modeling (SEM)
            - Multi-group analysis
            - Mediation/moderation testing
            """)
        
        st.markdown("""
        **Key AMOS Concepts:**
        
        | Shape | Meaning |
        |-------|---------|
        | 🔲 Rectangle | Observed variable |
        | ⭕ Oval | Latent variable |
        | → Single arrow | Regression path |
        | ↔ Double arrow | Correlation |
        
        **Fit Indices to Report:**
        
        | Index | Good Fit Threshold |
        |-------|-------------------|
        | Chi-square/df | < 3 |
        | CFI | > 0.95 |
        | TLI | > 0.95 |
        | RMSEA | < 0.06 |
        | SRMR | < 0.08 |
        
        **Alternative:** Use **lavaan** package in R (free) for SEM
        """)

    # Software Comparison
    st.markdown("### 5.3 Software Selection Guide")
    
    with st.expander("📋 Which Software Should You Use?", expanded=True):
        st.markdown("""
        | Research Need | Recommended Software |
        |---------------|----------------------|
        | Basic statistics | Excel, SPSS |
        | Advanced statistics | R, SPSS |
        | Reproducible research | R, Python |
        | Mathematical publishing | LaTeX |
        | Matrix computation | MATLAB, R |
        | Qualitative analysis | ATLAS.ti, NVivo |
        | Structural equation modeling | AMOS, lavaan (R) |
        | Survey design | Qualtrics, Google Forms |
        | Reference management | Zotero, Mendeley |
        
        **Budget-Conscious Alternatives:**
        
        | Commercial | Free Alternative |
        |------------|------------------|
        | SPSS | R, JAMOVI, JASP |
        | MATLAB | GNU Octave, Python |
        | AMOS | lavaan (R) |
        | ATLAS.ti | RQDA (R), QualCoder |
        | MS Office | LibreOffice, Google Docs |
        """)

    # Learning Resources
    with st.expander("📚 Learning Resources", expanded=True):
        st.markdown("""
        **Recommended Books:**
        
        | Topic | Book |
        |-------|------|
        | Statistics | Gupta & Kapoor - Fundamentals of Mathematical Statistics |
        | R | Mark Gardener - Beginning R |
        | MATLAB | MATLAB Programming (PHI) |
        | SPSS | SPSS Handbook (Himalaya Publishing) |
        
        **Online Resources:**
        
        | Platform | Best For |
        |----------|----------|
        | Coursera | Comprehensive courses |
        | DataCamp | R, Python, SQL |
        | YouTube (StatQuest) | Statistics concepts |
        | Stack Overflow | Coding help |
        | Cross Validated | Statistics Q&A |
        | Overleaf Learn | LaTeX tutorials |
        """)

# Footer
show_footer()
