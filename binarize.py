from PIL import Image
import numpy as np 
import sys 
import cv2

def printArray(T):
	print("elements dans ce tableau", len(T))
	print("elements par lignes", len(T[0]))
	for i in T :
		print(i)


def binarize(image):

	image = Image.open(image)
	T = np.asarray(image).tolist()

	newT = []
	for i in T :
		Ttmp = [] 
		try : 
			for j in i :
				if j == True or j == False:				
					Ttmp.append(j)
				elif j == 255 :
					Ttmp.append(True)
				elif j == 0 :
					Ttmp.append(False)
			newT.append(Ttmp)

		except :
			print("'j")
			return 
	printArray(newT)

	image = Image.fromarray(np.asarray(newT))
	image.save(image)

if __name__ == '__main__':
	image = Image.open(sys.argv[1])
	printArray(np.asarray(image).tolist())
	binarize(sys.argv[1])