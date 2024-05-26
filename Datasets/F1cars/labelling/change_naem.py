import os

def rename_files(directory):
    # Przechodzenie przez wszystkie pliki w podanym katalogu
    for filename in os.listdir(directory):
        # Sprawdzenie, czy plik ma rozszerzenie .txt
        if filename.endswith('.txt'):
            # Podział nazwy pliku na część bazową i rozszerzenie
            base_name, ext = os.path.splitext(filename)
            # Sprawdzenie, czy .0 występuje w bazowej części nazwy
            if '.0' in base_name:
                # Usunięcie pierwszej kropki i 0
                new_base_name = base_name.replace('.0', '', 1)
                # Stworzenie nowej nazwy pliku
                new_filename = new_base_name + ext
                # Stworzenie pełnych ścieżek do starego i nowego pliku
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)
                # Zmiana nazwy pliku
                os.rename(old_file, new_file)
                print(f'Renamed: {old_file} -> {new_file}')

# Przykład użycia
directory_path = 'C:\\Users\\pylko\\Repo_YOLO_project\\Object-detection-project\\Datasets\\F1cars\\labelling\\labels'
rename_files(directory_path)
