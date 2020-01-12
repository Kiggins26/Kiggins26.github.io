import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import user_scraper
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\vision.json"
def starter_images(imgDest):
            client = vision.ImageAnnotatorClient()

     #   dir = "C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\InitalPic"
     #   list = os.listdir(dir)  # dir is your directory path
     #   numFiles = len(list)
     #   for i in list:
     #       file_name = os.path.abspath("C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\InitalPic\\"+i)

            file_name=imgDest
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)
            response = client.label_detection(image=image)
            labels = response.label_annotations
            client = vision.ImageAnnotatorClient()
            objects = client.object_localization(image=image).localized_object_annotations

            for object_ in objects:
                print(object_.name)
                label_list.append(object_)

            print('Labels:')
            for label in labels:
                label_list.append(label.description)

            print("-----------------------------------------------------------------------------------------------------------------------------")
            return label_list
#"C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\Images\\3865022_fpx.jfif"
def infoGen(AttList):
    userlist = []
    for i in AttList:
        userlist.append(getFollowerFromUsers(get_users_by_tag(i)))
    return userlist
