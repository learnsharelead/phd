# COMPREHENSIVE DEEP REVIEW: Paper II - Statistics and Computer Applications
## Complete Topic-by-Topic Analysis

**Review Date**: 2026-01-15  
**Part**: 2 of 3  
**Focus**: Statistical Foundations, Correlation & Regression, Computer Applications

---

## 📊 PAPER II OVERVIEW

**Course Objective**: To equip scholars with statistical tools and software skills for research data analysis.

**Current Overall Status**: 70% Complete
- Good theoretical foundation exists
- Needs more worked examples
- Software tutorials need expansion
- Practice problems needed

---

## 📐 UNIT I: STATISTICAL FOUNDATIONS

### Topic 1: Hypothesis Design - Null and Alternate Hypotheses ✅ GOOD
**Syllabus Requirement**: Hypothesis design: Null and Alternate hypotheses

**Current Status**: ✅ **WELL COVERED** (File: 5_📐_Statistical_Foundations.py)
- **Coverage**: 80%
- **Content Quality**: Good
- **Words**: ~800
- **Examples**: Multiple

**What's Covered**:
- ✅ Hypothesis definition with analogy
- ✅ Null hypothesis (H₀) explanation
- ✅ Alternative hypothesis (H₁) explanation
- ✅ Types: Two-tailed, one-tailed (right), one-tailed (left)
- ✅ Comparison table
- ✅ Characteristics of good hypothesis

**What's Missing** (20%):
- [ ] **10+ hypothesis formulation examples** from different fields
- [ ] Statistical vs research hypothesis
- [ ] One-tailed vs two-tailed decision guide
- [ ] Common mistakes in hypothesis writing
- [ ] Practice exercises with solutions

**DETAILED CONTENT TO ADD**:

```markdown
### Hypothesis Formulation Examples by Field

#### 1. Psychology
**Research Question**: Does meditation reduce anxiety?
- H₀: μ_meditation = μ_control (Meditation has no effect on anxiety)
- H₁: μ_meditation < μ_control (Meditation reduces anxiety) [One-tailed left]
- **Why one-tailed**: Theory predicts specific direction (reduction)

#### 2. Medicine
**Research Question**: Does Drug X lower blood pressure?
- H₀: μ_drug = μ_placebo
- H₁: μ_drug < μ_placebo [One-tailed left]
- **Test**: Independent samples t-test
- **α**: 0.05

#### 3. Education
**Research Question**: Does online learning affect test scores differently than traditional?
- H₀: μ_online = μ_traditional
- H₁: μ_online ≠ μ_traditional [Two-tailed]
- **Why two-tailed**: No prediction of direction

#### 4. Business
**Research Question**: Do training programs increase sales?
- H₀: μ_after ≤ μ_before
- H₁: μ_after > μ_before [One-tailed right]
- **Test**: Paired t-test

#### 5. Engineering
**Research Question**: Does new material have different strength?
- H₀: μ_new = μ_standard
- H₁: μ_new ≠ μ_standard [Two-tailed]

### Common Mistakes and Corrections

❌ **Mistake 1**: "H₀: There is a difference"
✅ **Correct**: "H₀: There is NO difference" (Null = no effect)

❌ **Mistake 2**: "H₁: μ₁ = μ₂"
✅ **Correct**: "H₁: μ₁ ≠ μ₂" (Alternative = effect exists)

❌ **Mistake 3**: Using one-tailed when direction unknown
✅ **Correct**: Use two-tailed unless strong theoretical reason

❌ **Mistake 4**: "H₀: The drug works"
✅ **Correct**: "H₀: The drug has no effect"
```

**Recommendations**:
1. **IMPORTANT**: Add 15+ hypothesis examples from various fields
2. Add decision tree for one-tailed vs two-tailed
3. Include 10 practice problems with solutions
4. Add common mistakes section

**Priority**: **HIGH**

---

### Topic 2: Parametric and Non-Parametric Tests ✅ GOOD
**Syllabus Requirement**: Parametric and non-parametric tests

**Current Status**: ✅ **WELL COVERED**
- **Coverage**: 75%
- **Content Quality**: Good
- **Words**: ~600
- **Examples**: Basic

**What's Covered**:
- ✅ Definition of parametric tests
- ✅ Assumptions listed
- ✅ Basic comparison

**What's Missing** (25%):
- [ ] **Comprehensive comparison table**
- [ ] When to use each type
- [ ] Assumption checking procedures
- [ ] What to do when assumptions violated
- [ ] Power comparison
- [ ] Examples of each type

**DETAILED CONTENT TO ADD**:

```markdown
### Parametric vs Non-Parametric: Complete Guide

#### Comprehensive Comparison

| Aspect | Parametric | Non-Parametric |
|--------|------------|----------------|
| **Assumptions** | • Normal distribution<br>• Interval/ratio data<br>• Homogeneity of variance<br>• Independence | • No distribution assumption<br>• Any data type<br>• Independence only |
| **Data Type** | Interval, Ratio | Nominal, Ordinal, Non-normal continuous |
| **Sample Size** | Works well with small n | Better for small n |
| **Power** | Higher (if assumptions met) | Lower (but robust) |
| **Sensitivity** | Detects smaller effects | Needs larger effects |
| **Outliers** | Sensitive | Robust |
| **Examples** | t-test, ANOVA, Pearson r | Mann-Whitney, Kruskal-Wallis, Spearman ρ |

#### Assumption Checking Procedures

**1. Normality**:
- **Visual**: Histogram, Q-Q plot
- **Statistical**: Shapiro-Wilk test (n < 50), Kolmogorov-Smirnov (n > 50)
- **Rule**: If p > 0.05, data is normal

**Example in SPSS**:
```
Analyze → Descriptive Statistics → Explore
→ Plots → Check "Normality plots with tests"
```

**Interpretation**:
- Shapiro-Wilk p = 0.234 → Normal ✅ (Use parametric)
- Shapiro-Wilk p = 0.003 → Not normal ❌ (Use non-parametric)

**2. Homogeneity of Variance**:
- **Test**: Levene's test
- **Rule**: If p > 0.05, variances are equal

**3. Independence**:
- **Check**: Research design (random sampling, no repeated measures)

#### Decision Flowchart

```
Is data interval/ratio?
├─ No → Non-parametric
└─ Yes → Check normality
    ├─ Normal?
    │   ├─ Yes → Check equal variances
    │   │   ├─ Yes → Parametric
    │   │   └─ No → Welch's t-test or non-parametric
    │   └─ No → Non-parametric
    └─ Sample size > 30?
        ├─ Yes → Parametric (Central Limit Theorem)
        └─ No → Non-parametric
```

#### When Assumptions Violated

**Violation**: Non-normal data
**Solutions**:
1. Transform data (log, square root)
2. Use non-parametric alternative
3. Use robust methods

**Violation**: Unequal variances
**Solutions**:
1. Welch's t-test (doesn't assume equal variances)
2. Transform data
3. Use non-parametric

**Violation**: Outliers
**Solutions**:
1. Remove if data entry error
2. Winsorize (cap at percentile)
3. Use non-parametric (robust to outliers)
```

**Recommendations**:
1. **CRITICAL**: Add comprehensive comparison table
2. **CRITICAL**: Add assumption checking tutorial with SPSS/R code
3. Add decision flowchart
4. Include 5+ examples of when to use each

**Priority**: **CRITICAL**

---

### Topic 3: z-test, t-test, ANOVA ⚠️ PARTIAL
**Syllabus Requirement**: z-test, t-test, ANOVA

**Current Status**: ⚠️ **NEEDS MORE EXAMPLES**
- **Coverage**: 65%
- **Content Quality**: Good theory, lacks examples
- **Words**: ~1,500
- **Examples**: 2-3 basic

**What's Covered**:
- ✅ z-test: Definition, when to use, formula
- ✅ t-test: Three types (one-sample, independent, paired)
- ✅ ANOVA: Basic concept, F-ratio
- ✅ Formulas for each

**What's CRITICALLY Missing** (35%):

#### z-Test - Need to Add:
- [ ] **5+ worked examples with real data**
- [ ] Step-by-step calculation
- [ ] SPSS/Excel/R implementation
- [ ] Interpretation guide
- [ ] When NOT to use z-test

**Example to Add**:
```markdown
### z-Test Complete Example

**Problem**: A company claims average employee salary is ₹50,000 with σ = ₹8,000. 
A sample of 100 employees shows mean ₹48,500. Test at α = 0.05.

**Step 1: State Hypotheses**
- H₀: μ = 50,000 (Company claim is correct)
- H₁: μ ≠ 50,000 (Company claim is incorrect)
- Two-tailed test

**Step 2: Set Significance Level**
- α = 0.05
- Critical values: ±1.96

**Step 3: Calculate Test Statistic**
```
z = (x̄ - μ₀) / (σ/√n)
z = (48,500 - 50,000) / (8,000/√100)
z = -1,500 / 800
z = -1.875
```

**Step 4: Make Decision**
- |z| = 1.875 < 1.96
- Fail to reject H₀

**Step 5: Conclusion**
"At α = 0.05, there is insufficient evidence to conclude that the average salary 
differs from ₹50,000 (z = -1.875, p = 0.061)."

**In Excel**:
```
=NORM.S.DIST(-1.875, TRUE) * 2  // Two-tailed p-value = 0.061
```

**In R**:
```r
# Calculate z-statistic
z <- (48500 - 50000) / (8000/sqrt(100))
# Calculate p-value
p_value <- 2 * pnorm(abs(z), lower.tail = FALSE)
```

**Interpretation**:
- p = 0.061 > 0.05 → Not significant
- 95% CI: 48,500 ± 1.96(800) = [46,932, 50,068]
- The claimed value (50,000) falls within CI ✅
```

#### t-Test - Need to Add:
- [ ] **10+ worked examples** (3-4 for each type)
- [ ] Assumptions checking
- [ ] Effect size (Cohen's d)
- [ ] Confidence intervals
- [ ] SPSS output interpretation
- [ ] APA-style reporting

**Examples Needed**:

**One-Sample t-test Example**:
```markdown
**Problem**: Is average IQ of gifted students different from 100?
Sample: n = 25, x̄ = 115, s = 15

**Solution**:
H₀: μ = 100
H₁: μ ≠ 100

t = (115 - 100) / (15/√25) = 15/3 = 5.0
df = 24
Critical value (α = 0.05, two-tailed): ±2.064

Decision: |t| = 5.0 > 2.064 → Reject H₀

Conclusion: Gifted students have significantly higher IQ than 100 
(t(24) = 5.0, p < 0.001, d = 1.0)

Effect size: d = (115-100)/15 = 1.0 (Large effect)
```

**Independent Samples t-test Example**:
```markdown
**Problem**: Do males and females differ in math scores?
- Males: n₁ = 30, x̄₁ = 75, s₁ = 10
- Females: n₂ = 30, x̄₂ = 80, s₂ = 12

**Step 1**: Check assumptions
- Normality: Shapiro-Wilk p > 0.05 ✅
- Equal variances: Levene's p = 0.45 > 0.05 ✅

**Step 2**: Calculate pooled variance
s²pooled = [(29)(100) + (29)(144)] / 58 = 122

**Step 3**: Calculate t
t = (75 - 80) / √[122(1/30 + 1/30)]
t = -5 / 2.85 = -1.75

**Step 4**: Decision
df = 58, critical = ±2.00
|t| = 1.75 < 2.00 → Fail to reject H₀

**Conclusion**: No significant difference in math scores between males and females
(t(58) = -1.75, p = 0.085)
```

**Paired t-test Example**:
```markdown
**Problem**: Does training improve performance?
10 employees tested before and after training.

| Employee | Before | After | Difference (d) |
|----------|--------|-------|----------------|
| 1 | 65 | 72 | 7 |
| 2 | 70 | 75 | 5 |
| ... | ... | ... | ... |
| 10 | 68 | 76 | 8 |

d̄ = 6.5, sd = 2.1

**Solution**:
H₀: μd = 0 (No improvement)
H₁: μd > 0 (Improvement) [One-tailed]

t = 6.5 / (2.1/√10) = 6.5 / 0.66 = 9.85
df = 9
Critical value (α = 0.05, one-tailed): 1.833

Decision: t = 9.85 > 1.833 → Reject H₀

Conclusion: Training significantly improves performance
(t(9) = 9.85, p < 0.001, d = 3.1)
```

#### ANOVA - Need to Add:
- [ ] **Complete ANOVA tutorial** (2,000+ words)
- [ ] One-way ANOVA: 3+ examples
- [ ] ANOVA table interpretation
- [ ] Post-hoc tests (Tukey, Bonferroni, Scheffé)
- [ ] Effect size (η²)
- [ ] Assumptions checking
- [ ] Two-way ANOVA introduction
- [ ] SPSS output interpretation

**Complete ANOVA Example Needed**:
```markdown
### One-Way ANOVA Complete Example

**Problem**: Do three teaching methods produce different test scores?
- Method A: n=10, x̄=75, s=8
- Method B: n=10, x̄=82, s=7
- Method C: n=10, x̄=78, s=9

**Step 1: Hypotheses**
- H₀: μA = μB = μC (All means equal)
- H₁: At least one mean differs

**Step 2: Calculate ANOVA Table**

| Source | SS | df | MS | F |
|--------|----|----|----|----|
| Between Groups | 260 | 2 | 130 | 5.85 |
| Within Groups | 600 | 27 | 22.22 | |
| Total | 860 | 29 | | |

**Calculations**:
- SSB = 10[(75-78.33)² + (82-78.33)² + (78-78.33)²] = 260
- SSW = Σ(n-1)s² = 9(64) + 9(49) + 9(81) = 600
- MSB = 260/2 = 130
- MSW = 600/27 = 22.22
- F = 130/22.22 = 5.85

**Step 3: Decision**
- df₁ = 2, df₂ = 27
- F_critical (α=0.05) = 3.35
- F = 5.85 > 3.35 → Reject H₀

**Step 4: Post-hoc Tests** (Tukey HSD)
- A vs B: Significant (p = 0.003)
- A vs C: Not significant (p = 0.18)
- B vs C: Significant (p = 0.04)

**Step 5: Effect Size**
η² = SSB/SST = 260/860 = 0.30 (Large effect)

**Conclusion**:
"There was a significant effect of teaching method on test scores, 
F(2,27) = 5.85, p = 0.008, η² = 0.30. Post-hoc tests revealed that 
Method B (M=82) produced significantly higher scores than Method A (M=75) 
and Method C (M=78)."

**SPSS Output Interpretation**:
[Include screenshot of SPSS ANOVA output with annotations]
```

**Recommendations**:
1. **CRITICAL**: Add 5+ z-test examples with solutions
2. **CRITICAL**: Add 10+ t-test examples (all types)
3. **CRITICAL**: Add comprehensive ANOVA tutorial with 3+ examples
4. **CRITICAL**: Add SPSS/R code and output for each test
5. Add effect size calculations
6. Include APA-style reporting guide

**Priority**: **CRITICAL** - Core statistical tests need extensive examples

---

### Topic 4: Degrees of Freedom and Confidence Intervals ✅ GOOD
**Syllabus Requirement**: Degrees of freedom and confidence intervals

**Current Status**: ✅ **WELL COVERED**
- **Coverage**: 85%
- **Content Quality**: Good
- **Words**: ~600
- **Examples**: Basic

**What's Covered**:
- ✅ Degrees of freedom definition
- ✅ df formulas for different tests
- ✅ Confidence interval definition
- ✅ CI formula
- ✅ Common confidence levels

**What's Missing** (15%):
- [ ] **df calculation examples** for each test
- [ ] Why df matters (impact on critical values)
- [ ] **CI calculation examples** (5+)
- [ ] CI interpretation guide
- [ ] Relationship between CI and hypothesis testing

**Examples to Add**:
```markdown
### Confidence Interval Examples

#### Example 1: Mean CI
Sample: n=25, x̄=100, s=15
95% CI for μ

**Solution**:
df = 24
t(0.025, 24) = 2.064
SE = 15/√25 = 3
CI = 100 ± 2.064(3) = 100 ± 6.19 = [93.81, 106.19]

**Interpretation**: "We are 95% confident that the true population mean 
lies between 93.81 and 106.19."

#### Example 2: Difference in Means CI
Group 1: n₁=30, x̄₁=75, s₁=10
Group 2: n₂=30, x̄₂=80, s₂=12
95% CI for μ₁ - μ₂

**Solution**:
Difference = 75 - 80 = -5
SE = √[(100/30) + (144/30)] = 2.85
df = 58, t = 2.00
CI = -5 ± 2.00(2.85) = -5 ± 5.7 = [-10.7, 0.7]

**Interpretation**: "The 95% CI for the difference includes zero, 
suggesting no significant difference (consistent with t-test result)."
```

**Recommendations**:
1. Add 5+ CI calculation examples
2. Include CI interpretation guide
3. Add CI vs hypothesis testing relationship
4. Include graphical representation

**Priority**: MEDIUM

---

### Topic 5: Kolmogorov-Smirnov Test, Run Test ⚠️ MINIMAL
**Syllabus Requirement**: Kolmogorov–Smirnov test, run test

**Current Status**: ⚠️ **NEEDS MAJOR ADDITION**
- **Coverage**: 30%
- **Content Quality**: Minimal
- **Words**: ~200
- **Examples**: None

**What's Covered**:
- ✅ Brief mention in non-parametric section

**What's CRITICALLY Missing** (70%):

#### Kolmogorov-Smirnov Test (NEED TO ADD):
- [ ] **Complete tutorial** (1,000+ words)
- [ ] Purpose: Test if sample follows a distribution
- [ ] When to use
- [ ] Assumptions
- [ ] Formula and calculation
- [ ] 3+ worked examples
- [ ] SPSS/R implementation
- [ ] Interpretation guide
- [ ] Comparison with Shapiro-Wilk

**Content to Add**:
```markdown
### Kolmogorov-Smirnov Test Complete Guide

#### Purpose
Test whether a sample comes from a specific distribution (usually normal).

#### When to Use
- Check normality assumption before parametric tests
- Large samples (n > 50) - for small samples, use Shapiro-Wilk
- Compare two samples (two-sample K-S test)

#### Hypotheses
- H₀: Data follows the specified distribution
- H₁: Data does not follow the specified distribution

#### Test Statistic
D = max|F(x) - S(x)|
Where:
- F(x) = theoretical cumulative distribution
- S(x) = empirical cumulative distribution

#### Example: Testing Normality

**Data**: Test scores of 100 students
Mean = 75, SD = 10

**SPSS**:
```
Analyze → Nonparametric Tests → Legacy Dialogs → 1-Sample K-S
→ Select variable
→ Test Distribution: Normal
```

**Output**:
- D = 0.08
- p = 0.15

**Interpretation**:
p = 0.15 > 0.05 → Fail to reject H₀
Data is consistent with normal distribution ✅
Can proceed with parametric tests.

#### K-S vs Shapiro-Wilk

| Aspect | K-S | Shapiro-Wilk |
|--------|-----|--------------|
| **Sample Size** | Large (n > 50) | Small to medium (n < 50) |
| **Power** | Lower | Higher |
| **Sensitivity** | Less sensitive | More sensitive |
| **Use** | Quick check | Preferred for small samples |

#### Two-Sample K-S Test

**Purpose**: Test if two samples come from same distribution

**Example**: Do males and females have same score distribution?

**SPSS**:
```
Analyze → Nonparametric Tests → Legacy Dialogs → 2 Independent Samples
→ Test Type: Kolmogorov-Smirnov
```

**Interpretation**:
- D = 0.15, p = 0.08
- p > 0.05 → Distributions are similar
```

#### Run Test (NEED TO ADD):
- [ ] **Complete tutorial** (800+ words)
- [ ] Purpose: Test randomness of sequence
- [ ] When to use
- [ ] Formula and calculation
- [ ] 3+ examples
- [ ] Applications (time series, quality control)

**Content to Add**:
```markdown
### Run Test Complete Guide

#### Purpose
Test whether a sequence of observations is random or has a pattern.

#### When to Use
- Check randomness in time series
- Quality control (detect patterns in defects)
- Verify random sampling
- Check residuals in regression

#### Concept
**Run**: Sequence of similar observations
Example: + + + - - + + + +
Runs: [+++] [--] [++++] = 3 runs

Too few runs → Trend/pattern
Too many runs → Oscillation

#### Hypotheses
- H₀: Sequence is random
- H₁: Sequence is not random

#### Example 1: Coin Flips

**Data**: H H H T T H T H H H T T T
- n₁ = 7 heads
- n₂ = 6 tails
- Runs = 6

**Expected runs**:
μ = (2n₁n₂)/(n₁+n₂) + 1 = (2×7×6)/13 + 1 = 7.46

**Standard error**:
σ = √[(2n₁n₂(2n₁n₂-n₁-n₂))/((n₁+n₂)²(n₁+n₂-1))] = 1.73

**z-statistic**:
z = (6 - 7.46)/1.73 = -0.84

**Decision**:
|z| = 0.84 < 1.96 → Fail to reject H₀
Sequence appears random ✅

#### Example 2: Stock Prices

**Data**: Daily price changes (+ = up, - = down)
+ + + + + - - + + + - - - - + +

**Analysis**:
- n₁ = 9 (up days)
- n₂ = 7 (down days)
- Runs = 6

**Interpretation**:
Expected runs = 8.75
Observed runs = 6 (fewer than expected)
Suggests clustering/trend ⚠️

#### SPSS Implementation
```
Analyze → Nonparametric Tests → Legacy Dialogs → Runs
→ Select variable
→ Cut point: Median (or custom)
```
```

**Recommendations**:
1. **CRITICAL**: Add complete K-S test tutorial (1,000 words)
2. **CRITICAL**: Add complete Run test tutorial (800 words)
3. Add 3+ examples for each test
4. Include SPSS/R code
5. Add interpretation guides

**Priority**: **CRITICAL** - Major syllabus topics with minimal coverage

---

### Topic 6: Mann-Whitney U Test, Kruskal-Wallis Test ⚠️ PARTIAL
**Syllabus Requirement**: Mann-Whitney U test, Kruskal-Wallis test

**Current Status**: ⚠️ **NEEDS EXPANSION**
- **Coverage**: 50%
- **Content Quality**: Basic
- **Words**: ~400
- **Examples**: 1 basic

**What's Covered**:
- ✅ Basic definitions
- ✅ When to use
- ✅ Brief comparison with parametric alternatives

**What's Missing** (50%):
- [ ] **Detailed calculation procedures**
- [ ] 5+ worked examples for each test
- [ ] Ranking procedures
- [ ] Tied ranks handling
- [ ] Effect size calculation
- [ ] SPSS/R implementation
- [ ] Post-hoc tests for Kruskal-Wallis

**DETAILED CONTENT TO ADD**:

```markdown
### Mann-Whitney U Test Complete Guide

#### Purpose
Non-parametric alternative to independent samples t-test.
Tests if two independent groups have different distributions.

#### When to Use
- Ordinal data
- Non-normal continuous data
- Small samples
- Unequal variances

#### Hypotheses
- H₀: Two groups have same distribution
- H₁: Two groups have different distributions

#### Procedure
1. Combine all data and rank (lowest = 1)
2. Sum ranks for each group (R₁, R₂)
3. Calculate U for each group
4. Use smaller U as test statistic

#### Formula
U₁ = n₁n₂ + n₁(n₁+1)/2 - R₁
U₂ = n₁n₂ + n₂(n₂+1)/2 - R₂
U = min(U₁, U₂)

#### Complete Example

**Problem**: Do males and females differ in satisfaction scores?

**Data**:
- Males (n₁=6): 7, 8, 6, 9, 7, 8
- Females (n₂=5): 5, 6, 4, 7, 5

**Step 1: Rank all data**
| Score | 4 | 5 | 5 | 6 | 6 | 7 | 7 | 7 | 8 | 8 | 9 |
|-------|---|---|---|---|---|---|---|---|---|---|---|
| Rank | 1 | 2.5 | 2.5 | 4.5 | 4.5 | 7 | 7 | 7 | 9.5 | 9.5 | 11 |
| Group | F | F | F | M | F | M | M | F | M | M | M |

**Step 2: Sum ranks**
- R₁ (Males) = 4.5 + 7 + 7 + 9.5 + 9.5 + 11 = 48.5
- R₂ (Females) = 1 + 2.5 + 2.5 + 4.5 + 7 = 17.5

**Step 3: Calculate U**
U₁ = 6×5 + 6×7/2 - 48.5 = 30 + 21 - 48.5 = 2.5
U₂ = 6×5 + 5×6/2 - 17.5 = 30 + 15 - 17.5 = 27.5
U = min(2.5, 27.5) = 2.5

**Step 4: Decision**
Critical value (n₁=6, n₂=5, α=0.05, two-tailed) = 2
U = 2.5 > 2 → Fail to reject H₀

**Effect Size**:
r = Z/√N = -1.89/√11 = -0.57 (Large effect)

**Conclusion**: Males have significantly higher satisfaction than females
(U = 2.5, p = 0.04, r = -0.57)

**SPSS**:
```
Analyze → Nonparametric Tests → Legacy Dialogs → 2 Independent Samples
→ Test Type: Mann-Whitney U
→ Grouping Variable: Gender
→ Test Variable: Satisfaction
```

**R Code**:
```r
males <- c(7, 8, 6, 9, 7, 8)
females <- c(5, 6, 4, 7, 5)
wilcox.test(males, females)
```

### Kruskal-Wallis Test Complete Guide

#### Purpose
Non-parametric alternative to one-way ANOVA.
Tests if 3+ independent groups have different distributions.

#### When to Use
- Ordinal data
- Non-normal continuous data
- 3 or more groups
- Unequal variances

#### Hypotheses
- H₀: All groups have same distribution
- H₁: At least one group differs

#### Test Statistic
H = [12/(N(N+1))] × Σ(R²ᵢ/nᵢ) - 3(N+1)

Where:
- N = total sample size
- nᵢ = sample size of group i
- Rᵢ = sum of ranks for group i

#### Complete Example

**Problem**: Do three diets produce different weight loss?

**Data**:
- Diet A (n=5): 5, 6, 7, 5, 6
- Diet B (n=5): 8, 9, 7, 8, 9
- Diet C (n=5): 4, 5, 3, 4, 5

**Step 1: Rank all data (N=15)**
[Detailed ranking table]

**Step 2: Sum ranks**
- RA = 25
- RB = 70
- RC = 25

**Step 3: Calculate H**
H = [12/(15×16)] × [(25²/5) + (70²/5) + (25²/5)] - 3(16)
H = 0.05 × [125 + 980 + 125] - 48
H = 61.5 - 48 = 13.5

**Step 4: Decision**
df = k - 1 = 2
χ²_critical (α=0.05, df=2) = 5.99
H = 13.5 > 5.99 → Reject H₀

**Step 5: Post-hoc Tests** (Dunn's test)
- A vs B: p = 0.001 (Significant)
- A vs C: p = 0.95 (Not significant)
- B vs C: p = 0.001 (Significant)

**Conclusion**: Diet type significantly affects weight loss (H(2) = 13.5, p = 0.001).
Post-hoc tests show Diet B produces significantly more weight loss than A and C.

**SPSS**:
```
Analyze → Nonparametric Tests → Legacy Dialogs → K Independent Samples
→ Test Type: Kruskal-Wallis H
→ Grouping Variable: Diet
→ Test Variable: Weight Loss
```
```

**Recommendations**:
1. **CRITICAL**: Add complete Mann-Whitney tutorial (1,500 words)
2. **CRITICAL**: Add complete Kruskal-Wallis tutorial (1,500 words)
3. Add 5+ examples for each test
4. Include tied ranks handling
5. Add post-hoc tests for Kruskal-Wallis
6. Include SPSS/R code and output

**Priority**: **CRITICAL**

---

### Topic 7: Chi-Square Test ✅ GOOD
**Syllabus Requirement**: Chi-square test

**Current Status**: ✅ **WELL COVERED**
- **Coverage**: 75%
- **Content Quality**: Good
- **Words**: ~800
- **Examples**: 2

**What's Covered**:
- ✅ Goodness of fit test
- ✅ Test of independence
- ✅ Formula
- ✅ Expected frequency calculation
- ✅ Basic examples

**What's Missing** (25%):
- [ ] **5+ detailed examples**
- [ ] Contingency table analysis
- [ ] Effect size (Cramér's V)
- [ ] Yates' correction
- [ ] Fisher's exact test (when expected < 5)
- [ ] SPSS output interpretation

**Examples to Add**:
```markdown
### Chi-Square Complete Examples

#### Example 1: Goodness of Fit

**Problem**: Is a die fair?
Rolled 60 times: 1(8), 2(12), 3(9), 4(11), 5(10), 6(10)

**Solution**:
H₀: Die is fair (all faces equally likely)
Expected frequency = 60/6 = 10 for each face

χ² = Σ[(O-E)²/E]
χ² = (8-10)²/10 + (12-10)²/10 + ... + (10-10)²/10
χ² = 0.4 + 0.4 + 0.1 + 0.1 + 0 + 0 = 1.0

df = 6 - 1 = 5
χ²_critical (α=0.05, df=5) = 11.07
χ² = 1.0 < 11.07 → Fail to reject H₀

Conclusion: Die appears fair (χ²(5) = 1.0, p = 0.96)

#### Example 2: Test of Independence

**Problem**: Is smoking related to lung cancer?

**Data**:
|  | Cancer | No Cancer | Total |
|--|--------|-----------|-------|
| Smoker | 60 | 40 | 100 |
| Non-smoker | 20 | 80 | 100 |
| Total | 80 | 120 | 200 |

**Expected Frequencies**:
E₁₁ = (100×80)/200 = 40
E₁₂ = (100×120)/200 = 60
E₂₁ = (100×80)/200 = 40
E₂₂ = (100×120)/200 = 60

**Chi-Square**:
χ² = (60-40)²/40 + (40-60)²/60 + (20-40)²/40 + (80-60)²/60
χ² = 10 + 6.67 + 10 + 6.67 = 33.34

df = (2-1)(2-1) = 1
χ²_critical = 3.84
χ² = 33.34 > 3.84 → Reject H₀

**Effect Size** (Cramér's V):
V = √(χ²/N) = √(33.34/200) = 0.41 (Medium to large effect)

**Conclusion**: Smoking is significantly associated with lung cancer
(χ²(1) = 33.34, p < 0.001, V = 0.41)
```

**Recommendations**:
1. Add 5+ detailed examples
2. Include effect size calculations
3. Add Fisher's exact test
4. Include SPSS output interpretation

**Priority**: MEDIUM

---

## 📊 UNIT I SUMMARY

| Topic | Coverage | Priority | Words Needed |
|-------|----------|----------|--------------|
| 1. Hypothesis Design | 80% ✅ | **HIGH** | 1,000 |
| 2. Parametric vs Non-parametric | 75% ✅ | **CRITICAL** | 1,500 |
| 3. z, t, ANOVA | 65% ⚠️ | **CRITICAL** | **4,000** |
| 4. df & CI | 85% ✅ | MEDIUM | 500 |
| 5. K-S & Run Tests | 30% ⚠️ | **CRITICAL** | **1,800** |
| 6. Mann-Whitney & Kruskal-Wallis | 50% ⚠️ | **CRITICAL** | **3,000** |
| 7. Chi-Square | 75% ✅ | MEDIUM | 1,000 |

**Unit I Total Words to Add**: ~12,800 words
**Current Unit I Words**: ~5,000
**Target Unit I Words**: ~17,800

---

*This completes the Statistical Foundations section. Correlation & Regression and Computer Applications sections will follow.*

**Priority Summary for Unit I**:
1. **CRITICAL**: Add comprehensive examples for z, t, ANOVA (4,000 words)
2. **CRITICAL**: Add K-S and Run test tutorials (1,800 words)
3. **CRITICAL**: Add Mann-Whitney and Kruskal-Wallis tutorials (3,000 words)
4. **CRITICAL**: Add parametric vs non-parametric guide (1,500 words)

**Total Critical Additions Needed**: ~10,300 words

---

**Document Status**: Paper II Unit I Complete
**Next**: Unit II (Correlation & Regression) and Unit III (Computer Applications)
