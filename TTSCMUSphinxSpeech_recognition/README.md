 Quickstart- interactions with the Dialogflow API Tutorial:
 https://cloud.google.com/dialogflow/docs/quick/api#detect-intent-text-python

 # [CMUSphinx STT - CMUSphinx Method Association - (TODO)TTS] loop

TODO - see how integrate own model folder

This class creates Listen Loop - listening user voice, converting to text with CMUsphinx STT , then calls method for utterance string, and (TODO)reads with a TTS API

Uses (speech_recognition) module instead of (Decoder). For python with support for pocketsphinx 

 speak3 () uses speech_recognition module

 Tested on:
 * Ubuntu 16.04
 * Ubuntu 18.

CMUsphinx model training data 
    sample rate         16khz
    number of channels  1, 16bit Mono
    bandwidth           
16khz model works for 16khz audio. 8khz model works for both 16khz and 8khz but less accurate.

Convert the trained models .lm and .dic to language-model.lm.bin and pronounciation-dictionary.dict and put them under /speech_recognition/pocketsphinx-data/en-US
To convert lm to lm.bin: inside sphinxbase folder: sphinx_lm_convert -i your_model.lm.(dmp) -o your_model.lm.bin