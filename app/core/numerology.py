def life_path_number(dob):
    digits = [int(d) for d in dob.strftime("%d%m%Y")]
    total = sum(digits)

    while total > 9:
        total = sum(int(d) for d in str(total))

    return total


LIFE_PATH_TRAITS = {
    1: "Independent and leadership oriented",
    2: "Emotional and supportive",
    3: "Creative and expressive",
    4: "Practical and disciplined",
    5: "Adventurous and energetic",
    6: "Caring and family oriented",
    7: "Thoughtful and introspective",
    8: "Ambitious and goal driven",
    9: "Compassionate and idealistic"
}


def numerology_compatibility(lp1, lp2):
    diff = abs(lp1 - lp2)
    score = max(60, 90 - diff * 5)
    return score
