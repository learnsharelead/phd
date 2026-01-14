# 🎓 Ph.D. Research Methods Hub

> **Complete Coursework Platform: Paper I, II, and III for Doctoral Research**

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

## 🎯 Overview

A comprehensive Ph.D. coursework platform covering **Research Methodology (Paper I)**, **Statistics and Computer Applications (Paper II)**, and **Ethics in Research and Publications (Paper III)**. Features interactive tutorials, all formulas with memory tips, real-world case studies, and practical software guides.

| Stats | |
|-------|---|
| **Papers** | 3 complete courses |
| **Units** | 12 comprehensive modules |
| **Formulas** | 50+ with derivations |
| **Credits** | 6 total (2 per paper) |

---

## � Paper I: Research Methodology

*Credits: 2 | Objective: Develop a strong foundation in research concepts, design, data collection, and scholarly reporting.*

### Unit I: Introduction to Research
- ✅ Meaning and types of research (Descriptive, Analytical, Applied, Quantitative, Qualitative)
- ✅ Conceptual vs Empirical research
- ✅ Research procedures and interdisciplinary research
- ✅ Literature survey and problem identification
- ✅ Experimental, quasi-experimental, exploratory, and conclusive research
- ✅ Cross-sectional and time-series research
- ✅ Research objectives, characteristics, and hypothesis formulation

### Unit II: Research Design & Data Collection
- ✅ Research design: definition and types
- ✅ Questionnaire design and preparation
- ✅ Prerequisites of a good questionnaire
- ✅ Data collection methods

### Unit III: Measurement, Scaling & Sampling
- ✅ Validity and reliability: concepts and types
- ✅ Construction and validation of questionnaires
- ✅ Cronbach's Alpha
- ✅ Measurement scales: nominal, ordinal, interval, ratio
- ✅ Scaling techniques (Likert, Semantic Differential)
- ✅ Sampling methods: probability and non-probability

### Unit IV: Research Report & Publication
- ✅ Primary and secondary data
- ✅ Sampling techniques: simple random, stratified, systematic
- ✅ Research report writing: structure, tables, references
- ✅ Citation styles (APA, IEEE, Vancouver)
- ✅ Journal publication process
- ✅ Research metrics: Impact Factor, SNIP, SJR, IPP
- ✅ Citation metrics: h-index, g-index, i10-index

---

## 📐 Paper II: Statistics and Computer Applications

*Credits: 2 | Objective: Equip scholars with statistical tools and software skills for research data analysis.*

### Unit I: Statistical Foundations
- ✅ Hypothesis design: Null and Alternate hypotheses
- ✅ Parametric and non-parametric tests
- ✅ z-test, t-test, ANOVA
- ✅ Degrees of freedom and confidence intervals
- ✅ Kolmogorov–Smirnov test, Run test
- ✅ Mann-Whitney U test, Kruskal-Wallis test
- ✅ Chi-square test

### Unit II: Correlation & Regression
- ✅ Charts and tables
- ✅ Correlation analysis (Pearson, Spearman)
- ✅ Regression: properties, curve fitting
- ✅ Least squares method
- ✅ Classical assumptions of linear regression
- ✅ Gauss-Markov theorem
- ✅ Estimation and prediction
- ✅ Multiple regression analysis

### Unit III: Computer Applications
- ✅ MS Excel: features, formulas, Data Analysis ToolPak
- ✅ SPSS: interface, procedures, syntax
- ✅ R: statistical computing, ggplot2, packages
- ✅ MATLAB: matrix operations, statistical functions
- ✅ LaTeX: document structure, equations, bibliography
- ✅ ATLAS.ti: qualitative data analysis
- ✅ AMOS: structural equation modeling

### 📝 Formula Cheat Sheet
- All essential formulas with derivations
- Memory tips and mnemonics
- Quick reference cards
- 4-week study schedule
- Common mistakes to avoid

---

## 📚 Paper III: Ethics in Research and Publications

*Credits: 2 | Objective: Build ethical researchers with integrity in scientific conduct.*

### Unit I: Philosophy, Ethics & Scientific Conduct
- ✅ Introduction to Philosophy: Definition, Nature, Scope
- ✅ Ethics: Moral Philosophy, Moral Judgments
- ✅ Intellectual Honesty and Research Integrity
- ✅ Scientific Misconduct: Fabrication, Falsification, Plagiarism (FFP)
- ✅ Redundant Publications, Salami Slicing
- ✅ Authorship and Contributorship (ICMJE, CRediT)

### Unit II: Research Metrics and Databases
- ✅ Journal Metrics: Impact Factor, CiteScore, SNIP, SJR
- ✅ Author Metrics: h-index, g-index, i10-index
- ✅ Citation Databases: Scopus, Web of Science, PubMed
- ✅ Open Access: DOAJ, PLOS, BASE

### Unit III: Online Tools and Publication Policy
- ✅ Open Access Publishing: Gold, Green, Hybrid
- ✅ SHERPA/RoMEO: Self-archiving policies
- ✅ Predatory Journals: Detection, UGC-CARE
- ✅ Plagiarism Software: Turnitin, Urkund
- ✅ Conflict of Interest management

### Case Studies
- 🧬 Hwang Woo-suk (Stem Cell Fraud)
- ⚡ Jan Hendrik Schön (Physics Fabrication)
- ❤️ Piero Anversa (Cardiac Stem Cell)
- 🧠 Diederik Stapel (Psychology Fraud)
- 💉 Andrew Wakefield (Vaccine-Autism)
- 🇮🇳 Cases from India

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/learnsharelead/phd-research-hub.git
cd phd-research-hub

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run Home.py
```

The app will open at `http://localhost:8501`

---

## 📁 Project Structure

```
phd-research-hub/
├── Home.py                                # Landing page
├── pages/
│   ├── 1_📖_Philosophy_Ethics.py         # Paper III - Unit I
│   ├── 2_📊_Research_Metrics.py          # Paper III - Unit II
│   ├── 3_🔧_Online_Tools.py              # Paper III - Unit III
│   ├── 4_📋_Case_Studies.py              # Paper III - Case Studies
│   ├── 5_📐_Statistical_Foundations.py   # Paper II - Unit I
│   ├── 6_📈_Correlation_Regression.py    # Paper II - Unit II
│   ├── 7_💻_Computer_Applications.py     # Paper II - Unit III
│   ├── 8_📝_Formula_Cheat_Sheet.py       # Paper II - Cheat Sheet
│   ├── 9_🔬_Intro_Research.py            # Paper I - Unit I
│   ├── 10_📋_Research_Design.py          # Paper I - Unit II
│   ├── 11_📏_Measurement_Sampling.py     # Paper I - Unit III
│   └── 12_📄_Report_Publication.py       # Paper I - Unit IV
├── utils/
│   ├── __init__.py
│   ├── nav.py                             # Navigation component
│   ├── seo.py                             # SEO utilities
│   └── styles.py                          # Custom CSS
├── assets/                                # Images and resources
├── requirements.txt
└── README.md
```

---

## ✨ Key Features

### 🎓 Learning Experience
- **All Formulas** — Every statistical formula with step-by-step derivation
- **Memory Tips** — Mnemonics and patterns to remember formulas
- **Analogies** — Complex concepts explained through everyday examples
- **Visual Diagrams** — Flowcharts and architecture diagrams
- **Case Studies** — Real-world fraud analyzed in depth
- **Interactive Elements** — Expanders, tabs, organized content

### 📝 Cheat Sheet Features
- Printable quick reference card
- Test selection decision table
- Critical values quick lookup
- 4-week study schedule
- Common mistakes to avoid

### 🔍 Expert SEO
- JSON-LD Structured Data (Schema.org)
- Course Schema for educational content
- FAQ Schema for featured snippets

---

## 📚 References

- **C.R. Kothari** – *Research Methodology: Methods and Techniques*
- **Gupta & Kapoor** – *Fundamentals of Mathematical Statistics*
- **Mark Gardener** – *Beginning R*
- **MATLAB Programming** – *PHI*
- **SPSS Handbook** – *Himalaya Publishing*
- ACM, IEEE, Elsevier, Springer resources

---

## 🎯 Learning Outcomes

After completing these courses, you will be able to:

### Paper I (Research Methodology)
- ✅ Design research studies with proper methodology
- ✅ Create valid and reliable questionnaires
- ✅ Select appropriate sampling methods
- ✅ Write publication-ready research reports

### Paper II (Statistics)
- ✅ Design and test statistical hypotheses
- ✅ Perform parametric and non-parametric tests
- ✅ Conduct correlation and regression analysis
- ✅ Use Excel, SPSS, R, MATLAB, and LaTeX

### Paper III (Ethics)
- ✅ Understand philosophical foundations of ethics
- ✅ Identify and avoid scientific misconduct
- ✅ Navigate research metrics and databases
- ✅ Recognize predatory journals

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

---

**Made with ❤️ for Ph.D. Researchers**
