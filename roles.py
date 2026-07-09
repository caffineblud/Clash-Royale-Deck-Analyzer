from data_loader import cards_data

ROLE_RULES = {
    "Win Condition": lambda c: cards_data[c]["type"] == "win_condition",

    "Small Spell": lambda c: c in {
        "Zap",
        "The Log",
        "Barbarian Barrel",
        "Giant Snowball",
        "Arrows"
    },

    "Big Spell": lambda c: c in {
        "Fireball",
        "Poison",
        "Rocket",
        "Lightning",
        "Earthquake"
    },

    "Building": lambda c:
        cards_data[c]["type"] == "building",

    "Tank Killer": lambda c: c in {
        "Mini P.E.K.K.A",
        "P.E.K.K.A",
        "Inferno Tower",
        "Hunter",
        "Inferno Dragon"
    },

    "Air Defense": lambda c:
        cards_data[c]["air_defense"],

    "Splash Damage": lambda c:
        cards_data[c]["splash"],

    "Reset Card": lambda c: c in {
        "Zap",
        "Electro Wizard",
        "Electro Spirit",
        "Zappies",
        "Lightning"
    },

    "Cycle Card": lambda c:
        cards_data[c]["elixir"] <= 2,
}


def analyze_roles(deck):
    """
    Returns:
        {
            "Win Condition": True,
            "Building": False,
            ...
        }
    """

    results = {}

    for role, rule in ROLE_RULES.items():
        results[role] = any(rule(card) for card in deck)

    return results