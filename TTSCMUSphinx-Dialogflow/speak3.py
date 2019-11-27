#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from os import environ, path
from pocketsphinx import *
from sphinxbase import *

#import pyaudio
import speech_recognition as sr


import re
import sys
import os
# from google.cloud import speech
# from google.cloud.speech import enums
# from google.cloud.speech import types
#from google.api_core.exceptions import OutOfRange
#from MicrophoneStream import MicrophoneStream
#from GTTS import GTTS
from dialogflow import DF_intents
import time

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + "/yourdialogflowauthkey.json" 
#getcwd() returns current working directory of a process.

class ListenLoop:
    def __init__(self, project_id, df_action, lang, device=0, rate=44100):#device is the audio interface, have to check the index

        self.RATE = rate#SHOULD IT BE 16000?????????????????????????????????????????????????????????
        self.CHUNK = 1024# int(rate / 10)  # 100ms
        #self.client = speech.SpeechClient()
        #self.tts = GTTS()
        self.lang = lang
        self.df = DF_intents(project_id, project_id + "1", df_action, debug=True)
        self.stream = object()#returns a featureless object which is a base for all classes
        self.device = device

    def run(self):
        #main 'listen and recognition' function
        try:
            r = sr.Recognizer()
            r.pause_threshold = 0.4 #default 0.8 s, recording until it encounters pause_threshold seconds of non-speaking
            speech = sr.Microphone(device_index=2)
            print("started stream")

            while True:
                with speech as source:
                    audio = r.adjust_for_ambient_noise(source)
                    buf = r.listen(source) # listen for the first phrase and extract it into audio data
                try:
                    if buf:
                        #print(buf)
                        recog = r.recognize_sphinx(buf)  # recognize speech using Sphinx
                        print("Sphinx thinks you said '" + recog + "'")
                        # self.df.detect_intent_texts([transcript], self.lang.lang)
                    else:
                        break
                except sr.UnknownValueError:  
                    print("Sphinx could not understand audio")  
                except sr.RequestError as e:  
                    print("Sphinx error; {0}".format(e))
        except:
            print("erro")
           

    def change_lang(self, lang):
        self.lang = lang
        #self.stream.stop()

class LangParams:
    def __init__(self, lang, locale, phrases, start_phrase):
        self.lang = lang
        self.locale = locale
        self.phrases = phrases
        self.start_phrase = start_phrase



