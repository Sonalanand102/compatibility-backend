from fastapi import APIRouter
from app.models.schemas import CompatibilityRequest
from app.core.engine import calculate_compatibility

router = APIRouter()   # 👈 THIS WAS MISSING

@router.post("/calculate")
def calculate(data: CompatibilityRequest):
    result = calculate_compatibility(data.user_dob, data.partner_dob)

    return {
        "overallCompatibility": result["overall"],
        "numerology": {
            "score": result["numerology"],
            "insight": "Numerology shows emotional and value-based tendencies."
        },
        "zodiac": {
            "score": result["zodiac"],
            "insight": f"Sun sign interaction between {result['signs'][0]} and {result['signs'][1]}."
        },
        "emotionalAlignment": {
            "score": result["emotional"],
            "insight": "Reflects emotional response harmony."
        },
        "aiInsights": result["ai"]
    }
