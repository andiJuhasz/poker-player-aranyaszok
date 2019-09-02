from __future__ import print_function
import random



class Player:
    VERSION = "1.1 random "

    def betRequest(self, game_state):
        log(game_state["players"])
        log("dfgoiufgllidfudfiusdoiusdi")

        return random.randint(0, 100)

    def showdown(self, game_state):
        pass

def log(message):
    import sys
    print(message, file=sys.stderr)

if __name__ == '__main__':
    log("fofisrfh")