import os

from google.cloud import texttospeech

class TextToSpeech:
    def __init__(self, auth_credentials):
        self.authenticate(auth_credentials)
        self.client = texttospeech.TextToSpeechClient()

    def authenticate(self, credentials_path):
        ## Set the path to the credentials
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    def set_vars(self, input_text, target_language):
        self.synthesis_input = texttospeech.types.SynthesisInput(text=input_text)
        self.target_language = target_language  ## eventually, get target language from translation

    def get_audio(self):
        ## build voice request, select language code
        self.voice = texttospeech.types.VoiceSelectionParams(
            language_code=self.target_language,
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

        ## set type of audio file to return
        self.audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        ## perform text-to-speech request
        with open('output.mp3', 'wb') as out:
            out.write(self.client.synthesize_speech(self.synthesis_input, self.voice, self.audio_config).audio_content)
            print('Audio content written to file output.mp3')

        ## and return it (idk if this will be useful)
        return self.client.synthesize_speech(self.synthesis_input, self.voice, self.audio_config).audio_content

## testing
'''
path = 'C:\\Users\\kelly\\Desktop\\translate\\translate_test.json'
input1 = "What's up, fuckers."  ## set some input text
input2 = "Not much, fuckers"
lang1 = "en-US"                 ## set some target languages
lang2 = "da-DK"

T1 = TextToSpeech(path)     ## instantiate TextToSpeechObject
T1.set_vars(input1, lang1)  ## set input text to translate and target language
a = T1.get_audio()          ## generate audio file (also returns the audio written to output.mp3)
'''
