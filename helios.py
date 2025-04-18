# imports
import os
import platform
from functions import Liker
from functions import Poster
from functions import Commenter
from functions import instragam_sort_comments
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
f = open("pics/pic.pic", "r")
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
        yn = input("Would you like all bots to like? y/n :: ")
        if(yn == "y"):
            Liker.massLiker(botArray, link)
        if(yn == "n"):
            botSize = int(input("Please input the number of bots you would like to 'like' :: "))
            for i in botSize:
                botRay[i] = botArray[int(input("Please input the bot number :: "))]
        Liker.massLiker(botRay, link)

    elif command == "comment":
        link = input("Please input link :: ")
        commentBot = int(input("Please input bot number :: "))
        comment = (input("Please enter your comment :: "))
        Commenter.commenter(botArray[commentBot], link, comment)

    elif command == "post":
        postBot = int(input("Please input bot number :: "))
        Poster.poster(botArray[postBot])
        Poster(botArray[postBot])

    elif command == "sortComment":
        link = input("Please input a link :: ")
        instragam_sort_comments.process_comments(botArray[1],link)
    
    elif command == "massComment":
        link = input("Please input link :: ")
        commentDoc = input("Please input the txt file with comments :: ")
        yn = input("Would you like for all bots to comment? y/n :: ")
        if(yn == 'y'):
            Commenter.massComment(botArray, link, commentDoc)
        elif(yn == 'n'):
            botRay = {}
            botSize = int(input("How many bots would you like to comment? :: "))
            for i in range(botSize):
                botRay[i] = botArray[int(input("Please input the bot number to comment :: "))]
            Commenter.massComment(botRay, link, commentDoc)
        else: 
            print("Command not found try again")
    else:
        print("Command not found try again")
