from pydantic import BaseModel
from datetime import date

class CompatibilityRequest(BaseModel):
    user_dob: date
    partner_dob: date


class Insight(BaseModel):
    score: int
    insight: str


class CompatibilityResponse(BaseModel):
    overall_compatibility: int
    numerology: Insight
    zodiac: Insight
    emotional_alignment: Insight
    ai_summary: dict
