from ultralytics import YOLO
import cv2
import os

model_path = 'train_results/train_colab_1/weights/best.pt'
data_path = 'data/test/images'
save_path = 'runs/stats/colab_1'

# Załaduj model
model = YOLO(model_path)

# Definiowanie kolorów dla każdej klasy
colors = {
    'RedBull': (99, 2, 8),
    'Ferrari': (52, 52, 235),
    'Mercedes': (103, 103, 107),
    'AstonMartin': (91, 122, 12),
    'Mclaren': (7, 121, 242),
    'Haas': (255, 255, 255),
    'Sauber': (13, 245, 5),
    'Alpine': (176, 30, 110),
    'Williams': (201, 11, 8),
    'VisaRB': (0, 0, 0),
    'bolid': (52, 52, 235)
}

# Wykonaj predykcję
results = model.predict(source=data_path, show=True, conf=0.5, save=False, line_thickness=2)

# Przetwórz wyniki
for result in results:
    # Pobierz oryginalny obraz
    img = result.orig_img.copy()

    # Słownik do przechowywania liczby bolidów dla każdej klasy (zespołu)
    team_counts = {team: 0 for team in result.names.values()}

    # Iteruj po wykrytych obiektach
    for box in result.boxes:
        # Pobierz indeks klasy
        class_id = int(box.cls)
        # Pobierz nazwę klasy
        class_name = result.names[class_id]
        # Zwiększ licznik dla odpowiedniej klasy
        team_counts[class_name] += 1

        # Pobierz kolor dla klasy
        color = colors.get(class_name)

        # Rysuj prostokąt wokół wykrytego bolidu
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # Pobierz wysokość obrazu
    img_height = img.shape[0]

    # Dodaj liczby bolidów do obrazu w lewym dolnym rogu z tłem
    for idx, (team, count) in enumerate(team_counts.items()):
        text = f'{team}: {count}'
        # Oblicz szerokość i wysokość tekstu
        (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        # Ustal pozycję tekstu w lewym dolnym rogu
        x = 10
        y = img_height - 10 - idx * (text_height + 20)

        # Rysuj tło dla tekstu
        cv2.rectangle(img, (x, y - text_height - baseline), (x + text_width, y + baseline), (185, 189, 185), cv2.FILLED)

        # Rysuj tekst na tle
        color = colors.get(team)
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

    # Pobierz ścieżkę wyjściową
    output_path = os.path.join(save_path, os.path.basename(result.path))

    # Zapisz obraz z naniesionymi informacjami
    cv2.imwrite(output_path, img)

print(f"Predykcje zakończone. Wyniki zapisane w folderze {save_path}.")


