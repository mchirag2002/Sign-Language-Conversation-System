import pyttsx3
import speech_recognition as sr
import datetime
import os
import time
from google_images_search import GoogleImagesSearch
from PIL import Image
import creds

a = pyttsx3.init()
voices = a.getProperty('voices')
a.setProperty('voice', voices[1].id)

gis = GoogleImagesSearch(
    creds.api_key, creds.api_token)


hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    a.say("Good Morning!!")
elif hour >= 12 and hour < 18:
    a.say("Good afternoon!")
else:
    a.say("Good evening!")
a.say("Hello, what do you want to communicate?")

#a.say("Hello there! I am Edith! What can I do for you today?")
a.runAndWait()

r = sr.Recognizer()
x = 1
while x > 0:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1

        print("Listening....")
        audio = r.listen(source, timeout=5)
    try:
        text = r.recognize_google(audio)
        query = text.lower()
        print(query)
        #qu = 'friend'
        que = query + ' sign language'
        print(query)
        print(que)
        _search_params = {
            'q': que,
            'num': 1,
            'fileType': 'jpg',
            'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'}
        gis.search(search_params=_search_params,
                   path_to_dir='C:\\Users\\DELL\\Desktop\\New folder\\', custom_image_name=query)

        #p = 'C:\\Users\\DELL\\Desktop\\New folder\\hello.jpg'
        im = Image.open(
            r"C:\\Users\\DELL\\Desktop\\New folder\\{}.jpg".format(query))
        im.show()
        # time.sleep(10)
        #os.remove("C:\\Users\\DELL\\Desktop\\New folder\\hello.jpg")
    except:
        pyttsx3.speak(
            "Sorry I am unable to understand. Can you please repeat.")
        print("Sorry I am unable to understand. Can you please repeat.")
