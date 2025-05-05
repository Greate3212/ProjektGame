class Level:
    """
    Klasa odpowiedzialna za przechowywanie informacji na temat level'a.
    """
    # Konstruktor
    def __init__(self, level=1):
        self.level = level
        self.experience = 0
        self.experience_to_next_level = [0, 1000, 2000]

    def add_experience(self, amount):
        """
        Funkcja odpowiedzialna za przydzielanie xp.
        :param amount: Ilość xp'a
        :type amount: int
        :return:
        """
        """
        Jest w pętli, bo gdyby było bez. To w momencie, w którym gracz dostał,
        by pierdyliard xp, to nie dostałby odpowiedniego poziomu.
        Po prostu dostałby jeden, a reszta xp'a wpadła, by do zmiennej experience.
        """
        xp_to_give = 1
        for x in range(0, amount):
            self.add_xp_to_player(xp_to_give)
            xp_to_give += 1

    def add_xp_to_player(self, xp_to_give):
        """
        Rozbita część funkcji add_experience. Żeby wszystko było czytelne.
        Funkcja sprawdza, czy gracz dostanie poziom.
        :param xp_to_give: Ilość xp'a do przyznania
        :type xp_to_give: int
        :return:
        """
        if self.experience >= self.experience_to_next_level[self.level]:
            self.level += 1
        else:
            self.experience += xp_to_give