import translationHandler
import texttospeechHandler

# authentication credential, input text and target language
path = "C:\\Users\\kelly\\Desktop\\translate\\translate_test.json"
text = "I put my pencil over there."
lang = "Spanish"

## instantiating text-to-text and text-to-speech translator objects
t = translationHandler.TranslationHandler(path)
s = texttospeechHandler.TextToSpeech(path)
print('TranslationHandler and TextToSpeech objects created')

## getting text translation and language code
translation = t.translate(text, lang)
TTS_language_code = t.get_TTS_language_code()
print(text)
print(translation)

## making audio translation
s.set_vars(translation, TTS_language_code)
s.get_audio()
