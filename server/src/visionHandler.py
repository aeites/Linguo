import io
import os

from google.cloud import vision
from google.cloud.vision import types

class VisionHandler:
    def __init__(self, credentials_path):
        self.authenticate(credentials_path)
        # Instantiates a client
        self.client = vision.ImageAnnotatorClient()

    def authenticate(self, credentials_path):
        # Set the path to the credentials
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    # return meta data of the image
    def process_image(self, image_path):
        # The name of the image file to annotate
        file_name = os.path.join(os.path.dirname(__file__),
                                 image_path)
        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = self.client.label_detection(image=image)
        labels = response.label_annotations

        # print('Labels:')
        # for label in labels:
        #     print(label.description + ", Score: " + str(label.score))

        return labels
        # Get the top three image contexts, and their vertices positions


#
#vh = VisionHandler(r"D:\Users\Chana-PC\Documents\Linguo\server\src\vision-key.json")
# vh.process_image(r"D:\Users\Chana-PC\Documents\Linguo\server\src\resources\wakeupcat.jpg")
# vh.process_image(r"D:\Users\Chana-PC\Documents\Linguo\server\src\resources\office_image.jpg")
# vh.process_image(r"D:\Users\Chana-PC\Documents\Linguo\server\src\resources\office_test2.jfif")


