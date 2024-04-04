import requests

pixela_endpoint = "https://pixe.la/v1/users"


# CREATE ACCOUNT, once
TOKEN = "y41aO2ginB"
USERNAME = "Dmitry"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "no", # don't wanna
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


# CREATE GRAPH, once
GRAPH_ID = "graph1"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph", # my habit graph
    "unit": "Km", # measurement
    "type": "float",
    "color": "sora"
}

# secure, not part of URL
headers = {
    "X-USER-TOKEN": TOKEN
}

requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)


# POST A PIXEL
from datetime import datetime

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

quantity = input("How many km did you drive today: ")
today = datetime.today().strftime("%Y%m%d")

pixel_params = {
    "date": today,
    "quantity": quantity
}

requests.post(url=pixel_create_endpoint, json=pixel_params, headers=headers)


# UPDATE A PIXEL (PUT)
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

new_pixel_params = {
    "quantity": quantity
}

response = requests.put(url=pixel_update_endpoint, json=new_pixel_params, headers=headers)
print(response.text)


# DELETE A PIXEL (DELETE)
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)