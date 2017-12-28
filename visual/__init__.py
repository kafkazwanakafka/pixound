"""
visual
======

Part of pixound. Modules in visual allow to transform 
2d images into 1d sequences.

This file contains simple functions to transform image 
files into 2d arrays and vice versa.
"""
import imageio
import numpy as np
from matplotlib import pyplot as plt

def file_to_array(file_name):
    return  np.array(imageio.imread(file_name))

def array_to_file(array, file_name):
    imageio.imwrite(file_name, array) 

def show(array):
    plt.imshow(array)
    plt.show()
