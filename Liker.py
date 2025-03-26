import instagrapi
from instagrapi import Client

def liker(bots, link):
    botInstant = Client(request_timeout = 60)
    botInstant.login(bots.email, bots.password)
    LikeID = botInstant.media_id(botInstant.media_pk_from_url(link))
    botInstant.media_like(LikeID)
    print("This operation was completed successfully!")

        

#This is the main "Like" function. It will take one of the bot objects, use that to login, and then like a post declared by a hyperlink
        
