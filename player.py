from __future__ import print_function
import random


class Player:
    VERSION = "1.1 random "

    def betRequest(self, game_state):
        log("dfgoiufgllidfudfiusdoiusdi")
        log(game_state["players"][1]["hole_cards"][0]["rank"])

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
