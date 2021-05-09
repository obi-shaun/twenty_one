import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score_list = []
        self.is_staying = False
        self.total_score = 0
    
    def hit(self):
        self.score_list.append(random.randint(1, 10))
        self.total_score = sum(self.score_list)
    
    def stay(self):
        self.is_staying = True
    

    
    