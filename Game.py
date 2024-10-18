import arcade

import math

# Screen title and size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Fish Tower Defense"

SPRITE_SCALING = 1.0 
BALLOON_SPEED = 2.0
BULLET_SPEED = 50.0

class User:
    round = 1
    money = 650
    health = 150

    def __init__(self, round, money, health):
        self.round = round
        self.money = money
        self.health = health

class Balloon(arcade.Sprite):
    #BALOOOOONS

    def __init__(self, image, scale, path):
        #something about the image for the sprite
        super().__init__(image, scale)
        #path
        self.path = path
        self.cur_position = 0
        #speed TODO change based on balloon type? 
        self.speed = BALLOON_SPEED

    def update(self):
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

class Tower(arcade.Sprite):
    def __init__(self, image, scale):
        #something about the image for the sprite
        super().__init__(image, scale)

    def update(self,balloon):
       pass 



class Game(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMAZON)
        
        #map
        self.texture = None

        #balloons TODO will need to switch this to waves?
        self.balloons = None

        #TODO will need to come from map to be able to be placed
        self.towers = None
        self.harpoons = None

        self.frame_count = 0


    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        self.texture = arcade.load_texture("images/map.png")
        self.balloons = arcade.SpriteList()
        self.towers = arcade.SpriteList()
        self.harpoons = arcade.SpriteList()


        #test for top bar


        # Add a tower
        tower = arcade.Sprite("images/sungod.png", 0.5)
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

        balloon = Balloon("images/balloon.png",0.25,position_list)

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
        # create top bar texture
        bar = arcade.load_texture("images/bar2.webp")
        coin = arcade.load_texture("images/coins.png")
        heart = arcade.load_texture("images/health.png")
        sidebar = arcade.load_texture("images/sidebar.jpg")
        paper_banner = arcade.load_texture("images/paper_banner.png")
        # This command has to happen before we start drawing
        self.clear()

        # draw the top bar
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 1.05, 1400, 44, bar)
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 5, SCREEN_HEIGHT // 1.05, 40, 40, coin)
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 30, SCREEN_HEIGHT // 1.05, 40, 40, heart)

        arcade.draw_text(f": {User.health}",
                         start_x=50,
                         start_y=SCREEN_HEIGHT - 35,
                         color=arcade.color.BLACK,
                         font_size=24,
                         font_name="Comic Sans MS")

        arcade.draw_text(f"Round: {User.round}",
                         start_x=SCREEN_WIDTH - 350,
                         start_y=SCREEN_HEIGHT - 35,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="right",
                         width=300,
                         font_name="Comic Sans MS")

        arcade.draw_text(f": {User.money}",
                         start_x=SCREEN_WIDTH - 1000,
                         start_y=SCREEN_HEIGHT - 35,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="right",
                         width=300,
                         font_name="Comic Sans MS")

        # draw sidebar
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 2.2, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 1.1, sidebar)
        arcade.draw_rectangle_filled(825, 350, 75, 75, (0, 0, 0, 128))
        arcade.draw_rectangle_filled(925, 350, 75, 75, (0, 0, 0, 128))
        arcade.draw_rectangle_filled(825, 250, 75, 75, (0, 0, 0, 128))
        arcade.draw_rectangle_filled(925, 250, 75, 75, (0, 0, 0, 128))
        arcade.draw_rectangle_filled(825, 150, 75, 75, (0, 0, 0, 128))
        arcade.draw_rectangle_filled(925, 150, 75, 75, (0, 0, 0, 128))
        arcade.draw_rectangle_filled(825, 50, 75, 75, (0, 0, 0, 128))
        arcade.draw_rectangle_filled(925, 50, 75, 75, (0, 0, 0, 128))

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 1.17, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 9, paper_banner)

        arcade.draw_text(f"Fishermen",
                         start_x= SCREEN_WIDTH // 1.53,
                         start_y= SCREEN_HEIGHT // 1.2,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="right",
                         width=300,
                         font_name="Comic Sans MS")

        #draw the map
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2.45, 825,500,self.texture)

        self.balloons.draw()
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
        self.balloons.update()

        self.frame_count += 1

        for tower in self.towers:
            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = tower.center_x
            start_y = tower.center_y

            # Get the destination location for the bullet
            dest_x = self.balloons[0].center_x
            dest_y = self.balloons[0].center_y

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

        # Get rid of the bullet when it flies off-screen
        for bullet in self.harpoons:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()
            elif bullet.top == Balloon.top:
                User.money +=50

        self.harpoons.update()

        
def main():
    """ Main function """
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()