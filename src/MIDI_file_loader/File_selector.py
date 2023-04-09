      
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
import urllib.request

class FileSelector:
    @staticmethod
    def select_file():
        file_path, _ = QFileDialog.getOpenFileName(None, "Select MIDI File", "", "MIDI Files (*.mid *.midi)")
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
