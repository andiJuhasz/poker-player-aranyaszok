from __future__ import print_function
import random


class Player:
    VERSION = "1.1 random "

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

















        return random.randint(0, 100)

    def showdown(self, game_state):
        pass


def fold(game_state):
    return 0


# def call(game_state):
#     current_buy_in = game_state["current_buy_in"]
#     players = game_state["players"]
#     return current_buy_in - players[in_action][bet]


# def raise():


def log(message):
    import sys
    print(message, file=sys.stderr)


if __name__ == '__main__':
    log("fofisrfh")
