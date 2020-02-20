from typing import List
import random
from .ai_player import AIPlayer
from .random_ai import RandomAI
from BattleShip.src import game_config
from BattleShip.src import move


class SearchDestroyAI(AIPlayer):
    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)
        self.search_mode = True
        self.list_of_board_coords = self.list_of_all_board_coords()
        self.circle_around_list=[]

        # super().__init__(self,other_players: Iterable["Player"])



    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        self.name = "Search Destroy AI {}".format(player_num)

    def list_of_all_board_coords(self)->List:
        self.list_of_board_coords = []
        for i in range(self.board.num_rows):
            for j in range(self.board.num_cols):
                self.list_of_board_coords.append([i, j])
        #print(self.list_of_board_coords)
        return self.list_of_board_coords

    def select_random_from_list_all_coords(self)->str:
        self.fireat = random.choice(self.list_of_board_coords) #eg: [3,5]
        #print(self.fireat)
        #print(self.fireat[0],",",self.fireat[1])
        return (f'{self.fireat[0]},{self.fireat[1]}')    #eg: 3,5

    def delete_fireat_from_list(self):
        if len(self.list_of_board_coords) == 0:
            return False
        else:
            for i in self.list_of_board_coords:
                if i == self.fireat:
                    self.list_of_board_coords.remove(i)
                    return True

    def get_move(self):
        if self.search_mode == True:
            coords = self.select_random_from_list_all_coords()
            self.delete_fireat_from_list()
        else:
            coords = self.select_circle_coords()
            self.delete_circle()
        firing_location = move.Move.from_str(self, coords)
        return firing_location

    def select_circle_coords(self) -> str:
        self.fireat = self.circle_around_list[0]
        return (f'{self.fireat[0]},{self.fireat[1]}')


    def Search_Destroy_Fire_Method(self,other):
        if self.search_mode == True:
            #self.newrow, self.newcol = self.select_random_from_list_all_coords()
            #self.result = other.board.shoot(self.newrow,self.newcol)
            if self.result == "Hit":
                self.search_mode = False
                self.create_circle_around()
                return "Hit"
            else:
                return "Miss"
        else:
            self.nxtrow,self.nxtcol = self.get_next_from_circle_list()
            self.nxtresult = other.board.shoot(self.nxtrow,self.nxtcol)
            self.delete_from_circle_list()


    def create_circle_around(self): #eg: [[2,3],[5,2]....]
        self.circle_around_list = []
        self.save_hit_cell = []
        self.circle_around_list.append([self.newrow,self.newcol-1])
        self.circle_around_list.append([self.newrow-1,self.newcol])
        self.circle_around_list.append([self.newrow, self.newcol+1])
        self.circle_around_list.append([self.newrow+1, self.newcol])
        return self.circle_around_list

    def delete_circle(self):
        self.circle_around_list.pop(0)
        if len(self.circle_around_list) == 0:
            self.search_mode = True