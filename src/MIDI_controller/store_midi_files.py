
#Importing necessary libraries
import pygame.midi
import os

#Initializing midi
pygame.midi.init()

def store_piano_track(file_path: str) -> bool:
    """
    This function takes a file path as input,
    checks if the file is in MIDI format,
    and stores it for the game to use.

    Args:
    file_path: string - Path of the MIDI file

    Returns:
    True if the file is successfully stored.
    False if the file is not in the correct format.
    """
    #Checking if the file format is .mid or .midi
    if not file_path.endswith(('.mid', '.midi')):
        print("File format not supported!")
        return False

    if os.path.getsize(file_path) == 0:
        print("Empty file!")
        return False

    #Loading the MIDI file
    try:
        pygame.midi.Midi(file_path).file
        print("File loaded successfully!")
        #Storing the file
        with open("piano_tracks.txt", 'a+') as f:
            f.write(file_path + "\n")
        return True
    except pygame.midi.MidiException as ex:
        print("Error while loading file: ", ex)
        return False
