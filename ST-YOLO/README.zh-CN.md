ST-YOLO.yaml 是我们自定义的模型配置文件，文件中集成了 C2f_SCconv 模块和 TripletAttention 机制。您可以直接使用此 YAML 文件来训练模型，其使用方法与官方 YOLOv8 的指令一致。

要使用此配置文件训练模型，只需按照官方 YOLOv8 文档中的标准训练命令进行操作：
yolo train --cfg YOLOv8-ss.yaml --data your_dataset.yaml --epochs 100

请确保将 your_dataset.yaml 替换为您特定的数据集配置文件。此命令将使用 ST-YOLO.yaml 中定义的自定义模型结构启动训练过程。