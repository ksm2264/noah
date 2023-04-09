
import tkinter as tk
from tkinter import filedialog
import urllib.request 

class FileSelector:
    @staticmethod
    def select_file():
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("MIDI Files", "*.mid *.midi")])
        return file_path

    @staticmethod
    def load_remote_file(url):
        try:
            remote_file = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            raise Exception(f"Unable to fetch remote MIDI file - {str(e)}")
        file_path = 'remote_file.mid'
        with open(file_path, 'wb') as f:
            f.write(remote_file.read())

        #new file with modifications           
        with open(file_path, 'rb') as f:
            contents = f.read()

        note_count = {}
        for msg in mido.MidiFile(file_path):
            if msg.type not in ['note_on', 'note_off']:
                continue
            if msg.note not in note_count:
                note_count[msg.note] = 1
            else:
                note_count[msg.note] += 1

        #print note count
        print(note_count)

        return file_path

