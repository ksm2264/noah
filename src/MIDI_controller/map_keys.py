
# Importing necessary libraries and modules

import mido
from typing import Dict

# Creating a dictionary to map notes to keys on an on-screen keyboard 
# Assuming that the on-screen keyboard consists of a 2-D array where each row represents a key on the MIDI keyboard

KEY_MAPPING = {
    21: [(0,0)],
    22: [(0,1)],
    23: [(0,2)],
    24: [(0,3)],
    25: [(0,4)],
    26: [(1,0)],
    27: [(1,1)],
    28: [(1,2)],
    29: [(1,3)],
    30: [(1,4)],
    31: [(2,0)],
    32: [(2,1)],
