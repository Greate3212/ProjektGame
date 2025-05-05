import pygame

class Button:
    """
    Klasa reprezentująca przycisk w GUI.
    """

    def __init__(self, text: str, x: int, y: int, width: int, height: int,
                 callback: callable, color: tuple = (134, 207, 146),
                 hover_color_offset: int = 30, clicked_color_offset: int = 60):
        """
        Inicjalizuje obiekt przycisku.

        :param text: Tekst wyświetlany na przycisku.
        :type text: str
        :param x: Pozycja X lewego górnego rogu przycisku.
        :type x: int
        :param y: Pozycja Y lewego górnego rogu przycisku.
        :type y: int
        :param width: Szerokość przycisku.
        :type width: int
        :param height: Wysokość przycisku.
        :type height: int
        :param callback: Funkcja wywoływana po kliknięciu przycisku.
        :type callback: callable (funkcja bez argumentów)
        :param color: Kolor tła przycisku (domyślnie zielony).
        :type color: tuple (RGB)
        :param hover_color_offset: Offset koloru przy najechaniu myszą.
        :type hover_color_offset: int
        :param clicked_color_offset: Offset koloru przy kliknięciu.
        :type clicked_color_offset: int
        """
        self.rect = pygame.Rect(x, y, width, height)  # Prostokąt reprezentujący przycisk
        self.color = color  # Aktualny kolor przycisku
        self.text = text  # Tekst na przycisku
        self.font = pygame.font.SysFont(None, 36)  # Czcionka tekstu
        self.callback = callback  # Funkcja do wywołania po kliknięciu
        self.is_pressed = False  # Czy przycisk jest wciśnięty?
        self.hovered = False  # Czy mysz najechała na przycisk?
        self.base_color = color  # Bazowy kolor przycisku
        self.hover_color_offset = hover_color_offset  # Offset koloru przy najechaniu
        self.clicked_color_offset = clicked_color_offset  # Offset koloru przy kliknięciu

    def draw(self, surface: pygame.Surface) -> None:
        """
        Rysuje przycisk na danej powierzchni.

        :param surface: Powierzchnia, na której ma być narysowany przycisk.
        :type surface: pygame.Surface
        """
        draw_color = self.color  # Domyślnie użyjemy bazowego koloru

        if self.hovered:
            draw_color = self.adjust_color(self.base_color, self.hover_color_offset)  # Zmiana koloru przy najechaniu
            if self.is_pressed:
                draw_color = self.adjust_color(self.base_color, self.clicked_color_offset)  # Zmiana koloru przy kliknięciu

        pygame.draw.rect(surface, draw_color, self.rect)  # Rysowanie prostokąta przycisku
        text_surf = self.font.render(self.text, True, (255, 255, 255))  # Renderowanie tekstu
        text_rect = text_surf.get_rect(center=self.rect.center)  # Wyśrodkowanie tekstu
        surface.blit(text_surf, text_rect)  # Rysowanie tekstu na przycisku

    def handle_event(self, event: pygame.event.Event) -> bool:
        """
        Obsługuje zdarzenia związane z przyciskiem (najechanie, kliknięcie).

        :param event: Zdarzenie do obsłużenia.
        :type event: pygame.event.Event
        :return: True, jeśli zdarzenie zostało obsłużone, False w przeciwnym przypadku.
        :rtype: bool
        """
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)  # Sprawdza, czy mysz najechała
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Lewy przycisk myszy
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Lewy przycisk myszy
            if self.is_pressed and self.rect.collidepoint(event.pos):
                self.callback()  # Wywołanie funkcji callback
                self.is_pressed = False
                return True
            else:
                self.is_pressed = False
        return False

    def adjust_color(self, color: tuple, offset: int) -> tuple:
        """
        Modyfikuje kolor o dany offset (jaśniejszy lub ciemniejszy).

        :param color: Kolor do zmodyfikowania.
        :type color: tuple (RGB)
        :param offset: Wartość offsetu (dodatnia - jaśniejszy, ujemna - ciemniejszy).
        :type offset: int
        :return: Zmodyfikowany kolor.
        :rtype: tuple (RGB)
        """

        r, g, b = color
        r = max(0, min(255, r + offset))  # Ograniczenie do zakresu 0-255
        g = max(0, min(255, g + offset))
        b = max(0, min(255, b + offset))
        return r, g, b