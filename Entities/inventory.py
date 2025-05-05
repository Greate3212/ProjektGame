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
        """
        Inicjalizuje obiekt Inventory.
        """
        self.equiped_weapon = ""  # Przechowuje nazwę aktualnie założonej broni
        self.weapon_damage = 0  # Przechowuje obrażenia zadawane przez założoną broń
        self.equiped_armor = ""  # Przechowuje nazwę aktualnie założonej zbroi
        self.armor_level = 0  # Przechowuje poziom pancerza zapewniany przez założoną zbroję
        self.heal_items_amount = 0  # Przechowuje ilość posiadanych przedmiotów leczących
        self.amount_of_heal = 20  # Przechowuje ilość hp przywracaną przez jeden przedmiot leczący

    def have_heal(self):
        """
        Funkcja odpowiedzialna za sprawdzanie, czy osoba posiada jakieś itemy heal'ujące.
        :return:
        """
        if self.heal_items_amount > 0:  # Sprawdza, czy ilość przedmiotów leczących jest większa od 0
            return True  # Zwraca True, jeśli gracz posiada przedmioty leczące
        else:
            return False  # Zwraca False, jeśli gracz nie posiada przedmiotów leczących

    def heal_amount(self):
        """
        Funkcja odpowiedzialna za zwracanie informacji na temat ilości leczenia.
        :return:
        """
        return self.amount_of_heal  # Zwraca ilość hp przywracaną przez jeden przedmiot leczący

    def show_inventory(self):
        """
        Funkcja odpowiedzialna za zwracanie informacji o ekwipunku gracza.
        :return:
        """
        return self.equiped_weapon, self.equiped_armor, self.heal_items_amount  # Zwraca informacje o założonej broni, zbroi i ilości przedmiotów leczących
