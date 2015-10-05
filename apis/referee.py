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
winner_ids = []


parser = reqparse.RequestParser()


class Registration(Resource):
    """
    Player Registration
    """

    def __init__(self):
        self.matches_between = [('1', '2'), ('3', '4'), ('5', '6'), ('7', '8')]

    def post(self):
        """
        POST method for player registration in tournament
        sample payload = {
            '1': {
                'is_alive': 1,
                'player_name': u'Joey',
                'defence_set_length': u'8'
            }
        }
        """
        p_id = request.form['id']
        joined_players[p_id] = {}
        joined_players[p_id]['player_name'] = request.form['name']
        joined_players[p_id]['defence_set_length'] = request.form['length']
        joined_players[p_id]['is_alive'] = 1
        if len(joined_players) == 8:
            self.commence()

    def commence(self):
        """
        Start the game between players
        """
        round_winners = []

        if len(self.matches_between) == 0:
            return

        for i in xrange(0, len(self.matches_between)):
            if len(self.matches_between) != 0:
                players_tuple = self.matches_between.pop()

                player1_id = players_tuple[0]
                player2_id = players_tuple[1]

                player1 = Match._generate_random_array(
                    joined_players[player1_id]['defence_set_length'])
                player2 = Match._generate_random_array(
                    joined_players[player2_id]['defence_set_length'])
                round_winners.append(
                    Match().game(player1, player2, player1_id, player2_id))
        print winner_ids
        next_matches = []

        if len(round_winners) == 1:
            print "The Winner is ", round_winners[0]
            return

        for j in xrange(0, len(round_winners), 2):
            next_matches.append((round_winners[j], round_winners[j+1]))
            self.matches_between = next_matches

        self.commence()

    def get(self):
        return joined_players


MAIN_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Match():

    def game(self, player1, player2, player1_id, player2_id):
        """
        Game between two players
        :param player1 is the defence set array of player1
        :param player2 is the defence set array of player2
        :param player1_id is the id of player1
        :param player2_id is the id of player2
        :return ID of the winner
        """
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
            return player1_id
        else:
            return player2_id

    @staticmethod
    def _generate_random_array(length):
        """
        Generates array of input length containing random numbers ranged between
        1-10
        :param length of the defence set array
        """
        return sample(MAIN_ARRAY, int(length))


api.add_resource(Registration, '/register')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
