import cv2
import os

#Zapisuje klatkę filmiku co 3 sekundy i zapisuje do wskazanego katalogu

def extract_frames(video_path, output_dir, interval_seconds=None):
    # Wczytaj film
    cap = cv2.VideoCapture(video_path)

    # Sprawdź czy plik wideo jest prawidłowy
    if not cap.isOpened():
        print("Błąd: Nie można otworzyć pliku wideo.")
        return

    # Stwórz katalog wyjściowy, jeśli nie istnieje
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Zapisz klatkę co określony interwał czasowy (w sekundach)
        if interval_seconds and frame_count % int(fps * interval_seconds) == 0:
            frame_filename = os.path.join(output_dir, f"frame_imola_{int(frame_count/(fps * interval_seconds))}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved frame {int(frame_count/(fps * interval_seconds))}")

    cap.release()
    print(f"Zapisano {frame_count/(fps * interval_seconds)} klatek z {total_frames} wideo.")


video_path = "videos/Race-Highlights-2024-Emilia-Romagna-Grand-Prix.mp4"
output_directory = "images/"
interval_seconds = 3

extract_frames(video_path, output_directory, interval_seconds)
