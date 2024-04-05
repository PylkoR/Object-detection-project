from ultralytics import YOLO

model = YOLO("best.pt")

model.predict(source="test/images/A10_png.rf.9d5bd039e76fb95a256426daf5a4d59e.jpg", show=True, conf=0.5)
