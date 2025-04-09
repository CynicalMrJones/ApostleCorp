import instagrapi
import random
from instagrapi import Client


def commenter(bots, link, comment):
    botInstant = Client(request_timeout=60)
    try:
        botInstant.login(bots.email, bots.password)
        alink = botInstant.media_pk_from_url(link)
        mediaID = botInstant.media_id(alink)
        botInstant.media_comment(mediaID, comment)
    except:
        print(f'{bots.email} failed to post a comment ')

    print("The operation was completed successfully")


def massComment(bots, link, comments):
    commentRay = {}
    count = 0
    with open(comments, "r") as file:
        
        for line in file:
            commentRay[count] = line
            count += 1
    count = 0
    for i in bots:
        try:
            count = random.randrange(0,len(commentRay))
            commenter(bots[i], link, commentRay[count])
            commentRay.pop(count)
            count = 0
        except:
            print("There was an error. This operation is terminated")
    
