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

    #method to get files from the bucket
    def getUnprocessedFiles(self):
        # returns the file names of things to process
        bucket = self.storageHandler.getBucket()
        blobs = self.storageHandler.getBlobs(bucket)
        return bucket

##        ######
##        oneFile = input("Enter one file to download: ")
##        self.storageHandler.downloadOneBlob(bucket, oneFile)

    # TODO: pass in imagePath, and language from a tuple

    # push the files from the get unprocessed files, processes the
    def processImage(self, localImagePath, remoteImagePath, language):
        # Step 1: Get context for the image
        labelInfo = self.visionHandler.process_image(remoteImagePath)

        # TODO: Step 3: Send context to web scraper for sentences
        sentence = self.Scraper.scrape(labelInfo[0])

        translatedLabels = list()
        # Step 4: Send sentence/context to translator
        translatedLabels.add(translationHandler.translate(sentence, language))

        # GET DOWNLOADED IMAGE PATH
        # TODO: Step 5: Get overlay of image
        self.overlayHandler.process_image(localImagePath, translatedLabels)

        # TODO: Step 6: Output the image + text to speech translated text
        self.storageHandler.putImage()
        output.write(translatedLabels)


jsonfile = 'Linguo-495a24a54222.json'
s = Server(jsonfile)
s.getUnprocessedFiles()

