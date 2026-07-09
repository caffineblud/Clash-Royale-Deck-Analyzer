import customtkinter as ctk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
from pdf_export import export_pdf as export_to_pdf
from logic import *
from deck_storage import save_deck, load_saved_decks
from tkinter import filedialog
from roles import analyze_roles
from data_loader import cards_data
class DeckAnalyzerUI:

    def __init__(self, root):
        self.root = root
        self.cards = sorted(cards_data.keys())

        title = ctk.CTkLabel(
            root,
            text="🏆 Clash Royale Deck Analyzer V2",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=15)

        selector_frame = ctk.CTkFrame(root)
        selector_frame.pack(pady=10)

        self.card_selectors = []
        self.search_entries = []

        for i in range(8):
            frame = ctk.CTkFrame(selector_frame)
            frame.grid(row=i // 2, column=i % 2, padx=10, pady=10)

            search_entry = ctk.CTkEntry(
                frame,
                width=250,
                placeholder_text="Search card..."
            )
            search_entry.pack(pady=(5, 2))

            combo = ctk.CTkComboBox(
                frame,
                values=self.cards,
                width=250
            )
            combo.pack(pady=(2, 5))

            search_entry.bind(
                "<KeyRelease>",
                lambda e, idx=i: self.filter_cards(e, idx)
            )

            self.search_entries.append(search_entry)
            self.card_selectors.append(combo)

        btn_frame = ctk.CTkFrame(root)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Analyze", command=self.analyze).grid(row=0, column=0, padx=5)
        ctk.CTkButton(btn_frame, text="Save Deck", command=self.save_current_deck).grid(row=0, column=1, padx=5)
        ctk.CTkButton(btn_frame, text="Load Deck", command=self.load_deck).grid(row=0, column=2, padx=5)
        ctk.CTkButton(btn_frame, text="Elixir Graph", command=self.show_graph).grid(row=0, column=3, padx=5)
        ctk.CTkButton(btn_frame, text="Export", command=self.export).grid(row=0, column=4, padx=5)
        ctk.CTkButton(btn_frame, text="Clear", command=self.clear).grid(row=0, column=5, padx=5)

        self.result_box = ctk.CTkTextbox(root, width=900, height=500)
        self.result_box.pack(padx=20, pady=20, fill="both", expand=True)

    def filter_cards(self, event, index):
        text = self.search_entries[index].get().lower()
        filtered = [c for c in self.cards if text in c.lower()]
        if not filtered:
            filtered = self.cards
        self.card_selectors[index].configure(values=filtered)

    def get_deck(self):
        return [c.get().strip() for c in self.card_selectors]

    def analyze(self):

        deck = self.get_deck()

        if len(set(deck)) != 8:

            messagebox.showerror(
                "Error",
                "Select 8 unique cards."
            )
            return

        if not validate_deck(deck):

            messagebox.showerror(
                "Invalid Deck",
                "Only one Champion allowed."
            )
            return

        try:

            avg = calculate_average_elixir(deck)
            win = detect_win_condition(deck)
            strengths = analyze_strengths(deck)
            weaknesses = analyze_weaknesses(deck)
            stats = get_card_statistics(deck)
            archetype = detect_archetype(deck)
            synergy_score, synergy_pairs = calculate_synergy(deck)
            counters = analyze_counters(deck)
            recs = recommend_cards(deck)
            ratings = advanced_rating(deck)
            roles = analyze_roles(deck)
            report = f"""
Deck: {', '.join(deck)}

Average Elixir: {avg}
Archetype: {archetype}
Win Condition: {win}

Strengths:
{chr(10).join(strengths)}

Weaknesses:
{chr(10).join(weaknesses)}

Synergy Score: {synergy_score}
Combos:
{chr(10).join(synergy_pairs) if synergy_pairs else 'None'}

Counters:
{chr(10).join(counters) if counters else 'None'}

Recommendations:
{chr(10).join(
    f"• {card}\n  Reason: {reason}"
    for card, reason in recs
) if recs else "None"}
Deck Roles:
{chr(10).join(
    f"{'✓' if present else '✗'} {role}"
    for role, present in roles.items()
)}

Stats:
Troops: {stats['troops']}
Spells: {stats['spells']}
Buildings: {stats['buildings']}
Win Conditions: {stats['win_conditions']}
Champions: {stats['champions']}

Ratings:
Offense: {ratings['Offense']}
Defense: {ratings['Defense']}
Air Defense: {ratings['Air Defense']}
Cycle: {ratings['Cycle']}
Synergy: {ratings['Synergy']}

Overall: {ratings['Overall']}/100
"""
            self.result_box.delete("1.0", "end")
            self.result_box.insert("end", report)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_current_deck(self):
        name = simpledialog.askstring("Save Deck", "Enter deck name:")
        if name:
            save_deck(name, self.get_deck())

    def load_deck(self):
        decks = load_saved_decks()
        if not decks:
            return

        name = simpledialog.askstring(
            "Load Deck",
            "Available:\n" + "\n".join(decks.keys())
        )

        if name in decks:
            for combo, card in zip(self.card_selectors, decks[name]):
                combo.set(card)

    def show_graph(self):
        deck = self.get_deck()
        data = get_elixir_distribution(deck)

        plt.figure(figsize=(6, 4))
        plt.bar(list(data.keys()), list(data.values()))
        plt.title("Elixir Distribution")
        plt.xlabel("Elixir")
        plt.ylabel("Cards")
        plt.show()

    def export(self):

        report = self.result_box.get(
            "1.0",
            "end"
        )

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[
                ("PDF Files", "*.pdf")
            ]
        )

        if not file_path:
            return

        export_to_pdf(report, file_path)

        messagebox.showinfo(
            "Success",
            f"PDF saved successfully:\n{file_path}"
        )

    def clear(self):
        self.result_box.delete("1.0", "end")

        for combo in self.card_selectors:
            combo.set("")

        for entry in self.search_entries:
            entry.delete(0, "end")
