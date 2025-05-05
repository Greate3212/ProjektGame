import pygame

from GUI.guihandler import GUIHandler, GUI


def start():
    """
    Funkcja odpowiedzialna za inicjalizowanie startu gry.
    W funkcji tej są uruchamiane wszystkie wymagane procesy/klasy do uruchomienia gry.
    :return:
    """
    gui = GUI("Game", 800, 600)  # Tworzy obiekt GUI (okno gry) o nazwie "Game" i wymiarach 800x600
    return gui  # Zwraca utworzony obiekt GUI


def game_start():
    print("START!")  # Wypisuje "START!" na konsoli - Placeholder dla logiki uruchamiania gry


if __name__ == "__main__":
    # Tworzenie okna
    window = start()  # Wywołuje funkcję start() w celu utworzenia okna gry
    window.create_window()  # Wywołuje metodę create_window() obiektu GUI, aby utworzyć okno

    # Obiekt odpowiedzialny za elementy GUI
    handler = GUIHandler(window)  # Tworzy obiekt GUIHandler, który zarządza elementami GUI w oknie

    # Dodawnie elemntów GUI
    start = handler.add_button("Start", 100, 100, 100, 100,
                              game_start)  # Dodaje przycisk "Start" do GUIHandler. Po kliknięciu wywoływana jest funkcja game_start

    # Główna pętla gry
    while window.running:  # Pętla trwa, dopóki okno gry jest uruchomione

        # Sprawdzanie eventów/zdarzeń w grze. Jeżeli użytkownik coś kliknie, przesunie myszką, etc.
        # To tutaj są przechowywane informacje na ten temat
        for event in pygame.event.get():  # Pobiera listę wszystkich zdarzeń, które wystąpiły od ostatniej iteracji pętli

            # Sprawdzanie, czy event, jaki wywołał gracz, to wyłączenie gry.
            if event.type == pygame.QUIT:  # Sprawdza, czy użytkownik zamknął okno
                # Uruchomienie funkcji wyłączającej gry
                window.close_window()  # Wywołuje metodę close_window() obiektu GUI, aby zamknąć okno

            # Sprawdza, czy elementy GUI są wciskane.
            handler.handle_events(event)  # Przekazuje zdarzenie do GUIHandler, który obsługuje zdarzenia dla elementów GUI (np. przycisków)

        # "Rysowanie" przycisków
        handler.draw_all()  # Wywołuje metodę draw_all() obiektu GUIHandler, aby narysować wszystkie elementy GUI (np. przyciski) na ekranie

        # Odświeżanie ekranu
        window.refresh_screen()  # Wywołuje metodę refresh_screen() obiektu GUI, aby odświeżyć ekran i wyświetlić zmiany
