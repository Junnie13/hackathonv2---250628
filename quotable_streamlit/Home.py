import streamlit as st
import runpy
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent))

# Page config
st.set_page_config(
    page_title="Quotable - AI Marketing Intelligence",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (from branding guide)
st.markdown("""
<style>
:root {
    --primary-blue: #2F4FE0;
    --sky-blue: #63B3ED; 
    --slate-gray: #475569;
    --lime-green: #3AB795;
    --coral-red: #F56565;
    --soft-light: #F8FAFC;
}
.main > div {
    background-color: var(--soft-light);
}
.css-1d391kg h1 {
    color: var(--primary-blue);
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
}
.css-1lcbmhc {
    background-color: white;
    border-right: 2px solid var(--sky-blue);
}
.stButton > button {
    background-color: var(--primary-blue);
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: 600;
}
.stButton > button:hover {
    background-color: var(--sky-blue);
}
.metric-card {
    background: white;
    padding: 1rem;
    border-radius: 8px;
    border-left: 4px solid var(--primary-blue);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.success-metric {
    color: var(--lime-green);
    font-weight: bold;
}
.alert-metric {
    color: var(--coral-red);
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'leads_df' not in st.session_state:
    st.session_state.leads_df = None
if 'qualified_leads' not in st.session_state:
    st.session_state.qualified_leads = []
if 'campaigns' not in st.session_state:
    st.session_state.campaigns = []

# OpenAI API key input
api_input = st.sidebar.text_input(
    "🔑 OpenAI API Key",
    value=st.session_state.get("OPENAI_API_KEY", ""),
    type="password",
    help="Paste your OpenAI API key here"
)
if api_input:
    import os
    os.environ["OPENAI_API_KEY"] = api_input
    st.session_state["OPENAI_API_KEY"] = api_input

# App header
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 style="color: #2F4FE0; font-size: 3rem; margin-bottom: 0;">💬 QUOTABLE</h1>
    <p style="color: #475569; font-size: 1.2rem; margin-top: 0;">New Markets. Smarter Funnels. More Quotes.</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("## 🧭 Navigation")
pages = {
    "🔍 Lead Generation": "pages/1_Lead_Generation.py",
    "✉️ Campaign Creation": "pages/2_Campaign_Creation.py",
    "📊 Analytics Dashboard": "pages/3_Analytics_Dashboard.py",
    "🧠 Prescriptive Insights": "pages/4_Prescriptive_Insights.py"
}
selection = st.sidebar.radio("Choose a workflow:", list(pages.keys()))
page_script = Path(__file__).parent / pages[selection]
runpy.run_path(str(page_script), run_name="__main__")