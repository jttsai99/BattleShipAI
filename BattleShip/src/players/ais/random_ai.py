import random
from typing import List, Iterable
from random import seed

from .ai_player import AIPlayer
#from ...firing_location_error import FiringLocationError
from BattleShip.src import game_config, move


class RandomAI(AIPlayer):

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)
        self.fireat =[]
        #super().__init__(self,other_players: Iterable["Player"])


    def list_of_all_board_coords(self):
        self.list_of_board_coords = []
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self.list_of_board_coords.append((i, j))
        print(self.list_of_board_coords)
        return self.list_of_board_coords

    def select_random_from_list_all_coords(self):
        self.fireat = random.choice(self.list_of_board_coords)
        return self.fireat

    def get_move(self) -> move.Move:
        try:
            firing_location = move.Move.from_str(self,self.fireat)
        except ValueError as e:
            print(e)
        return firing_location


    def delete_fireat_from_list(self):
        if len(self.list_of_board_coords) == 0:
            return False
        else:
            for i in self.list_of_board_coords:
                if i == self.fireat:
                    self.list_of_board_coords.remove(i)
                    return True

