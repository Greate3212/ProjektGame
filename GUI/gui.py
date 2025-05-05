import sys
import pygame

class GUI:
    """
    Klasa odpowiedzialna za tworzenie, odświeżanie i zamykanie okna GUI.
    """

    def __init__(self, window_name: str, width: int, height: int):
        """
        Inicjalizuje obiekt GUI.

        :param window_name: Nazwa okna GUI.
        :type window_name: str
        :param width: Początkowa szerokość okna GUI.
        :type width: int
        :param height: Początkowa wysokość okna GUI.
        :type height: int
        """
        self.window_name = window_name  # Nazwa okna
        self.width = width  # Szerokość okna
        self.height = height  # Wysokość okna
        self.running = False  # Czy GUI jest uruchomione?
        self.fullscreen = False  # Czy tryb pełnoekranowy jest włączony?
        self.screen = None  # Powierzchnia okna (tworzona w create_window)
        self.clock = pygame.time.Clock()  # Zegar do kontrolowania FPS

    def create_window(self) -> None:
        """
        Tworzy okno GUI o zadanych wymiarach i nazwie.
        """
        pygame.init()  # Inicjalizacja Pygame
        pygame.display.set_caption(self.window_name)  # Ustawienie nazwy okna
        self.screen = pygame.display.set_mode((self.width, self.height))  # Tworzenie okna
        self.running = True  # Ustawienie flagi uruchomienia

    def refresh_screen(self) -> None:
        """
        Odświeża całą powierzchnię okna.
        """
        pygame.display.flip()  # Aktualizacja ekranu
        self.clock.tick(60)  # Kontrola FPS (60 klatek na sekundę)

    def close_window(self) -> None:
        """
        Zamyka okno GUI i kończy działanie Pygame.
        """
        self.running = False  # Ustawienie flagi uruchomienia na False
        pygame.quit()  # Zamknięcie Pygame
        sys.exit()  # Zamknięcie programu

    def toggle_fullscreen(self, a) -> None:  # TODO: Dodać type hinting dla argumentu 'a' (event?)
        """
        Przełącza między trybem pełnoekranowym a oknem.
        """
        self.fullscreen = not self.fullscreen  # Zmiana stanu flagi fullscreen
        if self.fullscreen:
            # Ustawienie trybu pełnoekranowego
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            # Ustawienie trybu oknowego
            self.screen = pygame.display.set_mode((self.width, self.height))