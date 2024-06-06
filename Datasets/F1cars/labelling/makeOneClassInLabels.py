import os
import fileinput

def change_first_character(directory):
    # Sprawdź czy podana ścieżka jest katalogiem
    if not os.path.isdir(directory):
        print("Podana ścieżka nie jest katalogiem.")
        return

    # Przejdź przez wszystkie pliki w katalogu
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Sprawdź czy to plik tekstowy
        if os.path.isfile(filepath) and filename.endswith('.txt'):
            # Otwórz plik w trybie do odczytu i zapisu
            with fileinput.FileInput(filepath, inplace=True) as file:
                for line in file:
                    # Zmień pierwszy znak w linii na '0'
                    print('0' + line[1:], end='')
            print(f"Pierwszy znak w pliku {filename} został zmieniony na '0'.")

directory_path = "labels_bolid"
change_first_character(directory_path)
