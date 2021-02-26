from tkinter import *
import tkinter.messagebox
root = Tk()
def error():
    tkinter.messagebox.showerror('System Error', 'Your system has ran into an error and needs to restart')
    root.destroy()
root.after(1, error)
root.mainloop()
