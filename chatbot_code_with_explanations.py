import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import time

#This explanation script should be run by code blocks for learning purposes,
# the chatbot_final-code_only script can be run as a whole if need be

"""
#An example of a greet method called within a person class

class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

# Create an instance of the Person class
person = Person("John")

# Call the greet method on the person instance
person.greet()  # Output: "Hello, my name is John"
 
#The method accesses the name attribute of the person instance and prints a greeting using the name.
"""

# Let's start by creating an empty class, then build it up.
#In python, classes usually have a method (function) which is called on an instance
class ChatBot(): #a chatbot class
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name

# Execute the AI
#if __name__ == "__main__":
    #ai = ChatBot(name="Ibot")

#Converting speech to text is the first major assignment for our AI bot via the speech recognition lib.
#That is, voice/audio inputs into text formats. We'll make use of Google API

#speech to text
#import speech_recognition as sr - where we need it from, but better to import in the first lines above

    def speech_to_text(self): #speech to text method function
        recognizer = sr.Recognizer() #a recogniser instance
        with sr.Microphone() as mic:
            print("listening to...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me -->", self.text)
        except:
            print("me --> ERROR")

# Execute the AI
#if __name__ == "__main__":
#    ai = ChatBot(name="Ibot")
#    while True:
#        ai.speech_to_text()

#you can run each code block individually to test.

#now let's give our chatbot the avenue to recognise its name when called upon, also responding accordingly
#and how to listen to specific words.
#the bot will be designed to not reply everything. Also, it needs a text to speech ability to reply,
#this is possible using Google Text to Speech lib

##this is where these imports below are required;
#from gtts import gTTS
#import os - Note: Try to import from the start of the script.

    @staticmethod
    def text_to_speech(text):
        print("Ibot --> ", text)
        speaker = gTTS(text=text, lang='en', slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3") #for macbook->afplay or for windows use->start
        os.remove("res.mp3")

#The wake_up method checks whether the chatbot's name is mentioned in the input text.
# The action_time method returns the current time.
    def wake_up(self, text):
        return True if self.name in text.lower() else False
#uncomment to run code
#Those two functions can be used like this
# Execute the AI
#if __name__ == "__main__":
#     ai = ChatBot(name="Ibot")
#     while True:
#         ai.speech_to_text()
#         ## wake up
#         if ai.wake_up(ai.text) is True:
#             res = "Hello I am Ibot the AI, what may I do for you?"
#         ai.text_to_speech(res)

#Let's UPGRADE our chatbot to do simple commands like Siri, Google Assistant etc
#For example, the chatbot should be able to answer accurately the precise time- when asked.
#To add this function to the chatbot class, see code continuation below;

#import datetime
    @staticmethod
    def action_time(self):
        return datetime.datetime.now().time().strftime('%H:%M')
    #and run the script after reading the above function to the AI class

#TIP (@staticmethod): This means that the text_to_speech and action_time methods can be called directly on the ChatBot
# class, without needing to create an instance of the class first.


#Introduction of Transformers package by Hugging Face (making the bot intelligent and not scripted)
#below;
#to be exact, we've used the DialogGPT trained and created by Microsoft based on millions of conversations and ongoing chats on the Reddit platform at a given interval of time.

import transformers
nlp = transformers.pipeline("conversational",
                            model="microsoft/DialoGPT-medium")
#Let's try it out
input_text = "hello!"
nlp(transformers.Conversation(input_text), pad_token_id=50256)

#to avoid getting a whole conversation back as the pipeline,
# let's extract only the response of the chatbot

chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
res = str(chat)
res = res[res.find("bot >> ")+6:].strip()

'''
# Run the AI
if __name__ == "__main__":
    ai = ChatBot(name="Ibot")
    while True:
        ai.speech_to_text()
    ## waking up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Ibot the AI, what may I do for you?"
         ## do any action
        elif "time" in ai.text:
            res = ai.action_time()
         ## respond politely
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(
                  ["you're welcome!","anytime!",
                   "no problem!","cool!",
                   "I'm here if you need me!","Cheerst!"])
        ai.text_to_speech(res)
'''

# Final -Running the AI
if __name__ == "__main__":

    ai = ChatBot(name="Ibot")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

    ex = True
    while ex:
        ai.speech_to_text()

        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Ibot the AI, what may I do for you?"

        ## action time
        elif "time" in ai.text:
            res = ai.action_time()

        ## respond politely
        elif any(i in ai.text for i in ["thank", "thanks"]):
            res = np.random.choice(
                ["My pleasure", "you're welcome!", "anytime!", "no problem!", "cool!", "I'm here if you need me!", "don't mention"])

        elif any(i in ai.text for i in ["exit", "close"]):
            res = np.random.choice(["Have a good day", "Bye", "Goodbye", "Cheers!"])

            ex = False
        ## conversation
        else:
            if ai.text == "ERROR":
                res = "Sorry, come again?"
            else:
                chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot >> ") + 6:].strip()

        ai.text_to_speech(res)
    print("----- Shutting down Ibot -----")


#The last code block at the end runs the chatbot. It creates an instance of the
#ChatBot class, named ai, and enters a loop that listens for speech, processes it, and responds with
#text-to-speech. The chatbot can recognise when it is being called by its name, respond with the
#current time when asked, and thank the user when appropriate. It can also exit the loop and shut down
#when told to do so. The chatbot uses the transformers library and the DialoGPT model to generate
#responses to other kinds of input.


