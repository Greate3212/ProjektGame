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
        self.heal_items_amount = 0
        self.amount_of_heal = 20

    def have_heal(self):
        """
        Funkcja odpowiedzialna za sprawdzanie, czy osoba posiada jakieś itemy heal'ujące.
        :return:
        """
        if self.heal_items_amount > 0:
            return True
        else:
            return False

    def heal_amount(self):
        """
        Funkcja odpowiedzialna za zwracanie informacji na temat ilości leczenia.
        :return:
        """
        return self.amount_of_heal

    def show_inventory(self):
        return self.equiped_weapon, self.equiped_armor, self.heal_items_amount
