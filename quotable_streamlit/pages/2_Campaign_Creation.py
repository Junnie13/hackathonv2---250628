import streamlit as st
from utils.ai_agents import generate_campaign
import pandas as pd

st.markdown("## ✉️ AI-Powered Campaign Generation")

# Ensure qualified leads exist
leads = st.session_state.get('qualified_leads', [])
if not leads:
    st.info("No qualified leads available. Please qualify leads first.")
    st.stop()

# Lead selection
options = {f"{l['name']} ({l['company']})": l for l in leads}
selected_keys = st.multiselect("Select leads to generate campaigns for", list(options.keys()))

# Cultural tone setting
culture = st.selectbox("Cultural Tone", ["Auto-detect", "Formal", "Conversational", "Direct"])

# Generate campaigns
if st.button("✉️ Generate Campaigns"):
    campaigns = []
    for key in selected_keys:
        lead = options[key]
        try:
            campaign = generate_campaign(lead, culture)
        except Exception as e:
            st.error(f"Error generating campaign for {lead.get('name','unknown')}: {e}")
            continue
        if not isinstance(campaign, dict):
            st.error(f"Invalid AI response for {lead.get('name','unknown')}")
            continue
        campaign_record = {
            "name": lead['name'],
            "company": lead['company'],
            "subject": campaign.get("subject", ""),
            "body": campaign.get("body", "")
        }
        campaigns.append(campaign_record)
    st.session_state.campaigns = campaigns

# Display generated campaigns
if st.session_state.get('campaigns'):
    df = pd.DataFrame(st.session_state.campaigns)
    for idx, row in df.iterrows():
        st.markdown(f"### {row['name']} @ {row['company']}")
        st.text_area("Subject", row['subject'], key=f"subj_{idx}")
        st.text_area("Body", row['body'], height=200, key=f"body_{idx}")

    # Export campaigns as CSV
    csv = df.to_csv(index=False)
    st.download_button("💾 Export Campaigns CSV", data=csv, file_name="campaigns.csv")