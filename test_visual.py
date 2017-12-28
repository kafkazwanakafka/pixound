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
snek = module.array_to_sequence(arr)
snek = snek.reshape(1, len(snek), 3)
visual.show(snek[0:50], aspect='auto')

