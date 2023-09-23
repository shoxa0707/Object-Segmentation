from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

results = model.train(
        batch=16,
        device=[0,1],
        data="datasets/data.yaml",
        epochs=20,
        imgsz=640,
    )
