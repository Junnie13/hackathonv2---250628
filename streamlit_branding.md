# 🎨 Quotable Streamlit App - Branding & Styling Guide

## 🧭 Brand Identity for Streamlit Implementation

**Voice:** Smart, confident, globally aware  
**Vibe:** Strategic, actionable, sleek  
**Platform:** Streamlit web application  

---

## 🌈 Streamlit Custom CSS Styling

### Color Palette Implementation
```python
# Add to your Streamlit app
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
    
    /* Custom styling for Streamlit components */
    .main > div {
        background-color: var(--soft-light);
    }
    
    /* Header styling */
    .css-1d391kg h1 {
        color: var(--primary-blue);
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
    }
    
    /* Sidebar styling */
    .css-1lcbmhc {
        background-color: white;
        border-right: 2px solid var(--sky-blue);
    }
    
    /* Button styling */
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
    
    /* Metric cards */
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid var(--primary-blue);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Success indicators */
    .success-metric {
        color: var(--lime-green);
        font-weight: bold;
    }
    
    /* Alert indicators */
    .alert-metric {
        color: var(--coral-red);
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)
```

---

## 📱 Streamlit App Structure & Navigation

### Main App Layout (app.py)
```python
import streamlit as st

st.set_page_config(
    page_title="Quotable - AI Marketing Intelligence",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS injection
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# App header
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 style="color: #2F4FE0; font-size: 3rem; margin-bottom: 0;">
        💬 QUOTABLE
    </h1>
    <p style="color: #475569; font-size: 1.2rem; margin-top: 0;">
        New Markets. Smarter Funnels. More Quotes.
    </p>
</div>
""", unsafe_allow_html=True)
```

### Page Navigation Sidebar
```python
# Sidebar navigation with icons
st.sidebar.markdown("## 🧭 Navigation")

pages = {
    "🔍 Lead Generation": "1_Lead_Generation.py",
    "✉️ Campaign Creation": "2_Campaign_Creation.py", 
    "📊 Analytics Dashboard": "3_Analytics_Dashboard.py",
    "🧠 Prescriptive Insights": "4_Prescriptive_Insights.py"
}

selected_page = st.sidebar.radio("Choose a workflow:", list(pages.keys()))
```

---

## 🎯 Component Styling Examples

### 1. Lead Generation Page Header
```python
st.markdown("""
<div class="metric-card">
    <h2 style="color: #2F4FE0;">🔍 Lead Generation & Qualification</h2>
    <p style="color: #475569;">Upload leads and let AI evaluate decision-making power and industry relevance.</p>
</div>
""", unsafe_allow_html=True)
```

### 2. Performance Metrics Display
```python
# Create colored metric cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3 style="color: #3AB795;">✅ Qualified Leads</h3>
        <h2 style="color: #3AB795;">47/100</h2>
        <p style="color: #475569;">High decision-maker score</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3 style="color: #2F4FE0;">📧 Campaigns Sent</h3>
        <h2 style="color: #2F4FE0;">24</h2>
        <p style="color: #475569;">Cross-cultural adaptation</p>
    </div>
    """, unsafe_allow_html=True)
```

### 3. AI Status Indicators
```python
# AI processing status
if st.button("🤖 Qualify Leads with AI"):
    with st.spinner("AI is evaluating leads..."):
        # AI processing simulation
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
    
    st.success("✅ AI qualification complete!")
```

---

## 📊 Chart Styling with Plotly

### Brand-Consistent Chart Colors
```python
import plotly.express as px
import plotly.graph_objects as go

# Quotable color scheme for charts
QUOTABLE_COLORS = {
    'primary': '#2F4FE0',
    'accent': '#63B3ED', 
    'success': '#3AB795',
    'alert': '#F56565',
    'slate': '#475569'
}

# Geographic performance chart
fig = px.bar(
    df, 
    x='country', 
    y='open_rate',
    color='open_rate',
    color_continuous_scale=['#F8FAFC', '#2F4FE0'],
    title="📍 Campaign Performance by Region"
)

fig.update_layout(
    plot_bgcolor='#F8FAFC',
    paper_bgcolor='white',
    font=dict(family="Inter, sans-serif", size=12, color='#475569'),
    title_font=dict(size=18, color='#2F4FE0', family="Poppins")
)

st.plotly_chart(fig, use_container_width=True)
```

---

## 🎪 Interactive UI Components

### 1. Lead Upload with Drag & Drop
```python
st.markdown("### 📁 Upload Lead Data")

uploaded_file = st.file_uploader(
    "Choose a CSV file with leads",
    type=['csv'],
    help="Upload a CSV with columns: name, title, company, location, email"
)

if uploaded_file is None:
    st.info("👆 Upload a CSV file or use our sample data below")
    if st.button("🎯 Use Sample Insurance Leads"):
        # Load sample data
        st.session_state.sample_data_loaded = True
```

### 2. AI Configuration Panel
```python
with st.expander("🛠️ AI Configuration"):
    col1, col2 = st.columns(2)
    
    with col1:
        qualification_threshold = st.slider(
            "Qualification Threshold", 
            0.0, 1.0, 0.7,
            help="Minimum score for lead qualification"
        )
    
    with col2:
        cultural_adaptation = st.selectbox(
            "Cultural Tone",
            ["Auto-detect", "Formal", "Conversational", "Direct"],
            help="How AI adapts messaging by region"
        )
```

### 3. Real-time AI Results Display
```python
# AI qualification results with progress
if st.button("🚀 Start AI Qualification"):
    results_container = st.empty()
    
    for i, lead in enumerate(leads_df.iterrows()):
        # Simulate AI processing
        with results_container.container():
            st.write(f"Processing lead {i+1}/{len(leads_df)}")
            
            # Show AI decision
            score = ai_qualify_lead(lead)
            if score > 0.7:
                st.success(f"✅ {lead['name']} - Qualified (Score: {score:.2f})")
            else:
                st.warning(f"⚠️ {lead['name']} - Not qualified (Score: {score:.2f})")
```

---

## 🏷️ Microcopy for Streamlit UI

### Page Headers & Descriptions
```python
PAGE_COPY = {
    "lead_generation": {
        "title": "🔍 Intelligent Lead Discovery",
        "subtitle": "Upload leads and let AI identify decision-makers",
        "empty_state": "No leads uploaded yet — let's find your next market opportunity.",
        "processing": "🤖 AI is analyzing decision-making power and industry fit...",
        "success": "✅ Lead qualification complete! Ready to create campaigns."
    },
    
    "campaign_creation": {
        "title": "✉️ AI-Powered Campaign Generation", 
        "subtitle": "Create culturally-adapted, personalized outreach at scale",
        "empty_state": "Select qualified leads to generate personalized campaigns.",
        "processing": "🌍 Adapting messaging for cultural context...",
        "success": "📧 Campaigns generated! Review before sending."
    },
    
    "analytics": {
        "title": "📊 Performance Intelligence Dashboard",
        "subtitle": "Track what works across cultures and regions",
        "insights": "💡 This campaign resonates 2x better in Southeast Asia",
        "recommendation": "🎯 Shift tone to data-driven for German prospects"
    },
    
    "prescriptive": {
        "title": "🧠 AI Strategy Recommendations",
        "subtitle": "Get prescriptive insights for your next campaign",
        "cta": "🚀 Apply these insights to optimize your next campaign"
    }
}
```

### Button & Action Labels
```python
BUTTON_COPY = {
    "upload": "📁 Upload Lead CSV",
    "sample": "🎯 Try Sample Data", 
    "qualify": "🤖 Start AI Qualification",
    "generate": "✉️ Generate Campaigns",
    "analyze": "📊 Analyze Performance",
    "optimize": "🧠 Get AI Insights",
    "export": "💾 Export Results",
    "send": "📨 Send Campaigns (Demo)"
}
```

---

## 🎨 Logo & Branding Implementation

### ASCII/Unicode Logo for Streamlit
```python
st.markdown("""
<div style="text-align: center; font-family: monospace; color: #2F4FE0; font-size: 1.5rem;">
    ___________________
   |  💬  Q U O T A B L E  |
   |___________________|
        Smart Funnels
</div>
""", unsafe_allow_html=True)
```

### Favicon & Page Configuration
```python
st.set_page_config(
    page_title="Quotable - AI Marketing Intelligence",
    page_icon="💬",  # Quote bubble emoji as favicon
    layout="wide"
)
```

---

## 🚀 Deployment Styling Notes

### Streamlit Cloud Configuration
```toml
# .streamlit/config.toml
[theme]
primaryColor = "#2F4FE0"
backgroundColor = "#F8FAFC"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#475569"
font = "sans serif"
```

### Mobile Responsiveness
```python
# Add mobile-friendly CSS
st.markdown("""
<style>
    @media (max-width: 768px) {
        .main > div {
            padding: 1rem 0.5rem;
        }
        
        .metric-card {
            margin-bottom: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)
```

This branding guide ensures your Streamlit app maintains the Quotable brand identity while leveraging Streamlit's strengths for rapid prototyping and demo presentation.