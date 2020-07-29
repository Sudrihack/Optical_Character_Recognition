from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import neighbors
import numpy as np
from numpy import asarray
import filextest
import fileytest
import filextrain 
import fileytrain 
import kfile
import os
from PIL import Image
import sys

def lire_entrainement():
	xtest, ytest, xtrain, ytrain, k = np.array(filextest.r()), np.array(fileytest.r()), np.array(filextrain.r()), np.array(fileytrain.r()), kfile.opti_k()
	return xtest, ytest, xtrain, ytrain, k

def reentrainement_provisoir() :
	mnist = fetch_openml('mnist_784', version=1)

	sample = np.random.randint(70000, size=1000)
	data = mnist.data[sample]
	target = mnist.target[sample]
	xtrain, xtest, ytrain, ytest = train_test_split(data, target, train_size=0.8)
	k = trouver_k_opti(xtrain, xtest, ytrain, ytest)
	return xtrain, xtest, ytrain, ytest, k

def trouver_k_opti(xtrain, xtest, ytrain, ytest):
	errors = []
	klist = []
	for k in range(2,15):
		knn = neighbors.KNeighborsClassifier(k)
		errors.append(100*(1 - knn.fit(xtrain, ytrain).score(xtest, ytest)))
		klist.append(k)
	k_opti = klist[errors.index(min(errors))]
	return k_opti

def tester_image_bdd():

	predicted = knn.predict(xtest)
	images = xtest.reshape((-1, 28, 28))
	predicted = knn.predict(xtest)
	images = xtest.reshape((-1, 28, 28))
	select = np.random.randint(images.shape[2], size=20)
	fig,ax = plt.subplots(5,4)
	for index, value in enumerate(select):
		try :
			plt.subplot(5,4,index+1)
			plt.axis('off')
			plt.imshow(images[value],cmap=plt.cm.gray_r,interpolation="nearest")
			plt.title('Le chiffre est :{}'.format( predicted[value]) )
		except :
			...

	plt.show()

def tester_une_seule_image(nameimg, xtest, ytest, xtrain, ytrain, k, afficher):

	xtest = xtest.tolist()
	xtest.append(traiter_image(nameimg))
	xtest = np.asarray(xtest)
	predicted = knn.predict(xtest)
	images = xtest.reshape((-1, 28, 28))
	select = np.random.randint(images.shape[0], size=5)
	if afficher == True :
		plt.imshow(images[-1], cmap=plt.cm.gray_r,interpolation="nearest")
		plt.axis('off')
		plt.title('le chiffre est :{}'.format(predicted[-1]))
		plt.show()

		plt.show()
		return predicted[-1]
	else :
		#print(predicted)
		return predicted[-1]


def traiter_image(nameimg):
	img = Image.open(nameimg)
	tab = np.asarray(img).tolist()
	T = []
	for i in tab :
		for j in i :
			if j == True :
				T.append(0)
			else :
				T.append(255)
	return T


def travail_img(img):
	image = Image.open(img)
	image.show()
	arr = np.asarray(image).tolist()
	#print(arr)
	
	narr = []
	for i in arr :
		T = []
		for j in arr :
			if j == True :
				T.append(1)
			else :
				T.append(0)
		narr.append(T)
	#print(narr)
	return narr
	
xtest, ytest, xtrain, ytrain, k = lire_entrainement()
knn = neighbors.KNeighborsClassifier(k)
knn.fit(xtrain, ytrain)
if __name__ == '__main__':
	filename = sys.argv[1]
	print(tester_une_seule_image(filename, xtest, ytest, xtrain, ytrain, k, False))
	#tester_image_bdd()