import os
import random
import shutil

# 设置训练集和验证集的路径
train_dir = 'D:\\yolov5-master\\train\\images'
val_dir = 'D:\\yolov5-master\\val\\images'
label_dir = 'D:\\yolov5-master\\train\\labels'
val_label_dir = 'D:\\yolov5-master\\val\\labels'

# 列出训练集目录下的所有文件
files = os.listdir(train_dir)

# 选择20%的文件作为验证集
val_files = random.sample(files, int(len(files) * 0.2))

# 将这些文件移动到验证集目录
for file in val_files:
    shutil.move(os.path.join(train_dir, file), os.path.join(val_dir, file))
    # 移动对应的标签文件
    label_file = file.rsplit('.', 1)[0] + '.txt'
    shutil.move(os.path.join(label_dir, label_file), os.path.join(val_label_dir, label_file))