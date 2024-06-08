from ultralytics import YOLO

model = YOLO("yolov8n.pt")

if __name__ == '__main__':
    model.train(data="data_vehicles.yaml", imgsz=640, epochs=1, batch=8, amp=False)

#yolo task=detect mode=train epochs=75 data=data_vehicles.yaml model=yolov8n.pt imgsz=640
