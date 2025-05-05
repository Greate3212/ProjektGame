from GUI.gui import GUI
from GUI.button import Button
from GUI.label import Label


class GUIHandler:
    def __init__(self, gui: GUI):
        """
        Inicjalizuje obiekt GUIHandler.

        :param gui: Obiekt GUI, którym zarządza ten handler.
        :type gui: GUI
        """
        self.gui = gui  # Przechowuje referencję do obiektu GUI
        self.buttons = []  # Tworzy pustą listę do przechowywania obiektów Button
        self.labels = [] # Tworzy pustą listę do przechowywania obiektów Label


    def add_label(self, text, x, y, width=0, height=0, color=(255, 255, 255), font_size=36, font_name=None):
        """
        Dodaje nowy label do GUI.

        :param text: Tekst do wyświetlenia.
        :type text: str
        :param x: Pozycja x lewego górnego rogu tekstu.
        :type x: int
        :param y: Pozycja y lewego górnego rogu tekstu.
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
        label = Label(text, x, y, width, height, color, font_size, font_name)
        self.labels.append(label)  # Dodaje do listy labeli


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
        Rysuje wszystkie elementy GUI na ekranie GUI.
        """
        for button in self.buttons:
            button.draw(self.gui.screen)
        for label in self.labels:
            label.draw(self.gui.screen)

    def handle_events(self, event):
        """
        Obsługuje zdarzenia dla wszystkich przycisków.

        :param event: Zdarzenie do obsłużenia.
        :type event: pygame.event.Event
        """
        for button in self.buttons:  # Iteruje przez listę przycisków
            button.handle_event(event)  # Wywołuje metodę handle_event() każdego przycisku, aby obsłużyć zdarzenie
