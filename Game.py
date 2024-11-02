import arcade
import arcade.gui
import math
import time
import random

#from tensorflow.python.ops.metrics_impl import true_positives

from tower import TOWER, FISHERMAN, WHALER, BOAT, FLYFISHER, NEANDERTHAL, WIZARD, SUPERFISHER, NETFISHER
from Fish import FISH
from User import USER
from Sidebar import SIDEBAR
# Screen title and size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Fish Tower Defense"

SPRITE_SCALING = 1.0 
BALLOON_SPEED = 2.0
BULLET_SPEED = 50.0

BUY_BOX_SIZE = 75


class Button:
    def __init__(self, x, y, width, height, tower_type, cost, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tower_type = tower_type
        self.cost = cost
        self.image = image
        self.is_hovered = False

    def draw(self):
        # Draw the button
        arcade.draw_texture_rectangle(self.x,
                                      self.y,
                                      self.width,
                                      self.height,
                                      self.image)

        if self.is_hovered:
            arcade.draw_rectangle_outline(self.x, self.y, 75, 75, arcade.color.BLACK, 3)

    def check_hover(self, mouse_x, mouse_y):
        # print(f"width: {self.width} // self.height: {self.height}")
        self.is_hovered = (
                self.x - self.width / 2 < mouse_x < self.x + self.width / 2 and
                self.y - self.height / 2 < mouse_y < self.y + self.height / 2
        )

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

class GameView(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()
        
        self.showUpgrade = False
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

        # Track the currently selected tower
        self.selected_tower_type = None
        # Track whether dragging is active
        self.is_dragging = False

        self.frame_count = 0

        self.user = USER()
        self.upgradeMenu = SIDEBAR(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 2.2, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 1.1)


        #pasued state for stopping between rounds
        self.paused = False

        
    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        self.texture = arcade.load_texture("images/map.png")
        self.fishes = arcade.SpriteList()

        #queue for fishes to be spawned from
        self.fish_queue = arcade.SpriteList()
        self.towers = arcade.SpriteList()
        self.harpoons = arcade.SpriteList()
        self.user.round = 1
        self.spawn_cycle_count = 0 


        # Add a tower
        tower = TOWER("images/sungod.png", "tower", 250,3,4)
        tower.center_x = 600
        tower.center_y = 200
        tower.angle = 180
        tower.scale=.5
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

        balloon = FISH("images/balloon.png",0.25,position_list, 2, 10, 100)

        balloon.center_x = position_list[0][0]
        balloon.center_y = position_list[0][1]

        self.fishes.append(balloon)
        self.last_spawn_time = time.time()

    def on_mouse_press(self, x, y, button, key_modifiers):
    #""" Called when the user presses a mouse button. """
        #if upgrade menu is open and your are clicking on the menu, skip
        if (self.showUpgrade and x >= 746):
            pass
        #else check if they are clicking on a tower
        else:
            self.showUpgrade = False
            for tower in self.towers:
                if tower.collides_with_point((x,y)):
                    print("open menu")
                    self.tower = tower.name
                    self.upgradeName = "upgrade"
                    self.upgradeLevel = tower.level
                    self.showUpgrade = True
                    button_x = 825
                    button_y = 350
                    button = Button(button_x, button_y, 75, 500, FISHERMAN(), 100, arcade.load_texture("images/health.png"))
                    self.upgradeMenu.add_button(button)

        # Check if a tower is being dragged
        if self.is_dragging:
            return  # Ignore clicks while dragging

        # Check if any button in the sidebar is clicked
        for button in self.sidebar.buttons:
            if button.is_hovered and self.user.money >= button.cost:
                # Start dragging the selected tower type
                self.selected_tower_type = button.tower_type
                self.current_tower = self.selected_tower_type()  # Instantiate the tower
                self.current_tower.center_x = x
                self.current_tower.center_y = y
                self.is_dragging = True
                print(f"{button.tower_type.__name__} selected!")
                break
            
        #if paused, unpause on mouse click
        if self.paused and button == arcade.MOUSE_BUTTON_LEFT:
            self.paused = False  # Resume the game on left click


    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        if self.is_dragging:
            # Finalize tower placement
            if self.user.money >= self.current_tower.cost:
                self.towers.append(self.current_tower)  # Add the tower to the list
                self.user.money -= self.current_tower.cost  # Deduct cost
                print(f"Placed {self.current_tower.__class__.__name__} at ({x}, {y})")

            # Stop dragging and reset
            self.is_dragging = False
            self.current_tower = None

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        self.mouse_x = x
        self.mouse_y = y
        #print(f"mouse x: {self.mouse_x} // mouse y: {self.mouse_y}")

        #checks if buttons are hovered
        for button in self.sidebar.buttons:
            button.check_hover(x, y)

        # Update the position of the tower being placed if dragging
        if self.is_dragging and self.current_tower is not None:
            self.current_tower.center_x = x
            self.current_tower.center_y = y

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        
        # create all texture
        bar = arcade.load_texture("images/bar2.png")
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

        # if not show upgrade menu, draw and act with the shop
        if not self.showUpgrade:
            # Sidebar
            self.sidebar = SIDEBAR(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 2.2, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 1.1)
            # left buttons
            button_positions = [
            (825, 350), (825, 250), (825, 150), (825, 50),
            (925, 350), (925, 250), (925, 150), (925, 50)
            ]
            tower_types = [FISHERMAN, WHALER, BOAT, FLYFISHER, NEANDERTHAL, WIZARD, SUPERFISHER, SUPERFISHER]

            for (button_x, button_y), tower_type in zip(button_positions, tower_types):
                button = Button(button_x, button_y, 75, 75, tower_type(), 100, buy_fisherman)
                button.tower_type = tower_type  # Assign the class, not an instance
                self.sidebar.add_button(button)

            # Update hover states and draw the sidebar
            for button in self.sidebar.buttons:
                button.check_hover(self.mouse_x, self.mouse_y)

                self.sidebar.draw(sidebar, paper_banner)
        #else draw the upgrade sidebar
        else:
            self.sidebar = SIDEBAR(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 2.2, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 1.1)
            self.upgradeMenu.drawUpgrade(paper_banner, paper_banner)
           
        # Create buttons
        


        #draw the map
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2.45, 825,500,self.texture)

        # for button in self.sidebar.buttons:
        #     if button.cost > self.user.money:
        #         #draw transparetn red over button
        #         pass
        # else:
        #     # Draw the currently placed tower if dragging
        #     if self.is_dragging and self.current_tower is not None:
        #         # Draw the current tower following the mouse
        #         self.current_tower.draw()

        self.fishes.draw()
        self.towers.draw()
        self.harpoons.draw()

        # Display the currently placed tower if dragging
        if self.is_dragging and self.current_tower is not None:
            self.current_tower.draw()

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

#if paused, eturn, wait to be unpaused
        if self.paused:
            return
        
#update cycle counter, each call to update is 1 cycle
        self.spawn_cycle_count += 1

#position list for creating new balloons
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

        

        for fish in self.fishes:
            fish.update(self.user)

        self.frame_count += 1
        if self.user.health == 0:
            pass

        # Get the current mouse position
        mouse_x, mouse_y = self.mouse_x, self.mouse_y

        # makes it so the game doesnt crash when there are no balloons, will change in future
        if len(self.fishes) >0:
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

                if tower.center_x - self.fishes[0].center_x < tower.radius:
                    # Set the enemy to face the player
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
                else:
                    for fish in self.fishes:
                        if arcade.check_for_collision(bullet, fish):
                            bullet.remove_from_sprite_lists()
                            self.user.money += 50

                            # Decrease the health of the fish/balloon when hit
                            fish.hp -= 1

                            # If the fish's health reaches zero, remove it from the list
                            if fish.hp <= 0:
                                self.fishes.remove(fish)
        else:
            # pause at round end
            self.paused = True
            
            #increment round
            self.user.round += 1

            #generate wave based on round number
            for i in range(self.user.round**2):
                Balloon = FISH("images/balloon.png",0.25,position_list, 2, 10, 100)
                Balloon.center_x = position_list[0][0]
                Balloon.center_y = position_list[0][1]
                #add fish to queue list
                self.fish_queue.append(Balloon)
                
        #seperate spawning of balloons by 5 update cycles
        if (self.spawn_cycle_count >= 5 and (len(self.fish_queue) > 0)):

            #reset update cycle counter
            self.spawn_cycle_count = 0

            #spawn fish from end of queue list
            self.fishes.append(self.fish_queue[(len(self.fish_queue)-1)])

            #remove fish from end of queue list
            self.fish_queue.pop()

        self.harpoons.update()
        
        

class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the start button
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        start_button.on_click = self.on_click_start
        self.v_box.add(start_button.with_space_around(bottom=20))

        # Create the help button
        help_button = arcade.gui.UIFlatButton(text="Help", width=200)
        help_button.on_click = self.on_click_help
        self.v_box.add(help_button.with_space_around(bottom=20))

        # Create the map select button
        map_select_button = arcade.gui.UIFlatButton(text="Select Map", width=200)
        map_select_button.on_click = self.on_click_map_select
        self.v_box.add(map_select_button)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Fish Tower Defense", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        self.manager.draw()

    def on_click_start(self, event):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

    def on_click_help(self, event):
        help_view = HelpView()
        self.window.show_view(help_view)

    def on_click_map_select(self, event):
        map_select_view = MapSelectView()
        self.window.show_view(map_select_view)

    def on_hide_view(self):
        self.manager.disable()

class HelpView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Help Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Instructions on how to play the game.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Click to go back", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        start_view = StartView()
        self.window.show_view(start_view)

class MapSelectView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Select Map", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Map selection screen. Click to go back.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        start_view = StartView()
        self.window.show_view(start_view)

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
