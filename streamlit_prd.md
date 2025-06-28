# Product Requirements Document (PRD) - Streamlit MVP

**Project Name:** Quotable  
**Tagline:** New Markets. Smarter Funnels. More Quotes.  
**Platform:** Streamlit Web Application

## 1. Overview

Quotable is an AI-powered Streamlit MVP designed to demonstrate intelligent international lead generation and marketing campaign optimization. The Streamlit implementation focuses on showcasing the AI workflow and analytics capabilities without complex backend infrastructure.

**Core Value Proposition:**
- Automated lead scraping and qualification
- AI-generated personalized email campaigns  
- Performance analytics with prescriptive insights
- Cultural intelligence for global markets

## 2. Streamlit App Structure

### Page 1: Lead Generation & Qualification
**Features:**
- File upload for CSV lead lists OR manual lead input
- AI-powered lead evaluation using OpenAI API
- Real-time filtering and scoring display
- Export qualified leads

### Page 2: Campaign Creation
**Features:**
- Lead selection from qualified database
- AI email generation with cultural customization
- Template preview and editing
- Bulk campaign preparation

### Page 3: Campaign Analytics Dashboard
**Features:**
- Mock campaign performance metrics
- Interactive charts (Plotly)
- Geographic performance breakdown
- ROI and conversion tracking

### Page 4: Prescriptive Insights
**Features:**
- Root cause analysis of campaign performance
- AI-generated improvement recommendations
- Benchmark comparisons
- Next campaign strategy suggestions

## 3. Technical Implementation

### Core Stack
- **Frontend:** Streamlit
- **AI:** OpenAI API (GPT-4)
- **Data:** Pandas + CSV files
- **Visualization:** Plotly, Streamlit charts
- **State Management:** Streamlit session state

### Data Flow
```
CSV Upload → AI Qualification → Campaign Generation → Mock Analytics → Prescriptive AI
```

### File Structure
```
quotable_streamlit/
├── app.py (main Streamlit app)
├── pages/
│   ├── 1_Lead_Generation.py
│   ├── 2_Campaign_Creation.py
│   ├── 3_Analytics_Dashboard.py
│   └── 4_Prescriptive_Insights.py
├── utils/
│   ├── ai_agents.py
│   ├── mock_data.py
│   └── analytics.py
├── data/
│   ├── sample_leads.csv
│   └── mock_campaigns.json
└── requirements.txt
```

## 4. AI Agent Prompts (Streamlit Optimized)

### Lead Qualification Agent
```python
LEAD_EVAL_PROMPT = """
You are an AI lead evaluator for insurance industry campaigns.
Analyze this lead and return a JSON response:

Lead: {name}, {title}, {company}, {location}

Return:
{
    "decision_maker_score": 0.0-1.0,
    "industry_relevance": 0.0-1.0,
    "overall_quality": "High/Medium/Low",
    "reasoning": "brief explanation"
}
"""
```

### Campaign Generator Agent
```python
CAMPAIGN_GEN_PROMPT = """
Generate a personalized email for this lead:
- Name: {name}
- Title: {title} 
- Company: {company}
- Location: {location}
- Cultural Context: {culture_notes}

Create a professional outreach email with:
1. Personalized subject line
2. Cultural tone appropriate for {location}
3. Insurance industry value proposition
4. Clear call-to-action

Format as JSON with subject and body fields.
"""
```

## 5. Streamlit Features Implementation

### Session State Management
```python
# Initialize session state for data persistence
if 'qualified_leads' not in st.session_state:
    st.session_state.qualified_leads = []
if 'campaigns' not in st.session_state:
    st.session_state.campaigns = []
```

### Interactive Components
- **File uploader** for lead CSV import
- **Multiselect** for lead filtering
- **Slider** for qualification thresholds
- **Text areas** for email editing
- **Download buttons** for exports

### Mock Data Integration
- Pre-populated sample leads for demo
- Simulated campaign performance metrics
- Geographic performance variations
- Industry benchmarks

## 6. Demo Workflow

### Step 1: Lead Upload (Page 1)
1. Upload CSV or use sample data
2. AI evaluates each lead in real-time
3. Display qualification scores and reasoning
4. Filter and export qualified leads

### Step 2: Campaign Creation (Page 2)
1. Select qualified leads
2. Choose geographic/cultural settings
3. AI generates personalized emails
4. Preview and edit campaigns
5. "Send" campaigns (demo mode)

### Step 3: Analytics Review (Page 3)
1. View mock campaign results
2. Geographic performance breakdown
3. A/B testing insights
4. Conversion funnel analysis

### Step 4: AI Insights (Page 4)
1. Root cause analysis of performance
2. Cultural optimization suggestions
3. Predictive benchmarking
4. Next campaign recommendations

## 7. Sample Data Structure

### Leads CSV Format
```csv
name,title,company,location,email,linkedin_url
John Smith,Chief Risk Officer,Global Insurance Co,Singapore,john@global.com,linkedin.com/in/johnsmith
Maria Garcia,VP Operations,Seguros Latina,Mexico City,maria@seguros.mx,linkedin.com/in/mariagarcia
```

### Mock Campaign Results
```json
{
    "campaign_id": "camp_001",
    "sent_date": "2024-06-15",
    "leads_contacted": 50,
    "open_rate": 0.24,
    "click_rate": 0.08,
    "response_rate": 0.04,
    "geography": "Singapore",
    "cultural_tone": "formal"
}
```

## 8. Development Milestones

| Milestone | Deliverable | ETA |
|-----------|-------------|-----|
| **Day 1** | Basic Streamlit structure + Lead upload | Complete |
| **Day 2** | AI lead qualification + Campaign generation | In Progress |
| **Day 3** | Analytics dashboard + Mock data integration | Planned |
| **Day 4** | Prescriptive insights + Demo polish | Planned |

## 9. Deployment Options

### Local Development
```bash
pip install streamlit openai pandas plotly
streamlit run app.py
```

### Cloud Deployment
- **Streamlit Cloud** (recommended for demo)
- **Heroku** 
- **Railway**
- **Replit**

## 10. Demo Script Integration

The Streamlit app will support the existing pitch flow:
1. **Problem demonstration** - Show inefficient manual lead qualification
2. **Solution walkthrough** - Live AI qualification and campaign generation  
3. **Results visualization** - Interactive analytics dashboard
4. **AI insights** - Prescriptive recommendations in action

## 11. Environment Variables

```env
OPENAI_API_KEY=your_openai_key
STREAMLIT_THEME_PRIMARY_COLOR=#2F4FE0
STREAMLIT_THEME_BACKGROUND_COLOR=#F8FAFC
```

## 12. Success Metrics for MVP

- **Functionality:** All 4 pages working with AI integration
- **Performance:** <3 second response times for AI calls
- **Usability:** Intuitive navigation and clear value demonstration
- **Demo Ready:** Polished UI matching brand guidelines
- **Data Flow:** Seamless lead → campaign → analytics → insights workflow