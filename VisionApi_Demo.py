import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\vision.json"


def localize_objects():
        # Instantiates a client
        client = vision.ImageAnnotatorClient()
        # The name of the image file to annotate
        dir = "C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\Images"
        list = os.listdir(dir)  # dir is your directory path
        numFiles = len(list)
        for i in list:
            file_name = os.path.abspath("C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\Images\\"+i)

            # Loads the image into memory
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

       #     path = "C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\69.jpg"

            client = vision.ImageAnnotatorClient()

    #        with open(path, 'rb') as image_file:
    #            content = image_file.read()
       #     image = vision.types.Image(content=content)

            objects = client.object_localization(image=image).localized_object_annotations

            for object_ in objects:
                print(object_.name)

            print('Labels:')
            for label in labels:
                print(label.description)
            print("-----------------------------------------------------------------------------------------------------------------------------")



localize_objects()

