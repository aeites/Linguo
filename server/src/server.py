from visionHandler import VisionHandler
from translationHandler import TranslationHandler
from storageHandler import StorageHandler

# Linguo Google Cloud python server process

class Server:
    def __init__(self, api_key_path):
        self.api_key_path = api_key_path

        self.visionHandler = VisionHandler(api_key_path)
        self.translationHandler = TranslationHandler(api_key_path)
        self.storageHandler = StorageHandler(api_key_path)

    #method to get files from the bucket
    def getUnprocessedFiles(self):
        # returns the file names of things to process
        print("Unsupported Method")

    # push the files from the get unprocessed files, processes the
    def processImages(self):
        # Step 1: Get list of all images? Maybe just one for now

        # Step 2: Get context for the image

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


