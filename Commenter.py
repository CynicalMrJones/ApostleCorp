import instagrapi
from instagrapi import Client


def commenter(bots, link, comment):
    botInstant = Client(request_timeout=60)
    try:
        botInstant.login(bots.email, bots.password)
    except:
        print(f'{bots.email} failed to post a comment')

    postedComment = botInstant.media_comment(CommentID, comment)
    #postedComment.dict()
    print("The operation was completed successfully")
