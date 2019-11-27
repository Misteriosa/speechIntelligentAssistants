#from GTTS import GTTS

class Methods:

    #def __init__(self):
        
        #self.tts = GTTS()

    def detect_intent_texts(self, text, speak = False):
        #execute the hardcoded method for a given utterance.
        if text == 'check alarm' or text == 'check the alarm' :
            print ("\nAlarm is ON \n")
        if text == 'where is the ashtray':
            print ("\nThe ashtray is near the wheel \n")
        if text == 'where is the steer wheel' or text == 'where is the steerwheel':
            print ("\nThe steer wheel is infront \n")
        #else:
            #print ("\nNo method associated \n")
       
        # if response.query_result.fulfillment_text != "" and speak:
        #     self.tts.speak(response.query_result.fulfillment_text)
