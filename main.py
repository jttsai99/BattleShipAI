import sys
from BattleShip.src import game

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Not enough arguments given.')
    else:
        print(len(sys.argv),"hi")
        print(sys.argv[1])
        print(sys.argv[2])
        print(sys.argv[0])
        game_of_battle_ship = game.Game(sys.argv[1],sys.argv[2])
        # #game_of_battle_ship = game.Game(sys.argv[1])
        # # #create game
        game_of_battle_ship.play()      #play game
