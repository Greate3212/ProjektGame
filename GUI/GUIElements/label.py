import pygame
from typing import Optional, Tuple

pygame.init()  # Inicjalizacja Pygame (raz wystarczy, ale dla pewności zostawiam)

class Label:
    """
    Klasa odpowiedzialna za wyświetlanie tekstu (etykiety) na ekranie.
    """

    def __init__(self, text: str, x: int, y: int, width: int = 0, height: int = 0,
                 color: Tuple[int, int, int] = (255, 255, 255),
                 font_size: int = 36, font_name: Optional[str] = None):
        """
        Inicjalizuje obiekt Label.

        :param text: Tekst do wyświetlenia.
        :type text: str
        :param x: Początkowa pozycja X lewego górnego rogu tekstu.
        :type x: int
        :param y: Początkowa pozycja Y lewego górnego rogu tekstu.
        :type y: int
        :param width: Szerokość obszaru tekstu (opcjonalne, 0 - automatyczna szerokość).
        :type width: int
        :param height: Wysokość obszaru tekstu (opcjonalne, 0 - automatyczna wysokość).
        :type height: int
        :param color: Kolor tekstu w formacie RGB (R, G, B). Domyślnie biały.
        :type color: Tuple[int, int, int]
        :param font_size: Rozmiar czcionki. Domyślnie 36.
        :type font_size: int
        :param font_name: Nazwa czcionki. Domyślnie None (czcionka systemowa).
        :type font_name: Optional[str]
        """
        self.text: str = text
        self.x: int = x
        self.y: int = y
        self.color: Tuple[int, int, int] = color
        self.font: pygame.font.Font = pygame.font.SysFont(font_name, font_size)
        self.text_surface: pygame.Surface = self.font.render(self.text, True, self.color)  # Renderowanie tekstu
        self.text_rect: pygame.Rect = self.text_surface.get_rect()
        self.width: int = width
        self.height: int = height
        if width > 0 and height > 0:
            self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
            self.text_rect.center: Tuple[int, int] = (x + width // 2, y + height // 2)  # Centrowanie początkowe
        else:
            self.text_rect.topleft: Tuple[int, int] = (x, y)  # Ustawienie pozycji tekstu

    def draw(self, surface: pygame.Surface) -> None:
        """
        Rysuje tekst na danej powierzchni.

        :param surface: Powierzchnia, na której ma zostać narysowany tekst.
        :type surface: pygame.Surface
        """
        if self.width > 0 and self.height > 0:
            pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)  # Rysowanie ramki (opcjonalne)
        surface.blit(self.text_surface, self.text_rect)  # Wyświetlanie tekstu na powierzchni

    def handle_event(self, event: pygame.event.Event) -> None:  # Label nie reaguje na zdarzenia
        """
        Pusta metoda handle_event.  Label nie reaguje na zdarzenia, więc nic tu nie robimy.

        :param event: Zdarzenie do obsłużenia (nieużywane).
        :type event: pygame.event.Event
        """
        pass

    def center_text(self) -> None:
        """
        Centruje tekst wewnątrz obszaru labela (jeśli zdefiniowano width i height).
        """
        if self.width > 0 and self.height > 0:
            self.text_rect.center = self.rect.center

    def change_text(self, new_text: str) -> None:
        """
        Ustawia nowy tekst dla label. Przydatne, gdy chcesz go zmieniać
        w trakcie działania programu.

        :param new_text: Nowy tekst.
        :type new_text: str
        """
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.color)  # Trzeba przenderować tekst
        self.text_rect = self.text_surface.get_rect()
        if self.width > 0 and self.height > 0:
            self.center_text()
        else:
            self.text_rect.topleft = (self.x, self.y)  # Upewniamy się, że pozycja jest ok

    def change_position(self, new_x: int, new_y: int) -> None:
        """
        Zmienia pozycję label.

        :param new_x: Nowa pozycja X.
        :type new_x: int
        :param new_y: Nowa pozycja Y.
        :type new_y: int
        """
        self.x = new_x
        self.y = new_y
        if self.width > 0 and self.height > 0:
            self.rect.topleft = (new_x, new_y)  # Zmieniamy pozycję prostokąta
            self.center_text()  # i centrujemy tekst
        else:
            self.text_rect.topleft = (self.x, self.y)

    def change_color(self, new_color: Tuple[int, int, int]) -> None:
        """
        Zmienia kolor tekstu.

        :param new_color: Nowy kolor w formacie RGB.
        :type new_color: Tuple[int, int, int]
        """
        self.color = new_color
        self.text_surface = self.font.render(self.text, True, self.color)  # Trzeba przenderować tekst z nowym kolorem

    def change_font_size(self, new_font_size: int) -> None:
        """
        Zmienia rozmiar czcionki.

        :param new_font_size: Nowy rozmiar czcionki.
        :type new_font_size: int
        """
        self.font = pygame.font.SysFont(None, new_font_size)
        self.text_surface = self.font.render(self.text, True, self.color)  # Trzeba przenderować tekst z nowym rozmiarem

    def change_font(self, new_font_name: str) -> None:
        """
        Zmienia czcionkę.

        :param new_font_name: Nazwa nowej czcionki.
        :type new_font_name: str
        """
        self.font = pygame.font.SysFont(new_font_name, self.font.get_height())
        self.text_surface = self.font.render(self.text, True, self.color)