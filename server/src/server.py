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



        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)

        # extracting data in json format
        data = r.json()

        # extracting latitude, longitude and formatted address
        # of the first matching location
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        formatted_address = data['results'][0]['formatted_address']

        # printing the output
        print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
              % (latitude, longitude, formatted_address))

        print("Unsupported Method")

    # Method to draw the text onto the image
    def drawText(self, image, coordinates, text):
        print("Unsupported Method")

    def get_api_key(self):
        f = open("API_Key.txt", "r")
        return f.read()
    # find way to use translate API


s = Server()
