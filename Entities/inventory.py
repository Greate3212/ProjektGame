class Inventory:
    """
    Klasa odpowiadająca za przechowywanie informacji na temat ekwipunku gracza.
    Informacji takich jak:
    — Jaką ma zbroję
    — Ile ta zbroja dodaje armor'a
    — Jaką ma broń
    — Ile ta broń zadanie damage'a
    — Jakie ma itemy heal'ujące

    """
    # Konstruktor
    def __init__(self):
        self.equiped_weapon = ""
        self.weapon_damage = 0
        self.equiped_armor = ""
        self.armor_level = 0
        self.heal_items = []