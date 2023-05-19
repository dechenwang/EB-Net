from ultralytics import YOLO


def main():
    # Load a model
    model = YOLO('ultralytics/models/v8/yolov8n-crosppf-zhuyili.yaml')  # build a new model from YAML
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
    # Train the model
    model.train(data='ultralytics/datasets/RSOD.yaml', epochs=150, imgsz=640)

if __name__ == "__main__":
    main()
