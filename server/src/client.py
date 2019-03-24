#client side
import argparse
from google.cloud import storage
from google.cloud.storage import Blob
from PIL import Image



# If you don't specify credentials when constructing the client,
# library will look for credentials in the environment.

storage_client = storage.Client.from_service_account_json('Linguo-495a24a54222.json')
##storage_client = storage.Client()


# Make an authenticated API request

bucketslist = list(storage_client.list_buckets())
print(bucketslist)
print("")

bucket = storage_client.get_bucket("storage_photos")
print(bucket)
print("")

blobs = bucket.list_blobs()
print(blobs)
print("")

x=1
for blob in blobs:
    print(blob.name)
    #filename = "blob" + str(x) + ".jpeg"
    blob.download_to_filename(blob.name)
    x=x+1


#### Add upload photos
encryption_key = "aa426195405adee2c8081bb9e7e74b19"
file = "Eventbright Banner.jpg"
jpgfile = Image.open(file)
blob = Blob(file, bucket)
with open(file, "rb") as my_file:
    blob.upload_from_file(my_file, get_content_type(file))
##with open(jpgfile, "rb") as my_file:
##    blob.upload_from_file(my_file)

