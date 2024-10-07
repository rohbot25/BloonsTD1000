# The Enemy Class (aka, Fish Class)

class Enemy:
    hp = 5
    points = 5
    spd = 1.0
    type = "fish"
    position = [0, 0]
    ID = 0

    def __init__(self, hp, points, spd, type, ID):
        self.hp = hp
        self.points = points
        self.spd = spd
        self.type = type
        self.ID = ID