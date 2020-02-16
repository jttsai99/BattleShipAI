import random
from typing import Iterable, List

from BattleShip.src import ship, orientation
from BattleShip.src.players.player import Player


class AIPlayer(Player):

    def __init__(self,other_players:Iterable["Player"]):
        super().__init__(other_players)

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
            self.name = "Ai {}".format(player_num)

    def place_ship(self, ship_: ship.Ship) -> None:
        while True:
            placement = self.get_ship_placement(ship_)
            try:
                self.board.place_ship(placement)
            except ValueError as e:
                pass
            else:
                return

    def get_ship_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        return random.choice([orientation.Orientation.HORIZONTAL, orientation.Orientation.VERTICAL])

    def get_ship_start_coords(self, ship_: ship.Ship, orientation_: orientation.Orientation):

        if orientation_ == orientation.Orientation.HORIZONTAL:
            row = random.randint(0, self.board.num_rows - 1)
            col = random.randint(0, self.board.num_cols - ship_.length)
        else:
            row = random.randint(0, self.board.num_rows - ship_.length)
            col = random.randint(0, self.board.num_cols - 1)
        return row, col