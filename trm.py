import subprocess
import os
import time
import sys
import b



print("PitBox terminal for Python")
while True:
    inp = input(".> ")

    if inp == 'dsbG':
        b.garbageinfochanger()
    if inp == 'restart':
        print("Restarting")
        subprocess.run(['python3', 'PitBox/main.py'])