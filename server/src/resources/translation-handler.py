from google.cloud import translate
import os

#translate_client = translate.Client.from_service_account_json('C:\\Users\\kelly\\Downloads\\My First Project-39acdbd3bbc1.json')

class Translate_Handler:
    def __init__(self, credentials_path):
        self.authenticate(credentials_path)

    def translate(self, label, language):
        tranlation = translate_client.translate(
            label,
            target_language=language
            )
        return translation['translatedText']

    def authenticate(self, credentials_path):
        # Set the path to the credentials
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

t = Translate_Handler('C:\\Users\\kelly\\Downloads\\My First Project-39acdbd3bbc1.json')

text = 'Hello, world'
lang = 'sp'

print(t.translate(text, lang))
