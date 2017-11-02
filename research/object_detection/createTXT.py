import os  
import random  
'''
trainval_percent:用于训练及评估的数据集占总数据集的比例
test_percent:100% - trainval_percent.用于测试的数据集占总数据集的比例
train_percent:用于训练的数据集占trainval数据集的比例
eval_percent:用于评估的数据集占trainval_percent数据集的比例
'''
trainval_percent = 0.8  
train_percent = 0.5  
xmlfilepath = '/Users/wuga/models/research/object_detection/VOC2007/Annotations'
txtsavepath = '/Users/wuga/models/research/object_detection/VOC2007/ImageSets/Main'  
total_xml = os.listdir(xmlfilepath)  
  
num=len(total_xml)  
list=range(num)  
tv=int(num*trainval_percent)  
tr=int(tv*train_percent)  
trainval= random.sample(list,tv)  
train=random.sample(trainval,tr)  
  
ftrainval = open('/Users/wuga/models/research/object_detection/VOC2007/ImageSets/Main/trainval.txt', 'w')  
ftest = open('/Users/wuga/models/research/object_detection/VOC2007/ImageSets/Main/test.txt', 'w')  
ftrain = open('/Users/wuga/models/research/object_detection/VOC2007/ImageSets/Main/train.txt', 'w')  
fval = open('/Users/wuga/models/research/object_detection/VOC2007/ImageSets/Main/val.txt', 'w')  
  
for i  in list:  
    name=total_xml[i][:-4]+'\n'  
    if i in trainval:  
        ftrainval.write(name)  
        if i in train:  
            ftrain.write(name)  
        else:  
            fval.write(name)  
    else:  
        ftest.write(name)  
  
ftrainval.close()  
ftrain.close()  
fval.close()  
ftest .close() 