from GUI.gui import GUI
from GUI.button import Button


class GUIHandler:
    def __init__(self, gui: GUI):
        """
        Inicjalizuje obiekt GUIHandler.

        :param gui: Obiekt GUI, którym zarządza ten handler.
        :type gui: GUI
        """
        self.gui = gui  # Przechowuje referencję do obiektu GUI
        self.buttons = []  # Tworzy pustą listę do przechowywania obiektów Button

    def add_button(self, text, x, y, width, height, callback):
        """
        Dodaje nowy przycisk do GUI.

        :param text: Tekst na przycisku.
        :type text: str
        :param x: Pozycja x przycisku.
        :type x: int
        :param y: Pozycja y przycisku.
        :type y: int
        :param width: Szerokość przycisku.
        :type width: int
        :param height: Wysokość przycisku.
        :type height: int
        :param callback: Funkcja wywoływana po kliknięciu przycisku.
        :type callback: function
        """
        btn = Button(text, x, y, width, height, callback)  # Tworzy nowy obiekt Button
        self.buttons.append(btn)  # Dodaje przycisk do listy przycisków

    def draw_all(self):
        """
        Rysuje wszystkie przyciski na ekranie GUI.
        """
        for button in self.buttons:  # Iteruje przez listę przycisków
            button.draw(self.gui.screen)  # Wywołuje metodę draw() każdego przycisku, aby go narysować

    def handle_events(self, event):
        """
        Obsługuje zdarzenia dla wszystkich przycisków.

        :param event: Zdarzenie do obsłużenia.
        :type event: pygame.event.Event
        """
        for button in self.buttons:  # Iteruje przez listę przycisków
            button.handle_event(event)  # Wywołuje metodę handle_event() każdego przycisku, aby obsłużyć zdarzenie
