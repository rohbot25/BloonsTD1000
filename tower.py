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

        

#TODO put in the correct base info per tower
class FISHERMAN(TOWER):

    def __init__(self):
        super().__init__("art/base_fisherman.png","Fisherman",1000,25,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 50
    
    def upgrade(self):
        if(self.level < self.max):
            self.rate += 10
            self.level +=1

        
class WHALER(TOWER):
    
    def __init__(self):
        super().__init__("images/sungod.png","Whaler",1000,25,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 100
    
    def upgrade(self):
        self.rate += 10
        self.level +=1

class BOAT(TOWER):

    def __init__(self):
        super().__init__("images/sungod.png","Boat",1000,25,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 150
    
    def upgrade(self):
        
        self.rate += 10
        self.level +=1

class FLYFISHER(TOWER):

    def __init__(self):
        super().__init__("images/sungod.png","Flyfisher",1000,25,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 200
    
    def upgrade(self):
        self.rate += 10
        self.level +=1

class NEANDERTHAL(TOWER):

    def __init__(self):
        super().__init__("images/sungod.png","Neanderthal",1000,25,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 250
    
    def upgrade(self):
        self.rate += 10
        self.level +=1

class WIZARD(TOWER):
     
    def __init__(self):
        super().__init__("images/sungod.png","Wizard",1000,25,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 300
    
    def upgrade(self):
        self.rate += 10
        self.level +=1

class SUPERFISHER(TOWER):
     
    def __init__(self):
        super().__init__("images/sungod.png","Superfisher",1000,25,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 350
    
    def upgrade(self):
        self.rate += 10
        self.level +=1

class NETFISHER(TOWER):
      
    def __init__(self):
        super().__init__("images/sungod.png","Netfisher",1000,25,50)
        #max amount of upgrade
        self.max = 3
        self.cost = 400
    
    def upgrade(self):
        self.rate += 10
        self.level +=1