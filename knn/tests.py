import matplotlib.pyplot as plt
from PIL import Image
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1)
import numpy as np

def traiter_image(nameimg):
	img = Image.open(nameimg)
	tab = np.asarray(img).tolist()
	T = []
	for i in tab :
		for j in i :
			if j == True :
				T.append(50)
			else :
				T.append(600)
	#Tf = np.asarray(Tf)
	#Tf.reshape((-1, 28, 28))
	return T


sample = np.random.randint(70000, size=1000)
data = mnist.data[sample]
target = mnist.target[sample]
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(data, target, train_size=0.8)
from sklearn import neighbors

# On récupère le classifieur le plus performant
knn = neighbors.KNeighborsClassifier(4)
knn.fit(xtrain, ytrain)


xtest = xtest.tolist()
xtest.append(traiter_image('3.bmp'))


xtest = np.asarray(xtest)


# On récupère les prédictions sur les données test
predicted = knn.predict(xtest)

# On redimensionne les données sous forme d'images
images = xtest.reshape((-1, 28, 28))

# On selectionne un echantillon de 12 images au hasard
select = np.random.randint(images.shape[0], size=5)

plt.imshow(images[-1], cmap=plt.cm.gray_r,interpolation="nearest")
plt.title('Predicted: {}'.format(predicted[-1]))
plt.show()

"""
# On affiche les images avec la prédiction associée
fig,ax = plt.subplots(3,4)
print(fig, ax)

for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(images[value],cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title('Predicted: {}'.format( predicted[value]) )
"""

plt.show()
