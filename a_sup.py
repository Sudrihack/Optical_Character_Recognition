from PIL import Image
import numpy as np 
import sys 

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