
import mido

def parse_midi(file_path):
    """
    Given the path to a MIDI file, extract its track data and return it as a dictionary.
    The dictionary maps track names to a list of note events.
    Each note event is a tuple of (time, note_number, velocity, duration)
    """
    midi_file = mido.MidiFile(file_path)
    track_data = {}

    for track in midi_file.tracks:
        current_time = 0
        notes_on = {}
        track_notes = []
        for msg in track:
            current_time += msg.time
            if msg.type == 'note_on':
                note_number = msg.note
                velocity = msg.velocity
                notes_on[note_number] = velocity
                track_notes.append((current_time, note_number, velocity, None))
            elif msg.type == 'note_off':
                note_number = msg.note
                if note_number in notes_on:
                    velocity = notes_on.pop(note_number)
                    last_event = track_notes[-1]
                    duration = current_time - last_event[0]
                    track_notes[-1] = (last_event[0], last_event[1], last_event[2], duration)
        track_name = track.name if track.name else f"Track {track.number}"
        track_data[track_name] = track_notes

    return track_data
