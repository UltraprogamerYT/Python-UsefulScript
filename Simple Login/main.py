#Load all the system files
import os

#simple username saveing
if not os.path.isfile("User"):
	print("Welcome\nPlease Create an account\n")
	x = input("Username: ")
	f = open("User" , "w")
	f.write(x)
	f.close()

#Use this to only run stuff once!
if not os.path.isfile("used"):
	f = open("User")	
	x = f.readline()	
	print("Hey " , x , "Hope your good")
	f = open("used" , "w")
	f.close

