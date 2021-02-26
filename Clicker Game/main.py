from tkinter import *
import time


master = Tk()

def uiPrint():
    info()
    print("")
    print(click)


def info():
    print("")
    print("")

info()

click = 0
mult = 1
dcp1 = 0

def blankLine():
    for i in range(20):
        print("")

def purchaseDoubleClicksCommand():
    global click
    global mult
    if click < 5:
        print("Not enough clicks!")
        blankLine()
    elif click >= 5:
        mult = mult+1
        click = click - 5
        print("Double Clicks Purchased!")
        blankLine()


def purchaseAutoClickerCommand():
    global click
    if click < 7:
        print("Not enough clicks!")
        blankLine()
    elif click >= 7:
        click = click - 7
        print("Auto clicker purchased!")
        while True:
            click = click + 1
            time.sleep(1)


def buttonCommand():
    global click
    global mult
    click += 1*(mult)
    uiPrint()

    if click == 100:
        print('''Achievement Unlocked: Junior Clicker!
        BONUS 100 clicks!''')
        click += 100

    elif click == 400:
        print ('''Achievement Unlocked: Little Ninja Clicks!
        BONUS 200!''')
        click += 300

    elif click == 1500:
        print ('''Achievement Unlocked: Click Ninja Master!
        QUAD CLICKS!''')
        mult = mult * 4

    elif click == 3000:
        print ('''Achievement Unlocked:  Jackie Chan Style!
        8 TIMES THE CLICKS!''')
        mult = mult * 8


mainClickButton = Button(master, text="Click!", command = buttonCommand)
mainClickButton.pack()

mainClickButton = Button(master, text="End Game", command = i)
mainClickButton.pack()

master.title("Clicker! v0.0.6")
master.geometry("%sx%s+%s+%s" % (200,70,512,512))
mainloop()