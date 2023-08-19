import speech_recognition as sr
import os
def say(text):
    os.system(f"say {text}")
def catchTalk():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-in")
        print(f"User stated: {query}")
        return query


if __name__ == '__main__':
    print('PyCharm')
    say("Hi, im Adam, How can i assist you toodayyy?")

    while True:
        print("Listening...")
        text = catchTalk()
        say(text)
