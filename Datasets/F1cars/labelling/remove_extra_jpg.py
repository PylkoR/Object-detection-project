import os

#usuwa zdjęcia z katalogu /images, które nie mają odpowiadającej etykiety w katalogu /labels_teams

# Ścieżki do katalogów zawierających zdjęcia i pliki tekstowe
photo_dir = "images"
txt_dir = "labels_teams"

# Pobranie listy plików w obu katalogach
photo_files = os.listdir(photo_dir)
txt_files = os.listdir(txt_dir)

# Utworzenie zbiorów nazw plików bez rozszerzeń
photo_names = {os.path.splitext(file)[0] for file in photo_files}
txt_names = {os.path.splitext(file)[0] for file in txt_files}

# Sprawdzenie, czy każde zdjęcie ma odpowiadający plik txt
missing_txt_files = photo_names - txt_names

# Usunięcie zdjęć bez odpowiadającego pliku txt
for missing_txt in missing_txt_files:
    photo_path = os.path.join(photo_dir, missing_txt + ".jpg")
    if os.path.exists(photo_path):
        os.remove(photo_path)
        print(f"Usunięto zdjęcie: {missing_txt}.jpg")

print("Zakończono sprawdzanie i usuwanie niepotrzebnych zdjęć.")