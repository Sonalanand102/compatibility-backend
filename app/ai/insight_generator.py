import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-pro-latest"

SYSTEM_INSTRUCTIONS = """
You are a relationship insight generator.

Rules:
- Insights are based only on date of birth tendencies
- Do NOT claim guarantees, destiny, soulmate, or perfection
- Keep tone neutral, supportive, and human
- Avoid deterministic or absolute language
"""


def generate_ai_insights(data: dict) -> dict:
    prompt = f"""
{SYSTEM_INSTRUCTIONS}

Numerology Score: {data['numerology_score']}
Zodiac Score: {data['zodiac_score']}
Emotional Alignment: {data['emotional_alignment']}

User Traits: {data['user_traits']}
Partner Traits: {data['partner_traits']}

Generate:
1. Overall summary (2 lines)
2. Strengths (2 bullet points)
3. Challenges (2 bullet points)
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[prompt]  # ✅ IMPORTANT
        )

        text = (
            response.candidates[0]
            .content.parts[0]
            .text
        )

        return {
            "generated": True,
            "content": text.strip()
        }

    except Exception as e:
        print("❌ Gemini Error:", str(e))  # ✅ DEBUG LINE

        return {
            "generated": False,
            "content": "AI insights are currently unavailable. Please rely on score-based compatibility."
        }
