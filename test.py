from ultralytics import YOLO



model = YOLO("Beans_detector.pt")  # load a custom model


results = model("TestImg.jpg")  # predict on an image



for result in results:
    xywh = result.boxes.xywh  
    xywhn = result.boxes.xywhn  
    xyxy = result.boxes.xyxy  
    xyxyn = result.boxes.xyxyn  
    names = [result.names[cls.item()] for cls in result.boxes.cls.int()] 
    confs = result.boxes.conf  
    result.show()
