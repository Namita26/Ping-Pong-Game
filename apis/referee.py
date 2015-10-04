"""
Referee API
Date: 4 Oct, 2015
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from random import randint, sample

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
        Match().start_game()

    def get(self):
        return joined_players


class Match(Resource):
    def __init__(self):
        self.main_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.matches_between = [(1, 2), (3, 4), (5, 6), (7, 8)]

    def start_game(self):
        print "In start game"
        player2 = [1, 2, 3, 4, 5, 6, 7, 8]
        player1 = [10, 1, 4, 5, 9, 8, 7]
        # player1 = Match._generate_random_array(
        #     joined_players[self.matches_between[0][0]]["defence_set_length"])
        # player2 = Match._generate_random_array(
        #     joined_players[self.matches_between[0][1]]["defence_set_length"])
        Match().game(player1, player2)

    def game(self, player1, player2):
        print "In game"
        offensive = "player1"
        player1_score = 0
        player2_score = 0
        while(player1_score < 5 and player2_score < 5):
            offence_number = randint(1, 10)
            if offensive == "player1":
                if offence_number in player2:
                    player2_score = player2_score + 1
                    offensive = "player2"
                else:
                    player1_score = player1_score + 1
            else:
                if offence_number in player1:
                    player1_score = player1_score + 1
                    offensive = "player1"
                else:
                    player2_score = player2_score + 1

        if player1_score > player2_score:
            print "Player1", player1_score
        else:
            print "Player2", player2_score

    def _generate_random_array(self, length):
        return sample(self.main_array, length)


api.add_resource(Referee, '/')
api.add_resource(Registration, '/register')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
