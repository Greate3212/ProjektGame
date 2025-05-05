class Level:
    """
    Klasa odpowiedzialna za przechowywanie informacji na temat level'a.
    """

    # Konstruktor
    def __init__(self, level=1):
        """
        Inicjalizuje obiekt Level.

        :param level: Początkowy poziom gracza. Domyślnie 1.
        :type level: int
        """
        self.level = level  # Przechowuje aktualny poziom gracza
        self.experience = 0  # Przechowuje aktualną ilość doświadczenia gracza
        self.experience_to_next_level = [0, 1000,
                                        2000]  # Przechowuje listę ilości doświadczenia wymaganych do osiągnięcia kolejnych poziomów

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
        for x in range(0, amount):  # Iteruje przez ilość otrzymanego doświadczenia
            self.add_xp_to_player(xp_to_give)  # Dodaje doświadczenie graczowi
            xp_to_give += 1

    def add_xp_to_player(self, xp_to_give):
        """
        Rozbita część funkcji add_experience. Żeby wszystko było czytelne.
        Funkcja sprawdza, czy gracz dostanie poziom.

        :param xp_to_give: Ilość xp'a do przyznania
        :type xp_to_give: int
        :return:
        """
        if self.experience >= self.experience_to_next_level[
            self.level]:  # Sprawdza, czy gracz ma wystarczająco doświadczenia, aby awansować
            self.level += 1  # Zwiększa poziom gracza
        else:
            self.experience += xp_to_give  # Dodaje doświadczenie do puli doświadczenia gracza
