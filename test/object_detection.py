from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import json


with open("./secret.json") as f:
    secret = json.load(f)

KEY = secret["KEY"]
ENDPOINT = secret["ENDPOINT"]

computervision_client = ComputerVisionClient(
    ENDPOINT, CognitiveServicesCredentials(KEY))

remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"

# # 画像の説明の取得
# print("===== Describe an image - remote =====")
# description_results = computervision_client.describe_image(remote_image_url)

# print("Description of remote image: ")
# if (len(description_results.captions) == 0):
#     print("No description detected.")
# else:
#     for caption in description_results.captions:
#         print("'{}' with confidence {:.2f}%".format(
#             caption.text, caption.confidence * 100))

# # 画像カテゴリの取得
# print("===== Categorize an image - remote =====")
# remote_image_features = ["categories"]
# categorize_results_remote = computervision_client.analyze_image(
#     remote_image_url, remote_image_features)

# print("Categories from remote image: ")
# if (len(categorize_results_remote.categories) == 0):
#     print("No categories detected.")
# else:
#     for category in categorize_results_remote.categories:
#         print(
#             "'{}' with confidence {:.2f}%".format(
#                 category.name,
#                 category.score * 100))

# # 画像タグの取得
# print("===== Tag an image - remote =====")
# tags_result_remote = computervision_client.tag_image(remote_image_url)

# print("Tags in the remote image: ")
# if (len(tags_result_remote.tags) == 0):
#     print("No tags detected.")
# else:
#     for tag in tags_result_remote.tags:
#         print(
#             "'{}' with confidence {:.2f}%".format(
#                 tag.name,
#                 tag.confidence * 100))

# # 物体を検出する
# print("===== Detect Objects - remote =====")
# remote_image_url_objects = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg"
# detect_objects_results_remote = computervision_client.detect_objects(
#     remote_image_url_objects)

# print("Detecting objects in remote image:")
# if len(detect_objects_results_remote.objects) == 0:
#     print("No objects detected.")
# else:
#     for object in detect_objects_results_remote.objects:
#         print("object at location {}, {}, {}, {}".format(
#             object.rectangle.x, object.rectangle.x + object.rectangle.w,
#             object.rectangle.y, object.rectangle.y + object.rectangle.h))

# ローカルファイルに対応させる
image_path = "img/sample01.jpg"
img = open(image_path, "rb")

print("===== Detect Objects - local =====")
detect_objects_results = computervision_client.detect_objects_in_stream(img)

print("Detecting objects in remote image:")
if len(detect_objects_results.objects) == 0:
    print("No objects detected.")
else:
    for object in detect_objects_results.objects:
        print("object at location {}, {}, {}, {}".format(
            object.rectangle.x, object.rectangle.x + object.rectangle.w,
            object.rectangle.y, object.rectangle.y + object.rectangle.h))
