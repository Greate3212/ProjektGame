class Entity:
    """
    Klasa bazowa, do tworzenia wrogów i graczy.
    """
    # Konstruktor
    def __init__(self, name, hp, armor_lvl, damage):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.armor_lvl = armor_lvl
        self.damage = damage
        self.dead = False

    def take_damage(self, amount):
        """
        Funkcja odpowiedzialna za zadawanie obrażen, zależnie od 'poziomu' zbroi.
        :param amount: Ilość obrażen
        :type amount: int
        :return:
        """
        if self.hp - amount >= 0:
            self.hp = self.hp - int((amount / self.armor_lvl))
        else:
            self.hp = 0
            self.dead = True



