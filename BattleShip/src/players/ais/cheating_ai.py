from typing import List

from .ai_player import AIPlayer

class CheatingAI(AIPlayer):
    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
            self.name = "Cheating Ai {}".format(player_num)