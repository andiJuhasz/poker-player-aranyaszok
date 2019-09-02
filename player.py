from __future__ import print_function
import random

values = {"2": 2,
          "3": 3,
          "4": 4,
          "5": 5,
          "6": 6,
          "7": 7,
          "8": 8,
          "9": 9,
          "10": 10,
          "J": 11,
          "Q": 12,
          "K": 13,
          "A": 14}


class Player:
    VERSION = "1.2 "

    def betRequest(self, game_state):
        log("OUR LOG**************************************************************************************************")
        players = game_state["players"]
        community_cards = game_state["community_cards"]
        hole_cards = []
        for player in players:
            if player["name"] == "AranyAszok":
                hole_cards = player["hole_cards"]

        game_cards = hole_cards + community_cards
        game_ranks = [game_card["rank"] for game_card in game_cards]
        hole_ranks = [hole_card["rank"] for hole_card in hole_cards]
        log(game_ranks)
        log(hole_ranks)
        amount_of_same_rank = []
        for rank in hole_ranks:
            amount_of_same_rank.append(game_ranks.count(rank))

        max_of_a_kind = max(amount_of_same_rank)
        if max_of_a_kind > 1:
            raise_amount = raise_(game_state, max_of_a_kind)
            return raise_amount
        else:
            return call(game_state)


def showdown(self, game_state):
    pass


def fold(game_state):
    return 0


def raise_(game_state, max_of_a_kind):
    current_buy_in = game_state["current_buy_in"]
    players = game_state["players"]
    in_action = game_state["in_action"]
    plus_bet = 0
    if max_of_a_kind == 2:
        plus_bet = 3
    elif max_of_a_kind == 3:
        plus_bet = 50
    elif max_of_a_kind == 4:
        plus_bet = 150
    minimum_raise = game_state["minimum_raise"]

    return current_buy_in - players[in_action]["bet"] + minimum_raise + plus_bet

def call(game_state):
    current_buy_in = game_state["current_buy_in"]
    players = game_state["players"]
    in_action = game_state["in_action"]
    return current_buy_in - players[in_action]["bet"]

def log(message):
    import sys
    print(message, file=sys.stderr)


if __name__ == '__main__':
    log("fofisrfh")
