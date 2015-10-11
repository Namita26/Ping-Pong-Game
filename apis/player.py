"""
@author: Namita Maharanwar
Player API
Date: 4 Oct, 2015
"""

from flask import Flask, request
from flask_restful import Resource, Api
import json
from random import randint, sample

app = Flask(__name__)
api = Api(app)

MAIN_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

players_info = {}

with open("apis/players_info.json", "r") as f:
    players_list = json.load(f)
for i in players_list:
    p_id = i['id']
    players_info[p_id] = {}
    players_info[p_id]['length'] = i['length']


class Player(Resource):
    """
    Player methods
    """
    def get(self):
        """
        :param player_tuple is the tuple of player between whom the match
        is fixed
        sample player_tuple = (1, 2) means match is between 1 and 2
        """
        id = int(request.args.get("playerid"))
        role = request.args.get("role")
        if role == u'offensive':
            return {"move": randint(1, 10)}
        else:
            return {"move": Player._generate_random_array(
                players_info[id]["length"])}

    @staticmethod
    def _generate_random_array(length):
        """
        Generates array of input length containing random numbers ranged between
        1-10
        :param length of the defence set array
        """
        return sample(MAIN_ARRAY, int(length))


api.add_resource(Player, '/moves/')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
