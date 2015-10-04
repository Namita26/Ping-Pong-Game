"""
Referee API
Date: 4 Oct, 2015
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

joined_players = {}


class Referee(Resource):
    def get(self):
        return "Hiii"


parser = reqparse.RequestParser()


class Registration(Resource):

    def post(self):
        id = request.form['id']
        joined_players[id] = {}
        joined_players[id]['player_name'] = request.form['name']
        joined_players[id]['defence_set_length'] = request.form['length']
        joined_players[id]['is_alive'] = 1
        print joined_players


api.add_resource(Referee, '/')
api.add_resource(Registration, '/register')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
