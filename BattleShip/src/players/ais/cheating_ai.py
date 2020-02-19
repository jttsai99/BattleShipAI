from typing import List
from BattleShip.src import move
from .ai_player import AIPlayer
from BattleShip.src import game_config
from .. import player
from ..player import Player

class CheatingAI(AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
            self.name = "Cheating Ai {}".format(player_num)

    def __str__(self) -> str:
        return self.name

    def scan_enemy_board(self,other)->str:
        for i in range(len(other.board.contents)):
            for j in range(len(other.board.contents[i])):
                if other.board[i][j]!= "*" or other.board[i][j]!= "X" or other.board[i][j]!= "O":
                    return (f'{other.board[i][j]},{other.board[i][j]}')

    def get_move(self):
        coords = self.scan_enemy_board(player)
        firing_location = move.Move.from_str(self, coords)
        return firing_location

    # def opponent_board(self):
    #      for opponent in self.opponents:
    #          if self is opponent:
    #              continue
    #          else:
    #              opponentBoard = opponent.board
    #      return opponentBoard