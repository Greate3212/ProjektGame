import pygame

from GUI.guihandler import GUIHandler, GUI


def start():
    """
    Funkcja odpowiedzialna za inicjalizowanie startu gry.
    W funkcji tej są uruchamiane wszystkie wymagane procesy/klasy do uruchomienia gry.
    :return:
    """
    gui = GUI("Project Game", 800, 600)  # Tworzy obiekt GUI (okno gry) o nazwie "Game" i wymiarach 800x600
    return gui  # Zwraca utworzony obiekt GUI


opened = 0
"""
Opened - zmienna przechowująca informacje jakie okno aktualnie jest otwarte:
 - 0 - main menu
 - 1 - settings
"""


def main_menu():
    global opened
    opened = 0

    main_menu_handler.clear_all()  # Wyczyść stare elementy
    # Funkcja/okienko menu głównego oraz jego wszystkie elementy
    main_menu_handler.add_label("Project Game", get_center_x(150), get_y_res(100) - 450, 150, 80, font_size=55,
                                font_name="Comic Sans MS")
    main_menu_handler.add_button("Start", get_center_x(200), get_y_res(100) - 200, 200, 100,
                                 game_start)  # Dodaje przycisk "Start" do GUIHandler. Po kliknięciu wywoływana jest funkcja game_start
    main_menu_handler.add_button("Settings", get_center_x(200), get_y_res(90) - 100, 200, 90, settings)
    main_menu_handler.add_button("Exit", get_center_x(200), get_y_res(80) - 10, 200, 80, window.close_window)
    main_menu_handler.add_label("v0.0.1", get_center_x(50) + 400 - 20, get_y_res(20), 50, 25, font_size=15,
                                font_name="Corbel")


def game_start():
    # Funkcja wywoływana po wciśnięciu przycisku 'start' w menu głównym
    print("START!")


def change_settings(a):
    global s_created, m_created
    s_created, m_created = False, False
    window.toggle_fullscreen("")
    pygame.time.delay(200)
    settings()
    window.screen.fill((0, 0, 0))
    main_menu_handler.draw_all()
    window.refresh_screen()


def settings():
    global opened
    opened = 1
    # Funkcja wywoływana po wsciśnięciu przycisku 'settings' w menu głównym
    main_menu_handler.clear_all()  # Wyczyść stare elementy
    main_menu_handler.add_label("Settings", get_center_x(150), get_y_res(550), 150, 100, font_size=55,
                                font_name="Comic Sans MS")
    main_menu_handler.add_checkbox("Fullscreen", get_center_x(200), get_y_res(450), callback=change_settings)
    main_menu_handler.add_button("Back", get_center_x(150), get_y_res(80), 150, 70, main_menu)


def get_y_res(height):
    return window.screen.get_height() - height


def get_center_x(width):
    # Funkcja zwracająca centralną pozycję względem osi x w oknie pycharm
    window_width = window.screen.get_width()
    return (window_width - width) // 2


if __name__ == "__main__":
    # Tworzenie okna
    window = start()  # Wywołuje funkcję start() w celu utworzenia okna gry
    window.create_window()  # Wywołuje metodę create_window() obiektu GUI, aby utworzyć okno

    # Obiekt odpowiedzialny za elementy GUI
    main_menu_handler = GUIHandler(window)  # Tworzy obiekt GUIHandler, który zarządza elementami GUI w oknie

    settings_handler = None
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

            # Sprawdza, czy elementy GUI są wciskane.
            main_menu_handler.handle_events(
                event)  # Przekazuje zdarzenie do GUIHandler, który obsługuje zdarzenia dla elementów GUI (np. przycisków)

        # "Rysowanie" okienka menu
        main_menu_handler.draw_all()  # Wywołuje metodę draw_all() obiektu GUIHandler, aby narysować wszystkie elementy GUI (np. przyciski) na ekranie

        # Odświeżanie ekranu
        window.refresh_screen()  # Wywołuje metodę refresh_screen() obiektu GUI, aby odświeżyć ekran i wyświetlić zmiany
