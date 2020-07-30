# OCR 
OCR = Optical Character Recognition 

# How to install

You will install sklearn, numpy, matplotlib, PIL to use this script
so :
<code>
	python -m pip install sklearn
</code>
<code>
	python -m pip install numpy
</code>
<code>
	python -m pip install matplotlib
</code>
<code>
	python -m pip install pillow
</code>

# How to use 

if your image are only one number (like 1, 2, 3, ..., 9) in (28*28) pixels and in .bixmap format (1 bit) you can use the command : "python prediction.py yourimage"

if you have a suite of numbers, with height 28 pixels, in any format, you can use "python index.py yourimage"

# Prediction

there are 2 functions into prediction.py to analyze images.
<ol>
	<li>tester_image_bdd() => to analyse images stock in the mnist_784 database</li>
	<li>tester_une_seule_image() => to analyse a specific image outside of the database</li>
<ol>
in this two functions you can display the result in matplotlib window or just return the final result

Warning :
<ol>
	<li>for now, this script can only analyze (28*28)px images, in bitmap format (1 bits).</li>
	<li>only number are predicted</li>
</ol>

# Training

to train the machine, use the entrainement.py script, you can adjust the number of elements in sample variable, adjust the range to find the best k (because we are in Knn type)

