# Import klasy
from entity import Entity


class Enemy(Entity):
    """
    Klasa dziedzicząca entity. Zawiera informacje o tym ile dany przeciwnik wyrzuca xp'a.
    """
    # Konstruktor
    def __init__(self, name, hp, armor_lvl, damage, money_drop):
        super().__init__(name, hp, armor_lvl, damage)
        self.money_drop = money_drop
