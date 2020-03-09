import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import time
#youtubeimport wolframalpha
import os
import sys
import nltk
import io
import numpy as np
import random
import string
#import sklern
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings("ignore")
#for opening and reading the file
def chatbot():
    engine = pyttsx3.init('espeak')

    def speak(audio):
        print('Computer: ' + audio)
        engine.say(audio)
        engine.runAndWait()

    path = '/home/p/Desktop/chatbot/pavan2.txt'
    f = open(path, 'r', errors='ignore')
    raw = f.read()
    raw = raw.lower()  # converts to lower case
    # punkt and wordnet should be downloaded
    # nltk.download('punkt')#punkt used to convert the list of words to strings
    # nltk.download('wordnet')#used as a dictionary where nltk find meanings and synonyms
    sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentenses
    word_tokens = nltk.word_tokenize(raw)  # converts to list of words
    # for testing the sent_tokens and word_tokens
    '''a = word_tokens[:2]
    print(a)
    b = sent_tokens[:2]
    print(b)
    '''

    # preprossesing of text
    lemmer = nltk.stem.WordNetLemmatizer()

    # word net is an dictionary  of english which is included in the nltk
    def LemTokens(tokens):
        return [lemmer.lemmatize(token) for token in tokens]

    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

    def LemNormalize(text):  # here text is the user input
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    # greeting
    GREETING_INPUT = ("hello", "hai", "hi", "sup", "greetings", "hey", "what'sap",)
    GREETING_OUTPUT = ["hai", "hi", "hello", "hi there", "i am gland you are taking to me"]

    def greeting(sentence):
        for word in sentence.split():
            if word.lower() in GREETING_INPUT:
                return random.choice(GREETING_OUTPUT)

    # vectorization for this we need to modules Tfidvectorizer and cosine_similarity
    # defining response
    def response(user_response):

        chatbot_response = ''
        sent_tokens.append(user_response)
        TfidVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidVec.fit_transform(
            sent_tokens)  # calling fit transform method and passing the sent tokens here the send tokens are converted into a vector form
        vals = cosine_similarity(tfidf[-1],
                                 tfidf)  # consine similarity for finding the similarity between the sentense tokens and user quations
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()  # for finding the matching btween quations and data stored in txt and converts it into a row matrix
        flat.sort()
        req_tfidf = flat[-2]
        if (req_tfidf != 0):  # it means there is nothing matching between the quation and data
            chatbot_response = chatbot_response + sent_tokens[idx]
            return chatbot_response
        else:
            chatbot_response = chatbot_response + " i am sorry idont understand you"
            return chatbot_response

    flag = True
    print("chatbot:My name is chatbot.I will answer your quaries about global warming. if you want to exit ,type bye")
    while (flag == True):
        r = sr.Recognizer()
        # url2 = 'https://www.youtube.com/'

        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            url = r.listen(source)
            # get = str(input('Command: '))
            user_response = r.recognize_google(url, language='en')

        user_response = user_response.lower()
        if (user_response != 'bye' or 'exit'):
            if (user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                print("chatbot:you are welcome..")
            else:
                if (greeting(user_response) != None):
                    print("chatbot:" + greeting(user_response))
                else:
                    print("chatbot:", end="")
                    print(response(user_response))
                    speak(response(user_response))

                    sent_tokens.remove(user_response)
        else:
            flag = False
            print("chatbot: Bye! take care..")
        # time.sleep(20)
chatbot()