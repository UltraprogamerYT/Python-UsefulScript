#Importing Required Modules

import webbrowser
import datetime
import time

#Defining Zoom Links(place your zoom codes there)

zoom1 = ("")
zoom2 = ("")
zoom3 = ("")
zoom4 = ("")

#Time Loop
while True:
    x = datetime.datetime.now()
    b = x.strftime("%H, %M, %f")
    print(b)
    time.sleep(1)

    #Setting up Runtimes(Change the times to your desired times)
        
    if b == "07, 26, 000000":
        webbrowser.open(zoom1)

    elif b == "08, 23, 000000":
        webbrowser.open(zoom2)

    elif b == "08, 57, 000000":
        webbrowser.open(zoom3)

    elif b == "09, 53, 000000":
        webbrowser.open(zoom4)
	



