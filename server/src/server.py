from visionHandler import VisionHandler
from translationHandler import TranslationHandler
from storageHandler import StorageHandler
from scraper import Scraper

# Linguo Google Cloud python server process

class Server:
    def __init__(self, api_key_path):
        self.api_key_path = api_key_path

        self.visionHandler = VisionHandler(api_key_path)
        self.translationHandler = TranslationHandler(api_key_path)
        self.scraper = Scraper()
        self.storageHandler = StorageHandler(api_key_path)

    # push the files from the get unprocessed files, processes the
    def processImage(self, localImagePath, remoteImagePath, language):
        # Step 1: Get context for the image
        labelInfo = self.visionHandler.process_image(remoteImagePath)

        # Step 2: Pass to webscraper for sentence phrase
        sentence = self.Scraper.scrape(labelInfo[0])

        # Step 3: Translate the sentence based on the phrase
        translatedLabels = list()
        translatedLabels.add(translationHandler.translate(sentence, language))

        # GET DOWNLOADED IMAGE PATH
        # TODO: Step 5: Get overlay of image
        self.overlayHandler.process_image(localImagePath, translatedLabels)

        # TODO: Step 6: Output the image + text to speech translated text
        self.storageHandler.uploadNewPhoto(,self.storageHandle.getBucket())
        output.write(translatedLabels)


# jsonfile = 'Linguo-495a24a54222.json'
# s = Server(jsonfile)
# s.getUnprocessedFiles()

