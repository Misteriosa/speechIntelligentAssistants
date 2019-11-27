#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from os import environ, path
from pocketsphinx import *
from sphinxbase import *
import time

MODELDIR = os.getcwd()
#MODELDIR =get_model_path() gets the model from the installed pocketsphinx
#MODELDIR = "/home/ubu/pocketsphinx-5prealpha/model"
#print 'modeldir .............'+MODELDIR
config = Decoder.default_config()

config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/9952.lm'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/9952.dic'))

config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)
import pyaudio


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


#the service credential needs owner permission
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + "/yourdialogflowauthkey.json" 
#getcwd() returns current working directory of a process.

class ListenLoop:
    def __init__(self, project_id, df_action, lang, device=0, rate=44100):#device is the audio interface, have to check the index

        self.RATE = rate
        self.CHUNK = 2048# int(rate / 10)  # 100ms
        #self.client = speech.SpeechClient()
        #self.tts = GTTS()
        self.lang = lang
        self.df = DF_intents(project_id, project_id + "1", df_action, debug=True)
        self.stream = object()#returns a featureless object which is a base for all classes
        self.device = device

    def run(self):
        #main 'listen and recognition' function
        try:
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=self.RATE, input_device_index=self.device, input=True, frames_per_buffer=self.CHUNK)
            stream.start_stream()

            in_speech_bf = False
            decoder.start_utt()
            print("started stream")
            print "Say something!"
            while True:
                buf = stream.read(self.CHUNK, exception_on_overflow = False)
                if buf:
                    #print(buf)
                    start_time = time.clock() # CPU time expressed in seconds
                    #time.time() # Wall wall-clock time expressed in seconds
                    decoder.process_raw(buf, False, False)
                    
                    if decoder.get_in_speech() != in_speech_bf:
                        #time.sleep(3)
                        #print "diferent"
                        in_speech_bf = decoder.get_in_speech()
                        #print in_speech_bf
                        if not in_speech_bf:
                            #print "not in_speech_bf   is TRUE"
                            decoder.end_utt()
                            transcript = decoder.hyp().hypstr
                            if not transcript: #se trasncript è una string vuota, non chiama detect_intent...
                                print ('decoder couldnt translate any utterance')
                            else:
                                print ('Microphone detected:   "'+ transcript +'"')   
                                #UNCOMMENT FOR INTENT DETECTION, WILL SPEND CREDITS                 
                                #self.df.detect_intent_texts(transcript, self.lang.lang)
                                end_time = time.clock()
                            try:
                                print end_time-start_time," seconds\n"
                            except:
                                print("time error")
                            print "Say something!"  
                            decoder.start_utt()

                        else:
                            print "utterance break, processing..."
                else:
                    break
            decoder.end_utt()
            stream.stop_stream()
            stream.close()
            p.terminate()
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



