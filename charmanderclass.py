from pokemon_battle_simulator import *
class Charmander:
    def __init__(self, nickname, fire, water , name):
        nickname = name
        self.nickname = nickname
        self.fire = fire
        self.water = water

    def battle_cry(self):
        print(self.nickname + " says: Charmander!")