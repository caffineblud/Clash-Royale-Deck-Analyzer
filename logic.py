from collections import Counter
from archetypes import detect_archetype
from recommendations import recommend_cards
from data_loader import cards_data

# -------------------------
# Basic Analysis
# -------------------------

def calculate_average_elixir(deck):
    total = sum(cards_data[card]["elixir"] for card in deck)
    return round(total / len(deck), 2)


def detect_win_condition(deck):

    win_conditions = []

    for card in deck:

        if cards_data[card]["type"] == "win_condition":
            win_conditions.append(card)

    if win_conditions:
        return ", ".join(win_conditions)

    return "No Win Condition Found"


# -------------------------
# Strength Analysis
# -------------------------

def analyze_strengths(deck):

    strengths = []

    air = sum(
        cards_data[c]["air_defense"]
        for c in deck
    )

    splash = sum(
        cards_data[c]["splash"]
        for c in deck
    )

    avg = calculate_average_elixir(deck)

    if air >= 3:
        strengths.append("Strong Air Defense")

    if splash >= 2:
        strengths.append("Good Splash Damage")

    if avg <= 3.5:
        strengths.append("Fast Cycle")

    if len(strengths) == 0:
        strengths.append("Balanced Deck")

    return strengths


# -------------------------
# Weakness Analysis
# -------------------------

def analyze_weaknesses(deck):

    weaknesses = []

    air = sum(
        cards_data[c]["air_defense"]
        for c in deck
    )

    spells = sum(
        cards_data[c]["type"] == "spell"
        for c in deck
    )

    avg = calculate_average_elixir(deck)

    if air < 2:
        weaknesses.append("Weak Against Air")

    if spells == 0:
        weaknesses.append("No Spell Support")

    if avg > 4.5:
        weaknesses.append("Heavy Elixir Cost")

    if len(weaknesses) == 0:
        weaknesses.append("No Major Weakness Found")

    return weaknesses


# -------------------------
# Card Statistics
# -------------------------

def get_card_statistics(deck):

    stats = {
        "troops": 0,
        "spells": 0,
        "buildings": 0,
        "win_conditions": 0,
        "champions": 0
    }

    for card in deck:

        card_type = cards_data[card]["type"]

        if card_type == "troop":
            stats["troops"] += 1

        elif card_type == "spell":
            stats["spells"] += 1

        elif card_type == "building":
            stats["buildings"] += 1

        elif card_type == "win_condition":
            stats["win_conditions"] += 1

        elif card_type == "champion":
            stats["champions"] += 1

    return stats

# -------------------------
# Synergy System
# -------------------------

SYNERGY_PAIRS = {

    ("Hog Rider", "Fireball"): 10,

    ("Goblin Barrel", "Princess"): 15,

    ("Golem", "Night Witch"): 20,

    ("Royal Giant", "Fisherman"): 15,

    ("Lava Hound", "Balloon"): 20,

    ("Miner", "Wall Breakers"): 15,

    ("Electro Giant", "Tornado"): 15
}


def calculate_synergy(deck):

    score = 0

    deck_set = set(deck)

    matched_pairs = []

    for pair, value in SYNERGY_PAIRS.items():

        if pair[0] in deck_set and pair[1] in deck_set:

            score += value

            matched_pairs.append(
                f"{pair[0]} + {pair[1]}"
            )

    return min(score, 100), matched_pairs


# -------------------------
# Counter Analysis
# -------------------------

COUNTERS = {

    "Hog Rider": [
        "Tesla",
        "Inferno Tower",
        "Tornado"
    ],

    "Golem": [
        "P.E.K.K.A",
        "Inferno Tower",
        "Mini P.E.K.K.A"
    ],

    "Goblin Barrel": [
        "The Log",
        "Arrows",
        "Barbarian Barrel"
    ],

    "Royal Giant": [
        "Inferno Tower",
        "P.E.K.K.A",
        "Mini P.E.K.K.A"
    ],

    "Balloon": [
        "Tesla",
        "Musketeer",
        "Archers"
    ]
}


def analyze_counters(deck):

    counters = []

    for card in deck:

        if card in COUNTERS:
            counters.extend(COUNTERS[card])

    return sorted(set(counters))


# -------------------------
# Deck Score
# -------------------------

def calculate_deck_score(deck):

    score = 50

    air = sum(
        cards_data[c]["air_defense"]
        for c in deck
    )

    splash = sum(
        cards_data[c]["splash"]
        for c in deck
    )

    spells = sum(
        cards_data[c]["type"] == "spell"
        for c in deck
    )

    avg = calculate_average_elixir(deck)

    synergy_score, _ = calculate_synergy(deck)

    score += air * 4
    score += splash * 2
    score += spells * 4
    score += synergy_score

    if 3 <= avg <= 4.5:
        score += 15

    return min(score, 100)


# -------------------------
# Advanced Rating System
# -------------------------

def advanced_rating(deck):

    air = sum(
        cards_data[c]["air_defense"]
        for c in deck
    )

    spells = sum(
        cards_data[c]["type"] == "spell"
        for c in deck
    )

    splash = sum(
        cards_data[c]["splash"]
        for c in deck
    )

    avg = calculate_average_elixir(deck)

    synergy_score, _ = calculate_synergy(deck)

    offense = min(
        100,
        50 + splash * 5
    )

    defense = min(
        100,
        50 + air * 5
    )

    air_defense = min(
        100,
        air * 15
    )

    cycle = max(
        20,
        100 - int(avg * 15)
    )

    synergy = min(
        100,
        50 + synergy_score
    )

    overall = round(
        (
            offense +
            defense +
            air_defense +
            cycle +
            synergy
        ) / 5,
        1
    )

    return {
        "Offense": offense,
        "Defense": defense,
        "Air Defense": air_defense,
        "Cycle": cycle,
        "Synergy": synergy,
        "Overall": overall
    }
    
#--------------------------
#deck health score
#--------------------------

def deck_health_score(deck):
    """
    Returns a detailed deck health breakdown.
    """

    air = sum(cards_data[c]["air_defense"] for c in deck)
    splash = sum(cards_data[c]["splash"] for c in deck)
    spells = sum(cards_data[c]["type"] == "spell" for c in deck)
    avg = calculate_average_elixir(deck)

    synergy_score, _ = calculate_synergy(deck)

    offense = min(100, 50 + splash * 5)

    defense = min(100, 50 + air * 6)

    cycle = max(30, 100 - int(avg * 15))

    spell_support = min(100, spells * 50)

    health = {
        "Offense": offense,
        "Defense": defense,
        "Cycle": cycle,
        "Air Defense": min(100, air * 15),
        "Spell Support": spell_support,
        "Synergy": synergy_score,
    }

    health["Overall"] = round(
        sum(health.values()) / len(health)
    )

    return health
# -------------------------
# Deck Comparison
# -------------------------

def compare_decks(deck1, deck2):

    score1 = calculate_deck_score(deck1)

    score2 = calculate_deck_score(deck2)

    if score1 > score2:
        winner = "Deck A"

    elif score2 > score1:
        winner = "Deck B"

    else:
        winner = "Tie"

    return score1, score2, winner


# -------------------------
# Elixir Distribution
# -------------------------

def get_elixir_distribution(deck):

    costs = [
        cards_data[card]["elixir"]
        for card in deck
    ]

    counter = Counter(costs)

    return dict(
        sorted(counter.items())
    )


# -------------------------
# Export Report
# -------------------------

def export_pdf(text):

    with open(
        "deck_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)
def compare_decks(deck1, deck2):

    score1 = calculate_deck_score(deck1)
    score2 = calculate_deck_score(deck2)

    ratings1 = advanced_rating(deck1)
    ratings2 = advanced_rating(deck2)

    if score1 > score2:
        winner = "Deck A"
    elif score2 > score1:
        winner = "Deck B"
    else:
        winner = "Tie"

    return {
        "score1": score1,
        "score2": score2,
        "ratings1": ratings1,
        "ratings2": ratings2,
        "winner": winner
    }
def get_deck_rank(score):

    if score >= 90:
        return "S"

    elif score >= 80:
        return "A"

    elif score >= 70:
        return "B"

    elif score >= 60:
        return "C"

    return "D"
def validate_deck(deck):

    champions = 0

    for card in deck:

        if cards_data[card]["type"] == "champion":
            champions += 1

    if champions > 1:
        return False

    return True