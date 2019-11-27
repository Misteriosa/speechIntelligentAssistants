#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from os import environ, path
from pocketsphinx import *
#from sphinxbase import *
import time

import os
#from pocketsphinx import LiveSpeech, get_model_path
#uses LiveSpeech library https://pypi.org/project/pocketsphinx/,
#the other options are Decoder (also possible use different model),  speech_recognition(seems not possible use different model)
MODELDIR = os.getcwd()#getcwd() returns current working directory of a process.
#MODELDIR =get_model_path() gets the model from the installed pocketsphinx
#MODELDIR = "/home/ubu/pocketsphinx-5prealpha/model"
#print 'modeldir .............'+MODELDIR
import re
import sys
from methods import Methods

class ListenLoop:
    #    def __init__(self, lang, device=0, rate=44100):
    def __init__(self, rate=44100):#device is the audio interface, have to check the index
        self.RATE = rate
        self.CHUNK = 2048# int(rate / 10)  # 100ms
        #self.tts = GTTS()
        self.hardocdedMethods = Methods()
        #self.device = device

    def run(self):
        speech = LiveSpeech(
            verbose=False,
            sampling_rate=self.RATE,
            buffer_size=self.CHUNK,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(MODELDIR, 'en-us/en-us'),
            lm=os.path.join(MODELDIR, 'en-us/9952.lm'),
            dic=os.path.join(MODELDIR, 'en-us/9952.dic')
        )

        print("started stream")
        print "Say something!"
        try:
            start_time = time.clock() # CPU time expressed in seconds
            #time.time() # Wall wall-clock time expressed in seconds
            for phrase in speech:
                text=str(phrase)
                print(text)
                if text=="": #se trasncript è una string vuota, non chiama detect_intent...
                    print ('couldnt translate any utterance')
                else:
                    self.hardocdedMethods.detect_intent_texts(text)
                    end_time = time.clock()
                    try:
                        print end_time-start_time," seconds\n"
                    except:
                        print("time error")
                print "Say something!"  
                #start_time = time.clock() 
        except:
            print("erro")       




