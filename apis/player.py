"""
Player API
Date: 4 Oct, 2015
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

joined_players = {}


class Player(Resource):

    def __init__(self, id, name, defence_length):
        self.player_id = id
        self.player_name = name
        self.defence_set_lenth = defence_length

    def is_shut_down(self, id, score):
        if score != 5:
            joined_players['id'] = 0

api.add_resource(Player, '/')


if __name__ == "__main__":
    app.run(debug=True)
