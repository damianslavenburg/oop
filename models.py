# <----------- Creats the charmander class ----------->
class Charmander:
    def __init__(self, nickname):
        self.nickname = nickname
        self.strenght = "fire"
        self.weakness = "water"

    def battle_cry(self):
        print(self.nickname + "!")
# <----------- Creates the pokeball class ----------->
class Pokeball:
    def __init__(self):
        self.is_open = False
        self.charmander = None

    def throw(self):
        if self.charmander is not None:
            self.is_open = True
            print("Pokeball opens up!")
            print("Charmander is released!")
            self.charmander.battle_cry()
        else:
            print("Pokeball is empty!")

    def return_charmander(self, charmander):
        if self.is_open:
            print("Pokeball closes!")
            self.is_open = False
            self.charmander = charmander
        else:
            print("Pokeball is already closed!")

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