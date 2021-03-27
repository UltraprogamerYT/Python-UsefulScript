from tkinter import *
import random
import tkinter.messagebox
root = Tk()
root.geometry('0x0')
choice = random.randrange(1, 4)
if choice == 1:
    tkinter.messagebox.showinfo('1 new message from Gordon Ramsey', 'Hey babe ;)')
if choice == 2:
    tkinter.messagebox.showerror('1 new message from ur mum', 'Do ur homework')
if choice == 3:
    tkinter.messagebox.showwarning('1 new message from ur mum', 'Im warning u')
root.mainloop()
