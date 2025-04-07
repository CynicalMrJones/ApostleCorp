# imports
import os
import platform
import Liker
import Poster
import Commenter
import instragam_sort_comments
from instagrapi import Client


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
        count = 0
        for i in botArray:
            print(count, i)
            count += 1
    elif command == "login":
        cl = Client(request_timeout=60)
        print("Which bot would you like to login with :: ")
        test = int(input("Login: "))
        try:
            cl.login(botArray[test].email, botArray[test].password)
            print("Login sucessful")
        except:
            print("Login Failed")
    elif command == "like":
        link = input("Please input link :: ")
        likerBot = int(input("Please input bot number :: "))
        Liker.liker(botArray[likerBot], link)
    elif command == "mass like":
        link = input("Please input link :: ")
        for i in botArray:
            Liker.liker(botArray[i], link)
        numLikes = int(input("How many bots should like the post :: "))
        i = 0
        while i < numLikes and i < len(botArray):
            Liker.liker(botArray[i], link)
            i += 1
    elif command == "comment":
        link = input("Please input link :: ")
        commentBot = int(input("Please input bot number :: "))
        comment = (input("Please enter your comment :: "))
        Commenter.commenter(botArray[commentBot], link, comment)
    elif command == "post":
        postBot = int(input("Please input bot number :: "))
        Poster(botArray[postBot])
    elif command == "sortComment":
        link = input("Please input a link :: ")
        instragam_sort_comments.process_comments(botArray[1],link)
    elif command == "massComment":
        link = input("Please input link :: ")
        commentDoc = input("Please input the txt file with comments :: ")
        botlen = int(input("Please input the number of bots you would like to comment :: "))
        botRay = {}
        for i in range(botlen):
            spot = int(input("Please input the bot number :: "))
        Commenter.massComment(botRay, link, commentDoc)
    else:
        print("Command not found try again")
