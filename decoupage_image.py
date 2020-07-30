
from PIL import Image 
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
import binarize
def traiter_image(nameimg):
    #img = Image.open(nameimg)
    tab = np.asarray(nameimg).tolist()
    T = []
    for i in tab :
        for j in i :
            if j == True :
                T.append(255)
            else :
                T.append(0)
    return T


def ajouter_ligne(lignepx, lettre, texte, a, filename):
    width, height = lignepx.size
    T = traiter_image(lignepx)
    blanc = [255] * height
    if 0 in T :
        for i in range(len(T)-1):
            lettre[i].append(T[i])
    else :
        if T == blanc and len(lettre[0]) != 0:
            a = 0
            while len(lettre[height-2]) < 28:
                if a%2 == 0 :
                    for i in range(len(blanc) -1):
                        lettre[i].append(blanc[i])
                    a+=1
                else : 
                    for i in range(len(blanc) -1):
                        lettre[i] = ajouter_debut(lettre[i], blanc[i])
                    a+=1
            while [] in lettre :
            	lettre[lettre.index([])] = [255] * len(lettre[0])
            cv2.imwrite(filename[0:-4] + "/"+str(a)+".bmp", np.asarray(lettre))
            binarize.binarize(filename[0:-4] + "/"+str(a)+".bmp")
            lettre = lettre_vierge(height)
    return texte, lettre


def ajouter_debut(liste, element):
    T = []
    T.append(element)
    for i in liste :
        T.append(i)
    return T


def lettre_vierge(height):
    lettre = []
    for i in range(height):
        lettre.append([])
    return lettre

def main(filename):
	if filename[-4::] == '.bmp' : 
		try : 
		    os.listdir(filename[0:-4])
		except : 
		    os.mkdir(filename[0:-4])
		image = Image.open(filename)
		width, height = image.size 

		left, top, right, bottom = 0, 0, 1, height
		a = 0
		lettre = lettre_vierge(height)
		texte = []
		while a<width :
		    im1 = image.crop((left+a, top, right+a, bottom))
		    #cv2.imwrite("separations_temp/" + str(a) +".bmp", im1)
		    texte, lettre = ajouter_ligne(im1, lettre, texte, a, filename)
		    a+=1
		return True
	else :
		print("format non accepté, veuillez donner des images .bmp codé en 8 bits")
		return False

if __name__ == '__main__':
	filename = sys.argv[1]
	main(filename)