class Character:
    def __init__(self, name, id, hp, atk, dfs, tec, spd):
        self.name = name
        self.id = id
        self.hp = hp
        self.atk = atk
        self.dfs = dfs
        self.tec = tec
        self.spd = spd


class Player(Character):
    def __init__(self, name, id, hp, atk, dfs, tec, spd, choice, ab1, ab2, ab3):
        super().__init__(name, id, hp, atk, dfs, tec, spd)
        self.choice = choice
        self.ab1 = ab1
        self.ab2 = ab2
        self.ab3 = ab3

    def change_choice(self):
        if self.choice != False:
            self.choice = False
            return
        self.choice = True
        return
