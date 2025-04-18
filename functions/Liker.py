from instagrapi import Client
# This is the main "Like" function. It will take one of the bot objects, use that to login, and then like a post declared by a hyperlink


def liker(bots, link):
    try:
        botInstant = Client(request_timeout=60)
        try:
            botInstant.login(bots.email, bots.password)
        except:
            print(f'{bots.email} failed to login')
            return -1
        LikeID = botInstant.media_id(botInstant.media_pk_from_url(link))
        botInstant.media_like(LikeID)
        print(f'{bots.email} liked the media')
    except:
        print(f'{bots.email} failed to like the media')

def massLiker(bots, link):
    try:
        for i in len(bots):
            liker(bots[i], link)
    except:
        print("There was an error")