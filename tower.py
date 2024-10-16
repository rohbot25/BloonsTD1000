class Tower:
    
    def __init__(self, name, radius, atk, rate):
        self.name = name
        self.radius = radius
        self.atk = atk
        self.rate = rate
        self.level = 0
        

#TODO put in the correct base info per tower
class Fisherman(Tower):

    def __init__(self):
        super().__init__("Fisherman",0.5,25,50)
        #max amount of upgrade
        self.max = 3
    
    def upgrade(self):
        if(self.level < self.max):
            self.rate += 10

        
class Harpoon(Tower):
    
    def __init__(self):
        super().__init__("Harpoon",0.5,25,50)
        #max amount of upgrade
        self.max = 3
    
    def upgrade(self):
        if(self.level < self.max):
            self.atk += 10 
