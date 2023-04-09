
# Importing necessary libraries and modules

import mido
from typing import Dict
from functools import lru_cache

# Creating a dictionary to map notes to keys on an on-screen keyboard 
# Assuming that the on-screen keyboard consists of a 2-D array where each row represents a key on the MIDI keyboard

@lru_cache(maxsize=None)
def create_key_mapping() -> Dict[int, list]:
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
        33: [(2,2)],
        34: [(2,3)],
        35: [(2,4)],
        36: [(3,0)],
        37: [(3,1)],
        38: [(3,2)],
        39: [(3,3)],
        40: [(3,4)],
        41: [(4,0)],
        42: [(4,1)],
        43: [(4,2)],
        44: [(4,3)],
        45: [(4,4)],
        46: [(5,0)],
        47: [(5,1)],
        48: [(5,2)],
        49: [(5,3)],
        50: [(5,4)],
        51: [(6,0)],
        52: [(6,1)],
        53: [(6,2)],
        54: [(6,3)],
        55: [(6,4)],
        56: [(7,0)],
        57: [(7,1)],
        58: [(7,2)],
        59: [(7,3)],
        60: [(7,4)],
        61: [(8,0)],
        62: [(8,1)],
        63: [(8,2)],
        64: [(8,3)],
        65: [(8,4)],
        66: