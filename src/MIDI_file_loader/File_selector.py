
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
        return file_path
