import streamlit as st
from utils.styles import apply_custom_css, show_footer
from utils.seo import inject_seo_meta
from utils.nav import show_top_nav

# SEO & Styles
inject_seo_meta(
    title="R Programming for Statistical Analysis | Complete Beginner's Guide [2024]",
    description="Learn R for statistics: data frames, t-tests, ANOVA, regression, ggplot2 visualization. Step-by-step tutorials with code examples.",
    keywords=[
        "r programming tutorial",
        "r statistics",
        "r for beginners",
        "rstudio tutorial",
        "r t-test",
        "r anova",
        "ggplot2 tutorial",
        "r data analysis"
    ],
    schema_type="TechArticle",
    canonical_url="https://researchethics.dev/software/r",
    reading_time=50
)
apply_custom_css()
show_top_nav(current_page="R Tutorial")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-radius: 10px; margin-bottom: 10px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">🔧 R Programming for Statistical Analysis</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #92400e;">From basics to advanced analysis with visualization</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🚀 Getting Started",
    "📊 Data & Basics",
    "🧪 Statistical Tests",
    "📈 Visualization",
    "💡 Tips & Resources"
])

# =============================================================================
# TAB 1: GETTING STARTED
# =============================================================================
with tab1:
    st.markdown("## 🚀 Getting Started with R")
    
    with st.expander("📥 Installation", expanded=True):
        st.markdown("""
        ### Step 1: Install R
        
        **Download R:**
        1. Go to [https://cran.r-project.org/](https://cran.r-project.org/)
        2. Click your operating system (Windows, Mac, Linux)
        3. Download latest version (e.g., R-4.3.2)
        4. Run installer, accept defaults
        
        ---
        ### Step 2: Install RStudio (Recommended)
        
        **Why RStudio?**
        - User-friendly interface
        - Code editor with syntax highlighting
        - Integrated help and plots
        - Package management
        
        **Download RStudio:**
        1. Go to [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)
        2. Download RStudio Desktop (Free)
        3. Install (R must be installed first)
        
        ---
        ### RStudio Interface
        
        **4 Main Panels:**
        
        1. **Source (Top Left)** - Write and save scripts (.R files)
        2. **Console (Bottom Left)** - Execute commands, see output
        3. **Environment/History (Top Right)** - View variables, command history
        4. **Files/Plots/Help (Bottom Right)** - Browse files, view plots, get help
        
        **Workflow:**
        1. Write code in Source panel
        2. Run line: Ctrl+Enter (Windows) or Cmd+Enter (Mac)
        3. See results in Console
        4. View plots in Plots panel
        
        ---
        ### First Commands
        
        **Try these in Console:**
        ```r
        # Basic calculator
        2 + 2                    # Result: 4
        10 * 5                   # Result: 50
        sqrt(16)                 # Result: 4
        
        # Create variable
        x <- 10                  # Assign 10 to x
        x                        # Display x
        
        # Get help
        ?mean                    # Help for mean function
        help(sd)                 # Help for sd function
        ```
        """)
    
    with st.expander("📦 Installing Packages", expanded=True):
        st.markdown("""
        ### Essential Packages for Statistics
        
        **What are packages?**
        - Collections of functions
        - Extend R's capabilities
        - Install once, load each session
        
        **Install packages (one-time):**
        ```r
        # Install essential packages
        install.packages("tidyverse")   # Data manipulation & ggplot2
        install.packages("psych")       # Descriptive statistics
        install.packages("car")         # ANOVA & regression
        install.packages("effsize")     # Effect sizes
        install.packages("ggplot2")     # Visualization
        ```
        
        **Load packages (each session):**
        ```r
        library(tidyverse)
        library(psych)
        library(car)
        library(effsize)
        ```
        
        **Check if package is installed:**
        ```r
        # List all installed packages
        installed.packages()
        
        # Check specific package
        "ggplot2" %in% installed.packages()
        ```
        
        **Update packages:**
        ```r
        update.packages()
        ```
        """)

# =============================================================================
# TAB 2: DATA & BASICS
# =============================================================================
with tab2:
    st.markdown("## 📊 Data Structures & Basic Operations")
    
    with st.expander("🔢 Vectors & Data Types", expanded=True):
        st.markdown("""
        ### Creating Vectors
        
        **Numeric vector:**
        ```r
        scores <- c(75, 82, 68, 90, 77)
        scores                           # Display
        length(scores)                   # Count: 5
        mean(scores)                     # Mean: 78.4
        ```
        
        **Character vector:**
        ```r
        names <- c("Alice", "Bob", "Carol", "David", "Eve")
        names[1]                         # First element: "Alice"
        ```
        
        **Factor (categorical):**
        ```r
        group <- factor(c("Control", "Treatment", "Control", "Treatment"))
        levels(group)                    # Show categories
        table(group)                     # Frequency count
        ```
        
        **Logical vector:**
        ```r
        passed <- c(TRUE, TRUE, FALSE, TRUE, FALSE)
        sum(passed)                      # Count TRUE: 3
        ```
        
        ---
        ### Vector Operations
        
        ```r
        # Arithmetic
        scores + 5                       # Add 5 to all
        scores * 1.1                     # Multiply all by 1.1
        
        # Indexing
        scores[1]                        # First element: 75
        scores[c(1,3,5)]                 # Elements 1, 3, 5
        scores[scores > 80]              # All scores > 80
        
        # Logical operations
        scores > 75                      # TRUE/FALSE for each
        which(scores > 80)               # Indices where TRUE
        ```
        """)
    
    with st.expander("📋 Data Frames", expanded=True):
        st.markdown("""
        ### Creating Data Frames
        
        **Method 1: From vectors**
        ```r
        # Create data frame
        df <- data.frame(
          StudentID = 1:5,
          Name = c("Alice", "Bob", "Carol", "David", "Eve"),
          PreTest = c(65, 70, 68, 72, 64),
          PostTest = c(82, 75, 85, 78, 70),
          Group = factor(c("Active", "Active", "Trad", "Trad", "Active"))
        )
        
        # View data
        df                               # Print entire data frame
        head(df)                         # First 6 rows
        tail(df)                         # Last 6 rows
        str(df)                          # Structure
        summary(df)                      # Summary statistics
        ```
        
        **Method 2: Import from CSV**
        ```r
        # Read CSV file
        df <- read.csv("data.csv")
        
        # Or with tidyverse
        library(readr)
        df <- read_csv("data.csv")
        ```
        
        ---
        ### Accessing Data
        
        ```r
        # Access columns
        df$PreTest                       # PreTest column
        df[, "PreTest"]                  # Same thing
        df[, 3]                          # 3rd column
        
        # Access rows
        df[1, ]                          # First row
        df[1:3, ]                        # Rows 1-3
        
        # Access specific cells
        df[1, 3]                         # Row 1, Column 3
        df$PreTest[1]                    # First PreTest score
        
        # Subset data
        df[df$Group == "Active", ]       # Only Active group
        subset(df, PostTest > 75)        # PostTest > 75
        ```
        
        ---
        ### Descriptive Statistics
        
        ```r
        # Single variable
        mean(df$PreTest)                 # Mean
        median(df$PreTest)               # Median
        sd(df$PreTest)                   # Standard deviation
        var(df$PreTest)                  # Variance
        min(df$PreTest)                  # Minimum
        max(df$PreTest)                  # Maximum
        range(df$PreTest)                # Min and Max
        quantile(df$PreTest)             # Quartiles
        
        # Multiple variables
        summary(df)                      # All variables
        
        # Using psych package
        library(psych)
        describe(df[, c("PreTest", "PostTest")])
        
        # Output:
        #          vars n  mean   sd median min max range  skew kurtosis   se
        # PreTest     1 5 67.80 3.11  68.00  64  72     8  0.00    -1.91 1.39
        # PostTest    2 5 78.00 5.70  78.00  70  85    15  0.00    -1.36 2.55
        ```
        """)

# =============================================================================
# TAB 3: STATISTICAL TESTS
# =============================================================================
with tab3:
    st.markdown("## 🧪 Statistical Tests in R")
    
    with st.expander("📋 t-Tests", expanded=True):
        st.markdown("""
        ### One-Sample t-Test
        
        **Example:** Is mean PreTest different from 70?
        
        ```r
        # Data
        pretest <- c(65, 70, 68, 72, 64, 66, 69, 71, 67, 68)
        
        # One-sample t-test
        t.test(pretest, mu = 70)
        
        # Output:
        #   One Sample t-test
        # 
        # data:  pretest
        # t = -2.45, df = 9, p-value = 0.037
        # alternative hypothesis: true mean is not equal to 70
        # 95 percent confidence interval:
        #  66.12 69.88
        # sample estimates:
        # mean of x 
        #      68
        
        # One-tailed test
        t.test(pretest, mu = 70, alternative = "less")
        
        # Effect size
        library(effsize)
        cohen.d(pretest, f = NA, mu = 70)
        ```
        
        ---
        ### Independent Samples t-Test
        
        **Example:** Compare Active vs Traditional groups
        
        ```r
        # Data
        active <- c(82, 75, 85, 78, 80, 83)
        traditional <- c(70, 72, 68, 75, 71, 69)
        
        # t-test
        t.test(active, traditional, var.equal = TRUE)
        
        # Output:
        #   Two Sample t-test
        # 
        # data:  active and traditional
        # t = 4.23, df = 10, p-value = 0.0017
        # alternative hypothesis: true difference in means is not equal to 0
        # 95 percent confidence interval:
        #   4.12 14.88
        # sample estimates:
        # mean of x mean of y 
        #     80.50     71.00
        
        # Check equal variances first
        var.test(active, traditional)
        # If p > 0.05, use var.equal = TRUE
        # If p < 0.05, use var.equal = FALSE (Welch's t-test)
        
        # Effect size
        cohen.d(active, traditional)
        ```
        
        ---
        ### Paired Samples t-Test
        
        **Example:** PreTest vs PostTest
        
        ```r
        # Data
        pretest <- c(65, 70, 68, 72, 64, 66, 69, 71, 67, 68)
        posttest <- c(82, 75, 85, 78, 80, 83, 79, 81, 77, 80)
        
        # Paired t-test
        t.test(posttest, pretest, paired = TRUE)
        
        # Output:
        #   Paired t-test
        # 
        # data:  posttest and pretest
        # t = 12.65, df = 9, p-value = 1.2e-06
        # alternative hypothesis: true difference in means is not equal to 0
        # 95 percent confidence interval:
        #   9.45 13.55
        # sample estimates:
        # mean of the differences 
        #                   11.5
        
        # Effect size
        cohen.d(posttest, pretest, paired = TRUE)
        ```
        """)
    
    with st.expander("📊 ANOVA", expanded=True):
        st.markdown("""
        ### One-Way ANOVA
        
        **Example:** Compare three teaching methods
        
        ```r
        # Create data
        scores <- c(75, 78, 72, 80, 76,      # Method A
                    85, 88, 82, 90, 87,      # Method B
                    70, 73, 68, 75, 71)      # Method C
        method <- factor(rep(c("A", "B", "C"), each = 5))
        
        # Create data frame
        df <- data.frame(scores, method)
        
        # One-way ANOVA
        model <- aov(scores ~ method, data = df)
        summary(model)
        
        # Output:
        #             Df Sum Sq Mean Sq F value   Pr(>F)    
        # method       2  636.4   318.2   34.55 1.35e-05 ***
        # Residuals   12  110.4     9.2                     
        
        # Effect size (eta-squared)
        library(effectsize)
        eta_squared(model)
        
        # Post-hoc tests
        TukeyHSD(model)
        
        # Output:
        #   Tukey multiple comparisons of means
        # 
        # $method
        #          diff       lwr       upr     p adj
        # B-A  10.2000   5.82000  14.58000 0.0001
        # C-A  -4.8000  -9.18000  -0.42000 0.0321
        # C-B -15.0000 -19.38000 -10.62000 0.0000
        
        # Check assumptions
        # 1. Normality
        shapiro.test(residuals(model))
        
        # 2. Homogeneity of variance
        library(car)
        leveneTest(scores ~ method, data = df)
        ```
        """)
    
    with st.expander("📈 Correlation & Regression", expanded=True):
        st.markdown("""
        ### Correlation
        
        ```r
        # Data
        attendance <- c(95, 88, 92, 85, 90, 87, 93, 89, 91, 86)
        scores <- c(82, 75, 80, 70, 78, 72, 81, 76, 79, 73)
        
        # Pearson correlation
        cor.test(attendance, scores)
        
        # Output:
        #   Pearson's product-moment correlation
        # 
        # data:  attendance and scores
        # t = 6.32, df = 8, p-value = 0.0002
        # alternative hypothesis: true correlation is not equal to 0
        # 95 percent confidence interval:
        #  0.6234 0.9645
        # sample estimates:
        #       cor 
        # 0.9123456
        
        # Spearman correlation (non-parametric)
        cor.test(attendance, scores, method = "spearman")
        ```
        
        ---
        ### Linear Regression
        
        ```r
        # Simple linear regression
        model <- lm(scores ~ attendance)
        summary(model)
        
        # Output:
        # Coefficients:
        #             Estimate Std. Error t value Pr(>|t|)    
        # (Intercept)  -12.500      8.234  -1.518    0.168    
        # attendance     1.000      0.092  10.870 1.23e-05 ***
        # 
        # Residual standard error: 2.449 on 8 degrees of freedom
        # Multiple R-squared:  0.9367,	Adjusted R-squared:  0.9288 
        # F-statistic: 118.2 on 1 and 8 DF,  p-value: 1.234e-05
        
        # Interpretation:
        # - Intercept = -12.5 (score when attendance = 0)
        # - Slope = 1.0 (1% increase in attendance → 1 point increase)
        # - R² = 0.937 (93.7% of variance explained)
        # - F(1,8) = 118.2, p < .001 (model is significant)
        
        # Make predictions
        new_data <- data.frame(attendance = c(85, 90, 95))
        predict(model, new_data)
        
        # Check assumptions
        par(mfrow = c(2,2))
        plot(model)
        ```
        """)

# =============================================================================
# TAB 4: VISUALIZATION
# =============================================================================
with tab4:
    st.markdown("## 📈 Data Visualization with ggplot2")
    
    with st.expander("📊 Basic Plots", expanded=True):
        st.markdown("""
        ### Histogram
        
        ```r
        library(ggplot2)
        
        # Data
        scores <- c(65, 70, 68, 72, 64, 66, 69, 71, 67, 68, 
                    75, 78, 72, 80, 76, 70, 73, 68, 75, 71)
        df <- data.frame(scores)
        
        # Histogram
        ggplot(df, aes(x = scores)) +
          geom_histogram(binwidth = 2, fill = "steelblue", color = "black") +
          labs(title = "Distribution of Test Scores",
               x = "Score",
               y = "Frequency") +
          theme_minimal()
        ```
        
        ---
        ### Boxplot
        
        ```r
        # Data with groups
        scores <- c(75, 78, 72, 80, 76,      # Method A
                    85, 88, 82, 90, 87,      # Method B
                    70, 73, 68, 75, 71)      # Method C
        method <- factor(rep(c("A", "B", "C"), each = 5))
        df <- data.frame(scores, method)
        
        # Boxplot
        ggplot(df, aes(x = method, y = scores, fill = method)) +
          geom_boxplot() +
          labs(title = "Test Scores by Teaching Method",
               x = "Method",
               y = "Score") +
          theme_minimal() +
          scale_fill_brewer(palette = "Set2")
        ```
        
        ---
        ### Scatter Plot
        
        ```r
        # Data
        attendance <- c(95, 88, 92, 85, 90, 87, 93, 89, 91, 86)
        scores <- c(82, 75, 80, 70, 78, 72, 81, 76, 79, 73)
        df <- data.frame(attendance, scores)
        
        # Scatter plot with regression line
        ggplot(df, aes(x = attendance, y = scores)) +
          geom_point(size = 3, color = "steelblue") +
          geom_smooth(method = "lm", se = TRUE, color = "red") +
          labs(title = "Relationship: Attendance vs Scores",
               x = "Attendance (%)",
               y = "Test Score") +
          theme_minimal()
        ```
        
        ---
        ### Bar Chart with Error Bars
        
        ```r
        # Calculate means and SDs
        library(dplyr)
        summary_df <- df %>%
          group_by(method) %>%
          summarise(
            mean_score = mean(scores),
            sd_score = sd(scores),
            se_score = sd(scores) / sqrt(n())
          )
        
        # Bar chart
        ggplot(summary_df, aes(x = method, y = mean_score, fill = method)) +
          geom_bar(stat = "identity") +
          geom_errorbar(aes(ymin = mean_score - se_score, 
                           ymax = mean_score + se_score),
                       width = 0.2) +
          labs(title = "Mean Scores by Method (±SE)",
               x = "Method",
               y = "Mean Score") +
          theme_minimal() +
          scale_fill_brewer(palette = "Set1")
        ```
        """)

# =============================================================================
# TAB 5: TIPS & RESOURCES
# =============================================================================
with tab5:
    st.markdown("## 💡 Tips & Resources")
    
    with st.expander("⚡ Essential Tips", expanded=True):
        st.markdown("""
        ### R Basics
        
        **Assignment:**
        ```r
        x <- 10              # Preferred
        x = 10               # Also works
        10 -> x              # Rarely used
        ```
        
        **Comments:**
        ```r
        # This is a comment
        x <- 10  # Comment after code
        ```
        
        **Case Sensitivity:**
        ```r
        myVar <- 10
        myvar <- 20          # Different variable!
        ```
        
        **Getting Help:**
        ```r
        ?mean                # Help for function
        ??regression         # Search help
        example(mean)        # Run examples
        ```
        
        ---
        ### Common Errors & Solutions
        
        | Error | Cause | Solution |
        |-------|-------|----------|
        | `object not found` | Variable doesn't exist | Check spelling, run creation code |
        | `could not find function` | Package not loaded | Run `library(package)` |
        | `non-numeric argument` | Wrong data type | Convert with `as.numeric()` |
        | `subscript out of bounds` | Index too large | Check vector length |
        | `package not installed` | Missing package | Run `install.packages()` |
        
        ---
        ### Best Practices
        
        1. **Use Scripts**
           - Save code in .R files
           - Reproducible analysis
           - Easy to modify
        
        2. **Comment Your Code**
           ```r
           # Load data
           df <- read.csv("data.csv")
           
           # Calculate mean by group
           aggregate(score ~ group, data = df, FUN = mean)
           ```
        
        3. **Use Meaningful Names**
           ```r
           # Good
           student_scores <- c(75, 82, 68)
           
           # Bad
           x <- c(75, 82, 68)
           ```
        
        4. **Check Your Data**
           ```r
           str(df)              # Structure
           summary(df)          # Summary
           head(df)             # First rows
           ```
        
        5. **Save Your Workspace**
           ```r
           save.image("mywork.RData")    # Save all
           load("mywork.RData")          # Load later
           ```
        """)
    
    with st.expander("📚 Learning Resources", expanded=True):
        st.markdown("""
        ### Free Online Resources
        
        **Official Documentation:**
        - [R Documentation](https://www.r-project.org/other-docs.html)
        - [CRAN Task Views](https://cran.r-project.org/web/views/)
        
        **Tutorials:**
        - [R for Data Science](https://r4ds.had.co.nz/) - Free online book
        - [Swirl](https://swirlstats.com/) - Learn R in R
        - [DataCamp](https://www.datacamp.com/courses/free-introduction-to-r) - Interactive courses
        
        **Cheat Sheets:**
        - [RStudio Cheat Sheets](https://www.rstudio.com/resources/cheatsheets/)
        - Base R, dplyr, ggplot2, and more
        
        **Community:**
        - [Stack Overflow](https://stackoverflow.com/questions/tagged/r) - Q&A
        - [RStudio Community](https://community.rstudio.com/) - Forums
        - [R-bloggers](https://www.r-bloggers.com/) - Tutorials and news
        
        ---
        ### Quick Reference
        
        **Data Import/Export:**
        ```r
        read.csv("file.csv")              # Import CSV
        write.csv(df, "file.csv")         # Export CSV
        read.table("file.txt")            # Import text
        load("file.RData")                # Load R data
        ```
        
        **Data Manipulation:**
        ```r
        subset(df, condition)             # Filter rows
        df[order(df$column), ]            # Sort
        aggregate(y ~ x, data=df, FUN=mean) # Group by
        ```
        
        **Statistical Tests:**
        ```r
        t.test(x, y)                      # t-test
        aov(y ~ x, data=df)               # ANOVA
        cor.test(x, y)                    # Correlation
        lm(y ~ x, data=df)                # Regression
        chisq.test(table(x, y))           # Chi-square
        ```
        """)

show_footer()
