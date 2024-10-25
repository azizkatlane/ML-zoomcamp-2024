import requests

url='http://0.0.0.0:5353/predict'
client = client = {"job": "management", "duration": 400, "poutcome": "success"}

response =requests.post(url , json=client).json()
print(response)