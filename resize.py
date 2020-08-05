import cv2

def main(nameImage):
	src = cv2.imread(nameImage, cv2.IMREAD_UNCHANGED)
	output = cv2.resize(src, (28,28))
	cv2.imwrite(nameImage,output) 