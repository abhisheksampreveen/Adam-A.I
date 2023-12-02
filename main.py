import speech_recognition as sr
import os
import webbrowser
import datetime
import requests
import json


def say(text):
    os.system(f"say {text}")


# weather
api_key = 'your weather api here'
def weather():
    city = "mangalore"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']
    temp = round(temp - 273.15, 2)
    print(f"The temperature in {city} is {temp} degrees Celsius")
    say(f"The temperature in {city} is {temp} degrees Celsius")
    if 'main' in data:
        temp = data['main']['temp']
    else:
        # Handle the case where 'main' key is missing
        temp = None
    return temp


# microphone and output
def catchTalk():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User stated: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry"
        
def password():
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()_+-="
    numbers = "0123456789"

    all = lower + upper + symbols + numbers
    length = 16
    password = "".join(random.sample(all, length))
    print(password)
    return password



# addition and subtraction fo two numbers

def perform_operation(operation, num1, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        result = 'Invalid operation'
    return result


# starting of the code
if __name__ == '__main__':
    print('AdamAI Chatbot')
    say("Hi, how can i help you today...?")
    while True:
        print("listening..")
        query = catchTalk()
        sites = [["YouTube", "https://www.youtube.com"], ["Wikipedia", "https://www.wikipedia.com"],
                 ["Google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening.... {site[0]} .....")
                webbrowser.open(site[1])
        if "open music" in query:
            musicPath = "your music path"
            import subprocess, sys

            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, musicPath])
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"sir the time is{hour}:{min} ")
        if "open your appname" in query:
            codePath = "application path"
            import subprocess, sys

            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, codePath])
        if "hello" in query:
            say("Hello sir")
        if "how are you" in query:
            say("doing great!   ... what about you? sir.")


        if "what can you do" in query:
            say("well i can do a variety of things like opening apps opening websites, opening apps, play music and much more ")
        if "what is your name" in query:
            say("My name is Adam")
        if "which version are you" in query:
            say("I am currently of version 1.0")
        if "suggest a strong password" in query:
            say("the password is") 
            password()
        if "what language are you using" in query:
            say("I am currently using Python")
        if "what type of AI are you " in query:
            say("I am narrow or weak ai like alexa or siri")
        if "do you know Maria" in query:
            say("yes, i know that fool")
        if "tell me something funny" in query:
            say("Of course sir. Why did the scarecrow win an award? Because he was outstanding in his field")
        if "tell me a joke" in query:
            say("What do you call a fake noodle ? An impasta.")
        if "what is your favorite color" in query:
            say("I like purple")
        if "what is your favorite food" in query:
            say("I like pizza")
        if "what is an AI" in query:
            say("An artificial intelligence is a computer program that can think like humans and mimic their behaviors")
        if "what is a computer program" in query:
            say("A computer program is a set of instructions that are executed by a computer")
        if "the weather" in query:
            weather()
        if "do you know Maria?" in query:
            say("yeah, i know that fool")
        if 'add' in query:
            operation = 'add'
        if 'subtract' in query:
            operation = 'subtract'
        if 'multiply' in query:
            operation = 'multiply'
        if 'divide' in query:
            operation = 'divide'
        if "bye" in query:
            say("goodBye sir")
            break
