import random


class Player:
    VERSION = "1.1 random "

    def betRequest(self, game_state):
        return random.randint(0, 100)

    def showdown(self, game_state):
        pass
