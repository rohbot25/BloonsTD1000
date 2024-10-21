import arcade
import math

class FISH(arcade.Sprite):

    def __init__(self, image, scale, path,speed):
        #something about the image for the sprite
        super().__init__(image, scale)
        #path
        self.path = path
        self.cur_position = 0
        #speed TODO change based on balloon type? 
        self.speed = speed
    
    def update(self,User):
        #path follow update

        #
        start_x = self.center_x
        start_y = self.center_y

        #end
        dest_x = self.path[self.cur_position][0]
        dest_y = self.path[self.cur_position][1]

        # difference
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        # alingment
        angle = math.atan2(y_diff, x_diff)

        #actual distance
        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        # if close lower speed so doesn't break
        speed = min(self.speed, distance)

        # Calculate vector to travel
        change_x = math.cos(angle) * speed
        change_y = math.sin(angle) * speed

        # Update our location
        self.center_x += change_x
        self.center_y += change_y

        # How far are we?
        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)

        # If we are there, head to the next point.
        if distance <= self.speed:
            self.cur_position += 1

            # Reached the end of the list, start over.
            if self.cur_position >= len(self.path):
                self.cur_position = 0
                User.health -=10
                User.round += 1

class REDFISH(FISH):
    def __init__(path):
        super().__init__("art/base_level_fish.png",1.0,path,1.0)
class BLUEFISH(FISH):
    def __init__(path):
        super().__init__("art/base_level_fish.png",1.0,path,1.0)

class GREENFISH(FISH):
    def __init__(path):
        super().__init__("art/base_level_fish.png",1.0,path,1.0)

class SHARK(FISH):
    def __init__(path):
        super().__init__("art/base_level_fish.png",1.0,path,1.0)
