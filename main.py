import sys
from BattleShip.src import game
from random import seed

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Not enough arguments given.')
    else:
        game_of_battle_ship = game.Game(sys.argv[1],int(sys.argv[2]))    #create game
        game_of_battle_ship.play()      #play game
