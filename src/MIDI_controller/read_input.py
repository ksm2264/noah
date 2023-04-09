from mido import MidiFile, MidiTrack, Message
import time

def convert_to_notes():
    """
    This function reads the input from the MIDI keyboard and converts it into 
    playable notes, which can be used for the rhythm game.
    """
    with MidiFile('input.mid') as mid:
        for i, track in enumerate(mid.tracks):
            print('Track {}: {}'.format(i, track.name))
            for msg in track:
                if msg.type == 'note_on':
                    print(msg.note, msg.velocity)
                    time.sleep(0.1)
                elif msg.type == 'note_off':
                    print(msg.note)

def check_timing(on_screen_notes, played_notes):
    """
    This function checks the timing of the played notes against the on-screen notes.
    """
    timing_accuracy = 0
    for i in range(len(on_screen_notes)):
        if on_screen_notes[i].timing == played_notes[i].timing and on_screen_notes[i].note == played_notes[i].note:
            timing_accuracy += 1
    return (timing_accuracy/len(on_screen_notes))*100

def score_user(timing_accuracy):
    """
    This function calculates and updates the user's score based on the accuracy of the timing.
    """
    score = 0
    if timing_accuracy >= 90:
        score = 5
    elif timing_accuracy >= 70:
        score = 3
    elif timing_accuracy >= 50:
        score = 1
    else:
        score = 0
    return score
