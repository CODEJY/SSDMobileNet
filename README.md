SSD-MobileNet
===
简介
---
主要步骤：
1. 制作Pascal VOC标准格式数据集（参考Pascal VOC 2007数据集）
2. 将VOC数据集转换为TFRecord格式，用于tensorflow读取数据
3. 训练模型
4. 评估模型
5. 生成.pb文件，用于测试或移植客户端

文件树
---
> object_detection: ssd-mobilenet整个框架代码文件夹  

>> CTNDATA: Pascal VOC格式的数据集，包括训练、评估  

>> test_images: 测试固化后的模型(.pb文件)所用的测试图片  

>> anchor_generators: 在多个cnn layer生成anchor  

>> box_coders: 计算预测框的位置  
  
>> builders:  工具类文件夹  
>>> model_builder_test.py: 测试运行环境是否配置正确

>> checkpoints: 预训练模型的checkpoints，此模型基于coco数据集进行的fine-tune  

>> data: .pbtxt文件，用于配置检测出的对象的id与name  

>> eval_dir: 用于存储执行eval.py评估模型后生成的tensorboard文件  

>> models: 构建ssd-mobilenet神经网络层的代码文件  

>> TFRecord: 存储.record文件，由VOC格式数据集转换得到  

>> train: 存储执行train.py后生成的checkpoints以及tensorboard文件  

>> train.py: 执行训练  

>> trainer.py: 为train.py提供工具,由train.py调用  

>> ssd_mobilenet_v1_coco.config: pipeline配置文件，num_classes、train、eval等相关参数配置  

>> eval.py: 评估模型  

>> eval_util.py: 为eval.py提供工具，由eval.py调用  

>> evaluator.py: 为eval.py提供工具，由eval.py调用  

>> export_inference_graph.py: 生成.pb文件,用于测试或移植客户端  

>> export_model: 存储export_inference_graph.py生成的.pb文件  

>> exporter.py: 为export_inference_graph.py提供工具  

>> object_detection_tutorial.ipynb: 读取pb文件，测试固化后的模型。输入一个或多个图片，输出检测后的图片  

>> create_pascal_tf_record.py: 将VOC格式数据集转换为tfrecord格式的脚本文件  

>> createTXT.py: 构建完整的VOC格式数据集，基于VOC数据集Annotations文件夹的xml格式文件，生成所需的txt文件，包括test.txt,train.txt.trainval.txt,val.txt,用于create_pascal_tf_record.py  

>> random_horizontal_flip.py: 对图片进行水平镜像处理，用于丰富测试数据  

>> Composite_Images.py: 合成图片，增加训练数据。取一张仅包含集装箱正面的图片，覆盖到一张包含复杂背景的图片的随机（合理）位置上  

>> get_env_version.py: 获取当前环境的各依赖库的版本  

>> rename_file.py: 批量重命名文件名字

> slim: 依赖库，ssd-mobilenet是基于tensorflow-slim实现的

运行
---
- 在docker中运行项目，docker镜像文件已上传到docker hub，拉取方式：docker pull wujy1284/ssdmobilenet
- 在docker中`每次`开启新的terminal都必须在research目录下执行以下两条指令  

```
	- protoc object_detection/protos/*.proto --python_out=.
	- export PYTHONPATH=$PYTHONPATH:pwd:pwd/slim
``` 
- 训练指令  

```
python object_detection/train.py \
    --logtostderr \
    --pipeline_config_path=${PATH_TO_YOUR_PIPELINE_CONFIG} \
    --train_dir=${PATH_TO_TRAIN_DIR}
```  
- 评估指令  

```
python object_detection/eval.py \
    --logtostderr \
    --pipeline_config_path=${PATH_TO_YOUR_PIPELINE_CONFIG} \
    --checkpoint_dir=${PATH_TO_TRAIN_DIR} \
    --eval_dir=${PATH_TO_EVAL_DIR}
```  
- 生成.pb文件，执行export_inference_graph.py  

```
python object_detection/export_inference_graph.py \
    --input_type image_tensor \
    --pipeline_config_path ${PIPELINE_CONFIG_PATH} \
    --trained_checkpoint_prefix ${TRAIN_PATH} \
    --output_directory output_inference_graph.pb
```

注意
---
此模型与Google官方开源的代码有一些区别，我做了一些修改，具体的会写在wiki中