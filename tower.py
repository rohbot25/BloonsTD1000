class Tower:
    #Unique ID
    ID = 0
    #Attack Radius
    radius = 2.0
    
    #Damage per attack
    atk = 50

    #Rate of attack
    rate = 1;

    #Name of tower
    name = "Fisherman"

    #Upgrade number, could change to a tuple if we want to add upgrade paths
    #Should not be altered upon initializing
    upg = 0
    
    
    def __init__(self, ID, name, radius, atk, rate):
        self.ID = ID
        self.name = name
        self.radius = radius
        self.atk = atk
        self.rate = rate

    def upgrade(upg, radius, atk, rate):
        upg += 1
        radius += .5
        atk += 25
        rate += .5
        

    

    
