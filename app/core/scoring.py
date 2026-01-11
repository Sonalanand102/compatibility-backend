def overall_score(numerology, zodiac, emotional):
    return int(
        numerology * 0.5 +
        zodiac * 0.3 +
        emotional * 0.2
    )
