# Import biblioteki odpowiedzialnej za GUI
import sys

import pygame


class GUI:
    """
    Klasa odpowiedzialna za tworzenie, odświeżanie i zamykanie GUI
    """

    # Konstruktor
    def __init__(self, window_name, width, height):
        """
        Inicjalizuje obiekt GUI.

        :param window_name: Nazwa okna GUI.
        :type window_name: str
        :param width: Szerokość okna GUI.
        :type width: int
        :param height: Wysokość okna GUI.
        :type height: int
        """
        self.window_name = window_name  # Przechowuje nazwę okna
        self.width = width  # Przechowuje szerokość okna
        self.height = height  # Przechowuje wysokość okna
        self.running = False  # Flaga wskazująca, czy GUI jest uruchomione

        # Tworzenie pustych zmiennych, które są przypisywane potem w create window
        self.screen = None  # Powierzchnia okna (będzie utworzona później)
        self.clock = pygame.time.Clock()  # Obiekt zegara do kontrolowania liczby klatek na sekundę

    def create_window(self):
        """
        Funkcja odpowiedzialna za tworzenie okna, o odpowiednich zmiennych/ustawieniach
        :return:
        """
        pygame.init()  # Inicjalizuje bibliotekę Pygame
        pygame.display.set_caption(self.window_name)  # Ustawia tytuł okna
        self.screen = pygame.display.set_mode((self.width, self.height))  # Tworzy okno o podanych wymiarach
        self.clock = pygame.time.Clock()  # Inicjalizuje zegar
        self.running = True  # Ustawia flagę uruchomienia na True, wskazując, że GUI jest uruchomione

    def refresh_screen(self):
        """
        Funkcja odpowiedzialna za odświeżanie okna.
        Odświeża okno, za każdym razem, gdy coś zostanie dodane do okna, trzeba go odświeżyć.
        :return:
        """
        pygame.display.flip()  # Aktualizuje całą powierzchnię okna
        self.clock.tick(60)  # Kontroluje liczbę klatek na sekundę (FPS) na 60

    def close_window(self):
        """
        Funkcja odpowiedzialna za zamykanie okna.
        :return:
        """
        self.running = False  # Ustawia flagę uruchomienia na False, wskazując, że GUI ma zostać zamknięte
        pygame.quit()  # Zamyka bibliotekę Pygame
        sys.exit() # Wyłącza grę
