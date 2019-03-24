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
        for blob in blobs:
            print(blob.name)
            blob.download_to_filename(blob.name)
            
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


jsonfile = 'Linguo-495a24a54222.json'
s = StorageHandler(jsonfile)
bucket = s.getBucket()
blobs = s.getBlobs(bucket)
s.downloadAllBlobs(blobs)
file = input("Enter file name: ")
s.uploadNewPhoto(file, bucket)


# storage_client = storage.Client.from_service_account_json('Linguo-495a24a54222.json')
#
# # Make an authenticated API request
# bucketslist = list(storage_client.list_buckets())
# bucket = storage_client.get_bucket("storage_photos")
# blobs = bucket.list_blobs()
#
# x=1
# for blob in blobs:
#     print(blob.name)
#     #filename = "blob" + str(x) + ".jpeg"
#     blob.download_to_filename(blob.name)
#     x=x+1
#
# #### Add upload photos
# file = "Eventbright Banner.jpg"
# blob = Blob(file, bucket)
# with open(file, "rb") as my_file:
#     blob.upload_from_file(my_file)

