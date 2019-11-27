# speechIntelligentAssistants

python codes for CMUSphinx SST and google SST using different libraries.

No intent derivation:
	CMUSphinx local STT, 3 different libraries, local method derivation
		TTSCMUSphinxSpeech_recognition
		TTSCMUSphinxLiveSpeech
		TTSCMUSphinxPyAudio
	google cloud SST, speech_recognition library, local method derivation
		TTSGoogleSpeech_recognition

Intent derivation:
	CMUSphinx local STT, Decoder library, cloud Dialogflow intent derivation
		TTSCMUSphinx-Dialogflow
