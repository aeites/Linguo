#client side
from google.cloud import storage
from google.cloud.storage import Blob

# If you don't specify credentials when constructing the client,
# library will look for credentials in the environment.

class StorageHandler:
    def __init__(self, jsonfile):
        self.storage_client = storage.Client.from_service_account_json(jsonfile)        
        
    def defineBucket(self):
        bucketslist = list(self.storage_client.list_buckets())
        bucket = self.storage_client.get_bucket("storage_photos")
        return bucket

    def defineBlobs(self, bucket):
        blobs = bucket.list_blobs()
        return blobs

    def downloadAllBlobs(self, blobs):
        for blob in blobs:
            print(blob.name)
            blob.download_to_filename(blob.name)
            
    def uploadNewPhoto(self, file, bucket):
        blob = Blob(file, bucket)
        with open(file, "rb") as my_file:
            blob.upload_from_file(my_file)



jsonfile = 'Linguo-495a24a54222.json'
s = StorageHandler(jsonfile)
bucket = s.defineBucket()
blobs = s.defineBlobs(bucket)
s.downloadAllBlobs(blobs)
file = input("Enter file name: ")
s.uploadNewPhoto(file, bucket)
