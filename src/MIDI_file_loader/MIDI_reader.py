
from mido import MidiFile
from src.MIDI_file_loader.File_selector import load_file

class MIDI_reader:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_file(self):
        # Check if the file was loaded through internet
        if self.file_path.startswith('http'):
            file_content = load_file(self.file_path)
            with open(self.file_path, 'wb') as f:
                f.write(file_content)
        
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

