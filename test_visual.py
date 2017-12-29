#!/usr/bin/env python3
"""
This script visualizes the output of a sequencing module.

Usage:
    ./test_visual.py <module-in-visual> [<image>]
"""

import sys
import importlib

import numpy as np

import visual

try:
    module = importlib.import_module('visual.'+sys.argv[1])
except ModuleNotFoundError:
    print("No such module:",sys.argv[1])
    print("Exiting")
    exit()
except IndexError:
    print(__doc__)
    exit()

try:
    arr = visual.file_to_array(sys.argv[2])
except IndexError:
    arr = visual.file_to_array('images/coyote.jpg')

try:
    snek = module.shape_to_path(arr.shape)
except InvalidShapeError as e:
    print("Error: Invalid shape.", e.args[0])
    print("Exiting")
    exit()

visual.show_path(arr.shape, snek, title="Path taken by "+sys.argv[1])

visual.show(arr, title="Input image")

seq = visual.apply_path(arr, snek)
visual.show_sequence(seq, title="Generated sequence")
