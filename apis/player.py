"""
Player API
Date: 4 Oct, 2015
"""

from flask import Flask
from flask_restful import Resource, Api
import requests
import json

app = Flask(__name__)
api = Api(app)

joined_players = {}


class Player(Resource):
    """
    Player methods
    """
    def __init__(self, id, name, defence_length):
        self.player_id = id
        self.player_name = name
        self.defence_set_length = defence_length

    def is_shut_down(self, id, score):
        if score != 5:
            joined_players['id'] = 0

api.add_resource(Player, '/')


if __name__ == "__main__":
    with open("apis/players_info.json", "r") as f:
        players_info = json.load(f)
    for payload in players_info:
        print requests.post("http://127.0.0.1:5001/register", data=payload)
