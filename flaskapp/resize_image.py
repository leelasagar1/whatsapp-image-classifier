import cv2
import os
path = '/content/drive/My Drive/mobile_gallery_image_classification/validation'
for folder in os.listdir(path):
	for image in os.listdir(os.path.join(path,folder)):
		try:
			im = cv2.imread(os.path.join(os.path.join(path,folder),image))
			im = cv2.resize(cv2.cvtColor(im, cv2.COLOR_BGR2RGB), (256, 256))
			cv2.imwrite(os.path.join(os.path.join(path,folder),image), im)
			print("pass")
		except:
			print(os.path.join(os.path.join(path,folder),image))
			os.remove(os.path.join(os.path.join(path,folder),image))
			pass