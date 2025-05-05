import pygame


class GUI:
    """
    Klasa odpowiedzialna za tworzenie, odświeżanie i zamykanie GUI
    """

    # Konstruktor
    def __init__(self, window_name, width, height):
        self.window_name = window_name
        self.width = width
        self.height = height
        self.running = False

    def create_window(self):
        """
        Funkcja odpowiedzialna za tworzenie okna, o odpowiednich zmiennych/ustawieniach
        :return:
        """
        pygame.init()
        pygame.display.set_caption(self.window_name)
        screen = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()
        self.running = True

    @staticmethod
    def refresh_screen():
        """
        Funkcja odpowiedzialna za odświeżanie okna, za każdym razem, gdy coś zostanie dodane do okna, trzeba go odświeżyć.
        :return:
        """
        pygame.display.flip()

    def close_window(self):
        """
        Funkcja odpowiedzialna za zamykanie okna.
        :return:
        """
        self.running = False
        pygame.quit()
