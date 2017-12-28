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

def show_path(shape, path):
    """Draws an image of the path on a 2d plane."""
    arr = np.zeros(shape)
    step = 1/len(path)
    for i in np.arange(len(path)):
        x = path[i][0]
        y = path[i][1]
        arr[x][y] = i*step
    plt.imshow(arr)
    plt.show()

def apply_path(array, path):
    """Turns a 2d array into a 1d array along a path."""
    sequence = []
    for pos in path:
        sequence.append(array[pos[0]][pos[1]])
    sequence = np.array(sequence)
    return sequence

def show(array, path, **kwargs):
    """Shows an array as a picture on a matplotlib plot."""
    seq = apply_path(array, path)
    seq = seq.reshape(1, len(seq), 3)
    plt.imshow(seq, **kwargs)
    plt.show()
