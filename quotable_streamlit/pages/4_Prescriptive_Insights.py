import streamlit as st
from utils.mock_data import load_mock_campaigns
from utils.ai_agents import generate_insights

st.markdown("## 🧠 AI Strategy Recommendations")

# Load or retrieve campaign data
campaigns = st.session_state.get('campaigns')
if not campaigns:
    campaigns = load_mock_campaigns()

# Generate prescriptive insights
with st.spinner("🚀 Generating prescriptive insights..."):
    insights = generate_insights(campaigns)

# Display root cause analysis
st.markdown("### 🔍 Root Cause Analysis")
root_causes = insights.get("root_causes", [])
if root_causes:
    for rc in root_causes:
        st.write(f"- {rc}")
else:
    st.write("No root causes identified.")

# Display recommendations
st.markdown("### 🛠️ Improvement Recommendations")
recommendations = insights.get("recommendations", [])
if recommendations:
    for rec in recommendations:
        st.write(f"- {rec}")
else:
    st.write("No recommendations provided.")

# Display next campaign strategy suggestions
st.markdown("### 🎯 Next Campaign Strategy Suggestions")
strategy = insights.get("strategy", [])
if strategy:
    for strat in strategy:
        st.write(f"- {strat}")
else:
    st.write("No strategy suggestions available.")

# Import insights to lead generation (demo placeholder)
if st.button("🔄 Use Insights to Restart Campaign"):
    steps = insights.get("recommendations", []) + insights.get("strategy", [])
    st.session_state['lead_description'] = "\n".join(steps)
    st.success("✅ Insights imported to Lead Generation tab (demo).")