from visionHandler import VisionHandler
from translationHandler import TranslationHandler
from storageHandler import StorageHandler
from scraper import Scraper
from overlayHandler import OverlayHandler

# Linguo Google Cloud python server process

class Server:
    def __init__(self, api_key_path):
        self.api_key_path = api_key_path

        self.visionHandler = VisionHandler(api_key_path)
        self.translationHandler = TranslationHandler(api_key_path)
        self.scraper = Scraper()
        self.storageHandler = StorageHandler(api_key_path)
        self.overlayHandler = OverlayHandler()

    # push the files from the get unprocessed files, processes the
    def processImage(self, localImagePath, remoteImagePath, language):
        # Step 1: Get context for the image
        labelInfo = self.visionHandler.process_image(remoteImagePath)
        print(labelInfo[0].description)

        # Step 2: Pass to webscraper for sentence phrase
        sentence = self.scraper.scrape(labelInfo[0].description)
        print(sentence)

        # Step 3: Translate the sentence based on the phrase
        translatedLabels = list()
        translatedLabels.append(self.translationHandler.translate(sentence, language))
        print(translatedLabels)

        # GET DOWNLOADED IMAGE PATH
        # Step 5: Get overlay of image
        overlayImagePath = self.overlayHandler.add_overlay(localImagePath, sentence)

        # Step 6: Output the image + text to speech translated text
        #self.storageHandler.uploadNewPhoto(overlayImagePath, self.storageHandle.getBucket())
        return (translatedLabels, overlayImagePath)


# jsonfile = 'Linguo-495a24a54222.json'
# s = Server(jsonfile)
# s.getUnprocessedFiles()

api_key = r"C:\Users\kelly\Desktop\translate\translate_test.json"
sh = StorageHandler(api_key)
localPath = r"cat.jpg"
remotePath = sh.uploadNewPhoto(localPath, sh.getBucket())

s = Server(api_key)

s.processImage(localPath, remotePath, "spanish")
