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

class InvalidShapeError(Exception):
    """
    Raised when an algorithm receives an image with a shape 
    it cannot turn into a sequence.
    """

def file_to_array(file_name):
    """
    Takes an image and returns a numpy array of its colour values.
    If the image length or width aren't even it is cut by one 
    row or column so that it is.
    """
    array = np.array(imageio.imread(file_name))
    if array.shape[0]%2 != 0:
        array = np.delete(array, array.shape[0], 0)
    if array.shape[1]%2 != 0:
        array = np.delete(array, array.shape[1], 1)
    return array

def array_to_file(array, file_name):
    """Takes a numpy array and saves it into an image file."""
    imageio.imwrite(file_name, array) 

def show(array, **kwargs):
    """Shows an array as a picture on a matplotlib plot."""
    plt.imshow(array, **kwargs)
    plt.show()
