from ultralytics import YOLO

model = YOLO("firstModel60Epochs.pt")

model.predict(source="soldiers.jpg", show=True, conf=0.5)
