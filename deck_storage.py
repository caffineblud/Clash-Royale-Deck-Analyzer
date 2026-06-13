import json

FILE = "data/saved_decks.json"


def load_saved_decks():

    try:

        with open(FILE, "r") as f:
            return json.load(f)

    except:

        return {}


def save_deck(name, deck):

    decks = load_saved_decks()

    decks[name] = deck

    with open(FILE, "w") as f:

        json.dump(
            decks,
            f,
            indent=4
        )