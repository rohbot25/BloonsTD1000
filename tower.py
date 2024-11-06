import arcade

class TOWER(arcade.Sprite):
    
    def __init__(self,image, name, radius, atk, rate):
        super().__init__(image,1.0)
        self.name = name
        self.radius = radius
        self.atk = atk
        self.rate = rate
        self.level = 0
        self.cost = 0

        

#Fisherman cost = 50, upgrade = 100, increase fire rate 2x, normal range, 25 damage
class FISHERMAN(TOWER):

    def __init__(self):
        super().__init__("art/base_fisherman.png","Fisherman",200,25,25)
        #max amount of upgrade
        self.max = 3
        self.cost = 50
        self.upgradeCost = 100
    
    def upgrade(self):
        self.rate *= 2
        self.level +=1

#Whaler cost = 100, upgrade = 200, increase damage 2x, slower throw  wider range 
class WHALER(TOWER):
    
    def __init__(self):
        super().__init__("images/sungod.png","Whaler",300,50,25)
        #max amount of upgrade
        self.max = 3
        self.cost = 100
        self.upgradeCost = 200
    
    def upgrade(self):
        self.atk *= 2
        self.level +=1

#Boat cost = 150 upgrade = 300, increase range, same attack and speed as base fisherman
class BOAT(TOWER):

    def __init__(self):
        super().__init__("images/sungod.png","Boat",200,25,25)
        #max amount of upgrade
        self.max = 3
        self.cost = 150
        self.upgradeCost = 300
    
    def upgrade(self):
        self.radius *= 2
        self.level +=1

#upgraded fisherman type, more range, better starting buffs, increase dmage and rate, upgrade = 500
class FLYFISHER(TOWER):

    def __init__(self):
        super().__init__("images/sungod.png","Flyfisher",300,50,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 200
        self.upgradeCost = 500

    
    def upgrade(self):
        self.atk *= 1.5
        self.rate *= 1.5
        self.level +=1

#damage buff - whaler type wider range suuper slow
class NEANDERTHAL(TOWER):

    def __init__(self):
        super().__init__("images/sungod.png","Neanderthal",400,100,10)
        #max amount of upgrade
        self.max = 3
        self.cost = 250
        self.upgradeCost = 500
    
    def upgrade(self):
        self.atk *= 2
        self.level +=1

#wizard overall upgrade 
class WIZARD(TOWER):
     
    def __init__(self):
        super().__init__("images/sungod.png","Wizard",200,50,25)
        #max amount of upgrade
        self.max = 3
        self.cost = 300
        self.upgradeCost = 600
    
    def upgrade(self):
        self.atk *= 1.5
        self.rate *= 1.5
        self.radius *= 1.5
        self.level +=1

#THE GOAT 
class SUPERFISHER(TOWER):
     
    def __init__(self):
        super().__init__("images/sungod.png","Superfisher",500,100,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 1000
        self.upgradeCost = 2500
    
    def upgrade(self):
        self.atk *= 2
        self.rate *= 2
        self.radius *= 2
        self.level +=1

#can upgrade a bunch small overall buffs
class NETFISHER(TOWER):
      
    def __init__(self):
        super().__init__("images/sungod.png","Netfisher",200,25,25)
        #max amount of upgrade
        self.max = 10
        self.cost = 400
        self.upgradeCost = 100
    
    def upgrade(self):
        self.radius += 50
        self.atk += 50
        self.rate += 50
        self.level +=1