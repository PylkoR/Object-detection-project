import os
import shutil

def move_txt_files_with_matching_images(images_dir, txt_dir, target_dir):
    # Upewnij się, że katalog docelowy istnieje
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Pobierz zestaw nazw plików bez rozszerzeń z katalogu ze zdjęciami
    image_files = {os.path.splitext(filename)[0] for filename in os.listdir(images_dir) if not filename.startswith('.')}

    # Przeglądaj pliki txt w katalogu txt
    for txt_filename in os.listdir(txt_dir):
        if txt_filename.endswith('.txt') and not txt_filename.startswith('.'):
            # Sprawdź, czy istnieje odpowiadający plik ze zdjęciem
            base_name = os.path.splitext(txt_filename)[0]
            if base_name in image_files:
                # Przenieś plik .txt do katalogu docelowego
                src_path = os.path.join(txt_dir, txt_filename)
                dest_path = os.path.join(target_dir, txt_filename)
                shutil.move(src_path, dest_path)
                print(f"Przeniesiono: {txt_filename}")


images_directory = 'data/test/images'
labels_directory = 'labelling/labels_teams'
target_directory = 'data/test/labels_teams'

move_txt_files_with_matching_images(images_directory, labels_directory, target_directory)
