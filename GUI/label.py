import pygame

pygame.init()  # Inicjalizacja Pygame



class Label:
    """
    Klasa odpowiedzialna za wyświetlanie tekstu (label) na ekranie.
    """

    def __init__(self, text, x, y, width=0, height=0, color=(255, 255, 255),
                 font_size=36, font_name=None):
        """
        Inicjalizuje obiekt label.

        :param text: Tekst do wyświetlenia.
        :type text: str
        :param x: Początkowa pozycja x lewego górnego rogu tekstu.
        :type x: int
        :param y: Początkowa pozycja y lewego górnego rogu tekstu.
        :type y: int
        :param width: Szerokość obszaru tekstu (opcjonalne).
        :type width: int
        :param height: Wysokość obszaru tekstu (opcjonalne).
        :type height: int
        :param color: Kolor tekstu w formacie RGB (R, G, B). Domyślnie biały.
        :type color: tuple
        :param font_size: Rozmiar czcionki. Domyślnie 36.
        :type font_size: int
        :param font_name: Nazwa czcionki. Domyślnie None (czcionka systemowa).
        :type font_name: str
        """
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.text_surface = self.font.render(self.text, True,
                                             self.color)  # Renderowanie tekstu
        self.text_rect = self.text_surface.get_rect()
        self.width = width
        self.height = height
        if width > 0 and height > 0:
            self.rect = pygame.Rect(x, y, width, height)
            self.text_rect.center = (x + width // 2,
                                     y + height // 2)  # Centrowanie początkowe
        else:
            self.text_rect.topleft = (x, y)  # Ustawienie pozycji tekstu

    def draw(self, surface):
        """
        Rysuje tekst na danej powierzchni.

        :param surface: Powierzchnia, na której ma zostać narysowany tekst.
        :type surface: pygame.Surface
        """
        if self.width > 0 and self.height > 0:
            pygame.draw.rect(surface, (0, 0, 0),
                             self.rect, 1)  # Rysowanie ramki (opcjonalne)
        surface.blit(self.text_surface,
                     self.text_rect)  # Wyświetlanie tekstu na powierzchni

    def handle_event(self,
                     event):  # Metoda handle_event nie jest już potrzebna, ale zostawiam ją.
        """
        Pusta metoda handle_event.  Label nie reaguje na zdarzenia.
        """
        pass

    def center_text(self):
        """
        Centruje tekst wewnątrz obszaru labela.
        """
        if self.width > 0 and self.height > 0:
            self.text_rect.center = self.rect.center

    def change_text(self, new_text):
        """
        Ustawia nowy tekst dla label. Przydatne, jak chcesz go zmieniać
        w trakcie działania programu.
        :param new_text: Nowy tekst
        :type new_text: str
        """
        self.text = new_text
        self.text_surface = self.font.render(self.text, True,
                                             self.color)  # Trzeba przenderować tekst
        self.text_rect = self.text_surface.get_rect()
        if self.width > 0 and self.height > 0:
            self.center_text()
        else:
            self.text_rect.topleft = (self.x, self.y)  # Upewniamy się, że pozycja jest ok

    def change_position(self, new_x, new_y):
        """
        Zmienia pozycję label.
        :param new_x: Nowa pozycja X
        :type new_x: int
        :param new_y: Nowa pozycja Y
        :type new_y: int
        """
        self.x = new_x
        self.y = new_y
        if self.width > 0 and self.height > 0:
            self.rect.topleft = (new_x, new_y)  # Zmieniamy pozycję prostokąta
            self.center_text()  # i centrujemy tekst
        else:
            self.text_rect.topleft = (self.x, self.y)

    def change_color(self, new_color):
        """
        Zmienia kolor tekstu
        :param new_color: Nowy kolor w formacie RGB
        :type new_color: tuple
        """
        self.color = new_color
        self.text_surface = self.font.render(self.text, True,
                                             self.color)  # Trzeba przenderować tekst z nowym kolorem

    def change_font_size(self, new_font_size):
        """
        Zmienia rozmiar czcionki
        :param new_font_size: Nowy rozmiar czcionki
        :type new_font_size: int
        """
        self.font = pygame.font.SysFont(None, new_font_size)
        self.text_surface = self.font.render(self.text, True,
                                             self.color)  # Trzeba przenderować tekst z nowym rozmiarem

    def change_font(self, new_font_name):
        """
        Zmienia czcionkę
        :param new_font_name: Nazwa nowej czcionki
        :type new_font_name: str
        """
        self.font = pygame.font.SysFont(new_font_name,
                                         self.font.get_height())
        self.text_surface = self.font.render(self.text, True, self.color)
