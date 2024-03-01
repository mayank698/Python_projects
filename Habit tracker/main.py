import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

today = datetime.now()
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"9.74"
}


# response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
new_pixel_data = {
    "quantity":"15"
}
# response = requests.put(url=pixela_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)
