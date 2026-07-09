from data_loader import cards_data

def recommend_cards(deck):

    recommendations = []

    air_cards = sum(
        cards_data[c]["air_defense"]
        for c in deck
    )

    spells = sum(
        cards_data[c]["type"] == "spell"
        for c in deck
    )

    buildings = sum(
        cards_data[c]["type"] == "building"
        for c in deck
    )

    avg = sum(cards_data[c]["elixir"] for c in deck) / len(deck)

    if air_cards < 2:
        recommendations.append(
            ("Add Musketeer",
             "Your deck lacks reliable air defense.")
        )

    if spells == 0:
        recommendations.append(
            ("Add Fireball",
             "Your deck has no medium or big spell.")
        )

    if buildings == 0:
        recommendations.append(
            ("Add Tesla",
             "A defensive building improves matchups against tanks.")
        )

    if avg > 4.5:
        recommendations.append(
            ("Replace an expensive card with Skeletons",
             "Lower average elixir for a faster cycle.")
        )

    return recommendations
    print(recommendations)