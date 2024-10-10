import arcade


class User:
    round = 1
    money = 650
    health = 150

    def __init__(self, round, money, health):
        self.round = round
        self.money = money
        self.health = health
