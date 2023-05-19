from ultralytics import YOLO


def main():
    model = YOLO("runs/detect/train/weights/best.pt")  # load a pretrained model (recommended for training)
    model.val(imgsz=640,batch=1)  # evaluate model performance on the validation set

if __name__ == "__main__":
    main()
