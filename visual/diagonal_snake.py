"""
Module implementing and extremely simple and straightforward
sequencing algorithm.

It can only sequence square images.
"""
import numpy as np

from visual import InvalidShapeError
import visual

def validate_shape(shape):
    if shape[0] == shape[1]:
        return True
    else:
        return False

def array_to_sequence(shape):
    if not validate_shape(shape):
        raise InvalidShapeError

    side = shape[0]
    seq = [(0,0)]
    for i in range(1, side):
        # List of pixel coords to add to sequence
        # need to list them because the lines will change direction
        l = []
        for j in range(i):
            l.append((j, i))
        for j in range(i, -1, -1):
            l.append((i, j))

        if i % 2:
            r = range(len(l))
        else:
            r = range(len(l)-1, -1, -1)
        for j in r:
            x = l[j][0]
            y = l[j][1]
            seq.append((x, y))

    seq = np.array(seq)
    return seq
