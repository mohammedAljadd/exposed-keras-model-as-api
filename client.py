import requests

BASE = "http://127.0.0.1:5000/prediction"

image = {'image': open('me.jpg', 'rb')}

requests.post(BASE, files=image)
