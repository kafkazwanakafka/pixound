"""
Module for cropping images to the desired shape.

Offers to square or square and crop to the nearest
power of two.
"""
import math, visual

def crop_square(shape):
    # If square already square exception
    l1 = len(shape[0])
    l2 = len(shape[1])
    length = (l1, l2)[l1 > l2]
    
    # Crop to square
    
    pass

def crop_power(shape):
    # Must be square exception
    length = len(shape[0])
    power = int(math.log(length, 2))

    # Crop to power
    
    pass
