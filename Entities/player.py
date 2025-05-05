# Import override'a
# Override — to nadpisywanie funkcji.
# W klasie bazowej istnieje funkcja, ale ci się nie podoba?
# Jeb override i nadpisujesz własną nową.
from typing_extensions import override

# Importowanie klas
from Entities.entity import Entity
from Entities.inventory import Inventory
from Entities.level_handler import Level


class Player(Entity):
    """
    Klasa dziedzicząca po klasie Entity. Odpowiada za przetrzymywanie informacji na temat gracza.
    Informacji takich jak:
    — Obiekt/klasę jego poziomu
    — Obiekt/klasę jego ekwipunku
    """

    # Konstruktor
    def __init__(self, name, hp, armor_lvl, damage):
        """
        Inicjalizuje obiekt Player.

        :param name: Nazwa gracza.
        :type name: str
        :param hp: Początkowa ilość punktów życia gracza.
        :type hp: int
        :param armor_lvl: Poziom pancerza gracza.
        :type armor_lvl: int
        :param damage: Obrażenia zadawane przez gracza.
        :type damage: int
        """
        super().__init__(name, hp, armor_lvl, damage)  # Wywołuje konstruktor klasy bazowej (Entity)
        self.level = Level()  # Tworzy obiekt Level dla gracza, zarządzający jego poziomem i doświadczeniem
        self.inventory = Inventory()  # Tworzy obiekt Inventory dla gracza, zarządzający jego ekwipunkiem

    @override
    def take_damage(self, amount):
        """
        Nadpisanie funkcji odpowiedzialnej za zadawanie obrażeń.
        Nadpisałem, bo gracz ma dodatkowy armor zależny od zbroi.

        :param amount: Ilość obrażeń.
        :return:
        """
        if self.hp - amount >= 0:
            self.hp = self.hp - int(
                (amount / (self.armor_lvl + self.inventory.armor_level)))  # Oblicza obrażenia, uwzględniając pancerz gracza i dodatkowy pancerz z ekwipunku
        else:
            self.hp = 0  # Ustawia hp na 0, jeśli obrażenia są większe niż aktualne hp
            self.dead = True  # Ustawia flagę martwego na True

    def heal_hp(self):
        """
        Funkcja odpowiedzialna za leczenie gracza.
        """
        if self.inventory.have_heal():  # Sprawdza, czy gracz posiada przedmioty leczące
            if self.hp + self.inventory.heal_amount() >= self.max_hp:
                self.hp = self.max_hp  # Jeśli leczenie przywróciłoby więcej niż max hp, ustaw hp na max hp
            else:
                self.hp += self.inventory.heal_amount()  # Dodaje ilość hp przywracaną przez przedmiot leczący
