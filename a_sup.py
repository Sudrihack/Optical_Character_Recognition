from PIL import Image
import numpy as np 

img = Image.open("separations/1_2_3/135.bmp")

print(np.asarray(img))