import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import user_scraper
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\vision.json"
label_list = []

def starter_images(imgDest):
            client = vision.ImageAnnotatorClient()

     #   dir = "C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\InitalPic"
     #   list = os.listdir(dir)  # dir is your directory path
     #   numFiles = len(list)
     #   for i in list:
     #       file_name = os.path.abspath("C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\InitalPic\\"+i)

            file_name=imgDest
            print(file_name)
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)
            response = client.label_detection(image=image)
            labels = response.label_annotations
            client = vision.ImageAnnotatorClient()
            objects = client.object_localization(image=image).localized_object_annotations

            for object_ in objects:
                print(object_.name)
                label_list.append(object_.name)

            print('Labels:')
            for label in labels:
                print("Label starter "+ label.description)
                label_list.append(label.description)


            print("-----------------------------------------------------------------------------------------------------------------------------")
            return(label_list)
#"C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\Images\\3865022_fpx.jfif"

def infoGen(label_list):           #calls path
    #  userlist= starter_images(path)
    user_list=[]
    for i in label_list:
        results = user_scraper.get_users_by_tag(i)
        user_list.append(user_scraper.getFollowerFromUsers(results))
      #  user_list.append(user_scraper.getFollowerFromUsers(user_scraper.get_users_by_tag(i)))

    return user_list
