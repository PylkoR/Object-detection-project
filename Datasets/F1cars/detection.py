from ultralytics import YOLO

model = YOLO("results/train_colab_1/weights/best_colab_1.pt")

photo = model.predict(source="data/videos/Imola15s.mp4", show=True, conf=0.5, save=True, line_thickness=1, hide_labels=True, hide_conf=True)
