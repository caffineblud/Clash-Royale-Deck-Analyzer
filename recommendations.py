from logic import cards_data

def recommend_cards(deck):

    recommendations = []

    air_cards = sum(
        cards_data[c]["air_defense"]
        for c in deck
    )

    if air_cards < 2:
        recommendations.extend([
            "Archers",
            "Musketeer",
            "Phoenix"
        ])

    spells = sum(
        cards_data[c]["type"] == "spell"
        for c in deck
    )

    if spells == 0:
        recommendations.extend([
            "Fireball",
            "Arrows",
            "Zap"
        ])

    return list(set(recommendations))