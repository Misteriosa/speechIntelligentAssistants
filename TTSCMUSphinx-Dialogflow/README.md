 Quickstart- interactions with the Dialogflow API Tutorial:
 https://cloud.google.com/dialogflow/docs/quick/api#detect-intent-text-python

 # [CMUSphinx STT - Dialogflow - (TODO)TTS] loop

 Python CMUsphinx Speech To Text to Dialogflow to ? Text To Speech API

This class creates Listen Loop - listening user voice, converting to text with CMUsphinx STT , then process with Dialogflow, achieves a feedback and reading with ? TTS API

Uses (Decoder) instead of (speech_recognition module for python with support for pocketsphinx) from pocketsphinx

 speak.py (i made, not finished) uses CMUsphinx and generator and asynchronous callback in the audio_interface.open()
 speak1.py (i made, finished/works) uses CMUsphinx and just a 'while True', have to check if works 
 speakOriginal.py uses google cloud
 speak3 (i made, not finished) uses speech_recognition module

 Tested on:
 * Ubuntu 16.04
 * Ubuntu 18.

CMUsphinx model training data 
    sample rate         16khz
    number of channels  1, 16bit Mono
    bandwidth           
16khz model works for 16khz audio. 8khz model works for both 16khz and 8khz but less accurate.

PERFORMANCE TEST
measure of time is started from the moment the decoder gets data from the buffer till after the intent returns

