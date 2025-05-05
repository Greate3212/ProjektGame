from GUI.button import Button
from GUI.checkbox import Checkbox
from GUI.gui import GUI
from GUI.label import Label
from typing import List, Tuple, Optional, Callable
import pygame


class GUIHandler:
    """
    Klasa odpowiedzialna za zarządzanie elementami GUI (przyciski, etykiety, checkbox-y).
    """

    def __init__(self, gui: GUI):
        """
        Inicjalizuje obiekt GUIHandler.

        :param gui: Obiekt GUI, którym zarządza ten handler.
        :type gui: GUI
        """
        self.gui: GUI = gui  # Przechowuje referencję do obiektu GUI
        self.buttons: List[Button] = []  # Lista przycisków
        self.labels: List[Label] = []  # Lista etykiet
        self.checkboxes: List[Checkbox] = []  # Lista checkbox-ów

    def add_label(self, text: str, x: int, y: int, width: int = 0, height: int = 0,
                  color: Tuple[int, int, int] = (255, 255, 255),
                  font_size: int = 36, font_name: Optional[str] = None) -> None:
        """
        Dodaje nową etykietę (label) do GUI.

        :param text: Tekst etykiety.
        :type text: str
        :param x: Pozycja X lewego górnego rogu etykiety.
        :type x: int
        :param y: Pozycja Y lewego górnego rogu etykiety.
        :type y: int
        :param width: Szerokość etykiety (opcjonalne, 0 - automatyczna szerokość).
        :type width: int
        :param height: Wysokość etykiety (opcjonalne, 0 - automatyczna wysokość).
        :type height: int
        :param color: Kolor tekstu w formacie RGB. Domyślnie biały.
        :type color: Tuple[int, int, int]
        :param font_size: Rozmiar czcionki. Domyślnie 36.
        :type font_size: int
        :param font_name: Nazwa czcionki. Domyślnie None (czcionka systemowa).
        :type font_name: Optional[str]
        """
        label = Label(text, x, y, width, height, color, font_size, font_name)
        self.labels.append(label)

    def add_button(self, text: str, x: int, y: int, width: int, height: int,
                   callback: Callable[[], None]) -> None:
        """
        Dodaje nowy przycisk do GUI.

        :param text: Tekst przycisku.
        :type text: str
        :param x: Pozycja X lewego górnego rogu przycisku.
        :type x: int
        :param y: Pozycja Y lewego górnego rogu przycisku.
        :type y: int
        :param width: Szerokość przycisku.
        :type width: int
        :param height: Wysokość przycisku.
        :type height: int
        :param callback: Funkcja wywoływana po kliknięciu przycisku (bez argumentów).
        :type callback: Callable[[], None]
        """
        btn = Button(text, x, y, width, height, callback)
        self.buttons.append(btn)

    def add_checkbox(self, text: str, x: int, y: int, size: int = 20,
                     color: Tuple[int, int, int] = (255, 255, 255),
                     checked_color: Tuple[int, int, int] = (0, 255, 0),
                     font_size: int = 36, font_name: Optional[str] = None,
                     initial_checked: bool = False,
                     callback: Optional[Callable[[bool], None]] = None) -> None:
        """
        Dodaje nowy checkbox do GUI.

        :param text: Tekst wyświetlany obok checkboxa.
        :type text: str
        :param x: Pozycja X lewego górnego rogu checkboxa.
        :type x: int
        :param y: Pozycja Y lewego górnego rogu checkboxa.
        :type y: int
        :param size: Rozmiar checkboxa (domyślnie 20).
        :type size: int
        :param color: Kolor obramowania i tekstu. Domyślnie biały.
        :type color: Tuple[int, int, int]
        :param checked_color: Kolor zaznaczonego checkboxa. Domyślnie zielony.
        :type checked_color: Tuple[int, int, int]
        :param font_size: Rozmiar czcionki tekstu. Domyślnie 36.
        :type font_size: int
        :param font_name: Nazwa czcionki. Domyślnie None (czcionka systemowa).
        :type font_name: Optional[str]
        :param initial_checked: Początkowy stan checkboxa. Domyślnie False.
        :type initial_checked: bool
        :param callback: Funkcja wywoływana przy zmianie stanu checkboxa (opcjonalne).
        :type callback: Optional[Callable[[bool], None]] (funkcja z jednym argumentem - bool)
        """
        checkbox = Checkbox(text, x, y, size, color, checked_color, font_size,
                            font_name, initial_checked)
        checkbox.set_callback(callback)  # Ustawiamy callback
        self.checkboxes.append(checkbox)  # Dodajemy checkbox do listy

    def clear_all(self) -> None:
        """
        Usuwa wszystkie elementy GUI.
        """
        self.buttons.clear()
        self.labels.clear()
        self.checkboxes.clear()

    def draw_all(self) -> None:
        """
        Rysuje wszystkie elementy GUI na ekranie GUI.
        """
        for button in self.buttons:
            button.draw(self.gui.screen)
        for label in self.labels:
            label.draw(self.gui.screen)
        for checkbox in self.checkboxes:  # Iterujemy po checkboxach
            checkbox.draw(self.gui.screen)  # Rysujemy każdy checkbox

    def handle_events(self, event: pygame.event.Event) -> None:
        """
        Obsługuje zdarzenia dla wszystkich elementów GUI.

        :param event: Zdarzenie do obsłużenia.
        :type event: pygame.event.Event
        """
        for button in self.buttons:
            button.handle_event(event)
        for checkbox in self.checkboxes:  # Iterujemy po checkboxach
            checkbox.handle_event(event)  # Obsługujemy zdarzenia dla checkboxów