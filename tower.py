import arcade

class TOWER(arcade.Sprite):
    
    def __init__(self,image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale,bullet_speed):
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
        self.bullet_speed = bullet_speed

        

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
        upgrade_cost = cost
        bullet = "images/fishhook.png"
        bullet_scale = 1.5
        bullet_speed = 25
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale,bullet_speed)
    
    def upgrade(self):
        self.rate -= 5
        self.level +=1
        self.upgrade_cost += self.level * 200

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
        upgrade_cost = cost
        bullet = "images/sun_gold.png"
        bullet_scale = 0.33
        bullet_speed = 20
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale, bullet_speed)
        
    
    def upgrade(self):
        self.atk *= 2
        self.level +=1
        self.upgrade_cost += self.level * 200

#Boat cost = 150 upgrade = 300, increase range, same attack and speed as base fisherman
class BOAT(TOWER):

    def __init__(self):
        image = "images/boat.png" 
        scale = 0.5
        name = "Boat"
        radius = 150
        atk = 1
        rate = 20
        cost = 150
        max = 3
        upgrade_cost = cost
        bullet = "images/oar.png"
        bullet_scale = 0.25
        bullet_speed = 25
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale,bullet_speed)
    
    def upgrade(self):
        self.radius += 50
        self.rate -=5
        self.level +=1
        self.upgrade_cost += self.level * 200

#upgraded fisherman type, more range, better starting buffs, increase dmage and rate, upgrade = 500
class FLYFISHER(TOWER):

    def __init__(self):
        image = "Images/fly_fisherman.png"
        scale = .9
        name = "Flyfisher"
        radius = 150
        atk = 1
        rate = 15
        cost = 200
        max = 3
        upgrade_cost = cost
        bullet = "images/coins.png"
        bullet_scale = .4
        bullet_speed = 35
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale,bullet_speed)
    
    def upgrade(self):
        self.atk *= 1.75
        self.rate -= 2
        self.level +=1
        self.upgrade_cost += self.level * 200

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
        upgrade_cost = cost
        bullet = "images/neanderthal_bullet.png"
        bullet_scale = .75
        bullet_speed = 35
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale,bullet_speed)
    
    def upgrade(self):
        self.atk *= 2
        self.level +=1
        self.upgrade_cost += self.level * 200

#wizard overall upgrade 
class WIZARD(TOWER):
     
    def __init__(self):
        image = "images/wizard.png"
        scale = 0.35
        name = "Wizard"
        radius = 250
        atk = 10
        rate = 90
        cost = 300
        max = 3
        upgrade_cost = cost
        bullet = "images/fireball.png"
        bullet_scale = .75
        bullet_speed = 20
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale, bullet_speed)
    
    def upgrade(self):
        self.atk += 3
        self.rate -= 5
        self.radius += 20
        self.bullet_scale += .3
        self.level +=1
        self.upgrade_cost += self.level * 200


#THE GOAT 
class SUPERFISHER(TOWER):
     
    def __init__(self):
        image = "images/superfisherman.png"
        scale = .17
        name = "Superfisher"
        radius = 350
        atk = .2
        rate = 1
        cost = 1000
        max = 1
        upgrade_cost = cost
        bullet = "images/lasers.png"
        bullet_scale = .2
        bullet_speed = 50
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale,bullet_speed)
    
    def upgrade(self):
        self.atk *= 2
        self.radius *= 1.2
        self.level +=1
        self.upgrade_cost += self.level * 200

#can upgrade a bunch small overall buffs
class ARCHER(TOWER):
      
    def __init__(self):
        image = "images/archer.png"
        scale = .15
        name = "Archer"
        radius = 2000
        atk = 15
        rate = 120
        cost = 400
        max = 3
        upgrade_cost = cost
        bullet = "images/arrow.png"
        bullet_scale = .1
        bullet_speed = 55
        super().__init__(image,scale, name, radius, atk, rate,max,cost,upgrade_cost,bullet,bullet_scale,bullet_speed)
    
    def upgrade(self):
        self.rate -=10
        self.level +=1
        self.upgrade_cost += self.level * 200
