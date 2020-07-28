from PIL import Image
import numpy as np 
import sys 
import cv2
def printArray(T):
	print("elements dans ce tableau", len(T))
	print("elements par lignes", len(T[0]))
	for i in T :
		print(i)

filename1 = sys.argv[1]
image = Image.open(filename1)
printArray(np.asarray(image).tolist())

filename2 = sys.argv[2]
image2 = Image.open(filename2)
printArray(np.asarray(image2).tolist())

"""
im = np.array(Image.open('29,99.jpg').convert('L').resize((256, 256)))
cv2.imwrite('29,99.bmp', im)
# <class 'numpy.ndarray'>
"""