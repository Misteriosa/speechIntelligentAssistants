#from GTTS import GTTS

class Methods:

    #def __init__(self):
        #self.tts = GTTS()

    def detect_intent_texts(self, text, speak = False):
        #execute the hardcoded method for a given utterance.
        #print "Microphone detected:   --",text,"--"
        
        if text == 'CHECK ALARM' or text == 'CHECK THE ALARM':
            print ("\nAlarm is ON \n")
        if text == 'WHERE IS THE ASHTRAY':
            print ("\nThe ashtray is near the wheel \n")
        if text == 'WHERE IS THE STEER WHEEL' or text == 'WHERE IS THE STEERWHEEL':
            print ("\nThe steer wheel is infront \n")
        #else:
            #print ("\nNo method associated \n")
       
        # if response.query_result.fulfillment_text != "" and speak:
        #     self.tts.speak(response.query_result.fulfillment_text)
