import random
from .ai_player import AIPlayer
from .game_config import GameConfig

class RandomAI(AIPlayer):
    super.__init__()

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

    def delete_fireat_from_list(self):
        if len(self.list_of_board_coords) == 0:
            return False
        else:
            for i in self.list_of_board_coords:
                if i == self.fireat:
                    self.list_of_board_coords.remove(i)
                    return True