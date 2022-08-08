import torch
from glob import glob
import shutil  # 파일 이동과 관련한 라이브러리
import os   # os와 관련된 라이브러리

img_path = r'40. 사진에서 사람을 인식하여 분류하기\원본이미지'

img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

print(img_list)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img_move_path = r'40. 사진에서 사람을 인식하여 분류하기\사람만분류'

for img_path in img_list:
    results = model(img_path)
    print(img_path)
    for pred in results.pred[0]:
        tag = results.names[int(pred[-1])] 
        print(tag)
        if tag == "person":
            print("move")
            shutil.move(img_path, img_move_path + '\\' + os.path.basename(img_path))  # 원본이미지 폴더에서 사람만 분류 폴더로 인물사진 이동시키기
            break