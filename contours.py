import numpy as np
import cv2
import os 
import sys
from PIL import Image 
import decoupage_image as crop
import resize
import binarize as bw

def main(image):
    filename = ''
    for i in image :
        if i == '.':
            break
        filename+=i
    #filename = image

    try : 
        os.listdir("separations/")
    except :
        os.system("mkdir separations/")

    try : 
        os.listdir("separations/"+filename)
    except :
        os.system("mkdir separations/"+filename)
    
    image = cv2.imread(image)
    width = image.shape[0]
    height = image.shape[1]
    """
    if width > 28 :
        coeff = 16
        newheight = int(height / coeff)
        newwidth = int(width)
        output = cv2.resize(image, (newwidth, newheight))
        cv2.imwrite('separations/'+filename+"/resize.png", output)
        image = cv2.imread('separations/'+filename+"/resize.png")
    """
    b = image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,250,255,cv2.THRESH_BINARY_INV)


    contours, h=cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    i = 1
    for cnt in contours:
        perimetre=cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,0.01*perimetre,True)
        
        M = cv2.moments(cnt)
        #print(M)
        try :
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        except :
            cX, cY = 0, 0
        blank_image = np.zeros((width,height,3), np.uint8)
        blank_image[0::] = (255)      # (B, G, R)
        #print(cnt.tolist())
        newcnt = []
        newcnt_temp = []
        for j in cnt.tolist() :
            for w in j :
                hor, vert= int(w[0]), int(w[1])
                newcnt_temp.append([hor, vert])
                newcnt.append(newcnt_temp)
                newcnt_temp = []
        newcnt = np.asarray(newcnt)
        a = cv2.drawContours(blank_image,[newcnt],-1,(0),2)
        T = []
        for ligne in a :
            T_temp = []
            for j in ligne:
                T_temptemp = []
                for z in j :
                    if z == 255 :
                        T_temp.append(True)
                    else :
                        T_temp.append(False)
                #T_temp.append(T_temptemp)
            T.append(T_temp)
        #print(T)

        data = Image.fromarray(np.asarray(T).astype(np.bool))
        data.save("separations/"+filename+"/"+str(i)+".bmp")


        image = b
        #cv2.imwrite("separations/"+filename+"/"+str(i)+".bmp", a)
        i+=1
    #cv2.imwrite('newimage.bmp',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    bonne_taille(filename)
    return True

    
def bonne_taille(filename):
    repo = "separations/"+filename+"/"
    liste_images = os.listdir(repo)
    a_conserver = []
    for img in liste_images :
        a_conserver, repo = crop.main(repo+img, repo, a_conserver)
    for i in os.listdir(repo):
        if i not in a_conserver:
            try :
                os.remove(repo+"/"+i)
            except :
                ...
        else : 
            resize.main(repo + i)
            bw.binarize(repo + i)

if __name__ == '__main__':
    main(sys.argv[1])
