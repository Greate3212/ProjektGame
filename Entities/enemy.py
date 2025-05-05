# Import klasy
from Entities.entity import Entity


class Enemy(Entity):
    """
    Klasa dziedzicząca po klasie Entity.
    Zawiera informacje o tym, ile dany przeciwnik wyrzuca xp'a i kasy.
    """

    # Konstruktor
    def __init__(self, name, hp, armor_lvl, damage, money_drop, exp_drop):
        """
        Inicjalizuje obiekt Enemy.

        :param name: Nazwa przeciwnika.
        :type name: str
        :param hp: Początkowa ilość punktów życia przeciwnika.
        :type hp: int
        :param armor_lvl: Poziom pancerza przeciwnika.
        :type armor_lvl: int
        :param damage: Obrażenia zadawane przez przeciwnika.
        :type damage: int
        :param money_drop: Ilość pieniędzy wypadająca z przeciwnika po śmierci.
        :type money_drop: int
        :param exp_drop: Ilość doświadczenia wypadająca z przeciwnika po śmierci.
        :type exp_drop: int
        """
        super().__init__(name, hp, armor_lvl, damage)  # Wywołuje konstruktor klasy bazowej (Entity)
        self.money_drop = money_drop  # Przechowuje ilość pieniędzy wypadających z przeciwnika
        self.experience_drop = exp_drop  # Przechowuje ilość doświadczenia wypadającego z przeciwnika
