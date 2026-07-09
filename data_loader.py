import json

def load_cards():
    with open("data/cards.json", "r", encoding="utf-8") as file:
        return json.load(file)

cards_data = load_cards()