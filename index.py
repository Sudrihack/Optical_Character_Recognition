import contours
import prediction 
import sys
import os
from sklearn import neighbors
import numpy as np
import filextest
import fileytest
import filextrain 
import fileytrain
import kfile
def lire_entrainement():
	xtest, ytest, xtrain, ytrain, k = np.array(filextest.r()), np.array(fileytest.r()), np.array(filextrain.r()), np.array(fileytrain.r()), kfile.opti_k()
	return xtest, ytest, xtrain, ytrain, k

if __name__ == '__main__':
	filename = sys.argv[1]
	etat = contours.main(filename)
	if etat == True :
		liste_img = os.listdir("separations/" + filename[0:-4])
		predict = ''
		xtest, ytest, xtrain, ytrain, k = lire_entrainement()
		for i in liste_img :
			print("separations/"+filename[0:-4]+"/"+i)
			predict += prediction.tester_une_seule_image("separations/"+filename[0:-4]+"/"+i, xtest, ytest, xtrain, ytrain, k, False)
			#predict = prediction.tester_une_seule_image(filename, xtest, ytest, xtrain, ytrain, k, False)
		print(predict)
	else :
		print("probleme de decoupage de l'image")