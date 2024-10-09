import arcade
from Map import MAP
import math

# Screen title and size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Fish Tower Defense"

SPRITE_SCALING = 1.0 
BALLOON_SPEED = 2.0

class Balloon(arcade.Sprite):
    #BALOOOOONS

    def __init__(self, image, scale, position_list):
        #something about the image for the sprite
        super().__init__(image, scale)
        #path
        self.path = position_list
        self.cur_position = 0
        #speed TODO change based on balloon type? 
        self.speed = BALLOON_SPEED

    def update(self):
        #path follow update

        #
        start_x = self.center_x
        start_y = self.center_y

        #end
        dest_x = self.position_list[self.cur_position][0]
        dest_y = self.position_list[self.cur_position][1]

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
            #if self.cur_position >= len(self.position_list):
                #self.cur_position = 0

class Game(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMAZON)
        basic_path_cords = [[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3]]
        #second [] is for hazards
        self.current_map = MAP(basic_path_cords,[])
        
        #grid option
        self.path_list = None
        self.hazards_list = None
        self.free_list = None
        
        #map option
        self.texture = None

        self.balloons = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        self.texture = arcade.load_texture("images/map.png")
            
        self.balloons = arcade.SpriteList()

        position_list = [
            [0,220],
            [325,220],
            [325,330],
            [200,330],
            [200,35],
            [85,35],
            [85,130],
            [425,130],
            [425,250],
            [525,250],
            [525,75],
            [300,75],
            [300,0]
        ]

        balloon = Balloon("images/balloon.png",0.5,position_list)

        balloon.center_x = position_list[0][0]
        balloon.center_y = position_list[0][1]

        self.balloons.append(balloon)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        #draw the map
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3, 750,375,self.texture)

        self.balloons.draw()

        # Draw grid overlay
        self.draw_grid()

    def draw_grid(self):
        # Draw a grid on top of the map for easier pixel locating
        grid_size = 25  # Size of each grid cell in pixels
        line_color = arcade.color.GRAY

        # Draw vertical lines
        for x in range(0, SCREEN_WIDTH, grid_size):
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, line_color, 2)

        # Draw horizontal lines
        for y in range(0, SCREEN_HEIGHT, grid_size):
            arcade.draw_line(0, y, SCREEN_WIDTH, y, line_color, 2)
    
    #update the position of the sprites
    def on_update(self,delta_time):
        self.balloons.update()
        
def main():
    """ Main function """
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()