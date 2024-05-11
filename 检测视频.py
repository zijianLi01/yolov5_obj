import os

videos = [
    "D:\\yolov5-master\\videos\\helmet.mp4",
    "D:\\yolov5-master\\videos\\site.mp4",
    "D:\\yolov5-master\\videos\\worker1.mp4",
    "D:\\yolov5-master\\videos\\worker2.mp4"
]

for video in videos:
    command = f"python detect.py --source {video} --weights D:\\yolov5-master\\runs\\train\\exp\\weights\\best.pt"
    os.system(command)
