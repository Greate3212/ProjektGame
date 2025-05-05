# Import override'a
# Override — to nadpisywanie funkcji.
# W klasie bazowej istnieje funkcja, ale ci się nie podoba?
# Jeb override i nadpisujesz własną nową.
from typing_extensions import override

# Importowanie klas
from entity import Entity
from inventory import Inventory
from level_handler import Level


class Player(Entity):
    """
    Klasa dziedzicząca entity. Odpowiada za przetrzymywanie informacji na temat gracza.
    Informacji takich jak:
    — Obiekt/klasę jego poziomu
    — Obiekt/klasę jego ekwipunku
    """

    # Konstruktor
    def __init__(self, name, hp, armor_lvl, damage):
        super().__init__(name, hp, armor_lvl, damage)
        self.level = Level()
        self.inventory = Inventory()

    @override
    def take_damage(self, amount):
        """
        Nadpisanie funkcji odpowiedzialnej za zadawanie obrażeń.
        Nadpisałem, bo gracz ma dodatkowy armor zależny od zbroi.
        :param amount:
        :return:
        """
        if self.hp - amount >= 0:
            self.hp = self.hp - int((amount / (self.armor_lvl + self.inventory.armor_level)))
        else:
            self.hp = 0
            self.dead = True

    def heal_hp(self):
        if self.inventory.have_heal():
            if self.hp + self.inventory.heal_amount() >= self.max_hp:
                self.hp = self.max_hp
            else:
                self.hp += self.inventory.heal_amount()
