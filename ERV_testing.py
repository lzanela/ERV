import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from ERV_unsharp_masking import rgb2gray, unsharp_masking

img = mpimg.imread('kodim04.png')     
gray = rgb2gray(img)
img = np.array(gray)
img = unsharp_masking(img, 2)
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
