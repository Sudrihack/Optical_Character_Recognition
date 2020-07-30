# OCR 
OCR = Optical Character Recognition 

# How to install

You will install sklearn, numpy, matplotlib, PIL to use this script
so :
<ul>
	<li>
		<code>
			python -m pip install sklearn
		</code>
	</li>
	<li>
		<code>
			python -m pip install numpy
		</code>
	</li>
	<li>
		<code>
			python -m pip install matplotlib
		</code>
	</li>
	<li>
		<code>
			python -m pip install pillow
		</code>
	</li>
</ul>

# How to use 

if your image are only one number (like 1, 2, 3, ..., 9) in (28*28) pixels and in .bixmap format (1 bit) you can use the command : "python prediction.py yourimage"

if you have a suite of numbers, with height 28 pixels, in any format, you can use "python index.py yourimage"

# Prediction

there are 2 functions into prediction.py to analyze images.
<ul>
	<li>tester_image_bdd() => to analyse images stock in the mnist_784 database</li>
	<li>tester_une_seule_image() => to analyse a specific image outside of the database</li>
</ul>
in this two functions you can display the result in matplotlib window or just return the final result

<div style="color:red;">Warning :</div>
<ul>
	<li>for now, this script can only analyze (28*28)px images, in bitmap format (1 bits).</li>
	<li>only number are predicted</li>
</ul>

# Training

to train the machine, use the entrainement.py script, you can adjust the number of elements in sample variable, adjust the range to find the best k (because we are in Knn type)

