import requests
import json

with open("apis/players_info.json", "r") as f:
    players_info = json.load(f)

for payload in players_info:
    print requests.post("http://127.0.0.1:5001/register", data=payload)
