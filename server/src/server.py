from visionHandler import VisionHandler
from translationHandler import TranslationHandler
from storageHandler import StorageHandler

# Linguo Google Cloud python server process

class Server:
    def __init__(self, api_key_path):
        self.api_key_path = api_key_path

        #self.visionHandler = VisionHandler(api_key_path)
        #self.translationHandler = TranslationHandler(api_key_path)
        self.storageHandler = StorageHandler(api_key_path)

    #method to get files from the bucket
    def getUnprocessedFiles(self):
        # returns the file names of things to process
        bucket = self.storageHandler.getBucket()
        blobs = self.storageHandler.getBlobs(bucket)
        self.storageHandler.downloadAllBlobs(blobs)

        ######
        oneFile = input("Enter one file to download: ")
        self.storageHandler.downloadOneBlob(bucket, oneFile)

    # TODO: pass in imagePath, and language from a tuple

    # push the files from the get unprocessed files, processes the
    def processImage(self, language):
        # TODO: Step 1: Get list of all image? Maybe just one for now
        imagePath = self.storageHandler.getSingleImage()

        # Step 2: Get context for the image
        labelInfo = self.visionHandler.process_image(imagePath)

        # TODO: Step 3: Send context to web scraper for sentences

        # TODO: Step 3.1: process the label info
        processedLabels = labelInfo  # test code for now
        translatedLabels = list()
        # Step 4: Send sentence/context to translator
        for label in processedLabels:
            translatedLabels.add(translationHandler.translate(label, language))

        # TODO: Step 5: Get overlay of image
        overlayHandler.process_image(translatedLabels)

        # TODO: Step 6: Output the image + text to speech translated text
        self.storageHandler.putImage()
        output.write(translatedLabels)

        # api-endpoint
        print("Unsupported Method")


    # Method to draw the text onto the image
    def drawText(self, image, coordinates, text):
        print("Unsupported Method")


    def set_api_key(self):
        print("unsupported method")


    def startProcess(self):
    # find way to use translate API
        print("Unsupported method")

# TODO: have a file that provides the config for processing each image

jsonfile = 'Linguo-495a24a54222.json'
s = Server(jsonfile)
s.getUnprocessedFiles()

