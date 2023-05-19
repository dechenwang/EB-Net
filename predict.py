from ultralytics import YOLO


def main():
    model = YOLO("runs/detect/v8n-rsod/weights/best.pt")  # load a pretrained model (recommended for training)
    model.predict(source="ultralytics/datasets/RSOD/images/test",save=True)  # evaluate model performance on the validation set

if __name__ == "__main__":
    main()
