from google.cloud import storage
from google.cloud import vision
from gtts import gTTS
import pygame
import time

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

class AudioHandler:
        
    def produceAudio(self, labels, language):
        for i in range(0, len(labels)):
            myobj = gTTS(text=labels[i], lang=language, slow=False) 
            audioFile = "{}.mp3".format(labels[i])
            
            #saving audiofile
            myobj.save(audioFile)
            
            #playing audiofile
            pygame.mixer.init()
            pygame.mixer.music.load(audioFile)
            pygame.mixer.music.play()
            time.sleep(.8)

    def produceCode(self, language):
        return texttospeech[language]