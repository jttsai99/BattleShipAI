from typing import List
import random
from .ai_player import AIPlayer
from .random_ai import RandomAI

class SearchDestroyAI(AIPlayer):
    def __init__(self, player_num: int, other_players: List["Player"]):
        super.__init__()
        self.search_mode = True

    def list_of_all_board_coords(self):
        self.list_of_board_coords = []
        for i in range(self.board.num_rows):
            for j in range(self.board.num_cols):
                self.list_of_board_coords.append((i, j))
        print(self.list_of_board_coords)
        return self.list_of_board_coords

    def select_random_from_list_all_coords(self):
        self.fireat = random.choice(self.list_of_board_coords)
        return self.fireat


    # def Search_Destroy_Fire_Method(self):
    #     if self.search_mode == True:
    #         self.newrow, self.newcol = self.select_random_from_list_all_coords()
    #         self.result = opponent.board.shoot(self.newrow,self.newcol)
    #         if self.result == "Hit":
    #             self.search_mode = False
    #             self.create_circle_around()
    #             return "Hit"
    #         else:
    #             return "Miss"
    #     else:
    #         self.nxtrow,self.nxtcol = self.get_next_from_circle_list()
    #         self.nxtresult = opponent.board.shoot(self.nxtrow,self.nxtcol)
    #         self.delete_from_circle_list()

    def check_return_status(self, status, hit_row, hit_col):
        if (self.search_mode == True):
            if (status == "Hit"):
                self.search_mode = False
                self.create_circle_around(hit_row, hit_col)
        else:
            self.saved_hit_cell.append(hit_row, hit_col)

    def get_move(self):
        if (self.search_mode == True):
            coords = self.select_random_from_list_all_coords()
            # coords should be of form str-> row,col
            firing_location = move.Move.from_str(self, coords)
            self.delete_fireat_from_list()
            return firing_location
        else:
            if (self.circle_around_list == []):
              # now calculate remaining cells to be tryout
              # will go either horizontal or vertical
              # based on already fired cells from 'save_hit_cell'

                if (self.save_hit_cell[0].row == self.save_hit_cell[1].row):
                    dir = "Horizontal"
                elif (self.save_hit_cell[0].col == self.save_hit_cell[1].col):
                    dir = "Vertical"

                # Put all the remaining cells to be Fired back in circle_list
                if (dir == "Horizontal"):
                    for cx in range(player.colmax):
                        circle_list.append(saved_hit_cell[0].row, cx)
                else:
                    for cy in range(player.rowmax):
                        circle_list.append(cy, saved_hit_cell[0].col)
            else:
                #  coords should be of str Type -> row,col
                new_cordin = circle_around_list[0]
                firing_location = move.Move.from_str(self, new_cordin)
                return firing_location









    def create_circle_around(self):
        self.circle_around_list = []
        self.save_hit_cell = []
        self.circle_around_list.append((self.newrow - 1,self.newcol))
        self.circle_around_list.append((self.newrow,self.newcol-1))
        self.circle_around_list.append((self.newrow+1, self.newcol))
        self.circle_around_list.append((self.newrow, self.newcol+1))
        return self.circle_around_list

    def get_next_from_circle_list(self):
        for i in self.circle_around_list:
            return i

    def delete_from_circle_list(self):
        for i in self.circle_around_list:
            del self.circle_around_list[0]
            return self.circle_around_list


    def get_move(self):

        # coords should be string with "row,col"

        coords = Search_Destroy_Fire_Method(self)

        firing_location = move.Move.from_str(self, coords)
        return firing_location

