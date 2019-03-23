# Linguo Google Cloud python server process

class Server:
    def __init__(self):
        self.api_key = self.get_api_key()

    #method to get files from the bucket
    def getUnprocessedFiles(self):
        # returns the file names of things to process
        print("Unsupported Method")

    # push the files from the get unprocessed files, processes the
    def processFiles(self):
        print("Unsupported Method")

    # Method to draw the text onto the image
    def drawText(self, image, coordinates, text):
        print("Unsupported Method")

    def get_api_key(self):
        f = open("API_Key.txt", "r")
        return f.read()
    # find way to use translate API


s = Server()
