
import os
from instagrapi import Client

dirname = os.getcwd()

def poster(bots):
    botInstant = Client(request_timeout=60)
    try:
        botInstant.login(bots.email, bots.password)
        img = input("Please input the path to your photo (must be a .jpg or a .jpeg)")
        path = dirname + "/" + img
        capt = input("Input the photo caption :: ")
        botInstant.photo_upload(path, capt)
        print("This operation was completed successfully!")
    except:
        print(f'{bots.email} failed to login')


