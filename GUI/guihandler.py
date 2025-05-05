from GUI.GUIElements.button import Button
from GUI.GUIElements.checkbox import Checkbox
from GUI.gui import GUI
from GUI.GUIElements.label import Label
from GUI.GUIElements.dropdown import Dropdown  # Import Dropdown
from typing import List, Tuple, Optional, Callable
import pygame

class GUIHandler:
    """
    Klasa odpowiedzialna za zarządzanie elementami GUI (przyciski, etykiety, checkbox-y, dropdowny).
    """

    def __init__(self, gui: GUI):
        """
        Inicjalizuje obiekt GUIHandler.

        :param gui: Obiekt GUI, którym zarządza ten handler.
        :type gui: GUI
        """
        self.gui: GUI = gui
        self.buttons: List[Button] = []
        self.labels: List[Label] = []
        self.checkboxes: List[Checkbox] = []
        self.dropdowns: List[Dropdown] = []  # Dodajemy listę dropdownów

    def add_label(self, text: str, x: int, y: int, width: int = 0, height: int = 0,
                  color: Tuple[int, int, int] = (255, 255, 255),
                  font_size: int = 36, font_name: Optional[str] = None) -> None:
        """
        Dodaje nową etykietę (label) do GUI.
        """
        label = Label(text, x, y, width, height, color, font_size, font_name)
        self.labels.append(label)

    def add_button(self, text: str, x: int, y: int, width: int, height: int,
                   callback: Callable[[], None]) -> None:
        """
        Dodaje nowy przycisk do GUI.
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
        """
        checkbox = Checkbox(text, x, y, size, color, checked_color, font_size,
                            font_name, initial_checked)
        checkbox.set_callback(callback)
        self.checkboxes.append(checkbox)

    def add_dropdown(self, options: List[str], x: int, y: int, width: int, height: int,
                     font_size: int = 24, font_name: Optional[str] = None,
                     color: Tuple[int, int, int] = (255, 255, 255),
                     background_color: Tuple[int, int, int] = (50, 50, 50),
                     selected_option_callback: Optional[Callable[[str], None]] = None) -> None:
        """
        Dodaje nową listę rozwijaną do GUI.

        :param options: Lista opcji do wyboru.
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
        :type color: Tuple[int, int, int]
        :param background_color: Kolor tła listy.
        :type background_color: Tuple[int, int, int]
        :param selected_option_callback: Funkcja wywoływana przy wyborze opcji.
               Argumentem tej funkcji będzie wybrany tekst (str).
        :type selected_option_callback: Optional[Callable[[str], None]]
        """
        dropdown = Dropdown(options, x, y, width, height, font_size, font_name,
                            color, background_color, selected_option_callback)
        self.dropdowns.append(dropdown)
        return dropdown

    def clear_all(self) -> None:
        """
        Usuwa wszystkie elementy GUI.
        """
        self.buttons.clear()
        self.labels.clear()
        self.checkboxes.clear()
        self.dropdowns.clear()  # Czyścimy również dropdowny

    def draw_all(self) -> None:
        """
        Rysuje wszystkie elementy GUI na ekranie GUI.
        """
        for button in self.buttons:
            button.draw(self.gui.screen)
        for label in self.labels:
            label.draw(self.gui.screen)
        for checkbox in self.checkboxes:
            checkbox.draw(self.gui.screen)
        for dropdown in self.dropdowns:  # Rysujemy dropdowny
            dropdown.draw(self.gui.screen)

    def handle_events(self, event: pygame.event.Event) -> None:
        """
        Obsługuje zdarzenia dla wszystkich elementów GUI.
        """
        for button in self.buttons:
            button.handle_event(event)
        for checkbox in self.checkboxes:
            checkbox.handle_event(event)
        for dropdown in self.dropdowns:  # Obsługujemy zdarzenia dla dropdownów
            dropdown.handle_event(event)