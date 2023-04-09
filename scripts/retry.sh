#!/bin/bash

python3 setup.py sdist
pip install dist/my_project-0.1.tar.gz
python3 bot/main_test.py "switch from tkinter to pyqt"