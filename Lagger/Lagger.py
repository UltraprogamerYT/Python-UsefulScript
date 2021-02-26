import webbrowser
import random
import time


websites = ["https://www.google.com/", "https://twitter.com/home", "www.youtube.com", "GUCCI.com"]


while True:
    tabs = random.choice(websites)
    webbrowser.open(tabs, new=1)
    

while True:
