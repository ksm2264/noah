from mido import MidiFile

class MIDI_reader:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_file(self):
        mid = MidiFile(self.file_path)
        time = 0
        note_data = []

        for msg in mid:
            time += msg.time

            if msg.type == 'note_on':
                note_data.append({
                    'note': msg.note,
                    'velocity': msg.velocity,
                    'time': time
                })

        return note_data

    def get_metadata(self):
        mid = MidiFile(self.file_path)

        return {
            'tempo': mid.tempo,
            'key_signature': mid.key_signature,
            'time_signature': mid.time_signature
        }