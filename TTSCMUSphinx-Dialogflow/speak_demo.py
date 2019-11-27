# coding=utf-8
#pip install dialogflow
# sudo apt-get install portaudio19-dev   
# sudo apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev
# pip install pyaudio  
# pip install pocketsphinx

import time
from speak1 import  LangParams, ListenLoop

lang_en = LangParams("en", "en-US",
                     phrases = ["Wark", "Vark listen to me",
                      "ukrainska", "ukrajinska", "ukraine",
                      "find box", "find the box", "find the bottle","find bottle"],
                     start_phrase = "I'm ready! Talk to me"
                     )
# lang_ua = LangParams("uk", "uk-UA",
#                      phrases= ["Варк",
#                                "Шукай бутилку", "шукай коробку", "Варк, шукай бутилку"],
#                      start_phrase= "Ja gottov dopomohty")

def df_action(action):#action in the intent to be continued, like a interaction that isnt lost, this case it checks if user asked to change language
    #if (action == "lang_ua"):
        #listen.change_lang(lang_ua)
        # raise OutOfRange('Restart stream!')
    if (action == "lang_en"):
        listen.change_lang(lang_en)


listen =  ListenLoop(rate=16000,#44100
                     project_id="your_project_id",
                     df_action = df_action,
                     lang = lang_en,
                     device=2 #'aplay -L' to check devices and 'python usb.py', no caso sysdefault deu
                     )
#{'defaultSampleRate': 44100.0, 'defaultLowOutputLatency': 0.008707482993197279, 'defaultLowInputLatency': -1.0, 'maxInputChannels': 0L, 'structVersion': 2L, 'hostApi': 0L, 'index': 2, 'defaultHighOutputLatency': 0.034829931972789115, 'maxOutputChannels': 2L, 'name': u'Plantronics Headset: USB Audio (hw:1,0)', 'defaultHighInputLatency': -1.0}
#https://stackoverflow.com/questions/31073667/getting-ioerror-errno-invalid-number-of-channels-9998-when-using-mic-with-py
# while(True):
#     time.sleep(1)
listen.run()