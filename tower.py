import arcade

class TOWER(arcade.Sprite):
    
    def __init__(self,image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale):
        super().__init__(image,scale,hit_box_algorithm="None")
        self.name = name
        self.radius = radius
        self.atk = atk
        self.rate = rate
        self.level = 0
        self.cost = cost
        self.max = max
        self.upgrade_cost = upgrade_cost
        self.bullet = bullet
        self.bullet_scale = bullet_scale

        

#Fisherman cost = 50, upgrade = 100, increase fire rate 2x, normal range, 25 damage
class FISHERMAN(TOWER):

    def __init__(self):
        image = "Images/base_fisherman.png"
        scale = .75
        name = "Fisherman"
        radius = 150
        atk = 2
        rate = 30
        cost = 125
        max = 3
        upgrade_cost = 100
        bullet = "images/fishhook.png"
        bullet_scale = 1.5
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.rate -= 5
        self.level +=1

#God increase damage 2x, slower throw  wider range 
class GOD(TOWER):
    
    def __init__(self):
        image = "Images/god.png"
        scale = 0.2
        name = "God"
        radius = 2000
        atk = 5
        rate = 25
        cost = 1500
        max = 3
        upgrade_cost = 0
        bullet = "images/sun_gold.png"
        bullet_scale = 0.33
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
        
    
    def upgrade(self):
        self.atk *= 2
        self.level +=1

#Boat cost = 150 upgrade = 300, increase range, same attack and speed as base fisherman
class BOAT(TOWER):

    def __init__(self):
        image = "images/boat.png" 
        scale = 0.5
        name = "Boat"
        radius = 150
        atk = 1
        rate = 40
        cost = 150
        max = 3
        upgrade_cost = 300
        bullet = "images/oar.png"
        bullet_scale = 0.25
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.radius += 50
        self.level +=1

#upgraded fisherman type, more range, better starting buffs, increase dmage and rate, upgrade = 500
class FLYFISHER(TOWER):

    def __init__(self):
        image = "Images/base_fisherman.png"
        scale = 1.0
        name = "Flyfisher"
        radius = 150
        atk = 1
        rate = 40
        cost = 200
        max = 3
        upgrade_cost = 500
        bullet = "images/sun.png"
        bullet_scale = .2
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.atk *= 1.5
        self.rate -= 5
        self.level +=1

#damage buff - whaler type wider range suuper slow
class NEANDERTHAL(TOWER):

    def __init__(self):
        image = "Images/neanderthal_fisherman.png"
        scale = .75
        name = "Neanderthal"
        radius = 230
        atk = 5
        rate = 50
        cost = 250
        max = 3
        upgrade_cost = 500
        bullet = "images/neanderthal_bullet.png"
        bullet_scale = .75
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.atk *= 2
        self.level +=1

#wizard overall upgrade 
class WIZARD(TOWER):
     
    def __init__(self):
        image = "images/wizard.png"
        scale = 0.3
        name = "Wizard"
        radius = 250
        atk = 10
        rate = 90
        cost = 300
        max = 3
        upgrade_cost = 600
        bullet = "images/fireball.png"
        bullet_scale = .6
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.atk += 3
        self.rate -= 5
        self.radius += 20
        self.bullet_scale += .4
        self.level +=1


#THE GOAT 
class SUPERFISHER(TOWER):
     
    def __init__(self):
        image = "images/superfisherman.png"
        scale = .17
        name = "Superfisher"
        radius = 400
        atk = .2
        rate = 1
        cost = 1000
        max = 3
        upgrade_cost = 2500
        bullet = "images/lasers.png"
        bullet_scale = .2
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.atk *= 2
        self.rate *= 2
        self.radius *= 2
        self.level +=1

#can upgrade a bunch small overall buffs
class ARCHER(TOWER):
      
    def __init__(self):
        image = "images/archer.png"
        scale = .15
        name = "Archer"
        radius = 2000
        atk = 10
        rate = 120
        cost = 400
        max = 3
        upgrade_cost = 10
        bullet = "images/arrow.png"
        bullet_scale = .05
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.rate -=10
        self.level +=1