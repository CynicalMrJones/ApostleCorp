import instagrapi
from instagrapi import Client

def commenter(bots, link, comment):
    botInstant = Client(request_timeout = 60)
    botInstant.login(bots.email, bots.password)
    CommentID = botInstant.media_id(botInstant.media_pk_from_url(link))
     
    postedComment = botInstant.media_comment(CommentID, comment)

    #postedComment.dict()

    print("The operation was completed successfully")
