Importing necessary libraries and modules

Creating a dictionary to map notes to keys on an on-screen keyboard 
Assuming that the on-screen keyboard consists of a 2-D array where each row represents a key on the MIDI keyboard

Function takes a box of played notes as input and maps them to the corresponding keys on the on-screen keyboard.

Arguments:
note_box - A dictionary with note number and status as key value pairs

Returns:
A list of tuples, where each tuple contains the row and column of a key
