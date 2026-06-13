def detect_archetype(deck):

    deck_set = set(deck)

    if "Hog Rider" in deck_set:
        return "Cycle"

    if "Golem" in deck_set:
        return "Beatdown"

    if "Goblin Barrel" in deck_set:
        return "Bait"

    if "Mortar" in deck_set or "X-Bow" in deck_set:
        return "Siege"

    if "Royal Giant" in deck_set:
        return "Control"

    return "Unknown"