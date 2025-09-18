from ultralytics import YOLO

model = YOLO("yolo12s.pt")


results = model.train(data = "data.yaml", epochs=50)