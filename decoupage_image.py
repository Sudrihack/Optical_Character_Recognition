
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


def ajouter_ligne(lignepx, lettre, texte, a, filename, a_conserver):
    width, height = lignepx.size
    T = traiter_image(lignepx)
    blanc = [255] * height
    if 0 in T :
        for i in range(len(T)-1):
            lettre[i].append(T[i])
    else :
        if T == blanc and len(lettre[0]) != 0:
            center = 0
            while len(lettre[height-2]) < 28:
                if center%2 == 0 :
                    for i in range(len(blanc) -1):
                        lettre[i].append(blanc[i])
                    center+=1
                else : 
                    for i in range(len(blanc) -1):
                        lettre[i] = ajouter_debut(lettre[i], blanc[i])
                    center+=1
            while [] in lettre :
            	lettre[lettre.index([])] = [255] * len(lettre[0])

            name = ""
            etat = False
            for i in filename[::-1] :
                if i == '/':
                    etat = True
                if etat == True:
                    name+=i
            name = name[::-1] 

            cv2.imwrite(name+str(a)+".bmp", np.asarray(lettre))
            a_conserver.append(str(a)+".bmp")
            binarize.binarize(filename)
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

def main(filename, repo, a_conserver):
    extention = ''
    etat = False
    for i in filename:
        if etat == True :
            extention+=i 
        if i == '.':
            etat = True
            extention+=i 
    if extention == ".bmp" : 
        image = Image.open(filename)
        width, height = image.size 
        left, top, right, bottom = 0, 0, 1, height
        a = 0
        lettre = lettre_vierge(height)
        texte = []
        while a<width :
            im1 = image.crop((left+a, top, right+a, bottom))
            #cv2.imwrite("separations_temp/" + str(a) +".bmp", im1)
            texte, lettre = ajouter_ligne(im1, lettre, texte, a, filename, a_conserver)
            a+=1

        return a_conserver, repo
    else :
        print("format non accepté, veuillez donner des images .bmp codé en 8 bits")
        return False

if __name__ == '__main__':
	filename = sys.argv[1]
	main(filename)