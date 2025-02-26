import instagrapi
from instagrapi import Client
# Takes the array of bots and the link to the post as parameters
def liker(bots, link):
    try:
        for x in range(0, len(bots)):
            bots[x].media_like(link)
        print("The operation has been completed")
    except:
        print("The operation has failed")
        return 1
    return 0
    #returns 1 on function error

        

#This is the main "Like" function. It will take one of the bots/bot arrays and have them like a post declared by a hyperlink
