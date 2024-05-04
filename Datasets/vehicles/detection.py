from ultralytics import YOLO

model = YOLO("best_s_57.pt")

photo = model.predict(source="test_predict/", show=True, conf=0.5, save=True)
