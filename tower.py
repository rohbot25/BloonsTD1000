import arcade

class TOWER(arcade.Sprite):
    
    def __init__(self,image,scale, name, radius, atk, rate,max,cost,upgradeCost,bullet,bullet_scale):
        super().__init__(image,scale,hit_box_algorithm="None")
        self.name = name
        self.radius = radius
        self.atk = atk
        self.rate = rate
        self.level = 0
        self.cost = cost
        self.max = max
        self.upgradeCost = upgradeCost
        self.bullet = bullet
        self.bullet_scale = bullet_scale

        

#Fisherman cost = 50, upgrade = 100, increase fire rate 2x, normal range, 25 damage
class FISHERMAN(TOWER):

    def __init__(self):
        bullet = "images/sun.png"
        super().__init__("art/base_fisherman.png",3.0,"Fisherman",200,25,25,3,50,100,bullet,1.0)
    
    def upgrade(self):
        self.rate *= 2
        self.level +=1

#Whaler cost = 100, upgrade = 200, increase damage 2x, slower throw  wider range 
class WHALER(TOWER):
    
    def __init__(self):
        bullet = "images/sun.png"
        super().__init__("images/sungod.png",1.0,"Whaler",300,50,25,3,100,200,bullet,1.0)
        
    
    def upgrade(self):
        self.atk *= 2
        self.level +=1

#Boat cost = 150 upgrade = 300, increase range, same attack and speed as base fisherman
class BOAT(TOWER):

    def __init__(self):
        bullet = "images/oar.png"
        super().__init__("images/ship.png",0.075,"Boat",200,25,10,3,150,300,bullet,0.1)
    
    def upgrade(self):
        self.radius *= 2
        self.level +=1

#upgraded fisherman type, more range, better starting buffs, increase dmage and rate, upgrade = 500
class FLYFISHER(TOWER):

    def __init__(self):
        bullet = "images/sun.png"
        super().__init__("images/sungod.png",1.0,"Flyfisher",300,50,50,3,200,500,bullet,1.0)
        

    
    def upgrade(self):
        self.atk *= 1.5
        self.rate *= 1.5
        self.level +=1

#damage buff - whaler type wider range suuper slow
class NEANDERTHAL(TOWER):

    def __init__(self):
        bullet = "images/sun.png"
        super().__init__("images/sungod.png",1.0,"Neanderthal",400,100,10,3,250,500,bullet,1.0)
        
    
    def upgrade(self):
        self.atk *= 2
        self.level +=1

#wizard overall upgrade 
class WIZARD(TOWER):
     
    def __init__(self):
        bullet = "images/sun.png"
        super().__init__("images/sungod.png",1.0,"Wizard",200,50,25,3,300,600,bullet,1.0)
        
    
    def upgrade(self):
        self.atk *= 1.5
        self.rate *= 1.5
        self.radius *= 1.5
        self.level +=1

#THE GOAT 
class SUPERFISHER(TOWER):
     
    def __init__(self):
        bullet = "images/sun.png"
        super().__init__("images/sungod.png",1.0,"Superfisher",500,100,50,3,1000,2500,bullet,1.0)
    
    def upgrade(self):
        self.atk *= 2
        self.rate *= 2
        self.radius *= 2
        self.level +=1

#can upgrade a bunch small overall buffs
class NETFISHER(TOWER):
      
    def __init__(self):
        bullet = "images/sun.png"
        super().__init__("images/sungod.png",1.0,"Netfisher",200,25,25,10,400,100,bullet,1.0)
    
    def upgrade(self):
        self.radius += 50
        self.atk += 50
        self.rate += 50
        self.level +=1