import ctypes
import os
import pip
import subprocess
import time
import sys
#ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
clear = lambda: os.system('cls')

def import_or_install():
    try:
        import pyperclip
        import keyboard
        
    except ImportError:
        pip.main(['install', 'keyboard']) 
        pip.main(['install', 'pyperclip']) 

        clear()
import_or_install()
import pyperclip
import keyboard


from pathlib import Path
def main():
    os.system('python IPRequest.py')
    #subprocess.Popen(['mstsc'])
    p = subprocess.Popen(['mstsc'])
    p.communicate(input=pyperclip.paste())
# trying to get mstsc.exe to be on top and paste ip in textbox

main() 
quit()