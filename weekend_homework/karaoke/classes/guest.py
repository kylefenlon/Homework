class Guest:
    def __init__(self, name, cash, fav_song):
        self.name = name 
        self.cash = cash 
        self.fav_song = fav_song 

    def reduce_cash(self, amount):
        self.cash -= amount

