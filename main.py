import customtkinter as ctk

from ui import DeckAnalyzerUI


def main():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()

    root.title("Clash Royale Deck Analyzer V2")

    root.geometry("1100x850")

    root.minsize(1000, 750)

    app = DeckAnalyzerUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()