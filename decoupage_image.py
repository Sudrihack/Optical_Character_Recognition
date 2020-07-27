
from PIL import Image 
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

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

def ajouter_ligne(lignepx, lettre, texte, a):
    width, height = lignepx.size
    T = traiter_image(lignepx)
    blanc = [255] * height
    if 0 in T :
        for i in range(len(T)-1):
            lettre[i].append(T[i])
    else :
        if T == blanc and len(lettre[0]) != 0:
            cv2.imwrite("separations_temp/"+str(a)+".bmp", np.asarray(lettre))
            lettre = lettre_vierge()



    return texte, lettre

def lettre_vierge():
    lettre = []
    for i in range(height-1):
        lettre.append([])
    return lettre

try : 
    os.listdir("separations_temp")
except : 
    os.mkdir("separations_temp")
image = Image.open("test_reel.bmp")
width, height = image.size 

left, top, right, bottom = 0, 0, 1, height
a = 0
lettre = lettre_vierge()
texte = []
while a<width :
    im1 = image.crop((left+a, top, right+a, bottom))
    #cv2.imwrite("separations_temp/" + str(a) +".bmp", im1)
    texte, lettre = ajouter_ligne(im1, lettre, texte, a)
    a+=1

