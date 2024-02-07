class Charmander:
    def __init__(self, nickname):
        self.nickname = nickname
        self.strenght = "fire"
        self.weakness = "water"

    def battle_cry(self):
        print(self.nickname + "!")
            
class Trainer:
    def __init__(self, name, belt):
        self.name = name
        self.belt = belt

class Throw:
    def __init__(self, belt):
        for pokeball in belt:
            belt.remove[0]
            return (pokeball)

class Return:
    def __init__(self, belt, pokeball):
        belt.append(pokeball)
