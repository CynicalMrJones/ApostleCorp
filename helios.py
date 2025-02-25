
# imports
import os
import platform


# Class of Bots
class Bots:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __str__(self):
        return f"Bots gmail is {self.email}, and password is {self.password}"


# create the array of Bots
botArray = []
with open("InstagrapiLogins.txt", "r") as file:
    for line in file:
        entry = line.split()
        email, password = entry
        bot = Bots(email, password)
        botArray.append(bot)

# Grabbing prompt picture
f = open("pic.pic", "r")
draw = f.read()

# platform check for clearing the console
if platform.system() == "Linux":
    command_clear = "clear"
else:
    command_clear = "cls"

# clear the terminal
os.system(command_clear)

# draw the terminal
print(draw)

# main loop for program
while True:
    command = input("Command: ")
    if command == "quit":
        os.system(command_clear)
        break
    elif command == "clear":
        os.system(command_clear)
        print(draw)
    elif command == "show":
        for i in botArray:
            print(i)
    else:
        print(command)
