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
marked_keys = st.multiselect("🔖 Mark leads to send campaign", list(options.keys()), key="marked_leads")

# Cultural tone setting
culture = st.selectbox("Cultural Tone", ["Auto-detect", "Formal", "Conversational", "Direct"])

# Generate campaigns
if st.button("✉️ Generate Campaigns"):
    campaigns = []
    for key in marked_keys:
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

# Attachment of marketing material (demo placeholder)
material_file = st.file_uploader(
    "📎 Upload Marketing Material (e.g., webinar invite PDF)",
    type=['pdf','png','jpg'],
    help="Optional: attach event materials"
)
if material_file:
    st.session_state['material'] = material_file

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

    # Simulate sending emails
    if st.button("📨 Send All Campaign Emails"):
        # Update campaigns with any edits
        updated = []
        for idx, row in df.iterrows():
            subj = st.session_state.get(f"subj_{idx}", row['subject'])
            body = st.session_state.get(f"body_{idx}", row['body'])
            updated.append({
                "name": row['name'],
                "company": row['company'],
                "subject": subj,
                "body": body
            })
        st.session_state['campaigns'] = updated
        count = len(updated)
        st.session_state['sent_count'] = count
        st.success(f"✅ Sent {count} emails with updated content.")
        if st.session_state.get('material'):
            st.info("Included marketing material in emails (demo).")