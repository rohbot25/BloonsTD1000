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
        image = "art/base_fisherman.png" 
        scale = 3.0
        name = "Fisherman"
        radius = 100
        atk = 2
        rate = 30
        cost = 50
        max = 3
        upgrade_cost = 100
        bullet = "images/sun.png"
        bullet_scale = .2
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.rate -= 5
        self.level +=1

#Whaler cost = 100, upgrade = 200, increase damage 2x, slower throw  wider range 
class WHALER(TOWER):
    
    def __init__(self):
        image = "art/god.png"
        scale = 0.2
        name = "God"
        radius = 2000
        atk = 50
        rate = 50
        cost = 0
        max = 3
        upgrade_cost = 0
        bullet = "art/sun_gold.png"
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
        atk = 25
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
        image = "art/base_fisherman.png" 
        scale = 1.0
        name = "Flyfisher"
        radius = 150
        atk = 50
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
        image = "art/base_fisherman.png" 
        scale = 1.0
        name = "Neanderthal"
        radius = 400
        atk = 100
        rate = 50
        cost = 250
        max = 3
        upgrade_cost = 500
        bullet = "images/sun.png"
        bullet_scale = .2
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
        radius = 200
        atk = 50
        rate = 25
        cost = 300
        max = 3
        upgrade_cost = 600
        bullet = "images/fireball.png"
        bullet_scale = .25
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.atk *= 1.5
        self.rate -= 5
        self.radius += 50
        self.level +=1

#THE GOAT 
class SUPERFISHER(TOWER):
     
    def __init__(self):
        image = "art/base_fisherman.png" 
        scale = 3.0
        name = "Superfisher"
        radius = 100
        atk = 100
        rate = 30
        cost = 1000
        max = 3
        upgrade_cost = 2500
        bullet = "images/sun.png"
        bullet_scale = .2
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.atk *= 2
        self.rate *= 2
        self.radius *= 2
        self.level +=1

#can upgrade a bunch small overall buffs
class NETFISHER(TOWER):
      
    def __init__(self):
        image = "art/base_fisherman.png" 
        scale = 3.0
        name = "Netfisher"
        radius = 200
        atk = 25
        rate = 30
        cost = 400
        max = 10
        upgrade_cost = 100
        bullet = "images/sun.png"
        bullet_scale = .2
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale)
    
    def upgrade(self):
        self.radius += 50
        self.atk += 50
        self.rate += 50
        self.level +=1