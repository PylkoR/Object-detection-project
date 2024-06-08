from ultralytics import YOLO

model = YOLO("best.pt")

photo = model.predict(source="test_predict/", show=True, conf=0.5, save=True, line_thickness=2)
