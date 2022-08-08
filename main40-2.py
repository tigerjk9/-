import torch
from glob import glob

img_path = r'40. 사진에서 사람을 인식하여 분류하기\원본이미지'

img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

print(img_list)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # yolov5모델을 torch.hub에서 불러옵니다.

for img_path in img_list:   #원본 이미지 폴더에 이미지 수만큼 반복합니다.
    results = model(img_path)     #이미지에서 사람, 물건을 찾아 반환합니다.
    print(img_path)
    results.save(r'40. 사진에서 사람을 인식하여 분류하기\이미지확인용')   #이미지 확인용 폴더에 결과 사진을 저장합니다.
    for pred in results.pred[0]:
        tag = results.names[int(pred[-1])] 
        print(tag)