#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from os import environ, path
from pocketsphinx import *
from sphinxbase import *

MODELDIR = os.getcwd()
#MODELDIR = "/home/ubu/pocketsphinx-5prealpha/model/"
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
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
from MicrophoneStream import MicrophoneStream
#from GTTS import GTTS
from dialogflow import DF_intents
import time

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + "/yourdialogflowauthkey.json" 
#getcwd() returns current working directory of a process.

class ListenLoop:
    def __init__(self, project_id, df_action, lang, device=0, rate=44100):#device is the audio interface, have to check the index

        self.RATE = rate#SHOULD IT BE 16000?????????????????????????????????????????????????????????
        self.CHUNK = 1024 # int(rate / 10)  # 100ms
        #self.client = speech.SpeechClient()
        #self.tts = GTTS()
        self.lang = lang
        self.df = DF_intents(project_id, project_id + "1", df_action, debug=True)
        self.stream = object()#returns a featureless object which is a base for all classes
        self.device = device

    def run(self):
        #main 'listen and recognition' function
        try:
            decoder.start_utt()
            print("started stream")
            with MicrophoneStream(self.RATE, self.CHUNK, self.device) as self.stream:
                audio_generator = self.stream.generator()
                # requests = (types.StreamingRecognizeRequest(audio_content=content)
                #             for content in audio_generator)
                # responses = self.client.streaming_recognize(streaming_config, requests)
                in_speech_bf = False
                for content in audio_generator:
                    #print("inside for")
                    decoder.process_raw(content, False, False) 
                    if decoder.get_in_speech() != in_speech_bf:
                        in_speech_bf = decoder.get_in_speech()
                        if not in_speech_bf:
                            decoder.end_utt()
                            print ('Result:')
                            transcript = decoder.hyp().hypstr
                            print transcript                            
                            #self.df.detect_intent_texts(transcript, self.lang.lang)
                            decoder.start_utt()
                # Now, put the transcription responses to use.
                # self.tts.speak(self.lang.start_phrase)
                # self.listen_loop(responses)
            decoder.end_utt()
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



