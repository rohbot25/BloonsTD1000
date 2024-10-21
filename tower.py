import arcade

class TOWER(arcade.Sprite):
    
    def __init__(self,image, name, radius, atk, rate):
        super().__init__(image,1.0)
        self.name = name
        self.radius = radius
        self.atk = atk
        self.rate = rate
        self.level = 0
        

#TODO put in the correct base info per tower
class FISHERMAN(TOWER):

    def __init__(self):
        super().__init__("/Images/sungod.png","Fisherman",0.5,25,50)
        #max amount of upgrade
        self.max = 3
    
    def upgrade(self):
        if(self.level < self.max):
            self.rate += 10

        
class HARPOON(TOWER):
    
    def __init__(self):
        super().__init__("Harpoon",0.5,25,50)
        #max amount of upgrade
        self.max = 3
    
    def upgrade(self):
        if(self.level < self.max):
            self.atk += 10 
