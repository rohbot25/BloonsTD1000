import arcade
import math
from tower import TOWER
from Fish import FISH
from User import USER
# Screen title and size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Fish Tower Defense"

SPRITE_SCALING = 1.0 
BALLOON_SPEED = 2.0
BULLET_SPEED = 50.0

BUY_BOX_SIZE = 75

class Sidebar:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Creating the location for all the boxes
        self.box_list = [
            [825, 350],
            [925, 350],
            [825, 250],
            [925, 250],
            [825, 150],
            [925, 150],
            [825, 50],
            [925, 50]
        ]
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def draw(self, sidebar, paper_banner):
        # Draw the sidebar background
        arcade.draw_texture_rectangle(self.x,
                                      self.y,
                                      self.width,
                                      self.height,
                                      sidebar)
        for box_x, box_y in self.box_list:
            arcade.draw_rectangle_filled(box_x, box_y, BUY_BOX_SIZE, BUY_BOX_SIZE, (0, 0, 0, 128))
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 1.145,
                                      SCREEN_HEIGHT // 1.17,
                                      self.width,
                                      self.height // 9,
                                      paper_banner)
        arcade.draw_text(f"Fishermen",
                         start_x=SCREEN_WIDTH // 1.53,
                         start_y=SCREEN_HEIGHT // 1.2,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="right",
                         width=300,
                         font_name="Comic Sans MS")
    #
    #     # Draw the buttons
    #     for button in self.buttons:
    #         button.draw()

class Button:
    def __init__(self, x, y, width, height, tower, cost):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tower_type = tower
        self.cost = cost

    def draw(self, image):
        # Draw the button
        arcade.draw_texture_rectangle(self.x,
                                      self.y,
                                      self.width,
                                      self.height // 9,
                                      image)

#
#     def is_clicked(self, x, y):
#         return (
#             self.x <= x <= self.x + self.width and
#             self.y <= y <= self.y + self.height
#         )

class GameView(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()
        
        #map
        self.texture = None

        #balloons TODO will need to switch this to waves?
        self.fishes = None

        #TODO will need to come from map to be able to be placed
        self.towers = None
        self.harpoons = None

        # Initialize mouse position
        self.mouse_x = 0
        self.mouse_y = 0

        self.frame_count = 0

        self.user = USER()

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        self.texture = arcade.load_texture("images/map.png")
        self.fishes = arcade.SpriteList()
        self.towers = arcade.SpriteList()
        self.harpoons = arcade.SpriteList()

        # Add a tower
        tower = TOWER("images/sungod.png", "tower", 2,3,4)
        tower.center_x = 600
        tower.center_y = 200
        tower.angle = 180
        self.towers.append(tower)

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

        balloon = FISH("images/balloon.png",0.25,position_list)

        balloon.center_x = position_list[0][0]
        balloon.center_y = position_list[0][1]

        self.fishes.append(balloon)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        self.mouse_x = x
        self.mouse_y = y

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        
        # create all texture
        bar = arcade.load_texture("images/coins.png")
        coin = arcade.load_texture("images/coins.png")
        heart = arcade.load_texture("images/health.png")
        sidebar = arcade.load_texture("images/sidebar.jpg")
        paper_banner = arcade.load_texture("images/paper_banner.png")
        buy_fisherman = arcade.load_texture("art/base_fisherman.png")
        # This command has to happen before we start drawing
        self.clear()

        # draw the top bar
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 1.05, 1400, 44, bar)
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.05, 40, 40, coin)
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 30, SCREEN_HEIGHT // 1.05, 40, 40, heart)

        arcade.draw_text(f": {self.user.health}",
                         start_x=50,
                         start_y=SCREEN_HEIGHT - 35,
                         color=arcade.color.BLACK,
                         font_size=24,
                         font_name="Comic Sans MS")

        arcade.draw_text(f"Round: {self.user.round}",
                         start_x=SCREEN_WIDTH - 350,
                         start_y=SCREEN_HEIGHT - 35,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="right",
                         width=300,
                         font_name="Comic Sans MS")

        arcade.draw_text(f": {self.user.money}",
                         start_x=SCREEN_WIDTH - 1000,
                         start_y=SCREEN_HEIGHT - 35,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="right",
                         width=300,
                         font_name="Comic Sans MS")

        # draw sidebar

        # Sidebar
        self.sidebar = Sidebar(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 2.2, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 1.1)
        self.sidebar.draw(sidebar, paper_banner)

        # left buttons
        for i in range(3):
            Button(850, 350, 75, 500, "fisherman", 100)

        # right buttons
        for i in range(3):
            Button(850, 350, 75, 500, "fisherman", 100)





        #draw the map
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2.45, 825,500,self.texture)

        self.fishes.draw()
        self.towers.draw()
        self.harpoons.draw()

        # Draw grid overlay
        #self.draw_grid()

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
        for fish in self.fishes:
            fish.update(self.user)

        self.frame_count += 1
        if self.user.health == 0:
            pass

        # Get the current mouse position
        mouse_x, mouse_y = self.mouse_x, self.mouse_y



        for tower in self.towers:
            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = tower.center_x
            start_y = tower.center_y

            # Get the destination location for the bullet
            dest_x = self.fishes[0].center_x
            dest_y = self.fishes[0].center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            tower.angle = math.degrees(angle) - 90

            # Shoot every 60 frames change of shooting each frame
            if self.frame_count % 30 == 0:
                bullet = arcade.Sprite("images/sun.png",.1)
                bullet.center_x = start_x
                bullet.center_y = start_y

                # Angle the bullet sprite
                bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet.change_x = math.cos(angle) * BULLET_SPEED
                bullet.change_y = math.sin(angle) * BULLET_SPEED

                self.harpoons.append(bullet)

        # Get rid of the bullet when it flies off-screen or when it hits a balloon
        for bullet in self.harpoons:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()
            elif arcade.check_for_collision(bullet, self.fishes[0]):
                bullet.remove_from_sprite_lists()
                self.user.money += 50


        self.harpoons.update()
        

class StartView(arcade.View):
    # View for the start screen

    def on_show(self):
        # Set background color when view is shown
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        # Draw the start screen
        self.clear()
        arcade.draw_text("Fish Tower Defense", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to start", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # Start the game when the mouse is pressed
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class Game(arcade.Window):
    # Main application class

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.start_view = StartView()
        self.show_view(self.start_view)


def main():
    """ Main function """
    window = Game()
    arcade.run()


if __name__ == "__main__":
    main()
