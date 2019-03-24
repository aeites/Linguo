# Linguo Google Cloud python server process
import requests
from google.cloud import vision
from google.cloud.vision import types

class Server:
    def __init__(self):
        self.api_key = self.get_api_key()

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



    # find way to use translate API



s = Server()
