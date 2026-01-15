# Paper II: Statistics and Computer Applications
## Quick Reference Guide for Theory Exam

---

## 📊 Course Objective
**To equip scholars with statistical tools and software skills for research data analysis.**

---

## 📚 UNIT I: Statistical Foundations

### 1. Hypothesis Design

**Null Hypothesis (H₀):**
- Statement of "no effect" or "no difference"
- What we test against
- Example: H₀: μ₁ = μ₂ (no difference between groups)

**Alternative Hypothesis (H₁):**
- Statement of effect or difference
- What we accept if we reject H₀
- Types:
  - **Two-tailed**: H₁: μ₁ ≠ μ₂ (different, direction unknown)
  - **One-tailed (right)**: H₁: μ₁ > μ₂ (greater than)
  - **One-tailed (left)**: H₁: μ₁ < μ₂ (less than)

**Hypothesis Testing Steps:**
1. State H₀ and H₁
2. Choose significance level (α = 0.05 typically)
3. Select appropriate test
4. Calculate test statistic
5. Find critical value or p-value
6. Make decision (reject or fail to reject H₀)
7. State conclusion in context

### 2. Parametric vs Non-Parametric Tests

| Aspect | Parametric | Non-Parametric |
|--------|------------|----------------|
| **Assumptions** | Normal distribution, interval/ratio data | No distribution assumption, any data type |
| **Data Type** | Interval, Ratio | Nominal, Ordinal, Non-normal |
| **Power** | Higher (if assumptions met) | Lower |
| **Examples** | t-test, ANOVA, Pearson r | Mann-Whitney, Kruskal-Wallis, Spearman |

### 3. Parametric Tests

#### **z-Test**
- **When**: Large sample (n > 30), population σ known
- **Formula**: z = (x̄ - μ₀) / (σ/√n)
- **Critical value**: ±1.96 (α = 0.05, two-tailed)
- **Decision**: If |z| > 1.96, reject H₀

#### **t-Test**

**One-Sample t-test:**
- **When**: Compare sample mean to population mean, σ unknown
- **Formula**: t = (x̄ - μ₀) / (s/√n)
- **df**: n - 1

**Independent Samples t-test:**
- **When**: Compare means of two independent groups
- **Formula**: t = (x̄₁ - x̄₂) / √(s²pooled(1/n₁ + 1/n₂))
- **df**: n₁ + n₂ - 2

**Paired t-test:**
- **When**: Compare means of same group at two times
- **Formula**: t = d̄ / (sd/√n)
- **df**: n - 1 (n = number of pairs)

**t-test Assumptions:**
- ✅ Continuous data (interval/ratio)
- ✅ Normal distribution (or n > 30)
- ✅ Independent observations
- ✅ Equal variances (for independent samples)

#### **ANOVA (Analysis of Variance)**
- **When**: Compare means of 3+ groups
- **Null**: H₀: μ₁ = μ₂ = μ₃ = ... (all means equal)
- **Test Statistic**: F = MSbetween / MSwithin
- **df**: df_between = k - 1, df_within = N - k
- **Decision**: If F > F_critical, reject H₀ (at least one mean differs)

**ANOVA Table:**
| Source | SS | df | MS | F |
|--------|----|----|----|----|
| Between Groups | SSB | k-1 | MSB = SSB/(k-1) | F = MSB/MSW |
| Within Groups | SSW | N-k | MSW = SSW/(N-k) | |
| Total | SST | N-1 | | |

**Post-hoc Tests** (if ANOVA significant):
- Tukey HSD
- Bonferroni
- Scheffé

### 4. Degrees of Freedom (df)

**Quick Reference:**
| Test | df Formula |
|------|-----------|
| One-sample t-test | n - 1 |
| Independent t-test | n₁ + n₂ - 2 |
| Paired t-test | n - 1 |
| Chi-square | (rows - 1) × (columns - 1) |
| ANOVA (between) | k - 1 |
| ANOVA (within) | N - k |

### 5. Confidence Intervals

**Formula**: CI = x̄ ± (critical value × SE)

**For mean**: CI = x̄ ± t(α/2, df) × (s/√n)

**Common Levels:**
| Confidence Level | z-value | Interpretation |
|-----------------|---------|----------------|
| 90% | 1.645 | 90% confident true mean is in interval |
| 95% | 1.96 | 95% confident true mean is in interval |
| 99% | 2.576 | 99% confident true mean is in interval |

### 6. Non-Parametric Tests

#### **Kolmogorov-Smirnov Test**
- **Purpose**: Test if sample follows a specific distribution
- **When**: Check normality assumption
- **H₀**: Sample follows specified distribution
- **Alternative**: Shapiro-Wilk test (better for small samples)

#### **Run Test**
- **Purpose**: Test randomness of a sequence
- **When**: Check if data is random or has pattern
- **Application**: Time series, quality control

#### **Mann-Whitney U Test**
- **Purpose**: Non-parametric alternative to independent t-test
- **When**: Ordinal data or non-normal distributions
- **H₀**: Two groups have same distribution
- **Effect size**: r = Z/√N

#### **Kruskal-Wallis Test**
- **Purpose**: Non-parametric alternative to one-way ANOVA
- **When**: Ordinal data or non-normal, 3+ groups
- **H₀**: All groups have same distribution
- **Post-hoc**: Dunn's test

#### **Chi-Square (χ²) Test**

**Goodness of Fit:**
- **Purpose**: Test if observed frequencies match expected
- **Formula**: χ² = Σ[(O - E)²/E]
- **df**: k - 1 (k = number of categories)

**Test of Independence:**
- **Purpose**: Test if two categorical variables are related
- **Formula**: χ² = Σ[(O - E)²/E]
- **df**: (rows - 1) × (columns - 1)
- **Effect size**: Cramér's V

**Expected Frequency**: E = (row total × column total) / grand total

**Assumption**: All expected frequencies ≥ 5

### 7. Type I and Type II Errors

| Reality | H₀ True | H₀ False |
|---------|---------|----------|
| **Reject H₀** | Type I Error (α) | Correct (Power = 1-β) |
| **Fail to Reject H₀** | Correct | Type II Error (β) |

- **Type I Error (α)**: False Positive - Reject true H₀
- **Type II Error (β)**: False Negative - Fail to reject false H₀
- **Power (1-β)**: Probability of correctly rejecting false H₀

**Typical α = 0.05** (5% chance of Type I error)

---

## 📈 UNIT II: Correlation & Regression

### 1. Charts and Tables

**Chart Selection:**
| Data Type | Best Chart |
|-----------|-----------|
| Continuous vs Continuous | Scatter plot |
| Categorical vs Continuous | Bar chart, Box plot |
| Distribution | Histogram |
| Time series | Line chart |
| Proportions | Pie chart |

### 2. Correlation Analysis

#### **Pearson Correlation (r)**
- **Range**: -1 to +1
- **Interpretation**:
  - r = +1: Perfect positive correlation
  - r = 0: No correlation
  - r = -1: Perfect negative correlation
  
**Strength:**
| |r| | Strength |
|------|----------|
| 0.00-0.19 | Very weak |
| 0.20-0.39 | Weak |
| 0.40-0.59 | Moderate |
| 0.60-0.79 | Strong |
| 0.80-1.00 | Very strong |

**Formula**: r = Σ[(x - x̄)(y - ȳ)] / √[Σ(x - x̄)² × Σ(y - ȳ)²]

**Assumptions:**
- ✅ Linear relationship
- ✅ Continuous variables
- ✅ Normal distribution
- ✅ No outliers

**r² (Coefficient of Determination):**
- Proportion of variance explained
- Example: r = 0.7 → r² = 0.49 (49% variance explained)

#### **Spearman's Rank Correlation (ρ)**
- **When**: Ordinal data or non-linear relationship
- **Range**: -1 to +1
- **Method**: Rank data, then calculate Pearson on ranks

### 3. Regression Analysis

#### **Simple Linear Regression**

**Equation**: ŷ = a + bx
- ŷ = predicted value
- a = y-intercept
- b = slope
- x = predictor variable

**Least Squares Method:**
- **Slope**: b = Σ[(x - x̄)(y - ȳ)] / Σ(x - x̄)²
- **Intercept**: a = ȳ - b × x̄

**Interpretation:**
- **Slope (b)**: For every 1-unit increase in x, y changes by b units
- **Intercept (a)**: Value of y when x = 0

**R² (Coefficient of Determination):**
- Proportion of variance in y explained by x
- Range: 0 to 1
- Higher is better (but watch for overfitting)

**Adjusted R²:**
- Adjusts for number of predictors
- Use for comparing models

### 4. Properties and Assumptions of Regression

**Classical Assumptions:**
1. **Linearity**: Relationship is linear
2. **Independence**: Observations are independent
3. **Homoscedasticity**: Constant variance of errors
4. **Normality**: Errors are normally distributed
5. **No multicollinearity**: Predictors not highly correlated (multiple regression)

**Checking Assumptions:**
- Linearity: Scatter plot
- Normality: Histogram of residuals, Q-Q plot
- Homoscedasticity: Residual plot (residuals vs fitted values)
- Independence: Durbin-Watson test

### 5. Gauss-Markov Theorem

**Statement**: Under classical assumptions, OLS (Ordinary Least Squares) estimators are BLUE:
- **B**est: Minimum variance
- **L**inear: Linear function of y
- **U**nbiased: E(b) = β
- **E**stimator: Estimates population parameter

**Implication**: OLS is the optimal method for linear regression when assumptions are met.

### 6. Multiple Regression

**Equation**: ŷ = b₀ + b₁x₁ + b₂x₂ + ... + bₖxₖ

**Interpretation:**
- **b₁**: Change in y for 1-unit change in x₁, holding other variables constant

**Model Fit:**
- **R²**: Proportion of variance explained
- **Adjusted R²**: Penalizes for number of predictors
- **F-test**: Overall model significance

**Multicollinearity:**
- **Problem**: Predictors highly correlated
- **Detection**: VIF (Variance Inflation Factor) > 10
- **Solution**: Remove correlated predictors

**Standardized Coefficients (β):**
- Allows comparison of relative importance
- All variables on same scale

---

## 💻 UNIT III: Computer Applications

### 1. MS Excel

**Essential Formulas:**
| Function | Purpose | Example |
|----------|---------|---------|
| =AVERAGE() | Mean | =AVERAGE(A1:A10) |
| =STDEV.S() | Sample SD | =STDEV.S(A1:A10) |
| =CORREL() | Correlation | =CORREL(A1:A10, B1:B10) |
| =TTEST() | t-test | =TTEST(A1:A10, B1:B10, 2, 2) |
| =VLOOKUP() | Lookup value | =VLOOKUP(value, range, col, 0) |

**Data Analysis ToolPak:**
- Descriptive Statistics
- t-Test (all types)
- ANOVA
- Regression
- Correlation

**Charts:**
- Insert → Charts → Select type
- Scatter plot for correlation
- Histogram for distribution
- Box plot for group comparison

### 2. SPSS

**Interface:**
- **Data View**: Enter data
- **Variable View**: Define variables (name, type, measure)

**Measurement Levels:**
- **Scale**: Continuous (interval/ratio)
- **Ordinal**: Ordered categories
- **Nominal**: Categories

**Common Analyses:**
| Analysis | Menu Path |
|----------|-----------|
| Descriptives | Analyze → Descriptive Statistics → Descriptives |
| t-test | Analyze → Compare Means → Independent-Samples T Test |
| ANOVA | Analyze → Compare Means → One-Way ANOVA |
| Correlation | Analyze → Correlate → Bivariate |
| Regression | Analyze → Regression → Linear |
| Chi-square | Analyze → Descriptive Statistics → Crosstabs |

**Output Interpretation:**
- **Sig. (p-value)**: If < 0.05, significant
- **t or F value**: Test statistic
- **df**: Degrees of freedom
- **Mean Difference**: Difference between groups

**APA Reporting from SPSS:**
```
t(df) = value, p = .xxx
F(df1, df2) = value, p = .xxx
r = .xx, p = .xxx
```

### 3. R Programming

**Installation:**
1. Install R from r-project.org
2. Install RStudio from rstudio.com

**Basic Commands:**
```r
# Read data
data <- read.csv("file.csv")

# Descriptive statistics
mean(data$variable)
sd(data$variable)
summary(data)

# t-test
t.test(score ~ group, data = data)

# ANOVA
model <- aov(score ~ treatment, data = data)
summary(model)

# Correlation
cor.test(data$x, data$y)

# Regression
model <- lm(y ~ x, data = data)
summary(model)

# Multiple regression
model <- lm(y ~ x1 + x2 + x3, data = data)
summary(model)
```

**Essential Packages:**
```r
install.packages("tidyverse")  # Data manipulation
install.packages("ggplot2")    # Visualization
install.packages("psych")      # Psychology stats
install.packages("car")        # Regression diagnostics
```

**Visualization:**
```r
library(ggplot2)

# Scatter plot
ggplot(data, aes(x = x, y = y)) + geom_point()

# Box plot
ggplot(data, aes(x = group, y = score)) + geom_boxplot()

# Histogram
ggplot(data, aes(x = score)) + geom_histogram()
```

### 4. MATLAB

**Basic Operations:**
```matlab
% Descriptive statistics
mean(data)
std(data)
var(data)

% t-test
[h, p, ci, stats] = ttest(sample1, sample2)

% ANOVA
[p, tbl, stats] = anova1(data, group)

% Correlation
[r, p] = corrcoef(x, y)

% Regression
mdl = fitlm(x, y)
```

**Plotting:**
```matlab
% Scatter plot
scatter(x, y)

% Histogram
histogram(data)

% Box plot
boxplot(data, group)
```

### 5. LaTeX

**Basic Document:**
```latex
\documentclass{article}
\usepackage{amsmath}  % For equations
\usepackage{graphicx} % For figures

\begin{document}

\title{Research Paper}
\author{Your Name}
\maketitle

\section{Introduction}
Text here.

% Equation
\begin{equation}
y = \beta_0 + \beta_1 x + \epsilon
\end{equation}

% Table
\begin{table}[h]
\centering
\begin{tabular}{|c|c|}
\hline
Variable & Mean \\
\hline
X & 10.5 \\
Y & 20.3 \\
\hline
\end{tabular}
\caption{Descriptive Statistics}
\end{table}

% Figure
\begin{figure}[h]
\centering
\includegraphics[width=0.5\textwidth]{plot.png}
\caption{Scatter Plot}
\end{figure}

\end{document}
```

### 6. ATLAS.ti

**Purpose**: Qualitative data analysis

**Workflow:**
1. Import documents (text, audio, video)
2. Create codes
3. Code segments of data
4. Create memos
5. Build networks
6. Generate reports

### 7. AMOS

**Purpose**: Structural Equation Modeling (SEM)

**Components:**
- **Observed variables**: Measured directly (rectangles)
- **Latent variables**: Not directly measured (ovals)
- **Paths**: Relationships (arrows)

**Model Fit Indices:**
- **χ²/df**: < 3 good
- **CFI**: > 0.95 good
- **RMSEA**: < 0.06 good
- **SRMR**: < 0.08 good

---

## 🎯 Test Selection Flowchart

```
What type of data?
├─ Continuous (Interval/Ratio)
│   ├─ Normal distribution?
│   │   ├─ Yes → Parametric tests
│   │   │   ├─ Compare to population → z-test (n>30) or t-test
│   │   │   ├─ Compare 2 groups → Independent t-test
│   │   │   ├─ Compare same group twice → Paired t-test
│   │   │   └─ Compare 3+ groups → ANOVA
│   │   └─ No → Non-parametric tests
│   │       ├─ Compare 2 groups → Mann-Whitney U
│   │       └─ Compare 3+ groups → Kruskal-Wallis
│   └─ Relationship between variables?
│       ├─ Linear → Pearson correlation, Regression
│       └─ Non-linear → Spearman correlation
└─ Categorical (Nominal/Ordinal)
    ├─ Ordinal → Spearman correlation, Mann-Whitney, Kruskal-Wallis
    └─ Nominal → Chi-square test
```

---

## 📝 Exam Preparation Checklist

### Formulas to Memorize:
- [ ] z-test formula
- [ ] t-test formula (all types)
- [ ] F-ratio for ANOVA
- [ ] Pearson correlation
- [ ] Regression slope and intercept
- [ ] Chi-square formula
- [ ] Confidence interval formula

### Concepts to Understand:
- [ ] When to use each test
- [ ] Assumptions of each test
- [ ] Interpretation of p-values
- [ ] Type I and Type II errors
- [ ] Degrees of freedom calculation
- [ ] R² interpretation
- [ ] Gauss-Markov theorem

### Software Skills:
- [ ] Excel: Data Analysis ToolPak
- [ ] SPSS: Basic analyses and output interpretation
- [ ] R: Basic commands and syntax
- [ ] LaTeX: Document structure

### Practice:
- [ ] Work through example problems
- [ ] Interpret SPSS/R output
- [ ] Write results in APA format
- [ ] Select appropriate test for scenarios

---

**Good Luck with Your Statistics Exam! 📊**

---

*Last Updated: 2026-01-15*
*For detailed explanations and examples, refer to the full course modules.*
