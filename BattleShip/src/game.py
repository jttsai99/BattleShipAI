import itertools
import random
from . import game_config
from .players import human_player, player
from .players.ais import random_ai, search_destroy_ai, cheating_ai


class Game(object):

    def __init__(self, game_config_file: str,seed:int, num_players: int = 2) -> None:
        super().__init__()
        random.seed(seed)
        self.game_config = game_config.GameConfig(game_config_file,seed)
        self.players = []
        self.player_turn = 0
        self.setup_players(num_players)


    def get_player_type(self, player_num):
        self.player_type = str(input("Enter one of ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi'] for Player {}'s type: ".format(player_num)).strip())
        if self.player_type.lower() in "cheatingai":
            self.player_type = "CheatingAi"
        elif self.player_type.lower() in "randomai":
            self.player_type = "RandomAi"
        elif self.player_type.lower() in "searchdestroyai":
            self.player_type = "SearchDestroyAi"
        elif self.player_type.lower() in "human":
            self.player_type = "Human"
        return self.player_type

    def setup_players(self, num_players: int) -> None:
        for player_num in range(1, num_players + 1):
            self.get_player_type(player_num)
            if self.player_type == "RandomAi":
                self.players.append(random_ai.RandomAI(player_num, self.game_config, self.players))
            elif self.player_type == "SearchDestroyAi":
                self.players.append(search_destroy_ai.SearchDestroyAI(player_num, self.game_config, self.players))
            elif self.player_type == "CheatingAi":
                self.players.append(cheating_ai.CheatingAI(player_num, self.game_config, self.players))
            else:
                self.players.append(human_player.HumanPlayer(player_num, self.game_config, self.players))


    def play(self) -> None:
        active_player = self.players[0]
        for active_player in itertools.cycle(self.players):
            self.do_current_players_turn(active_player)
            if self.game_is_over():
                break
        print(f'{active_player} won the game!')

    def do_current_players_turn(self, cur_player: player.Player) -> None:
        self.display_gamestate(cur_player)
        while True:
            move = cur_player.get_move()
            move.make()
            if move.ends_turn():
                break

    @property
    def num_players(self) -> int:
        return len(self.players)

    def get_active_player(self) -> human_player.HumanPlayer:
        return self.players[self.player_turn]

    def game_is_over(self) -> bool:
        return any(player_.all_ships_sunk() for player_ in self.players)

    def display_gamestate(self, cur_player: human_player.HumanPlayer) -> None:
        cur_player.display_scanning_boards()
        cur_player.display_firing_board()