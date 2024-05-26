from ultralytics import YOLO

model = YOLO("results/train_colab_1/weights/best_colab_1.pt")

photo = model.predict(source="data/test/images/", show=True, conf=0.6, save=True)
