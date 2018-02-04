"""
Module implementing pseudo hilbert curve sequencing algorithm.

Can only sequence square images with side length 2**n, n being
a natural number.
"""
import numpy as np
import math

from visual import InvalidShapeError
import visual

def rotate(n, x, y, rx, ry):
    if ry == -1:
        if rx == 0:
            x = n - 2 - x
            y = n - 2 - y

    t = x
    x = y
    y = t

    return (n, x, y, rx, ry)

def xy2d(n, x, y):
    d = 0
    s = n/2
    while s > 0:
        rx = (x and s) > 0
        ry = (y and s) > 0
        d += s * s * ((3 * rx) or ry)
        _, x, y, _, _ = rotate(s, x, y, rx, ry)
        s /= 2
    return d

def validate_shape(shape):
    if shape[0] == shape[1]:
        p = math.log(shape[0], 2)
        if p == int(p):
            return True
    else:
        return False

def shape_to_path(shape):
    if not validate_shape(shape):
        raise InvalidShapeError("Shape must be a square and power of two.")

    side = shape[0]
    seq = []
    
    for i in range(side):
        for j in range(side):
            d = xy2d(side, i, j)
            print(i, j, d)
            seq.append([(i, j), d])
    
    seq.sort(key=lambda x: x[1])

    for i in range(len(seq)): 
        del seq[i][-1]
        seq[i] = seq[i][0]

    seq = np.array(seq)
    return seq


