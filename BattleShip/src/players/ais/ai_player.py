import random
from typing import Iterable, List
from BattleShip.src import ship, orientation, game_config, ship_placement
from BattleShip.src.players.player import Player



class AIPlayer(Player):

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]):
        super().__init__(player_num, config, other_players)
        #self.fireatcoords = Player.player_type.fireat
        self.ai_place_ship()

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
            self.name = "Ai {}".format(player_num)

    def get_ship_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        return random.choice([orientation.Orientation.HORIZONTAL, orientation.Orientation.VERTICAL])

    def get_ship_start_coords(self, ship_: ship.Ship, orientation_: orientation.Orientation):

        if orientation_ == orientation.Orientation.HORIZONTAL:
            self.start_row = random.randint(0, self.board.num_rows - 1)
            self.start_col = random.randint(0, self.board.num_cols - ship_.length)
        else:
            self.start_row = random.randint(0, self.board.num_rows - ship_.length)
            self.start_col = random.randint(0, self.board.num_cols - 1)
        return self.start_row, self.start_col

    def ai_place_ship(self) -> None:
        #print("Entering ai_place_ship")
        for ship_ in self.ships.values():
            self.display_placement_board()
            self.place_ship(ship_)
        self.display_placement_board()

    def place_ship(self, ship_: ship.Ship) -> None:
        while True:
            placement = self.get_random_ai_ship_placement(ship_)
            try:
                self.board.place_ship(placement)
            except ValueError as e:
                pass
            else:
                return

    def get_random_ai_ship_placement(self,ship_):
        while True:
            try:
                orientation_ = self.get_ship_orientation(ship_)
                start_row, start_col = self.get_ship_start_coords(ship_,orientation_)
            except ValueError as e:
                pass
            else:
                return ship_placement.ShipPlacement(ship_, orientation_, start_row, start_col)