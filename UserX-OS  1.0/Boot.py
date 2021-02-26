import os

if not os.path.isfile("used"):
    print("Hi! Thanks for downloading UserX OS\nUserX is a program that mimics an operating system\ncreated by Shone, I made this for fun note this is not a real os it just resembles an OS\nType help for small list of commands, enjoy!")
    f = open("User", "w")
    input = input("please enter Name:\n")
    print('saving user')
    f.write(input)
    f.close()
    f = open("used", "w")
    f.close()
    print("contenueing boot...\n")
    import main
else:
    import main