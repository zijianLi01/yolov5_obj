# yolov5_obj
#train
 python train.py --img 640 --batch 16 --epochs 20 --data ./data/data.yaml --cfg ./models/yolov5s.yaml --weights ./yolov5s.pt                
#test
python val.py --data data.yaml --weights .\path of your best.pt    //need change the val path in data.yaml(val: ../val/images   to    val: ../test/images)
#detect
python detect.py --source .\path of your image or video --weights .\path of your best.pt                                                                 
                                                                                                                                                    
