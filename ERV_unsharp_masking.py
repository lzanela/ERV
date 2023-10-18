import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


## Herramientas

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])



## Implementación de unsharp masking

def unsharp_masking(img, sigma, a=1):
    M = np.subtract(img, scipy.ndimage.gaussian_filter(img, sigma))
    return img + a*M