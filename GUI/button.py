import pygame

class Button:
    """
    Klasa odpowiedzialna za tworzenie przycisku
    """

    def __init__(self, text, x, y, width, height, callback, color=(134, 207, 146), hover_color_offset=30, clicked_color_offset=60):
        """
        Inicjalizuje obiekt przycisku.
        ...
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(None, 36)
        self.callback = callback
        self.is_pressed = False
        self.hovered = False  # Nowy atrybut
        self.base_color = color  # Zachowaj bazowy kolor
        self.hover_color_offset = hover_color_offset
        self.clicked_color_offset = clicked_color_offset

    def draw(self, surface):
        """
        Rysuje przycisk na danej powierzchni.
        ...
        """
        draw_color = self.color
        if self.hovered:
            draw_color = self.adjust_color(self.base_color, self.hover_color_offset) # Użyj self.base_color
            if self.is_pressed:
                draw_color = self.adjust_color(self.base_color, self.clicked_color_offset) # Użyj self.base_color
        pygame.draw.rect(surface, draw_color, self.rect)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        """
        Obsługuje zdarzenia związane z przyciskiem, takie jak kliknięcia myszy.
        """
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hovered = True
            else:
                self.hovered = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.is_pressed and self.rect.collidepoint(event.pos):
                self.callback()
                self.is_pressed = False
                return True
            else:
                self.is_pressed = False
        return False

    def adjust_color(self, color, offset):
        """
        Modyfikuje kolor, nie przekraczając zakresu 0-255.
        """
        r, g, b = color
        r = max(0, min(255, r - offset))
        g = max(0, min(255, g - offset))
        b = max(0, min(255, b - offset))
        return (r, g, b)