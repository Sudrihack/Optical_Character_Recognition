"""
STEPS :
1) we take informations of bdd
2) we take a part of the bdd
3) we train the machine
4) we record the training into another py files
"""
from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import neighbors
import os
import sys

# to download mnist_784 if we have proxy server

"""
proxy = "proxy:port"

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
"""

def main(s = 1000, kmax = 20):
	mnist = fetch_openml('mnist_784', version=1)

	# we take a part of the bdd to gain time to training
	sample = np.random.randint(70000, size=s)
	data = mnist.data[sample]
	target = mnist.target[sample]

	# training
	xtrain, xtest, ytrain, ytest = train_test_split(data, target, train_size=0.8)

	# to find the best k
	errors = []
	klist = []
	for k in range(2,kmax):
		print('on analyse', k, end=" ")
		knn = neighbors.KNeighborsClassifier(k)
		print('#', end="")
		errors.append(100*(1 - knn.fit(xtrain, ytrain).score(xtest, ytest)))
		print('#')
		klist.append(k)
	k_opti = klist[errors.index(min(errors))]
	print("k opti : ", k_opti)

	print("longueur xtrain", len(xtrain))

	# on enregistre la phase d'entrainement
	filextrain = open("filextrain.py", "w")
	filextrain.write("def r():\n\treturn " + str(xtrain.tolist()))
	filextrain.close()

	fileytrain = open("fileytrain.py", "w")
	fileytrain.write("def r():\n\treturn " + str(ytrain.tolist()))
	fileytrain.close()

	filextest = open("filextest.py", "w")
	filextest.write("def r():\n\treturn " + str(xtest.tolist()))
	filextest.close()

	fileytest = open("fileytest.py", "w")
	fileytest.write("def r():\n\treturn " + str(ytest.tolist()))
	fileytest.close()

	kfile = open("kfile.py", 'w')
	kfile.write("def opti_k():\n\treturn "+str(k_opti))
	kfile.close()

if __name__ == '__main__':
	main()