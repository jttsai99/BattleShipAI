import abc

import self as self

from BattleShip.src.firing_location_error import FiringLocationError
from typing import Dict, List
from BattleShip.src import board, move, game_config, ship, orientation, ship_placement
import copy

class Player(abc.ABC):
    opponents: List["Player"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        self.name = 'No Name'
        self.init_name(player_num, other_players)
        self.player_type = ""#self.get_player_type()
        self.board = board.Board(config)
        self.opponents = other_players[:]  # a copy of other players
        self.ships = copy.deepcopy(config.available_ships)
        #self.place_ships()

        # make this player the opponent of all the other players
        for opponent in other_players:
            opponent.add_opponent(self)

    def get_player_type(self):
        self.player_type = str(input("Enter one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi'] for Player {}'s type: ".format(self.player_num)))
        if self.player_type.lower() in "human":
            self.player_type = "Human"
        elif self.player_type.lower() in "randomai":
            self.player_type = "RandomAi"
        elif self.player_type.lower() in "searchdestroyai":
            self.player_type = "SeachDestroyAi"
        elif self.player_type.lower() in "cheatingai":
            self.player_type = "CheatingAi"
        return self.player_type






    @abc.abstractmethod
    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        ...

    def add_opponent(self, opponent: "Player") -> None:
        self.opponents.append(opponent)

    def place_ships(self) -> None:
        for ship_ in self.ships.values():
            self.display_placement_board()
            self.place_ship(ship_)
        self.display_placement_board()

    def place_ship(self, ship_: ship.Ship) -> None:
        while True:
            placement = self.get_ship_placement(ship_)
            try:
                self.board.place_ship(placement)
            except ValueError as e:
                print(e)
            else:
                return

    def get_ship_placement(self, ship_: ship.Ship):
        while True:
            try:
                orientation_ = self.get_orientation(ship_)
                start_row, start_col = self.get_start_coords(ship_)
            except ValueError as e:
                print(e)
            else:
                return ship_placement.ShipPlacement(ship_, orientation_, start_row, start_col)

    def get_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        ...

    def get_start_coords(self, ship_: ship.Ship):
        ...

    def all_ships_sunk(self) -> bool:
        return all(ship_.health == 0 for ship_ in self.ships.values())

    @abc.abstractmethod
    def get_move(self) -> move.Move:
        ...

    def fire_at(self, row: int, col: int) -> None:
        opponent = self.opponents[0]
        if not opponent.board.coords_in_bounds(row, col):
            raise FiringLocationError(f'{row}, {col} '
                                      f'is not in bounds of our '
                                      f'{opponent.board.num_rows} X {opponent.board.num_cols} board.')
        elif opponent.board.has_been_fired_at(row, col):
            raise FiringLocationError(f'You have already fired at {row}, {col}.')
        else:
            opponent.receive_fire_at(row, col)
            self.display_scanning_boards()
            self.display_firing_board()

    def receive_fire_at(self, row: int, col: int) -> None:
        location_fired_at = self.board.shoot(row, col)
        if location_fired_at.contains_ship():
            ship_hit = self.ships[location_fired_at.content]
            ship_hit.damage()
            print(f"You hit {self.name}'s {ship_hit}!")
            if ship_hit.destroyed():
                print(f"You destroyed {self.name}'s {ship_hit}")
        else:
            print('Miss')

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return False
        else:
            return self.name == other.name

    def __ne__(self, other: object) -> bool:
        return self != other

    def display_placement_board(self) -> None:
        print(f"{self.name}'s Placement Board")
        print(self.get_visible_representation_of_board(), end='')

    def display_scanning_boards(self) -> None:
        print(f"{self.name}'s Scanning Board")
        for opponent in self.opponents:
            print(opponent.get_hidden_representation_of_board(), end='')

    def display_firing_board(self) -> None:
        print(f"\n{self.name}'s Board")
        print(self.get_visible_representation_of_board())

    def get_hidden_representation_of_board(self) -> str:
        return self.board.get_display(hidden=True)

    def get_visible_representation_of_board(self) -> str:
        return self.board.get_display(hidden=False)

    def __str__(self) -> str:
        return self.name

