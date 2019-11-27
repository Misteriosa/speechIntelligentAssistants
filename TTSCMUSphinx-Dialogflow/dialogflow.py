import dialogflow_v2 as dialogflow
#from GTTS import GTTS

class DF_intents:

    def __init__(self, project_id, session_id, action_func,debug=False):
        self.project_id = project_id
        self.session_id = session_id
        self.action_func=action_func
        #self.tts = GTTS()
        self.debug=debug

    def detect_intent_texts1(self,texts, language_code, speak = False):
        """Returns the result of detect intent with texts as inputs.
        Using the same `session_id` between requests allows continuation
        of the conversaion."""

        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(self.project_id, self.session_id)

        for text in texts:
            text_input = dialogflow.types.TextInput(
                text=text, language_code=language_code)

            query_input = dialogflow.types.QueryInput(text=text_input)
            try:
                response = session_client.detect_intent(
                    session=session, query_input=query_input)
            except:
                print ('types.QueryInput error')

            if self.debug:
                print('Detected intent: {} (confidence: {})\n'.format(
                    response.query_result.intent.display_name,
                    response.query_result.intent_detection_confidence))
                print('Fulfillment text: {}\n'.format(
                    response.query_result.fulfillment_text))
                print('Action text: {}\n'.format(
                    response.query_result.action))
               # print(response.query_result)
            # if response.query_result.fulfillment_text != "" and speak:
            #     self.tts.speak(response.query_result.fulfillment_text)
            if (response.query_result.action != ""): #do_action retrieved by the intent
                self.action_func(action = response.query_result.action)
                #action-The name of the action associated with the intent. Note: The action name must not contain whitespaces.

    def detect_intent_texts(self,text, language_code, speak = False):
        """Returns the result of detect intent with texts as inputs.
        Using the same `session_id` between requests allows continuation
        of the conversaion."""
        #print ('creating session')
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(self.project_id, self.session_id)
        print ('session created '+ self.session_id + ' with Dialogflow')

        try:
            text_input = dialogflow.types.TextInput(
                text=text, language_code=language_code)
        except:
            print ('types.TextInput error')
        try:
            query_input = dialogflow.types.QueryInput(text=text_input)
            #print query_input
        except:
            print ('types.QueryInput error')
        try:
            #print session
            response = session_client.detect_intent(session=session, query_input=query_input)
        except:
            print ('session_client.detect_intent error')

        if self.debug:
            print('Detected intent: {} (confidence: {})\n'.format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence))
            print('Fulfillment text: {}\n'.format(
                response.query_result.fulfillment_text))
            print('Action text: {}\n'.format(
                response.query_result.action))
           #print(response.query_result)
            
        # if response.query_result.fulfillment_text != "" and speak:
        #     self.tts.speak(response.query_result.fulfillment_text)
        if (response.query_result.action != ""): #do_action retrieved by the intent
            self.action_func(action = response.query_result.action)
            #action-The name of the action associated with the intent. Note: The action name must not contain whitespaces.



