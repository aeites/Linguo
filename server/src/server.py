from visionHandler.py  import VisionHandler
from translationHandler.py import TranslationHandler
# Linguo Google Cloud python server process

class Server:
    def __init__(self, api_key_path):
        self.api_key_path = api_key_path

        self.visionHandler = VisionHandler(api_key_path)
        self.translationHandler = TranslationHandler(api_key_path)

    def 



    #method to get files from the bucket
    def getUnprocessedFiles(self):
        # returns the file names of things to process
        print("Unsupported Method")

    # push the files from the get unprocessed files, processes the
    def processFiles(self):
        # api-endpoint
        URL = "http://maps.googleapis.com/maps/api/geocode/json"

        images = self.getUnprocessedFiles()


        print("Unsupported Method")

    # Method to draw the text onto the image
    def drawText(self, image, coordinates, text):
        print("Unsupported Method")


    def set_api_key(self):
        print("unsupported method")


    def startProcess
    # find way to use translate API



s = Server()
