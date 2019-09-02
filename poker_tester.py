from player import Player, log
import json


def load_test_state():
    with open('game_state_example.json', 'r') as f:
        game_state = json.load(f)
        return game_state


if __name__ == '__main__':
    game_state = load_test_state()
    log(f'game_state: {game_state}')

    player = Player()
    bet = player.betRequest(game_state)
    log(f'bet: {bet}')
