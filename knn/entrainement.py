"""
ce script nous permet de choisir le k optimal pour notre knn
et d'enregistrer dans des fichiers txt la phase d'entrainement
"""

from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import neighbors
import os
mnist = fetch_openml('mnist_784', version=1)

# on évite d'avoir trop de données en en prennant 
# qu'une partie au hasard pour gagner du temps
sample = np.random.randint(70000, size=1000)
data = mnist.data[sample]
target = mnist.target[sample]

# phase d'entrainement
xtrain, xtest, ytrain, ytest = train_test_split(data, target, train_size=0.8)

# test d'erreurs pour un seul k
"""
knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(xtrain, ytrain)
error = 1 - knn.score(xtest, ytest)
"""
#print('Erreur: %f' % error)

# pour afficher un graphique pour avoir le meilleur k possible
errors = []
klist = []
for k in range(2,15):
	print('on analyse', k, end=" ")
	knn = neighbors.KNeighborsClassifier(k)
	print('#', end="")
	errors.append(100*(1 - knn.fit(xtrain, ytrain).score(xtest, ytest)))
	print('#')
	klist.append(k)
k_opti = klist[errors.index(min(errors))]
print("k opti : ", k_opti)

# on affiche sur un graphique les erreurs
# plt.plot(range(2,15), errors, 'o-')
# plt.show()

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
