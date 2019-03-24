from google.cloud import translate
import os

texttotext = {
    "Danish":"da",
    "Dutch":"nl",
    "English":"en",
    "French":"fr",
    "German":"de",
    "Italian":"it",
    "Japanese":"ja",
    "Korean":"ko",
    "Norwegian":"no",
    "Polish":"pl",
    "Portuguese":"pt",
    "Russian":"ru",
    "Slovak":"sk",
    "Spanish":"es",
    "Swedish":"sv",
    "Turkish":"tr",
    "Ukrainian":"uk"
}

texttospeech = {
    "Danish":"da-DK",
    "Dutch":"nl-NL",
    "English":"en-US",
    "French":"fr-FR",
    "German":"de-DE",
    "Italian":"it-IT",
    "Japanese":"ja-JP",
    "Korean":"ko-KR",
    "Norwegian":"nb-NO",
    "Polish":"pl-PL",
    "Portuguese":"pt-PT",
    "Russian":"ru-RU",
    "Slovak":"sk-SK",
    "Spanish":"es-ES",
    "Swedish":"sv-SE",
    "Turkish":"tr-TR",
    "Ukrainian":"uk-UA"
}

class Translate_Handler:
    # create translation object
    # pass in text to translate and target language
    def __init__(self, credentials_path, text, language):
        self.text = text
        self.language = language
        # instantiate client
        self.translate_client = translate.Client()
        # authentication
        self.authenticate(credentials_path)

    # sets target language code
    def set_target_language(self):
        return texttotext[self.language]


    # returns translated text
    def translate(self):
        translation = self.translate_client.translate(
            self.text,
            self.set_target_language()
            )
        return translation['translatedText']

    # returns language code for text-to-speech translation
    def get_TTS_language_code(self):
        return texttospeech[self.language]

    def authenticate(self, credentials_path):
        # Set the path to the credentials
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path


# testing
'''
# text to text language codes
testtotext = [
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Japanese",
    "Italian",
    "Korean",
    "Norwegian",
    "Polish",
    "Portuguese",
    "Slovak",
    "Russian",
    "Spanish",
    "Swedish",
    "Turkish",
    "Ukrainian"
]

for x in testtotext:
    # set variables
    path = 'C:\\Users\\kelly\\Downloads\\My First Project-39acdbd3bbc1.json'
    text = 'Hello, world'
    lang = x

    # create translation object
    t = Translate_Handler(path, text, lang)

    # run translation
    trans = t.translate()

    print(trans)                        # print translated text
    print(t.set_target_language())      # print text-to-text code of target language
    print(t.get_TTS_language_code())    # print text-to-speech code of target language
    print("*****************")          # separator
'''
