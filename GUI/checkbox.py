import pygame

class Checkbox:
    """
    Klasa reprezentująca checkbox w GUI.
    """

    def __init__(self, text: str, x: int, y: int, size: int = 20,
                 color: tuple = (255, 255, 255), checked_color: tuple = (0, 255, 0),
                 font_size: int = 36, font_name: str = None, initial_checked: bool = False):
        """
        Inicjalizuje obiekt checkboxa.

        :param text: Tekst wyświetlany obok checkboxa.
        :type text: str
        :param x: Pozycja X lewego górnego rogu checkboxa.
        :type x: int
        :param y: Pozycja Y lewego górnego rogu checkboxa.
        :type y: int
        :param size: Rozmiar boku kwadratu checkboxa (domyślnie 20).
        :type size: int
        :param color: Kolor obramowania i tekstu (domyślnie biały).
        :type color: tuple (RGB)
        :param checked_color: Kolor wypełnienia, gdy checkbox jest zaznaczony (domyślnie zielony).
        :type checked_color: tuple (RGB)
        :param font_size: Rozmiar czcionki tekstu (domyślnie 36).
        :type font_size: int
        :param font_name: Nazwa czcionki (domyślnie None - czcionka systemowa).
        :type font_name: str
        :param initial_checked: Początkowy stan zaznaczenia (domyślnie False).
        :type initial_checked: bool
        """
        self.rect = pygame.Rect(x, y, size, size)  # Prostokąt reprezentujący checkbox
        self.color = color  # Kolor obramowania i tekstu
        self.checked_color = checked_color  # Kolor wypełnienia
        self.font = pygame.font.SysFont(font_name, font_size)  # Czcionka tekstu
        self.text_surface = self.font.render(text, True, color)  # Renderowanie tekstu
        self.text_rect = self.text_surface.get_rect(midleft=(x + size + 5, y + size // 2))  # Pozycja tekstu
        self.checked = initial_checked  # Czy checkbox jest zaznaczony?
        self.is_pressed = False  # Czy checkbox jest wciśnięty?
        self.callback = None  # Funkcja callback do wywołania przy zmianie stanu

    def draw(self, surface: pygame.Surface) -> None:
        """
        Rysuje checkbox na danej powierzchni.

        :param surface: Powierzchnia, na której ma być narysowany checkbox.
        :type surface: pygame.Surface
        """
        pygame.draw.rect(surface, self.color, self.rect, 2)  # Rysowanie obramowania
        if self.checked:
            pygame.draw.rect(surface, self.checked_color, self.rect)  # Rysowanie wypełnienia
        surface.blit(self.text_surface, self.text_rect)  # Rysowanie tekstu

    def handle_event(self, event: pygame.event.Event) -> bool:
        """
        Obsługuje zdarzenia związane z checkboxem (kliknięcia).

        :param event: Zdarzenie do obsłużenia.
        :type event: pygame.event.Event
        :return: True, jeśli zdarzenie zostało obsłużone, False w przeciwnym przypadku.
        :rtype: bool
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Lewy przycisk myszy
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Lewy przycisk myszy
            if self.is_pressed and self.rect.collidepoint(event.pos):
                self.checked = not self.checked  # Zmiana stanu zaznaczenia
                if self.callback:  # Wywołanie callback, jeśli istnieje
                    self.callback(self.checked)  # Przekazujemy aktualny stan
                self.is_pressed = False
                return True
            else:
                self.is_pressed = False
        elif event.type == pygame.MOUSEMOTION:
            if not self.rect.collidepoint(event.pos):
                self.is_pressed = False
        return False

    def set_callback(self, callback: callable) -> None:
        """
        Ustawia funkcję callback, która ma być wywołana przy zmianie stanu checkboxa.

        :param callback: Funkcja callback.
        :type callback: callable (funkcja z jednym argumentem - bool)
        """
        self.callback = callback