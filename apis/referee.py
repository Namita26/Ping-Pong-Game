from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

joined_players = {}


class Referee(Resource):
    def get(self):
        return "Hiii"


class Championship(Resource):
    def join(self, id, name, set_length):
        joined_players[id] = {}
        joined_players[id]['player_name'] = name
        joined_players[id]['defence_set_length'] = set_length
        joined_players[id]['is_alive'] = 1

    def is_shut_down(self, id, score):
        if score != 5:
            joined_players['id'] = 0

api.add_resource(Referee, '/')


if __name__ == "__main__":
    app.run(debug=True)
