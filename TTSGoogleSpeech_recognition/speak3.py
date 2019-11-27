#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from os import environ, path
from pocketsphinx import *
from sphinxbase import *
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
#from methods import Methods
import time
from methods import Methods

#getcwd() returns current working directory of a process.

class ListenLoop:
    def __init__(self, device=0, chunk=2048, rate=16000):#device is the audio interface, have to check the index

        self.RATE = rate
        self.CHUNK = chunk # int(rate / 10)  # 100ms
        #self.tts = GTTS()
        #self.df = DF_intents(project_id, project_id + "1", df_action, debug=True)
        self.device = device
        self.hardocdedMethods=Methods()
    def run(self):
        try:
            try:
                r = sr.Recognizer()
                #r.pause_threshold = 0.4 #default 0.8 s, recording until it encounters pause_threshold seconds of non-speaking
                speech = sr.Microphone()
                #speech = sr.Microphone(device_index=self.device)
                print("started stream")
            except:
                print("microphone error")
            while True:
                with speech as source:
                    buf = r.adjust_for_ambient_noise(source)
                    print('say something:')
                    buf = r.listen(source) # listen for the first phrase and extract it into audio data
                try:
                    #print(buf)
                    recog = r.recognize_google(buf)  # recognize speech using Sphinx
                    print("google thinks you said '" + recog + "'")
                    self.hardocdedMethods.detect_intent_texts(recog)
                    #sleep(5)
                except sr.UnknownValueError:  
                    print("google could not understand audio")  
                except sr.RequestError as e:  
                    print("google error; {0}".format(e))
                except:
                    print ("nao sei erro")
        except:
            print("erro")
       

