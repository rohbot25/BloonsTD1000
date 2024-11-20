import arcade
import math
from Game import DeathView


class FISH(arcade.Sprite):

    def __init__(self, image, scale, path, speed, hp, points, start_x=None, start_y=None):
        super().__init__(image, scale)
        self.hp = hp
        self.points = points
        self.path = path
        self.speed = speed
        self.cur_position = 0  # Default start at path index 0

        # Set starting position if provided
        if start_x is not None and start_y is not None:
            self.center_x = start_x
            self.center_y = start_y
            # Find closest point on path to this start position
            self.cur_position = self.find_nearest_path_position(start_x, start_y)
        else:
            # Default start at the beginning of the path
            self.center_x, self.center_y = path[0]

    def find_nearest_path_position(self, x, y):
        # Finds the nearest path position to a given x, y coordinate
        closest_index = 0
        min_distance = float('inf')
        for i, (px, py) in enumerate(self.path):
            dist = math.sqrt((x - px) ** 2 + (y - py) ** 2)
            if dist < min_distance:
                min_distance = dist
                closest_index = i
        return closest_index + 1

    def update(self, User, window):
        start_x = self.center_x
        start_y = self.center_y

        # Destination point on path
        dest_x = self.path[self.cur_position][0]
        dest_y = self.path[self.cur_position][1]

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y

        # Alignment and speed adjustment
        angle = math.atan2(y_diff, x_diff)
        distance = math.sqrt((self.center_x - dest_x) ** 2 + (self.center_y - dest_y) ** 2)
        speed = min(self.speed, distance)

        # Move toward the destination
        self.center_x += math.cos(angle) * speed
        self.center_y += math.sin(angle) * speed

        # If at destination, move to next path point
        if distance <= self.speed:
            self.cur_position += 1
            if self.cur_position >= len(self.path):
                self.remove_from_sprite_lists()
                User.health -= self.hp
                if User.health <= 0:
                    death_view = DeathView()
                    window.show_view(death_view)


class REDFISH(FISH):
    def __init__(self, path, start_x=None, start_y=None):
        super().__init__("Images/level_2_fish.png", 2.75, path, 4, 10, 20, start_x, start_y)

class BLUEFISH(FISH):
    def __init__(self, path, start_x=None, start_y=None):
        super().__init__("Images/base_level_fish.png", 2.75, path, 3, 5, 10, start_x, start_y)

class GREENFISH(FISH):
    def __init__(self, path, start_x=None, start_y=None):
        super().__init__("Images/green_fish.png", 2.75, path, 2, 15, 20, start_x, start_y)

class SHARK(FISH):
    def __init__(self, path, start_x=None, start_y=None):
        super().__init__("Images/blue_blimp_shark.png", 3.5, path, 1, 50, 10, start_x, start_y)

class ORCA(FISH):
    def __init__(self, path, start_x=None, start_y=None):
        super().__init__("Images/Orca.png", 1, path, 0.7, 100, 100, start_x, start_y)