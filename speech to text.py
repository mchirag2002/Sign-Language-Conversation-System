import pyttsx3
import speech_recognition as sr
import datetime
from PIL import Image
import time

a = pyttsx3.init()
voices = a.getProperty('voices')
a.setProperty('voice', voices[1].id)

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
        word = []
        word = query.split(" ")
        print(word)
        for a in word:
            for i in range(len(a)):
                if 'a' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\a.jpg")
                    im.show()
                    time.sleep(1)
                elif 'b' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\b.jpg")
                    im.show()
                    time.sleep(1)

                elif 'c' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\c.jpg")
                    im.show()
                    time.sleep(1)

                elif 'd' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\d.jpg")
                    im.show()
                    time.sleep(1)

                elif 'e' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\e.jpg")
                    im.show()
                    time.sleep(1)

                elif 'f' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\f.jpg")
                    im.show()
                    time.sleep(1)

                elif 'g' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\g.jpg")
                    im.show()
                    time.sleep(1)

                elif 'h' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\h.jpg")
                    im.show()
                    time.sleep(1)

                elif 'i' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\i.jpg")
                    im.show()
                    time.sleep(1)

                elif 'j' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\j.jpg")
                    im.show()
                    time.sleep(1)

                elif 'k' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\k.jpg")
                    im.show()
                    time.sleep(1)

                elif 'l' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\l.jpg")
                    im.show()
                    time.sleep(1)

                elif 'm' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\m.jpg")
                    im.show()
                    time.sleep(1)

                elif 'n' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\n.jpg")
                    im.show()
                    time.sleep(1)

                elif 'o' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\o.jpg")
                    im.show()
                    time.sleep(1)

                elif 'p' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\p.jpg")
                    im.show()
                    time.sleep(1)

                elif 'q' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\q.jpg")
                    im.show()
                    time.sleep(1)

                elif 'r' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\r.jpg")
                    im.show()
                    time.sleep(1)

                elif 's' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\s.jpg")
                    im.show()
                    time.sleep(1)

                elif 't' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\t.jpg")
                    im.show()
                    time.sleep(1)

                elif 'u' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\u.jpg")
                    im.show()
                    time.sleep(1)

                elif 'v' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\v.jpg")
                    im.show()
                    time.sleep(1)

                elif 'w' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\w.jpg")
                    im.show()
                    time.sleep(1)

                elif 'x' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\x.jpg")
                    im.show()
                    time.sleep(1)

                elif 'y' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\y.jpg")
                    im.show()
                    time.sleep(1)

                elif 'z' == a[i]:
                    im = Image.open(
                        r"E:\PROJECTS\SIH\signs\z.jpg")
                    im.show()
                    time.sleep(1)

                else:
                    print("Sorry I am unable to understand. Can you please repeat.")
                    pyttsx3.speak(
                        "Sorry I am unable to understand. Can you please repeat.")
            time.sleep(1)

    except:
        pyttsx3.speak(
            "Sorry I am unable to understand. Can you please repeat.")
        print("Sorry I am unable to understand. Can you please repeat.")
