# OCR 
OCR = Optical Character Recognition 


there are 2 functions into prediction.py to analyse images.
	-	tester_image_bdd() => to analyse images stock in the mnist_784 database
	-	tester_une_seule_image() => to analyse a specific image outside of the database 

Warning :
	for the moment, this script can only analyse (28*28)px images, in bitmap format (8 bits).

to train the machine, use the entrainement.py script, you can adjust the number of elements in sample variable, adjust the range to find the the best k (because we are in Knn type)

You will install sklearn, numpy, matplotlib, PIL to use this script 