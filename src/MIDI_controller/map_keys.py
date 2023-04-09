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
    66: [(9,0)],
    67: [(9,1)],
    68: [(9,2)],
    69: [(9,3)],
    70: [(9,4)],
    71: [(10,0)],
    72: [(10,1)],
    73: [(10,2)],
    74: [(10,3)],
    75: [(10,4)],
    76: [(11,0)],
    77: [(11,1)],
    78: [(11,2)],
    79: [(11,3)],
    80: [(11,4)],
    81: [(12,0)],
    82: [(12,1)],
    83: [(12,2)],
    84: [(12,3)],
    85: [(12,4)],
    86: [(13,0)],
    87: [(13,1)],
    88: [(13,2)],
    89: [(13,3)],
    90: [(13,4)],
    91: [(14,0)],
    92: [(14,1)],
    93: [(14,2)],
    94: [(14,3)],
    95: [(14,4)],
    96: [(15,0)],
    97: [(15,1)],
    98: [(15,2)],
    99: [(15,3)],
    100: [(15,4)],
    101: [(16,0)],
    102: [(16,1)],
    103: [(16,2)],
    104: [(16,3)],
    105: [(16,4)],
    106: [(17,0)],
    107: [(17,1)],
    108: [(17,2)],
}

def map_played_notes(note_box: Dict[list]) -> list:
    """
    Function takes a box of played notes as input and maps them to the corresponding keys on the on-screen keyboard.
    
    Arguments:
    note_box - A dictionary with note number and status as key value pairs
    
    Returns:
    A list of tuples, where each tuple contains the row and column of a key
    """
    
    played_notes = [note for note, status in note_box.items() if status == "on"]
    mapped_keys = []
    
    for note in played_notes:
        if note in KEY_MAPPING:
            mapped_keys.extend(KEY_MAPPING[note])
            
    return mapped_keys
