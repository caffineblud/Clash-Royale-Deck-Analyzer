# 🏆 Clash Royale Deck Analyzer V1

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI-1F6AA5?style=flat&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-11557c?style=flat&logo=matplotlib&logoColor=white)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF_Export-red?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

> A desktop application for analyzing, building, and optimizing your Clash Royale decks — with real-time scoring, synergy detection, archetype classification, and PDF export.

---

## 📸 Features at a Glance

| Feature | Description |
|---|---|
| 🃏 **Deck Builder** | Select 8 cards with live search/filter dropdowns |
| 📊 **Deck Analysis** | Elixir average, win condition, archetype, card stats |
| 💪 **Strengths & Weaknesses** | Automated air defense, splash, and spell coverage detection |
| ✨ **Synergy Scoring** | Detects known power combos and scores them 0–100 |
| 🎯 **Counter Detection** | Lists cards that counter your win conditions |
| ⭐ **Advanced Rating** | Offense / Defense / Air / Cycle / Synergy breakdown |
| 💾 **Save & Load Decks** | Persist your decks locally as JSON |
| 📈 **Elixir Graph** | Bar chart of elixir cost distribution |
| 📄 **PDF Export** | Export the full analysis report as a PDF |

---

## 🗂️ Project Structure

```
clash-royale-analyzer/
│
├── main.py               # 🚀 Entry point — launches the GUI
├── ui.py                 # 🖥️  CustomTkinter UI — all widgets and interactions
├── logic.py              # 🧠 Core analysis engine (scoring, synergy, counters, etc.)
├── archetypes.py         # 🏷️  Archetype detection logic
├── recommendations.py    # 💡 Card recommendation engine
├── deck_storage.py       # 💾 Save/load decks to JSON
├── pdf_export.py         # 📄 ReportLab-based PDF export
│
└── data/
    ├── cards.json        # 🃏 Card database (elixir, type, air_defense, splash flags)
    └── saved_decks.json  # 🗃️  Persisted user decks
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.10+ | Core application |
| **GUI** | [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) | Modern dark-themed desktop UI |
| **Charts** | [Matplotlib](https://matplotlib.org/) | Elixir distribution bar chart |
| **PDF** | [ReportLab](https://www.reportlab.com/) | Deck analysis PDF export |
| **Data** | JSON | Card database & saved deck storage |
| **Standard Lib** | `collections.Counter`, `tkinter` | Distribution counting, dialogs |

---

## 🧠 Analysis Engine — `logic.py`

The heart of the app. All analysis is stateless and purely functional.

### Scoring Pipeline

```
Deck (8 cards)
    │
    ├── calculate_average_elixir()     → float
    ├── detect_win_condition()         → string
    ├── detect_archetype()             → Hog Cycle / Beatdown / LavaLoon / etc.
    ├── analyze_strengths()            → list[str]
    ├── analyze_weaknesses()           → list[str]
    ├── get_card_statistics()          → {troops, spells, buildings, win_conditions, champions}
    ├── calculate_synergy()            → (score: int, matched_pairs: list[str])
    ├── analyze_counters()             → list[str]
    ├── recommend_cards()              → list[str]
    ├── advanced_rating()              → {Offense, Defense, Air Defense, Cycle, Synergy, Overall}
    └── calculate_deck_score()         → int (0–100)
```

### Archetype Detection

The analyzer identifies these archetypes automatically:

| Archetype | Key Cards |
|---|---|
| 🐗 Hog Cycle | Hog Rider + Skeletons + Ice Spirit |
| 💣 Log Bait | Goblin Barrel + Princess |
| 🔥 LavaLoon | Lava Hound + Balloon |
| 💀 Splashyard | Graveyard + Baby Dragon |
| 🗡️ Bridge Spam | P.E.K.K.A + Bandit |
| 🪨 Beatdown | Golem |

### Synergy Pairs

| Combo | Synergy Score |
|---|---|
| Golem + Night Witch | +20 |
| Lava Hound + Balloon | +20 |
| Goblin Barrel + Princess | +15 |
| Royal Giant + Fisherman | +15 |
| Miner + Wall Breakers | +15 |
| Electro Giant + Tornado | +15 |
| Hog Rider + Fireball | +10 |

### Deck Rank

| Score | Rank |
|---|---|
| 90–100 | 🏅 S |
| 80–89 | 🥇 A |
| 70–79 | 🥈 B |
| 60–69 | 🥉 C |
| < 60 | ❌ D |

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.10 or higher
- pip

### Install Dependencies

```bash
pip install customtkinter matplotlib reportlab
```

### Run the App

```bash
python main.py
```

---

## 💾 Data Format

### `cards.json` — Card Database

Each card entry follows this schema:

```json
"Hog Rider": {
    "elixir": 4,
    "type": "win_condition",
    "air_defense": 0,
    "splash": 0
}
```

**Card Types:** `troop`, `spell`, `building`, `win_condition`, `champion`

### `saved_decks.json` — Saved Decks

```json
{
    "my_deck": [
        "Hog Rider", "Fireball", "Musketeer",
        "Skeletons", "Ice Spirit", "Tesla",
        "The Log", "Ice Golem"
    ]
}
```

---

## 🔮 Planned Features

- [ ] 🌐 Meta tier list integration (live data)
- [ ] ⚔️ Head-to-head deck comparison UI
- [ ] 📱 Mobile-friendly web port
- [ ] 🤖 AI-powered deck suggestions
- [ ] 🗃️ Deck history and versioning

---

## 👨‍💻 Author
***Yash Kumar Singh***

Built with ❤️ for Clash Royale enthusiasts. V1 — first public release.
---
*v2-coming soon*
