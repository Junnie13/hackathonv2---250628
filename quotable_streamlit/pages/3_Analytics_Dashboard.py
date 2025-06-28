import streamlit as st
import pandas as pd
import plotly.express as px
from utils.mock_data import load_mock_campaigns

st.markdown("## 📊 Performance Intelligence Dashboard")
# Campaign progress & actionable insights
sent = st.session_state.get('sent_count', 0)
st.markdown(f"**📨 Emails Sent:** {sent}")
st.markdown("### 💡 Actionable Insights")
st.info("Demo: Consider re-engaging leads with low click rates using follow-up email.")

# Load mock campaign data
campaigns = load_mock_campaigns()
df = pd.DataFrame(campaigns)

if df.empty:
    st.info("No campaign performance data available.")
else:
    # Summary metric cards
    avg_open = df['open_rate'].mean()
    avg_click = df['click_rate'].mean()
    avg_response = df['response_rate'].mean()
    total_leads = df['leads_contacted'].sum()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #3AB795;">✅ Avg Open Rate</h3>
            <h2 style="color: #3AB795;">{avg_open:.1%}</h2>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #63B3ED;">📈 Avg Click Rate</h3>
            <h2 style="color: #63B3ED;">{avg_click:.1%}</h2>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #F56565;">📬 Avg Response Rate</h3>
            <h2 style="color: #F56565;">{avg_response:.1%}</h2>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #475569;">👥 Total Leads Contacted</h3>
            <h2 style="color: #475569;">{total_leads}</h2>
        </div>
        """, unsafe_allow_html=True)

    # Geographic performance chart
    fig = px.bar(
        df,
        x='geography',
        y='open_rate',
        color='open_rate',
        color_continuous_scale=['#F8FAFC', '#2F4FE0'],
        title="📍 Campaign Open Rates by Region"
    )
    fig.update_layout(
        plot_bgcolor='#F8FAFC',
        paper_bgcolor='white',
        font=dict(family="Inter, sans-serif", size=12, color='#475569'),
        title_font=dict(size=18, color='#2F4FE0', family="Poppins")
    )
    st.plotly_chart(fig, use_container_width=True)

    # Click rates chart
    fig2 = px.bar(
        df,
        x='geography',
        y='click_rate',
        color='click_rate',
        color_continuous_scale=['#F8FAFC', '#63B3ED'],
        title="📍 Campaign Click Rates by Region"
    )
    fig2.update_layout(
        plot_bgcolor='#F8FAFC',
        paper_bgcolor='white',
        font=dict(family="Inter, sans-serif", size=12, color='#475569'),
        title_font=dict(size=18, color='#63B3ED', family="Poppins")
    )
    st.plotly_chart(fig2, use_container_width=True)