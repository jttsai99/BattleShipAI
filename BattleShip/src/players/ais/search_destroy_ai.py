from .ai_player import AIPlayer
from .random_ai import RandomAI
class SearchDestroyAI(AIPlayer):
    def __init__(self):
        super.__init__()
        self.search_mode = True

    def Search_Destroy_Fire_Method(self):
        if self.search_mode == True:
            self.newrow,self.newcol = RandomAI.select_random_from_list_all_coords()
            self.result = opponent.board.shoot(self.newrow,self.newcol)
            if self.result == "Hit":
                self.search_mode = False
                self.create_circle_around()
                return "Hit"
            else:
                return "Miss"
        else:
            self.nxtrow,self.nxtcol = self.get_next_from_circle_list()
            self.nxtresult = opponent.board.shoot(self.nxtrow,self.nxtcol)
            self.delete_from_circle_list()



    def create_circle_around(self):
        self.circle_around_list = []
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




