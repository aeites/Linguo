#client side
from google.cloud import storage
from google.cloud.storage import Blob

# If you don't specify credentials when constructing the client,
# library will look for credentials in the environment.

class StorageHandler:
    def __init__(self, jsonfile):
        self.storage_client = storage.Client.from_service_account_json(jsonfile)        
        
    def getBucket(self):
        bucketslist = list(self.storage_client.list_buckets())
        bucket = self.storage_client.get_bucket("storage_photos")
        return bucket

    def getBlobs(self, bucket):
        blobs = bucket.list_blobs()
        return blobs

    def downloadAllBlobs(self, blobs):
        print(blobs.path)
        for blob in blobs:
            
            print(blob.name)
            print(blob.path)
            blob.download_to_filename(blob.name)

    def downloadOneBlob(self, bucket, fileRequest):
        blob = bucket.get_blob(fileRequest)
        blob.download_to_filename("crappy.jpeg")
            
##            if blob.name == fileRequest:
##                blob.download_to_filename(blob.name)
            
    def uploadNewPhoto(self, file, bucket):
        blob = Blob(file, bucket)
        # TODO: create csv/tuple for the input?
        with open(file, "rb") as my_file:
            blob.upload_from_file(my_file)

    # TODO: get an image from the image path
    def getImage(self, imagePath):
        print("Return image file path?")

    # TODO: draft method to read the configuration file for the processed images
    def readConfig(self, configPath):

        print("read config file")

####COMPLETED##
##jsonfile = 'Linguo-495a24a54222.json'
##s = StorageHandler(jsonfile)
##bucket = s.getBucket()
##blobs = s.getBlobs(bucket)
##s.downloadAllBlobs(blobs)

##TO DO##
##file = input("Enter file name: ")
##s.uploadNewPhoto(file, bucket)
