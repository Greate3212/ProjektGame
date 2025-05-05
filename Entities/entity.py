class Entity:
    """
    Klasa bazowa, do tworzenia wrogów i graczy.
    """

    # Konstruktor
    def __init__(self, name, hp, armor_lvl, damage):
        """
        Inicjalizuje obiekt Entity.

        :param name: Nazwa entity.
        :type name: str
        :param hp: Początkowa ilość punktów życia entity.
        :type hp: int
        :param armor_lvl: Poziom pancerza entity.
        :type armor_lvl: int
        :param damage: Obrażenia zadawane przez entity.
        :type damage: int
        """
        self.name = name  # Przechowuje nazwę entity
        self.hp = hp  # Przechowuje aktualną ilość punktów życia
        self.max_hp = hp  # Przechowuje maksymalną ilość punktów życia
        self.armor_lvl = armor_lvl  # Przechowuje poziom pancerza
        self.damage = damage  # Przechowuje obrażenia zadawane
        self.dead = False  # Flaga wskazująca, czy entity jest martwe (domyślnie False)

    def take_damage(self, amount):
        """
        Funkcja odpowiedzialna za zadawanie obrażeń, zależnie od 'poziomu' zbroi.

        :param amount: Ilość obrażeń.
        :type amount: int
        :return:
        """
        if self.hp - amount >= 0:
            self.hp = self.hp - int((amount / self.armor_lvl))  # Oblicza i odejmuje obrażenia, uwzględniając poziom pancerza
        else:
            self.hp = 0  # Ustawia hp na 0, jeśli obrażenia są większe niż aktualne hp
            self.dead = True  # Ustawia flagę martwego na True
