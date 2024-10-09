import arcade
from Map import MAP

# Screen title and size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Fish Tower Defense"

SPRITE_SCALING = 0.5


class Game(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMAZON)
        basic_path_cords = [[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3]]
        #second [] is for hazards
        self.current_map = MAP(basic_path_cords,[])
        
        self.path_list = None
        self.hazards_list = None
        self.free_list = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.path_list = arcade.SpriteList()
        self.free_list = arcade.SpriteList()
        
        #self.hazardsList
        map_end_horiz = int(SCREEN_WIDTH*(3/4))
        square_size = int(map_end_horiz / self.current_map.get_size())

        map_start = square_size

        map_end_vert = int(SCREEN_HEIGHT - square_size)
        
        coord = [0,0]
        for x in range(map_start,map_end_horiz,square_size):
            for y in range(map_start,map_end_vert,square_size):
                if(coord in self.current_map.get_path()):
                    path = arcade.Sprite("images/Path.png",SPRITE_SCALING)
                    path.center_x = x
                    path.center_y = y
                    self.path_list.append(path)
                elif(coord in self.current_map.get_hazards()):
                    pass
                else:
                    free = arcade.Sprite("images/Grass.png",SPRITE_SCALING)
                    free.center_x = x
                    free.center_y = y
                    self.free_list.append(free)
                
                coord[1] += 1 
                coord[1] = coord[1] % 6
                print(coord)
            coord[0] += 1
            print(coord)




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

        # Draw all the sprites.
        self.path_list.draw()
        self.free_list.draw()
        #self.hazards_list.draw()


def main():
    """ Main function """
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()