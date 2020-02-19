from typing import List
from BattleShip.src import move, players
from .ai_player import AIPlayer
from BattleShip.src import game_config

class CheatingAI(AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
            self.name = "Cheating Ai {}".format(player_num)

    def __str__(self) -> str:
        return self.name

    def scan_enemy_board(self,other)->str:
        for i in range(self.board.num_rows):
            for j in range(self.board.num_cols):
                if other.board.contents[i][j].representation()!= "*" and other.board.contents[i][j].representation()!= "X" and other.board.contents[i][j].representation()!= "O":
                    #print(other.board.contents[i][j])
                    return f'{i},{j}'

    def get_move(self):
        coords = self.scan_enemy_board(self.opponents[0])
        firing_location = move.Move.from_str(self, coords)
        return firing_location

    # def opponent_board(self):
    #      for opponent in self.opponents:
    #          if self is opponent:
    #              continue
    #          else:
    #              opponentBoard = opponent.board
    #      return opponentBoard