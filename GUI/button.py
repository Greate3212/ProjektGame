# Import biblioteki odpowiedzialnej za GUI
import pygame


class Button:
    """
    Klasa odpowiedzialna za tworzenie przycisku
    """
    # Konstruktor
    def __init__(self, text, x, y, width, height, callback):
        """
        Inicjalizuje obiekt przycisku.

        :param text: Tekst wyświetlany na przycisku.
        :type text: str
        :param x: Pozycja x lewego górnego rogu przycisku.
        :type x: int
        :param y: Pozycja y lewego górnego rogu przycisku.
        :type y: int
        :param width: Szerokość przycisku.
        :type width: int
        :param height: Wysokość przycisku.
        :type height: int
        :param callback: Funkcja wywoływana po kliknięciu przycisku.
        :type callback: function
        """
        self.rect = pygame.Rect(x, y, width, height)  # Tworzy prostokąt reprezentujący obszar przycisku
        self.color = (100, 100, 250)  # Ustawia kolor przycisku (szary odcień niebieskiego)
        self.text = text  # Przechowuje tekst do wyświetlenia na przycisku
        self.font = pygame.font.SysFont(None, 36)  # Ustawia czcionkę tekstu
        self.callback = callback  # Przechowuje funkcję callback do wywołania po kliknięciu

    # "Rysowanie" przycisku
    def draw(self, surface):
        """
        Rysuje przycisk na danej powierzchni.

        :param surface: Powierzchnia, na której ma zostać narysowany przycisk.
        :type surface: pygame.Surface
        """
        pygame.draw.rect(surface, self.color, self.rect)  # Rysuje prostokąt wypełniony kolorem
        text_surf = self.font.render(self.text, True, (255, 255, 255))  # Renderuje tekst na powierzchni
        text_rect = text_surf.get_rect(center=self.rect.center)  # Wyśrodkowuje prostokąt tekstu na prostokącie przycisku
        surface.blit(text_surf, text_rect)  # Wyświetla tekst na powierzchni przycisku

    def handle_event(self, event):
        """
        Obsługuje zdarzenia związane z przyciskiem, takie jak kliknięcia myszy.

        :param event: Zdarzenie do obsłużenia.
        :type event: pygame.event.Event
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(
                event.pos):  # Sprawdza, czy nastąpiło kliknięcie myszy wewnątrz obszaru przycisku
            self.callback()  # Wywołuje funkcję callback, jeśli przycisk został kliknięty
