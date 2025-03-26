import instagrapi
from instagrapi import Client

def poster(bots):
    botInstant = Client(request_timeout = 60)
    botInstant.login(bots.email, bots.password)
    img = input("Please input the path to your photo (must be a .jpg or a .jpeg)")
    capt = input("Input the photo caption")
    botInstant.photo_upload(img, capt)
    print("This operation was completed successfully!")
