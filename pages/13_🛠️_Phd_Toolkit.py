import streamlit as st
import pandas as pd
import datetime
from utils.styles import apply_custom_css, show_footer
from utils.nav import show_top_nav

apply_custom_css()
show_top_nav(current_page="Toolkit")

# Header
st.markdown("""
<div style="text-align: center; padding: 12px; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 10px; margin-bottom: 20px;">
    <h2 style="margin: 0 !important; font-size: 1.4rem !important;">🛠️ Ph.D. Survival Toolkit</h2>
    <p style="margin: 5px 0 0 0 !important; font-size: 14px; color: #475569;">Essential tools for planning, citing, and managing your research journey.</p>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["📅 Timeline Planner", "📝 Citation Generator", "🍅 Focus Timer"])

# =============================================================================
# TAB 1: TIMELINE PLANNER
# =============================================================================
with tab1:
    st.markdown("### 📅 Ph.D. Journey Planner")
    st.info("Visualize your doctoral timeline with standard milestones.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Configuration")
        start_date = st.date_input("Start Date", datetime.date.today())
        duration_years = st.slider("Duration (Years)", 3, 7, 4)
        
        milestones = {
            "Coursework": {"start_offset": 0, "duration_months": 12, "color": "#3b82f6"},
            "Literature Review": {"start_offset": 6, "duration_months": 12, "color": "#10b981"},
            "Comprehensive Exam": {"start_offset": 12, "duration_months": 3, "color": "#f59e0b"},
            "Proposal Defense": {"start_offset": 15, "duration_months": 3, "color": "#ef4444"},
            "Data Collection": {"start_offset": 18, "duration_months": 18, "color": "#8b5cf6"},
            "Data Analysis": {"start_offset": 30, "duration_months": 12, "color": "#ec4899"},
            "Thesis Writing": {"start_offset": 36, "duration_months": 12, "color": "#6366f1"},
            "Final Defense": {"start_offset": 46, "duration_months": 2, "color": "#14b8a6"}
        }
        
    with col2:
        # Create Data for Timeline
        data = []
        for task, details in milestones.items():
            start = start_date + datetime.timedelta(days=details["start_offset"]*30)
            end = start + datetime.timedelta(days=details["duration_months"]*30)
            data.append(dict(Task=task, Start=start, Finish=end, Color=details["color"]))
            
        df = pd.DataFrame(data)
        
        # Use Simple HTML/CSS Gantt for lightweight look without heavy dependencies
        st.markdown("#### Your Roadmap")
        
        for _, row in df.iterrows():
            total_days = duration_years * 365
            start_delta = (row['Start'] - start_date).days
            duration_days = (row['Finish'] - row['Start']).days
            
            left_pct = max(0, (start_delta / total_days) * 100)
            width_pct = min(100, (duration_days / total_days) * 100)
            
            st.markdown(f"""
            <div style="margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px; font-size: 13px; font-weight: 600; color: #334155;">
                    <span>{row['Task']}</span>
                    <span style="font-weight: 400; color: #64748b;">{row['Start'].strftime('%b %Y')} - {row['Finish'].strftime('%b %Y')}</span>
                </div>
                <div style="width: 100%; background-color: #e2e8f0; border-radius: 999px; height: 10px; position: relative;">
                    <div style="position: absolute; left: {left_pct}%; width: {width_pct}%; background-color: {row['Color']}; height: 100%; border-radius: 999px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        st.caption(f"Projected Completion: {(start_date + datetime.timedelta(days=duration_years*365)).strftime('%B %Y')}")

# =============================================================================
# TAB 2: CITATION GENERATOR
# =============================================================================
with tab2:
    st.markdown("### 📝 Quick Citation Generator")
    st.info("Generate bibliographies for your papers instantly.")
    
    ctype = st.selectbox("Source Type", ["Journal Article", "Book", "Website"])
    
    c1, c2 = st.columns(2)
    
    author_last = c1.text_input("Author Last Name", "Smith")
    author_first = c2.text_input("Author First Initial", "J")
    year = c1.text_input("Year", "2024")
    title = c2.text_input("Title", "The Impact of Artificial Intelligence")
    
    citation_text = ""
    
    if ctype == "Journal Article":
        journal = c1.text_input("Journal Name", "Journal of Research")
        volume = c2.text_input("Volume(Issue)", "10(2)")
        pages = c1.text_input("Page Range", "100-112")
        doi = c2.text_input("DOI", "10.1000/xyz123")
        
        if st.button("Generate Citation"):
            # APA Style
            citation_text = f"{author_last}, {author_first}. ({year}). {title}. *{journal}*, *{volume}*, {pages}. https://doi.org/{doi}"
            
    elif ctype == "Book":
        publisher = c1.text_input("Publisher", "Academic Press")
        location = c2.text_input("City/Location", "New York, NY")
        
        if st.button("Generate Citation"):
            citation_text = f"{author_last}, {author_first}. ({year}). *{title}*. {location}: {publisher}."

    elif ctype == "Website":
        site_name = c1.text_input("Website Name", "Research Daily")
        url = c2.text_input("URL", "https://example.com")
        
        if st.button("Generate Citation"):
            citation_text = f"{author_last}, {author_first}. ({year}). {title}. *{site_name}*. Retrieved from {url}"

    if citation_text:
        st.success("Citation Generated (APA 7th Style):")
        st.code(citation_text, language=None)
        st.caption("Double-click to select and copy.")

# =============================================================================
# TAB 3: FOCUS TIMER
# =============================================================================
with tab3:
    st.markdown("### 🍅 Pomodoro Focus Timer")
    st.info("Use the Pomodoro technique: 25 minutes of work, 5 minutes of break.")
    
    col_t1, col_t2 = st.columns([1, 1])
    
    with col_t1:
        work_min = st.number_input("Work Duration (min)", 15, 60, 25)
        if st.button("Start Focus Session"):
            with st.status("🍅 Focus Mode Active", expanded=True):
                st.write("Timer is running... (Simulated)")
                st.write(f"Objective: Focus for {work_min} minutes.")
                st.write("❌ Avoid checking emails.")
                st.write("❌ Put phone on silent.")
                st.write("✅ Write that paragraph!")
                
    with col_t2:
        st.markdown("""
        **Why this works:**
        The Pomodoro technique fights procrastination by breaking work into manageable chunks.
        
        1. **Pick a task.**
        2. **Set the timer.**
        3. **Work until the ring.**
        4. **Take a short break.**
        """)

show_footer()
