import os
import sys

#Checks if files are present
print("checking system files")
if not os.path.isfile("main.py"):
    sys.exit("File 'main' is missing")
if not os.path.isfile("Boot.py"):
    sys.exit("File 'Boot' is missing")

if not os.path.isfile("Dicts.py"):
    sys.exit("File 'Dicts' is missing")

if not os.path.isfile("used"):
    import Boot

if not os.path.isfile("User"):
    import Boot

try:
    import main
except:
    sys.exit("there was an error Loading 'main' file")
