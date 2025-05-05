from typing import List, Tuple, Optional, Callable

import pygame


class Dropdown:
    """
    Klasa reprezentująca listę rozwijaną w GUI.
    """

    def __init__(self, options: List[str], x: int, y: int, width: int, height: int,
                 font_size: int = 24, font_name: Optional[str] = None,
                 color: Tuple[int, int, int] = (255, 255, 255),
                 background_color: Tuple[int, int, int] = (50, 50, 50),
                 selected_option_callback: Optional[Callable[[str], None]] = None):
        """
        Inicjalizuje listę rozwijaną.

        :param options: Lista opcji do wyboru (teksty).
        :type options: List[str]
        :param x: Pozycja X lewego górnego rogu listy.
        :type x: int
        :param y: Pozycja Y lewego górnego rogu listy.
        :type y: int
        :param width: Szerokość listy.
        :type width: int
        :param height: Wysokość pojedynczego elementu listy.
        :type height: int
        :param font_size: Rozmiar czcionki.
        :type font_size: int
        :param font_name: Nazwa czcionki (opcjonalnie).
        :type font_name: Optional[str]
        :param color: Kolor tekstu.
        :type color: Tuple[int, int, int] (RGB)
        :param background_color: Kolor tła listy.
        :type background_color: Tuple[int, int, int] (RGB)
        :param selected_option_callback: Funkcja wywoływana przy wyborze opcji.
               Argumentem tej funkcji będzie wybrany tekst (str).
        :type selected_option_callback: Optional[Callable[[str], None]]
        """
        self.options: List[str] = options
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.font: pygame.font.Font = pygame.font.SysFont(font_name, font_size)
        self.color: Tuple[int, int, int] = color
        self.background_color: Tuple[int, int, int] = background_color
        self.selected_option: str = options[0] if options else ""  # Domyślnie pierwsza opcja
        self.is_open: bool = False
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
        self.selected_option_callback: Optional[Callable[[str], None]] = selected_option_callback

    def draw(self, surface: pygame.Surface) -> None:
        """
        Rysuje listę rozwijaną na danej powierzchni.

        :param surface: Powierzchnia, na której ma być narysowana lista.
        :type surface: pygame.Surface
        """

        # Rysowanie głównego prostokąta (wybrana opcja)
        pygame.draw.rect(surface, self.background_color, self.rect)
        text_surface = self.font.render(self.selected_option, True, self.color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

        # Rysowanie opcji, gdy lista jest rozwinięta
        if self.is_open:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.x, self.y + (i + 1) * self.height, self.width, self.height)
                pygame.draw.rect(surface, self.background_color, option_rect)
                text_surface = self.font.render(option, True, self.color)
                text_rect = text_surface.get_rect(center=option_rect.center)
                surface.blit(text_surface, text_rect)

    def set_selected_option(self, option: str):
        if option in self.options:
            print(f"Dropdown: Ustawiam selected_option na: {option}")  # Debug!
            self.selected_option = option
        else:
            print(f"Dropdown: Ostrzeżenie: Opcja '{option}' nie istnieje: {option}")

    def handle_event(self, event: pygame.event.Event) -> bool:
        """
        Obsługuje zdarzenia związane z listą rozwijaną (kliknięcia myszy).

        :param event: Zdarzenie do obsłużenia.
        :type event: pygame.event.Event
        :return: True, jeśli zdarzenie zostało obsłużone, False w przeciwnym przypadku.
        :rtype: bool
        """

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_open = not self.is_open  # Otwórz/zamknij listę
                return True
            elif self.is_open:
                # Sprawdzenie, czy kliknięto którąś z opcji
                for i in range(len(self.options)):
                    option_rect = pygame.Rect(self.x, self.y + (i + 1) * self.height, self.width, self.height)
                    if option_rect.collidepoint(event.pos):
                        self.selected_option = self.options[i]
                        self.is_open = False
                        if self.selected_option_callback:
                            self.selected_option_callback(self.selected_option)  # Wywołanie callback
                        return True
                self.is_open = False  # Zamknij listę, jeśli kliknięto poza opcjami
                return True
        return False
