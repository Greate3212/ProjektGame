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


opened = 0
"""
Opened - zmienna przechowująca informacje jakie okno aktualnie jest otwarte:
 - 0 - main menu
 - 1 - settings
"""
m_created = False
s_created = False

def main_menu():
    global opened, m_created
    opened = 0

    if not m_created:
        # Funkcja/okienko menu głównego oraz jego wszystkie elementy
        main_menu_handler.add_label("Project Game", get_center_x(150), (600 - 100) - 450, 150, 80, font_size=55,
                                    font_name="Comic Sans MS")

        main_menu_handler.add_button("Start", get_center_x(200), (600 - 100) - 200, 200, 100,
                                     game_start)  # Dodaje przycisk "Start" do GUIHandler. Po kliknięciu wywoływana jest funkcja game_start
        main_menu_handler.add_button("Settings", get_center_x(200), (600 - 90) - 100, 200, 90, settings)
        main_menu_handler.add_button("Exit", get_center_x(200), (600 - 80) - 10, 200, 80, window.close_window)

        main_menu_handler.add_label("v0.0.1", get_center_x(50) + 400 - 20, (600 - 20), 50, 25, font_size=15,
                                    font_name="Corbel")
        m_created = True
    else:
        pass


def game_start():
    # Funkcja wywoływana po wciśnięciu przycisku 'start' w menu głównym
    print("START!")


def settings():
    global opened, s_created
    opened = 1
    # Funkcja wywoływana po wsciśnięciu przycisku 'settings' w menu głównym

    if not s_created:
        settings_handler.add_label("Settings", get_center_x(150), (600 - 550), 150, 100, font_size=55,
                                   font_name="Comic Sans MS")
        settings_handler.add_button("Back", get_center_x(150), (600 - 80), 150, 70, main_menu)
        s_created = True
    else:
        pass


def get_center_x(width):
    # Funkcja zwracająca centralną pozycję względem osi x w oknie pycharm
    return (800 - width) // 2


if __name__ == "__main__":
    # Tworzenie okna
    window = start()  # Wywołuje funkcję start() w celu utworzenia okna gry
    window.create_window()  # Wywołuje metodę create_window() obiektu GUI, aby utworzyć okno

    # Obiekt odpowiedzialny za elementy GUI
    main_menu_handler = GUIHandler(window)  # Tworzy obiekt GUIHandler, który zarządza elementami GUI w oknie

    settings_handler = GUIHandler(window)
    # Dodawnie elemntów GUI main menu
    main_menu()

    # Główna pętla gry
    while window.running:  # Pętla trwa, dopóki okno gry jest uruchomione

        window.screen.fill((0, 0, 0))
        # Sprawdzanie eventów/zdarzeń w grze. Jeżeli użytkownik coś kliknie, przesunie myszką, etc.
        # To tutaj są przechowywane informacje na ten temat
        for event in pygame.event.get():  # Pobiera listę wszystkich zdarzeń, które wystąpiły od ostatniej iteracji pętli

            # Sprawdzanie, czy event, jaki wywołał gracz, to wyłączenie gry.
            if event.type == pygame.QUIT:  # Sprawdza, czy użytkownik zamknął okno
                # Uruchomienie funkcji wyłączającej gry
                window.close_window()  # Wywołuje metodę close_window() obiektu GUI, aby zamknąć okno

            if opened == 0:
                # Sprawdza, czy elementy GUI są wciskane.
                main_menu_handler.handle_events(
                    event)  # Przekazuje zdarzenie do GUIHandler, który obsługuje zdarzenia dla elementów GUI (np. przycisków)
            elif opened == 1:
                settings_handler.handle_events(event)

        if opened == 0:
            # "Rysowanie" okienka menu
            main_menu_handler.draw_all()  # Wywołuje metodę draw_all() obiektu GUIHandler, aby narysować wszystkie elementy GUI (np. przyciski) na ekranie
        elif opened == 1:
            # "Rysowanie" okienka ustawień
            settings_handler.draw_all()
        # Odświeżanie ekranu
        window.refresh_screen()  # Wywołuje metodę refresh_screen() obiektu GUI, aby odświeżyć ekran i wyświetlić zmiany
