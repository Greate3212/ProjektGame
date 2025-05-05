import pygame

from GUI.gui import GUI


def start():
    """
    Funkcja odpowiedzialna za inicjalizowanie startu gry.
    W funkcji tej są uruchamiane wszystkie wymagane procesy/klasy do uruchomienia gry.
    :return:
    """
    gui = GUI("Game", 800, 600)
    return gui


if __name__ == "__main__":
    window = start()
    # Tworzenie okna
    window.create_window()

    # Główna pętla gry
    while window.running:

        # Sprawdzanie eventów/zdarzeń w grze. Jeżeli użytkownik coś kliknie, przesunie myszką, etc.
        # To tutaj są przechowywane informacje na ten temat
        for event in pygame.event.get():

            # Sprawdzanie, czy event, jaki wywołał gracz, to wyłączenie gry.
            if event.type == pygame.QUIT:

                # Uruchomienie funkcji wyłączającej gry
                window.close_window()
