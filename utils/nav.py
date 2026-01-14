import streamlit as st
from streamlit_option_menu import option_menu

def show_top_nav(current_page="Home"):
    """Renders the top navigation bar for Ph.D. Research Methods Hub."""
    
    # Hide default sidebar nav
    st.markdown("""
        <style>
            [data-testid="stSidebarNav"] {display: none !important;}
            section[data-testid="stSidebar"] {display: none !important;}
        </style>
    """, unsafe_allow_html=True)
    
    # Define all pages
    page_map = {
        # Home
        "Home": "Home.py",
        # Paper I - Research Methodology
        "Intro to Research": "pages/9_🔬_Intro_Research.py",
        "Research Design": "pages/10_📋_Research_Design.py",
        "Measurement & Sampling": "pages/11_📏_Measurement_Sampling.py",
        "Report & Publication": "pages/12_📄_Report_Publication.py",
        # Paper II - Statistics
        "Statistical Foundations": "pages/5_📐_Statistical_Foundations.py",
        "Correlation & Regression": "pages/6_📈_Correlation_Regression.py",
        "Computer Applications": "pages/7_💻_Computer_Applications.py",
        "Formula Cheat Sheet": "pages/8_📝_Formula_Cheat_Sheet.py",
        # Paper III - Research Ethics
        "Philosophy & Ethics": "pages/1_📖_Philosophy_Ethics.py",
        "Research Metrics": "pages/2_📊_Research_Metrics.py",
        "Online Tools": "pages/3_🔧_Online_Tools.py",
        "Case Studies": "pages/4_📋_Case_Studies.py",
        # Resources
        "Toolkit": "pages/13_🛠️_Phd_Toolkit.py",
        "Glossary": "pages/14_📚_Glossary.py",
        "Sample Datasets": "pages/15_📁_Sample_Datasets.py",
        "Practice Problems": "pages/16_✏️_Practice_Problems.py",
        "Downloads": "pages/17_📥_Downloads.py",
    }
    
    # Group pages by paper
    paper1_pages = ["Intro to Research", "Research Design", "Measurement & Sampling", "Report & Publication"]
    paper2_pages = ["Statistical Foundations", "Correlation & Regression", "Computer Applications", "Formula Cheat Sheet"]
    paper3_pages = ["Philosophy & Ethics", "Research Metrics", "Online Tools", "Case Studies"]
    resources_pages = ["Toolkit", "Glossary", "Sample Datasets", "Practice Problems", "Downloads"]
    
    # Determine current paper
    if current_page in paper1_pages:
        current_paper = "Paper I"
    elif current_page in paper2_pages:
        current_paper = "Paper II"
    elif current_page in paper3_pages:
        current_paper = "Paper III"
    elif current_page in resources_pages:
        current_paper = "Resources"
    else:
        current_paper = "Home"
    
    # Paper selector row
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        paper = option_menu(
            menu_title=None,
            options=["🏠 Home", "📝 Paper I", "📐 Paper II", "📚 Paper III", "🛠️ Resources"],
            icons=["house", "journal-text", "calculator", "book", "tools"],
            default_index=0 if current_paper == "Home" else 
                         1 if current_paper == "Paper I" else 
                         2 if current_paper == "Paper II" else 
                         3 if current_paper == "Paper III" else 4,
            orientation="horizontal",
            styles={
                "container": {
                    "padding": "3px 8px !important", 
                    "background-color": "#f8fafc", 
                    "border-radius": "10px", 
                    "margin-bottom": "8px", 
                    "box-shadow": "0 1px 3px rgba(0,0,0,0.08)",
                    "border": "1px solid #e2e8f0"
                },
                "icon": {"font-size": "14px"}, 
                "nav-link": {
                    "font-size": "13px", 
                    "text-align": "center", 
                    "margin": "0 3px", 
                    "--hover-color": "#f1f5f9", 
                    "color": "#64748b",
                    "padding": "8px 12px",
                    "border-radius": "8px",
                    "font-weight": "500"
                },
                "nav-link-selected": {
                    "background-color": "#1e40af", 
                    "color": "white", 
                    "font-weight": "600"
                },
            },
            key="paper_nav"
        )
    
    # Handle paper selection
    if paper == "🏠 Home" and current_page != "Home":
        st.switch_page("Home.py")
        return
    
    # Module navigation based on selected paper
    if paper == "📝 Paper I":
        options = paper1_pages
        icons = ["search", "clipboard", "rulers", "file-text"]
        default_idx = paper1_pages.index(current_page) if current_page in paper1_pages else 0
    elif paper == "📐 Paper II":
        options = paper2_pages
        icons = ["calculator", "graph-up", "laptop", "file-earmark-text"]
        default_idx = paper2_pages.index(current_page) if current_page in paper2_pages else 0
    elif paper == "📚 Paper III":
        options = paper3_pages
        icons = ["book", "bar-chart", "tools", "clipboard-check"]
        default_idx = paper3_pages.index(current_page) if current_page in paper3_pages else 0
    elif paper == "🛠️ Resources":
        options = resources_pages
        icons = ["wrench", "journal-bookmark", "folder", "pencil-square", "download"]
        default_idx = resources_pages.index(current_page) if current_page in resources_pages else 0
    else:
        return  # Home selected, no module nav needed

    selected = option_menu(
        menu_title=None,
        options=options,
        icons=icons,
        default_index=default_idx,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "3px 8px !important", 
                "background-color": "#ffffff", 
                "border-radius": "8px", 
                "margin-bottom": "10px", 
                "box-shadow": "0 1px 2px rgba(0,0,0,0.05)",
                "border": "1px solid #e2e8f0"
            },
            "icon": {"color": "#1e40af", "font-size": "13px"}, 
            "nav-link": {
                "font-size": "12px", 
                "text-align": "center", 
                "margin": "0 2px", 
                "--hover-color": "#eff6ff", 
                "color": "#64748b",
                "padding": "6px 12px",
                "border-radius": "6px"
            },
            "nav-link-selected": {
                "background-color": "#eff6ff", 
                "color": "#1e40af", 
                "font-weight": "600"
            },
        },
        key="module_nav"
    )
    
    # Navigate if selection changed
    if selected != current_page:
        target_file = page_map[selected]
        st.switch_page(target_file)

