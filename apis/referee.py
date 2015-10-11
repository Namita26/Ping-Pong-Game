"""
Referee API
Date: 4 Oct, 2015
"""

from flask import Flask, request
from flask_restful import Resource, Api
import requests


app = Flask(__name__)
api = Api(app)


class Registration(Resource):
    """
    Player Registration
    """

    joined_players = {}

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
        Registration.joined_players[p_id] = {}
        Registration.joined_players[p_id]['player_name'] = request.form['name']
        Registration.joined_players[p_id]['defence_set_length'] = request.form['length']
        Registration.joined_players[p_id]['is_alive'] = 1
        if len(Registration.joined_players) == 8:
            Match().commence(Registration.joined_players)
            Registration.joined_players = {}

    # def get(self):
    #     print self.joined_players
    #     return self.joined_players


MAIN_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Match():

    def __init__(self):
        self.matches_between = [('1', '2'), ('3', '4'), ('5', '6'), ('7', '8')]
        self.report = []

    def commence(self, joined_players):
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

                round_winners.append(
                    self.game(player1_id, player2_id))
        next_matches = []

        if len(round_winners) == 1:
            Match._print_report(self.report)
            print "The Game Winner is ", round_winners[0]
            return

        for j in xrange(0, len(round_winners), 2):
            next_matches.append((round_winners[j], round_winners[j+1]))
            self.matches_between = next_matches

        self.commence(joined_players)

    def game(self, player1_id, player2_id):
        """
        Game between two players
        :param player1_id is the id of player1
        :param player2_id is the id of player2
        :return ID of the winner
        """
        player1_score = 0
        player2_score = 0
        player1_type = "offensive"
        player2_type = "defencive"

        while(player1_score < 5 and player2_score < 5):
            player1_move = Match._get_move(player1_id, player1_type)
            player2_move = Match._get_move(player2_id, player2_type)
            player1_score, player1_type, player2_score, player2_type = compute_move_winner(player1_move, player1_type, player1_score, player2_move, player2_type, player2_score)

        sub_game_winner_id = player1_id
        if player1_score < player2_score:
            sub_game_winner_id = player2_id

        self.report.append({
            "players": [player1_id, player2_id],
            "scores": [player1_score, player2_score],
            "sub_game_winner": sub_game_winner_id
        })
        return sub_game_winner_id

    @staticmethod
    def _get_move(player_id, player_type):
        """
        Offensive number or the defence array according to role
        :param player_id is player's id
        :player_type is role of the player like offensive or defencive
        """
        payload = {"playerid": player_id, "role": player_type}
        output = requests.get("http://127.0.0.1:5000/moves", params=payload)
        move = output.json()['move']
        return move

    @staticmethod
    def _print_report(report):
        for i in xrange(0, len(report)):
            print "---------------------"
            print "Match Number : ", i+1
            print "Players : ", report[i]["players"]
            print "Scores  : ", report[i]["scores"]
            print "winner  : ", report[i]["sub_game_winner"]


def compute_move_winner(player1_move, player1_type, player1_score,
                        player2_move, player2_type, player2_score):
    """
    :param player(x)_move is the offence_number or defence_array
    :param player(x)_type is offensive or defencive
    :param player(x)_score is player's scores
    """
    if player1_type == "offensive":
        if player1_move in player2_move:
            player2_score = player2_score + 1
            player2_type = "offensive"
            player1_type = "defensive"
        else:
            player1_score = player1_score + 1
    else:
        if player2_move in player1_move:
            player1_score = player1_score + 1
            player1_type = "offensive"
            player2_type = "defensive"
        else:
            player2_score = player2_score + 1
    return (player1_score, player1_type, player2_score, player2_type)


api.add_resource(Registration, '/register')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
