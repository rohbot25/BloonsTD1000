# The Enemy Class (aka, Fish Class)

class Enemy:
    hp = 5
    points = 5
    spd = 1.0
    type = "fish"
    position = [0, 0]

    def __init__(self, hp, points, spd, type):
        self.hp = hp
        self.points = points
        self.spd = spd
        self.type = type

    def checkLocation(self):
        return self.position

    def updatePosition(self):
        pass
