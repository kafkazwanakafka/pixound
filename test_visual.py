#!/usr/bin/env python3
"""
This script visualizes the output of a sequencing module.

Usage:
    ./test_visual.py <module-in-visual>
"""

import sys
import importlib

import visual

arr = visual.file_to_array('images/coyote.jpg')
module = importlib.import_module('visual.'+sys.argv[1])
snek = module.array_to_sequence(arr.shape)
print(snek)
visual.show_path(arr.shape, snek)

visual.show(arr, snek, aspect='auto')
