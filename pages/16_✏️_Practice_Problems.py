import streamlit as st
import random
from utils.styles import apply_custom_css, show_footer
from utils.nav import show_top_nav

# Page Config
st.set_page_config(page_title="Practice Problems | Ph.D. Hub", page_icon="✏️", layout="wide")
apply_custom_css()
show_top_nav(current_page="Practice Problems")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%); border-radius: 10px; margin-bottom: 20px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">✏️ Practice Problems</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #7c3aed;">Test your knowledge with problems covering all major topics.</p>
</div>
""", unsafe_allow_html=True)

# Tabs by Topic
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Descriptive Stats",
    "🎯 Hypothesis Testing",
    "📈 Correlation/Regression",
    "⚖️ Research Ethics",
    "📚 Research Methodology"
])

# =============================================================================
# TAB 1: DESCRIPTIVE STATISTICS
# =============================================================================
with tab1:
    st.markdown("## 📊 Descriptive Statistics Problems")
    
    with st.expander("Problem 1: Calculate Mean, Median, Mode", expanded=True):
        st.markdown("""
        **Dataset:** The following are the ages of 10 participants in a study:
        
        `23, 25, 27, 27, 28, 30, 31, 35, 40, 44`
        
        **Questions:**
        1. Calculate the **Mean**
        2. Calculate the **Median**
        3. Identify the **Mode**
        4. Calculate the **Range**
        """)
        
        with st.form("desc_prob1"):
            a1 = st.number_input("1. Mean (round to 1 decimal)", min_value=0.0, max_value=100.0, step=0.1)
            a2 = st.number_input("2. Median", min_value=0.0, max_value=100.0, step=0.1)
            a3 = st.number_input("3. Mode", min_value=0, max_value=100)
            a4 = st.number_input("4. Range", min_value=0, max_value=100)
            
            if st.form_submit_button("Check Answers"):
                score = 0
                # Mean = (23+25+27+27+28+30+31+35+40+44)/10 = 31.0
                if abs(a1 - 31.0) < 0.2:
                    st.success("✅ Mean is correct! (31.0)")
                    score += 1
                else:
                    st.error(f"❌ Mean is incorrect. Correct: 31.0 (Sum=310, n=10)")
                
                # Median = (28+30)/2 = 29
                if abs(a2 - 29.0) < 0.2:
                    st.success("✅ Median is correct! (29.0)")
                    score += 1
                else:
                    st.error(f"❌ Median is incorrect. Correct: 29.0 (average of 5th and 6th values)")
                
                # Mode = 27
                if a3 == 27:
                    st.success("✅ Mode is correct! (27)")
                    score += 1
                else:
                    st.error(f"❌ Mode is incorrect. Correct: 27 (appears twice)")
                
                # Range = 44-23 = 21
                if a4 == 21:
                    st.success("✅ Range is correct! (21)")
                    score += 1
                else:
                    st.error(f"❌ Range is incorrect. Correct: 21 (44-23)")
                
                st.metric("Score", f"{score}/4")

    with st.expander("Problem 2: Standard Deviation", expanded=False):
        st.markdown("""
        **Dataset:** `5, 10, 15, 20, 25`
        
        **Questions:**
        1. Calculate the **Sample Mean**
        2. Calculate the **Sample Variance** (using n-1)
        3. Calculate the **Sample Standard Deviation**
        """)
        
        with st.form("desc_prob2"):
            b1 = st.number_input("1. Sample Mean", min_value=0.0, max_value=100.0, step=0.1, key="b1")
            b2 = st.number_input("2. Sample Variance", min_value=0.0, max_value=200.0, step=0.1, key="b2")
            b3 = st.number_input("3. Sample SD (round to 2 decimals)", min_value=0.0, max_value=50.0, step=0.01, key="b3")
            
            if st.form_submit_button("Check Answers"):
                # Mean = 15, Var = 62.5, SD = 7.91
                score = 0
                if abs(b1 - 15.0) < 0.2:
                    st.success("✅ Mean is correct! (15.0)")
                    score += 1
                else:
                    st.error(f"❌ Mean is incorrect. Correct: 15.0")
                
                if abs(b2 - 62.5) < 1:
                    st.success("✅ Variance is correct! (62.5)")
                    score += 1
                else:
                    st.error(f"❌ Variance is incorrect. Correct: 62.5")
                
                if abs(b3 - 7.91) < 0.1:
                    st.success("✅ Standard Deviation is correct! (7.91)")
                    score += 1
                else:
                    st.error(f"❌ SD is incorrect. Correct: 7.91 (√62.5)")
                
                st.metric("Score", f"{score}/3")

# =============================================================================
# TAB 2: HYPOTHESIS TESTING
# =============================================================================
with tab2:
    st.markdown("## 🎯 Hypothesis Testing Problems")
    
    with st.expander("Problem 1: One-Sample t-Test", expanded=True):
        st.markdown("""
        **Scenario:** A researcher claims that the average IQ of students in a special program is greater than 100. A sample of 25 students has a mean IQ of 108 with a standard deviation of 15.
        
        **Test at α = 0.05 (one-tailed)**
        
        **Questions:**
        1. State the null and alternative hypotheses
        2. Calculate the t-statistic
        3. What are the degrees of freedom?
        4. The critical t-value for df=24, α=0.05 (one-tailed) is approximately **1.711**. Would you reject H₀?
        """)
        
        with st.form("hyp_prob1"):
            st.markdown("**1. Hypotheses:**")
            h0 = st.text_input("H₀:", placeholder="e.g., μ = 100")
            h1 = st.text_input("H₁:", placeholder="e.g., μ > 100")
            
            t_stat = st.number_input("2. t-statistic (round to 2 decimals)", min_value=-20.0, max_value=20.0, step=0.01)
            df_ans = st.number_input("3. Degrees of freedom", min_value=0, max_value=100)
            decision = st.radio("4. Decision:", ["Reject H₀", "Fail to Reject H₀"])
            
            if st.form_submit_button("Check Answers"):
                score = 0
                
                # t = (108-100)/(15/√25) = 8/3 = 2.67
                if abs(t_stat - 2.67) < 0.1:
                    st.success("✅ t-statistic is correct! (2.67)")
                    score += 1
                else:
                    st.error(f"❌ t-statistic incorrect. t = (108-100)/(15/√25) = 8/3 = 2.67")
                
                if df_ans == 24:
                    st.success("✅ df is correct! (n-1 = 24)")
                    score += 1
                else:
                    st.error(f"❌ df incorrect. df = n - 1 = 24")
                
                if decision == "Reject H₀":
                    st.success("✅ Decision is correct! (2.67 > 1.711, so reject H₀)")
                    score += 1
                else:
                    st.error("❌ Since t=2.67 > critical=1.711, we reject H₀")
                
                st.metric("Score", f"{score}/3")

    with st.expander("Problem 2: Chi-Square Test", expanded=False):
        st.markdown("""
        **Scenario:** A researcher wants to test if preference for coffee type is independent of gender.
        
        **Observed Frequencies:**
        
        |  | Espresso | Latte | Americano | Total |
        |--|----------|-------|-----------|-------|
        | Male | 30 | 20 | 50 | 100 |
        | Female | 20 | 40 | 40 | 100 |
        | **Total** | 50 | 60 | 90 | 200 |
        
        **Questions:**
        1. Calculate the expected frequency for Male-Espresso cell
        2. Calculate the Chi-Square contribution for Male-Espresso: (O-E)²/E
        3. What are the degrees of freedom for this test?
        """)
        
        with st.form("hyp_prob2"):
            exp_freq = st.number_input("1. Expected frequency (Male-Espresso)", min_value=0.0, max_value=100.0, step=0.1)
            chi_contrib = st.number_input("2. Chi-square contribution for Male-Espresso", min_value=0.0, max_value=20.0, step=0.01)
            chi_df = st.number_input("3. Degrees of freedom", min_value=0, max_value=20)
            
            if st.form_submit_button("Check Answers"):
                score = 0
                # E = (Row Total × Column Total) / Grand Total = (100 × 50) / 200 = 25
                if abs(exp_freq - 25.0) < 0.5:
                    st.success("✅ Expected frequency is correct! (25)")
                    score += 1
                else:
                    st.error("❌ Expected = (100 × 50) / 200 = 25")
                
                # (30-25)²/25 = 25/25 = 1
                if abs(chi_contrib - 1.0) < 0.1:
                    st.success("✅ Chi-square contribution is correct! (1.0)")
                    score += 1
                else:
                    st.error("❌ (O-E)²/E = (30-25)²/25 = 25/25 = 1.0")
                
                # df = (rows-1)(cols-1) = (2-1)(3-1) = 2
                if chi_df == 2:
                    st.success("✅ df is correct! ((2-1)(3-1) = 2)")
                    score += 1
                else:
                    st.error("❌ df = (r-1)(c-1) = (2-1)(3-1) = 2")
                
                st.metric("Score", f"{score}/3")

# =============================================================================
# TAB 3: CORRELATION/REGRESSION
# =============================================================================
with tab3:
    st.markdown("## 📈 Correlation & Regression Problems")
    
    with st.expander("Problem 1: Correlation Interpretation", expanded=True):
        st.markdown("""
        **Scenario:** A study found a Pearson correlation of r = 0.72 between hours of exercise per week and self-reported happiness scores (n = 50).
        
        **Questions:**
        """)
        
        with st.form("corr_prob1"):
            q1 = st.radio("1. What is the strength of this correlation?", 
                         ["Weak", "Moderate", "Strong", "Very Strong"])
            q2 = st.radio("2. What is the direction of this correlation?",
                         ["Positive", "Negative", "No direction"])
            q3 = st.number_input("3. What percentage of variance in happiness is explained by exercise? (R² × 100)", 
                                min_value=0.0, max_value=100.0, step=0.1)
            q4 = st.radio("4. Can we conclude that exercise CAUSES happiness?",
                         ["Yes", "No"])
            
            if st.form_submit_button("Check Answers"):
                score = 0
                
                if q1 == "Strong":
                    st.success("✅ Strength is correct! (r=0.72 is strong)")
                    score += 1
                else:
                    st.error("❌ r=0.72 indicates a STRONG correlation (0.7-0.9)")
                
                if q2 == "Positive":
                    st.success("✅ Direction is correct!")
                    score += 1
                else:
                    st.error("❌ r is positive, so direction is POSITIVE")
                
                # R² = 0.72² = 0.5184 = 51.84%
                if abs(q3 - 51.84) < 2:
                    st.success("✅ Variance explained is correct! (≈51.84%)")
                    score += 1
                else:
                    st.error("❌ R² = 0.72² = 0.5184 = 51.84%")
                
                if q4 == "No":
                    st.success("✅ Correct! Correlation ≠ Causation")
                    score += 1
                else:
                    st.error("❌ Correlation does NOT imply causation!")
                
                st.metric("Score", f"{score}/4")

    with st.expander("Problem 2: Regression Calculation", expanded=False):
        st.markdown("""
        **Given the following summary statistics:**
        - n = 10
        - Σx = 50, Σy = 80
        - Σxy = 450
        - Σx² = 300
        
        **Calculate the regression line: ŷ = b₀ + b₁x**
        """)
        
        with st.form("reg_prob1"):
            slope = st.number_input("1. Slope (b₁)", min_value=-10.0, max_value=10.0, step=0.01)
            intercept = st.number_input("2. Intercept (b₀)", min_value=-20.0, max_value=20.0, step=0.01)
            
            if st.form_submit_button("Check Answers"):
                score = 0
                # b₁ = (nΣxy - ΣxΣy) / (nΣx² - (Σx)²)
                # b₁ = (10*450 - 50*80) / (10*300 - 50²)
                # b₁ = (4500 - 4000) / (3000 - 2500) = 500/500 = 1.0
                
                # b₀ = ȳ - b₁x̄ = 8 - 1*5 = 3
                
                if abs(slope - 1.0) < 0.1:
                    st.success("✅ Slope is correct! (b₁ = 1.0)")
                    score += 1
                else:
                    st.error("❌ b₁ = (10×450 - 50×80) / (10×300 - 50²) = 500/500 = 1.0")
                
                if abs(intercept - 3.0) < 0.1:
                    st.success("✅ Intercept is correct! (b₀ = 3.0)")
                    score += 1
                else:
                    st.error("❌ b₀ = ȳ - b₁x̄ = 8 - 1×5 = 3.0")
                
                st.metric("Score", f"{score}/2")
                st.success("**Regression equation: ŷ = 3 + 1x**")

# =============================================================================
# TAB 4: RESEARCH ETHICS
# =============================================================================
with tab4:
    st.markdown("## ⚖️ Research Ethics Problems")
    
    with st.expander("Problem 1: Identify the Misconduct", expanded=True):
        st.markdown("""
        **For each scenario, identify the type of misconduct:**
        """)
        
        with st.form("ethics_prob1"):
            s1 = st.radio(
                "1. A researcher reports experimental results that were never actually collected.",
                ["Fabrication", "Falsification", "Plagiarism", "Salami Slicing"]
            )
            
            s2 = st.radio(
                "2. A researcher removes outliers that don't support the hypothesis without justification.",
                ["Fabrication", "Falsification", "Plagiarism", "Duplicate Publication"]
            )
            
            s3 = st.radio(
                "3. A researcher divides one study into 5 papers submitted to different journals.",
                ["Fabrication", "Ghost Authorship", "Salami Slicing", "Self-Plagiarism"]
            )
            
            s4 = st.radio(
                "4. A senior professor adds their name to a paper despite making no contribution.",
                ["Gift Authorship", "Ghost Authorship", "Plagiarism", "Fabrication"]
            )
            
            if st.form_submit_button("Check Answers"):
                score = 0
                
                if s1 == "Fabrication":
                    st.success("✅ Correct! Making up data is Fabrication.")
                    score += 1
                else:
                    st.error("❌ Creating non-existent data is FABRICATION.")
                
                if s2 == "Falsification":
                    st.success("✅ Correct! Manipulating data is Falsification.")
                    score += 1
                else:
                    st.error("❌ Manipulating real data is FALSIFICATION.")
                
                if s3 == "Salami Slicing":
                    st.success("✅ Correct! Dividing one study into many papers is Salami Slicing.")
                    score += 1
                else:
                    st.error("❌ Artificially dividing one study is SALAMI SLICING.")
                
                if s4 == "Gift Authorship":
                    st.success("✅ Correct! Adding undeserving authors is Gift/Honorary Authorship.")
                    score += 1
                else:
                    st.error("❌ Adding someone who didn't contribute is GIFT AUTHORSHIP.")
                
                st.metric("Score", f"{score}/4")

    with st.expander("Problem 2: ICMJE Authorship Criteria", expanded=False):
        st.markdown("""
        **Which of the following meet ICMJE authorship criteria? (Select all that apply)**
        """)
        
        with st.form("ethics_prob2"):
            c1 = st.checkbox("Dr. A: Designed the study, analyzed data, wrote the manuscript, approved final version")
            c2 = st.checkbox("Dr. B: Only provided funding for the research")
            c3 = st.checkbox("Dr. C: Collected data, revised manuscript critically, approved final version")
            c4 = st.checkbox("Dr. D: Head of department, automatically added to all papers")
            c5 = st.checkbox("Dr. E: Contributed to interpretation, drafted part of discussion, approved final version")
            
            if st.form_submit_button("Check Answers"):
                correct = [True, False, True, False, True]
                answers = [c1, c2, c3, c4, c5]
                
                score = sum(1 for a, c in zip(answers, correct) if a == c)
                
                st.markdown("**Correct Answers:**")
                st.success("✅ Dr. A qualifies - meets all 4 criteria")
                st.error("❌ Dr. B does NOT qualify - funding alone is insufficient")
                st.success("✅ Dr. C qualifies - substantial contribution, revision, approval")
                st.error("❌ Dr. D does NOT qualify - position alone is not a criterion")
                st.success("✅ Dr. E qualifies - interpretation, drafting, approval")
                
                st.metric("Score", f"{score}/5")

# =============================================================================
# TAB 5: RESEARCH METHODOLOGY
# =============================================================================
with tab5:
    st.markdown("## 📚 Research Methodology Problems")
    
    with st.expander("Problem 1: Research Types & Variables", expanded=True):
        st.markdown("""
        **Match the research scenario to the correct type:**
        """)
        
        with st.form("meth_prob1"):
            m1 = st.radio(
                "1. A study measuring how many students prefer online vs. offline classes.",
                ["Descriptive Research", "Experimental Research", "Correlational Research"]
            )
            
            m2 = st.radio(
                "2. A study where participants are randomly assigned to receive a drug or placebo.",
                ["Descriptive Research", "Experimental Research", "Correlational Research"]
            )
            
            m3 = st.radio(
                "3. A study examining if there's a relationship between sleep hours and test scores.",
                ["Descriptive Research", "Experimental Research", "Correlational Research"]
            )
            
            st.markdown("---")
            st.markdown("**4. In an experiment testing if caffeine improves memory:**")
            
            iv = st.radio("What is the Independent Variable (IV)?",
                         ["Memory score", "Caffeine (given or not)", "Age of participants"])
            dv = st.radio("What is the Dependent Variable (DV)?",
                         ["Memory score", "Caffeine (given or not)", "Age of participants"])
            
            if st.form_submit_button("Check Answers"):
                score = 0
                
                if m1 == "Descriptive Research":
                    st.success("✅ Correct! Describing preferences is Descriptive Research.")
                    score += 1
                else:
                    st.error("❌ Measuring preferences without manipulation is DESCRIPTIVE.")
                
                if m2 == "Experimental Research":
                    st.success("✅ Correct! Random assignment = Experimental.")
                    score += 1
                else:
                    st.error("❌ Random assignment with control group is EXPERIMENTAL.")
                
                if m3 == "Correlational Research":
                    st.success("✅ Correct! Examining relationships without manipulation is Correlational.")
                    score += 1
                else:
                    st.error("❌ Examining natural relationships is CORRELATIONAL.")
                
                if iv == "Caffeine (given or not)":
                    st.success("✅ IV is correct! (What the researcher manipulates)")
                    score += 1
                else:
                    st.error("❌ The IV is what's manipulated: CAFFEINE")
                
                if dv == "Memory score":
                    st.success("✅ DV is correct! (What's measured as outcome)")
                    score += 1
                else:
                    st.error("❌ The DV is what's measured: MEMORY SCORE")
                
                st.metric("Score", f"{score}/5")

    with st.expander("Problem 2: Sampling Methods", expanded=False):
        st.markdown("""
        **Identify the sampling method:**
        """)
        
        with st.form("meth_prob2"):
            sm1 = st.radio(
                "1. Every 10th person entering a mall is selected.",
                ["Simple Random", "Systematic", "Stratified", "Convenience"]
            )
            
            sm2 = st.radio(
                "2. The population is divided by age groups, then random samples are taken from each.",
                ["Simple Random", "Systematic", "Stratified", "Cluster"]
            )
            
            sm3 = st.radio(
                "3. A researcher surveys their own students because they're easily accessible.",
                ["Simple Random", "Purposive", "Stratified", "Convenience"]
            )
            
            sm4 = st.radio(
                "4. Using a random number generator to select participants from a list.",
                ["Simple Random", "Systematic", "Quota", "Snowball"]
            )
            
            if st.form_submit_button("Check Answers"):
                score = 0
                
                if sm1 == "Systematic":
                    st.success("✅ Correct! Every kth person = Systematic sampling")
                    score += 1
                else:
                    st.error("❌ Selecting every kth element is SYSTEMATIC sampling")
                
                if sm2 == "Stratified":
                    st.success("✅ Correct! Dividing into strata then sampling = Stratified")
                    score += 1
                else:
                    st.error("❌ Dividing into subgroups then sampling is STRATIFIED")
                
                if sm3 == "Convenience":
                    st.success("✅ Correct! Using easily available subjects = Convenience")
                    score += 1
                else:
                    st.error("❌ Using accessible subjects is CONVENIENCE sampling")
                
                if sm4 == "Simple Random":
                    st.success("✅ Correct! Random number selection = Simple Random")
                    score += 1
                else:
                    st.error("❌ Random selection with equal probability is SIMPLE RANDOM")
                
                st.metric("Score", f"{score}/4")

# Summary
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); padding: 20px; border-radius: 10px; text-align: center;">
    <h3 style="margin: 0 0 10px 0; color: #166534;">🎯 Keep Practicing!</h3>
    <p style="margin: 0; color: #166534;">Regular practice is the key to mastering statistics and research methods. Revisit these problems until you can solve them without hesitation.</p>
</div>
""", unsafe_allow_html=True)

show_footer()
