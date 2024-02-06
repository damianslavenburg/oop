import pokemon_battle_simulator
class Charmander:
    def __init__(self, nickname, fire, water):
        self.nickname = nickname
        self.fire = fire
        self.water = water

    def battle_cry(self):
        print(self.nickname + " says: Charmander!")