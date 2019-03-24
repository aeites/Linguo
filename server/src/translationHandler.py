import os

from google.cloud import translate

texttotext = {
    "danish":"da",
    "dutch":"nl",
    "english":"en",
    "french":"fr",
    "german":"de",
    "italian":"it",
    "japanese":"ja",
    "korean":"ko",
    "norwegian":"no",
    "polish":"pl",
    "portuguese":"pt",
    "russian":"ru",
    "slovak":"sk",
    "spanish":"es",
    "swedish":"sv",
    "turkish":"tr",
    "ukrainian":"uk"
}

texttospeech = {
    "danish":"da-DK",
    "dutch":"nl-NL",
    "english":"en-US",
    "french":"fr-FR",
    "german":"de-DE",
    "italian":"it-IT",
    "japanese":"ja-JP",
    "korean":"ko-KR",
    "norwegian":"nb-NO",
    "polish":"pl-PL",
    "portuguese":"pt-PT",
    "russian":"ru-RU",
    "slovak":"sk-SK",
    "spanish":"es-ES",
    "swedish":"sv-SE",
    "turkish":"tr-TR",
    "ukrainian":"uk-UA"
}

class TranslationHandler:
    # create translation object
    # pass in text to translate and target language
    def __init__(self, credentials_path):
        # authentication
        self.authenticate(credentials_path)
        # instantiate client
        self.translate_client = translate.Client()

    # sets target language code
    def set_target_language(self):
        return texttotext[self.language]


    # returns translated text
    def translate(self, text, language):
        self.text = text
        self.language = language
        translation = self.translate_client.translate(
            self.text,
            self.set_target_language()
            )
        return translation['translatedText']

    # returns language code for text-to-speech translation
    def get_TTS_language_code(self, input):
        return texttospeech[input]

    def authenticate(self, credentials_path):
        # Set the path to the credentials
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    def getLanguageList(self):
        return list(texttotext.keys())


## test_path = "C:\\Users\\kelly\\Desktop\\translate\\translate_test.json"
## t = TranslationHandler(test_path)
## print(t.translate('Hello, world!', 'Spanish'))


# testing

# text to text language codes
# testtotext = ["Danish" "Dutch", "English", "French", "German", "Japanese", "Italian", "Korean", "Norwegian", "Polish", "Portuguese", "Slovak", "Russian", "Spanish", "Swedish", "Turkish", "Ukrainian"]
#
# for x in testtotext:
#    ## set variables
#    #path = 'C:\\Users\\kelly\\Downloads\\My First Project-39acdbd3bbc1.json'
#    text = 'Hello, world'
#    lang = x
#
#    path = r"D:\Users\Chana-PC\Documents\Linguo\server\src\api-key.json"
#
#    ## create translation object
#    t = Translate_Handler(r"D:\Users\Chana-PC\Documents\Linguo\server\src\translate-key.json")
#
#    ## run translation
#    trans = t.translate(text, lang)
#
#    print(trans)                        # print translated text
#    print(t.set_target_language())      # print text-to-text code of target language
#    print(t.get_TTS_language_code())    # print text-to-speech code of target language
#    print("*****************")          # separator
