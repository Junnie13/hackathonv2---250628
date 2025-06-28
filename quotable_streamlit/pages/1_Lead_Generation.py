import streamlit as st
import pandas as pd
from pathlib import Path
from utils.ai_agents import ai_qualify_lead

st.markdown("## 🔍 Intelligent Lead Discovery")

# Lead guidance input (RAG placeholder)
lead_description = st.text_area(
    "Lead Search Guide",
    value=st.session_state.get("lead_description", ""),
    height=100,
    help="Describe criteria for leads (demo placeholder)"
)
st.session_state['lead_description'] = lead_description
guide_file = st.file_uploader(
    "📄 Upload Guide Document",
    type=['txt','pdf'],
    help="Optional demo placeholder for guide"
)
if guide_file:
    st.session_state['lead_guide'] = guide_file.read()
elif 'lead_guide' not in st.session_state:
    st.session_state['lead_guide'] = None
if lead_description:
    st.success("Lead guidance received (demo).")

# File upload or sample data
uploaded_file = st.file_uploader("📁 Upload Lead Data (CSV)", type=['csv'])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state.leads_df = df
elif st.button("🎯 Use Sample Insurance Leads"):
    sample_path = Path(__file__).parent.parent / "data" / "sample_leads.csv"
    df = pd.read_csv(sample_path)
    st.session_state.leads_df = df

# Ensure leads_df exists
if 'leads_df' not in st.session_state or st.session_state.leads_df is None:
    st.info("No leads loaded yet.")
    st.stop()

df = st.session_state.leads_df

# Qualification threshold
threshold = st.slider("Qualification Threshold", 0.0, 1.0, 0.7)

# AI qualification
if st.button("🤖 Start AI Qualification"):
    results = []
    for _, row in df.iterrows():
        lead = row.to_dict()
        evaluation = ai_qualify_lead(lead)
        lead.update(evaluation)
        results.append(lead)
    result_df = pd.DataFrame(results)
    st.session_state.lead_eval_df = result_df
    qualified = result_df[result_df['decision_maker_score'] >= threshold]
    st.session_state.qualified_leads = qualified.to_dict(orient='records')

# Display evaluation table
if 'lead_eval_df' in st.session_state:
    st.dataframe(st.session_state.lead_eval_df)

# Export qualified leads
if 'qualified_leads' in st.session_state and st.session_state.qualified_leads:
    qual_df = pd.DataFrame(st.session_state.qualified_leads)
    csv = qual_df.to_csv(index=False)
    st.download_button("💾 Export Qualified Leads", data=csv, file_name="qualified_leads.csv")