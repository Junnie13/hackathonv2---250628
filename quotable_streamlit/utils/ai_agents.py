import os
import json
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Prompts from PRD
LEAD_EVAL_PROMPT = """
You are an AI lead evaluator for insurance industry campaigns.
Analyze this lead and return a JSON response:

Lead: {name}, {title}, {company}, {location}

Return:
{{
    "decision_maker_score": 0.0-1.0,
    "industry_relevance": 0.0-1.0,
    "overall_quality": "High/Medium/Low",
    "reasoning": "brief explanation"
}}
"""

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

def ai_qualify_lead(lead: dict) -> dict:
    """
    Call OpenAI to evaluate a single lead.
    """
    prompt = LEAD_EVAL_PROMPT.format(**lead)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI lead evaluator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    content = response.choices[0].message.content
    return json.loads(content)

# Prescriptive insights prompt and generator
INSIGHTS_PROMPT = """
You are an AI performance analyst. Given campaign performance data, provide:
- Root cause analysis of performance issues
- Improvement recommendations
- Next campaign strategy suggestions
Return a JSON object with keys: root_causes (list), recommendations (list), strategy (list).
"""

def generate_insights(campaigns: list) -> dict:
    prompt = INSIGHTS_PROMPT + "\nCampaigns: " + json.dumps(campaigns)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI performance analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    content = response.choices[0].message.content
    return json.loads(content)

def generate_campaign(lead: dict, culture_notes: str = "Auto-detect") -> dict:
    """
    Call OpenAI to generate a campaign email for a single lead.
    """
    prompt = CAMPAIGN_GEN_PROMPT.format(culture_notes=culture_notes, **lead)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI campaign generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    content = response.choices[0].message.content
    return json.loads(content)