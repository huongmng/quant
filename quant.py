import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from PIL import Image 
import PIL 

#loading
im=imread('pizza.jpg')
im=Image.open(r"C:\Users\System-Pc\Desktop\flower1.jpg") 
print(im.width, im.height, im.mode, im.format)
#data of the img
im = np.array(im)
imshow(im)
plt.axis('off'), show()

#quantization
im=Image.open(r"C:\Users\System-Pc\Desktop\flower1.jpg")
im=im.quantize(248)
