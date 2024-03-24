from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(data="data.yaml", imgsz=320, epochs=70)
