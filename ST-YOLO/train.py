import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov8-ss.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='dataset/data.yaml',
                cache=True,
                imgsz=640,
                epochs=200,
                batch=16,
                close_mosaic=10,
                workers=8,
                device='0',
                optimizer='SGD', # using SGD
                # resume='runs/GF2_seg/SMLS-YOLO-enhance/weights/last.pt', # last.pt path
                # amp=False, # close amp
                # fraction=0.2,
                project='runs',
                name='ST-YOLO',
                )
