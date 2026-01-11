from app.core.numerology import (
    life_path_number,
    numerology_compatibility,
    LIFE_PATH_TRAITS
)
from app.core.zodiac import sun_sign, zodiac_compatibility
from app.core.scoring import overall_score
from app.ai.insight_generator import generate_ai_insights
from app.utils.cache import get_from_cache, set_to_cache


def calculate_compatibility(user_dob, partner_dob):
    cache_key = f"{user_dob}_{partner_dob}"

    # 🚀 1. CACHE CHECK
    cached_response = get_from_cache(cache_key)
    if cached_response:
        print("⚡ Cache hit:", cache_key)
        return cached_response

    print("🤖 Cache miss, generating new result")

    # 🧮 2. NORMAL LOGIC
    lp1 = life_path_number(user_dob)
    lp2 = life_path_number(partner_dob)

    numerology_score = numerology_compatibility(lp1, lp2)

    sign1 = sun_sign(user_dob)
    sign2 = sun_sign(partner_dob)

    zodiac_score = zodiac_compatibility(sign1, sign2)

    emotional_alignment = int((numerology_score + zodiac_score) / 2)
    overall = overall_score(numerology_score, zodiac_score, emotional_alignment)

    ai_payload = {
        "numerology_score": numerology_score,
        "zodiac_score": zodiac_score,
        "emotional_alignment": emotional_alignment,
        "user_traits": LIFE_PATH_TRAITS[lp1],
        "partner_traits": LIFE_PATH_TRAITS[lp2]
    }

    ai_insights = generate_ai_insights(ai_payload)

    final_response = {
        "numerology": numerology_score,
        "zodiac": zodiac_score,
        "emotional": emotional_alignment,
        "overall": overall,
        "signs": (sign1, sign2),
        "ai": ai_insights
    }

    # 💾 3. SAVE TO CACHE
    set_to_cache(cache_key, final_response)

    return final_response
