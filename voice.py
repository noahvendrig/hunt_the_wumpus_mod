import speech_recognition as sr
import pyttsx3
# import pywhatkit
import datetime

import random

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk():
    repeat_list = [
        "Come Again",
        "Say that again please",
        "What did you say?",
        "Could you please repeat yourself",
        "Sorry I didnt hear that",
    ]
    text = random.choice(repeat_list)
    engine.say(text)
    engine.runAndWait()


def take_command():
    # while True:
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jesus" in command:
                command = command.replace("jesus", "")
                # print(command)
                return command
            else:
                return "none"
    except:
        return "none"
        # pass


# talk(random.choice(repeat_list))

# def run_ipa():
#     command = take_command()

#     if "time" in command:
#         time = datetime.datetime.now().strftime("%I:%M %p")
#         talk("The current time is " + time)

#     else:
#         repeat_list = [
#             "Come Again",
#             "Say that again please",
#             "What did you say?",
#             "Could you please repeat yourself",
#             "Sorry I didnt hear that",
#         ]
#         talk(random.choice(repeat_list))


# def main():
#     run_ipa()
#     # while True:
#     #     run_ipa()
