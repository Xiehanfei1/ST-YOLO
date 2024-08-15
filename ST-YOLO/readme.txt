The ST-YOLO.yaml is our custom model configuration file, which incorporates the C2f_SCconv module and the TripletAttention mechanism. You can directly use this YAML file to train your model. The usage is consistent with the official YOLOv8 instructions.

To train the model using this configuration file, simply follow the standard training command as per the official YOLOv8 documentation:
yolo train --cfg YOLOv8-ss.yaml --data your_dataset.yaml --epochs 100

Make sure to replace your_dataset.yaml with your specific dataset configuration file. This command will initiate the training process using the customized model structure defined in ST-YOLO.yaml.