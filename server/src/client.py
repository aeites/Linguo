#client side
import argparse
from google.cloud import storage






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
    filename = "blob" + str(x) + ".jpeg"
    blob.download_to_filename(filename)
    x=x+1

##for blob in blobs:
##    print(blob.name)
##    blob.download_to_file(blob)
##    blob._do_download(

### Add upload photos



