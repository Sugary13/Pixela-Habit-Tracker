import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = os.getenv("TOKEN")
USERNAME = "sugary17"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2025, month=7, day=16)
today_strftime = today.strftime("%Y%m%d")

pixel_config = {
    "date": today_strftime,
    "quantity": "9.3"
}

pixel_update_config = {
    "quantity": "9.3"
}

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# response = requests.post(url=pixela_creation_endpoint, json=pixel_config, headers=headers)
# response.raise_for_status()

pixela_put_endpoint = f"{pixela_creation_endpoint}/{today_strftime}"

# response = requests.put(url=pixela_put_endpoint, json=pixel_update_config, headers=headers)
# response.raise_for_status()


response = requests.delete(url=pixela_put_endpoint, headers=headers)
response.raise_for_status()
