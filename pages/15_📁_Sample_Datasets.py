import streamlit as st
import pandas as pd
from utils.styles import apply_custom_css, show_footer
from utils.nav import show_top_nav

# Page Config
st.set_page_config(page_title="Sample Datasets | Ph.D. Hub", page_icon="📁", layout="wide")
apply_custom_css()
show_top_nav(current_page="Sample Datasets")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border-radius: 10px; margin-bottom: 20px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">📁 Sample Datasets</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #166534;">Practice data for statistical analysis — download and analyze!</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 t-Test Data", "📈 ANOVA Data", "🔗 Correlation Data", "🔢 Chi-Square Data"])

# =============================================================================
# TAB 1: T-TEST DATA
# =============================================================================
with tab1:
    st.markdown("### 📊 Dataset 1: Student Test Scores (t-Test)")
    st.markdown("Compare the exam scores of students who used a study app vs. those who didn't.")
    
    # Generate data
    import random
    random.seed(42)
    
    ttest_data = pd.DataFrame({
        "Student_ID": [f"S{i:03d}" for i in range(1, 31)],
        "Group": ["App Users"] * 15 + ["Non-Users"] * 15,
        "Score": [random.randint(70, 95) for _ in range(15)] + [random.randint(55, 85) for _ in range(15)]
    })
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.dataframe(ttest_data, use_container_width=True, height=300)
    with col2:
        st.markdown("""
        **Use this for:**
        - Independent Samples t-Test
        - Effect size (Cohen's d)
        
        **Variables:**
        - `Student_ID`: Identifier
        - `Group`: Categorical (App Users / Non-Users)
        - `Score`: Continuous (0-100)
        
        **Research Question:**
        *Do students using the study app score higher?*
        """)
    
    csv1 = ttest_data.to_csv(index=False)
    st.download_button("📥 Download t-Test Dataset (CSV)", csv1, "ttest_student_scores.csv", "text/csv")

# =============================================================================
# TAB 2: ANOVA DATA
# =============================================================================
with tab2:
    st.markdown("### 📈 Dataset 2: Employee Productivity (ANOVA)")
    st.markdown("Compare productivity scores across three different management styles.")
    
    random.seed(123)
    
    anova_data = pd.DataFrame({
        "Employee_ID": [f"E{i:03d}" for i in range(1, 46)],
        "Management_Style": ["Democratic"] * 15 + ["Autocratic"] * 15 + ["Laissez-faire"] * 15,
        "Productivity_Score": (
            [random.randint(75, 95) for _ in range(15)] +  # Democratic
            [random.randint(60, 80) for _ in range(15)] +  # Autocratic
            [random.randint(50, 75) for _ in range(15)]    # Laissez-faire
        )
    })
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.dataframe(anova_data, use_container_width=True, height=300)
    with col2:
        st.markdown("""
        **Use this for:**
        - One-Way ANOVA
        - Post-hoc tests (Tukey HSD)
        - Eta-squared effect size
        
        **Variables:**
        - `Employee_ID`: Identifier
        - `Management_Style`: Categorical (3 groups)
        - `Productivity_Score`: Continuous
        
        **Research Question:**
        *Does management style affect productivity?*
        """)
    
    csv2 = anova_data.to_csv(index=False)
    st.download_button("📥 Download ANOVA Dataset (CSV)", csv2, "anova_productivity.csv", "text/csv")

# =============================================================================
# TAB 3: CORRELATION DATA
# =============================================================================
with tab3:
    st.markdown("### 🔗 Dataset 3: Study Hours vs. GPA (Correlation & Regression)")
    st.markdown("Explore the relationship between weekly study hours and GPA.")
    
    random.seed(456)
    
    # Generate correlated data
    study_hours = [random.randint(5, 30) for _ in range(40)]
    gpa = [round(min(4.0, max(1.5, 1.5 + (h * 0.08) + random.uniform(-0.5, 0.5))), 2) for h in study_hours]
    
    corr_data = pd.DataFrame({
        "Student_ID": [f"S{i:03d}" for i in range(1, 41)],
        "Weekly_Study_Hours": study_hours,
        "GPA": gpa,
        "Year": [random.choice(["Freshman", "Sophomore", "Junior", "Senior"]) for _ in range(40)]
    })
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.dataframe(corr_data, use_container_width=True, height=300)
    with col2:
        st.markdown("""
        **Use this for:**
        - Pearson Correlation
        - Simple Linear Regression
        - Scatter plots
        
        **Variables:**
        - `Student_ID`: Identifier
        - `Weekly_Study_Hours`: Continuous (5-30)
        - `GPA`: Continuous (0.0-4.0)
        - `Year`: Categorical (control variable)
        
        **Research Question:**
        *Is there a relationship between study hours and GPA?*
        """)
    
    csv3 = corr_data.to_csv(index=False)
    st.download_button("📥 Download Correlation Dataset (CSV)", csv3, "correlation_study_gpa.csv", "text/csv")

# =============================================================================
# TAB 4: CHI-SQUARE DATA
# =============================================================================
with tab4:
    st.markdown("### 🔢 Dataset 4: Smoking Status vs. Exercise Frequency (Chi-Square)")
    st.markdown("Analyze if there's an association between smoking status and exercise habits.")
    
    random.seed(789)
    
    # Generate categorical data with some association
    n = 100
    smoking = []
    exercise = []
    
    for _ in range(n):
        smoke = random.choice(["Smoker", "Non-Smoker"])
        if smoke == "Smoker":
            ex = random.choices(["Never", "Sometimes", "Regularly"], weights=[0.5, 0.35, 0.15])[0]
        else:
            ex = random.choices(["Never", "Sometimes", "Regularly"], weights=[0.15, 0.35, 0.5])[0]
        smoking.append(smoke)
        exercise.append(ex)
    
    chi_data = pd.DataFrame({
        "Respondent_ID": [f"R{i:03d}" for i in range(1, n + 1)],
        "Smoking_Status": smoking,
        "Exercise_Frequency": exercise,
        "Age_Group": [random.choice(["18-30", "31-45", "46-60", "60+"]) for _ in range(n)]
    })
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.dataframe(chi_data, use_container_width=True, height=300)
        
        # Crosstab preview
        st.markdown("**Crosstab Preview:**")
        crosstab = pd.crosstab(chi_data["Smoking_Status"], chi_data["Exercise_Frequency"])
        st.dataframe(crosstab)
        
    with col2:
        st.markdown("""
        **Use this for:**
        - Chi-Square Test of Independence
        - Cramér's V effect size
        - Cross-tabulation
        
        **Variables:**
        - `Respondent_ID`: Identifier
        - `Smoking_Status`: Categorical (2 levels)
        - `Exercise_Frequency`: Categorical (3 levels)
        - `Age_Group`: Categorical (control)
        
        **Research Question:**
        *Is smoking status associated with exercise frequency?*
        """)
    
    csv4 = chi_data.to_csv(index=False)
    st.download_button("📥 Download Chi-Square Dataset (CSV)", csv4, "chisquare_smoking_exercise.csv", "text/csv")

# Summary Section
st.markdown("---")
st.markdown("## 📋 Dataset Summary")

summary = pd.DataFrame({
    "Dataset": ["Student Scores", "Employee Productivity", "Study Hours & GPA", "Smoking & Exercise"],
    "Statistical Test": ["Independent t-Test", "One-Way ANOVA", "Pearson Correlation / Regression", "Chi-Square Test"],
    "Sample Size": [30, 45, 40, 100],
    "Variables": ["2 groups, 1 DV", "3 groups, 1 DV", "2 continuous", "2 categorical"]
})

st.dataframe(summary, use_container_width=True, hide_index=True)

st.info("💡 **Tip:** Import these datasets into SPSS, R, or Excel to practice the statistical tests covered in Paper II.")

show_footer()
