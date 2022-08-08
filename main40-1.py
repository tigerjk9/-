from glob import glob

img_path = r'40. 사진에서 사람을 인식하여 분류하기\원본이미지'  # 원본 이미지가 저장된 경로

img_list = glob(img_path + '\*.jpg')    # 원본 이미지 폴더에 .jpg 파일을 찾아 파일의 경로를 리스트의 형태로 반환
img_list.extend(glob(img_path + '\*.png'))  # 원본 이미지 폴더에 .png 파일을 찾아 파일의 경로를 리스트의 형태로 반환

print(img_list)