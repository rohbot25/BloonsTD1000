import arcade
import time
import math
import random

# Screen title and size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Fish Tower Defense"

BULLET_SPEED = 35

from User import USER
from Sidebar import SIDEBAR
from tower import FISHERMAN, FLYFISHER, WHALER, NEANDERTHAL, WIZARD, BOAT, SUPERFISHER, NETFISHER
from Fish import  REDFISH, BLUEFISH, GREENFISH, SHARK, ORCA, WHALE
from Button import BUTTON
from Button import PauseUnpause

import arcade
import arcade.gui
import numpy


class GameView(arcade.View):
    """ Main application class. """

    def __init__(self, selected_map):
        super().__init__()

        self.show_upgrade = False
        self.upgrade_made = False
        #map
        self.texture = None

        #selected map for map selection
        self.selected_map = selected_map

        #pause button declaration
        self.pause_button = PauseUnpause(x=700, y=425, width=80, height=80, image=arcade.load_texture("Images/Pause.png"))

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
        self.upgrade_menu = SIDEBAR(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 2.2, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 1.1)

        #pasued state for stopping between rounds
        self.paused = False



    def setup(self):
        """ Set up the game here. Call this function to restart the game. """


        #set map to selected map
        self.map = self.selected_map
        self.texture = arcade.load_texture(self.map)
        self.fishes = arcade.SpriteList()

        #queue for fishes to be spawned from
        self.fish_queue = arcade.SpriteList()
        self.towers = arcade.SpriteList()
        self.harpoons = arcade.SpriteList()
        self.restricted = arcade.SpriteList() # List for restircted areas (transparent blocks/towers)

        self.user.round = 1
        self.spawn_cycle_count = 0

        position_list = [
            [0,275],
            [335,275],
            [335,425],
            [190,425],
            [190,35],
            [60,35],
            [60,175],
            [450,175],
            [450,335],
            [550,335],
            [550,75],
            [300,75],
            [300,0]
        ]

        # Points for topbar to restrict
        self.tb_y_start = 450
        self.tb_y_end = 500
        self.tb_x_start = 0
        self.tbsb_x_end = 1000
        # Points for sidebar to restrict
        self.sb_y_end = 450
        self.sb_y_start = 0
        self.sb_x_start = 750

        balloon = BLUEFISH(position_list)

        balloon.center_x = position_list[0][0]
        balloon.center_y = position_list[0][1]

        self.fishes.append(balloon)
        self.last_spawn_time = time.time()

    def on_mouse_press(self, x, y,button_fake, key_modifiers):
        #""" Called when the user presses a mouse button. """
        #if upgrade menu is open and your are clicking on the menu, skip

        if (self.show_upgrade and x >= 746):
            for button in self.upgrade_menu.buttons:
                button.check_hover(x,y)
                if button.is_hovered:
                    if button.cost != 0:
                        if self.user.money >= button.cost and self.tower.level < self.tower.max:
                            self.user.money -= button.cost
                            self.tower.upgrade()
                            self.max = self.tower.max
                            print(f"upgrade made!")
                            paper_banner = arcade.load_texture("images/paper_banner.png")
                            self.upgrade_menu.drawUpgrade(paper_banner, paper_banner,self.tower_name,self.tower)
                            self.upgrade_made = True
                    else:
                        print("trashing tower")
                        self.towers.remove(self.tower)
                        self.user.money += self.tower.cost // 2
                        print("sold for: " + str(self.tower.cost //2) )
                        self.show_upgrade = False

        #else check if they are clicking on a tower
        else:
            print("woah")
            self.show_upgrade = False
            for tower in self.towers:
                if tower.collides_with_point((x,y)):
                    print("open menu")
                    self.tower = tower
                    self.tower_name = tower.name
                    self.upgrade_level = tower.level
                    self.max = tower.max
                    self.upgrade_cost = tower.upgrade_cost
                    self.show_upgrade = True

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
            self.pause_button.on_mouse_press(x, y, button, key_modifiers)


    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if self.is_dragging and self.current_tower:

            xy_restrictions=[
                [[0,300],[250,300]],
                [[300,350],[250,450]],
                [[175,350],[400,450]],
                [[175,225],[25,450]],
                [[50,225],[0,50]],
                [[25,75],[25,175]],
                [[50,450],[150,200]],
                [[425,475],[175,350]],
                [[425,550],[300,350]],
                [[525,575],[75,325]],
                [[275,575],[50,125]],
                [[275,325],[0,100]]
            ]

            if not (self.is_in_restricted_sb_tb(x, y)
                    or not self.has_sufficient_money()
                    or not self.is_in_restricited_path(x, y, xy_restrictions)):

                self.current_tower.center_x = x
                self.current_tower.center_y = y
                self.towers.append(self.current_tower)  # Add the tower to the list
                self.user.money -= self.current_tower.cost  # Deduct cost
                print(f"Placed {self.current_tower.__class__.__name__} at ({x}, {y})")
                print(self.towers)
            else:
                print("Cannot place tower in restricted area.")
            # Stop dragging and reset
            self.is_dragging = False
            self.current_tower = None
            #Check for pause
        self.pause_button.on_mouse_release(x, y, button, modifiers)
        self.paused = self.pause_button.paused


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

        #check for pause hover
        self.pause_button.check_hover(x, y)

    # Has the money for a tower
    def has_sufficient_money(self):
        return self.user.money >= self.current_tower.cost

    # Checks to see if there are other towers there
    def can_place_tower(self, x, y):
        return all(
            abs(tower.center_x - x) >= 10 or abs(tower.center_y - y) >= 10
            for tower in self.towers
        )

    # Checks for sidebar or topbar
    def is_in_restricted_sb_tb(self, x, y):
        return (
                (self.tb_x_start < x < self.tbsb_x_end and self.tb_y_start < y < self.tb_y_end) or
                (self.sb_x_start < x < self.tbsb_x_end and self.sb_y_start < y < self.sb_y_end)
        )

    # Checks each point
    def is_in_restricited_path(selfself, x, y, path):
        for restriction in path:
            x_range, y_range = restriction
            if x_range[0] < x < x_range[1] and y_range[0] < y < y_range[1]:
                return False  # Point is in a restricted area
        return True  # Point is not in any restricted area


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
        buy_fisherman = arcade.load_texture("images/base_fisherman.png")
        buy_boat = arcade.load_texture("images/boat.png")
        buy_superfisherman = arcade.load_texture("images/superfisherman.png")
        buy_wizard = arcade.load_texture("images/wizard.png")
        buy_god = arcade.load_texture("images/god.png")
        buy_neanderthal = arcade.load_texture("images/neanderthal_fisherman.png")
        buy_archer =arcade.load_texture("images/archer.png")
        upgrade = arcade.load_texture("images/upgrade.png")
        trash = arcade.load_texture("images/trash.png")


        # This command has to happen before we start drawing
        self.clear()

        # if not show upgrade menu, draw and act with the shop

        #draw the map
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2.45, 825,500,self.texture)

        if not self.show_upgrade:
            # Sidebar
            self.sidebar = SIDEBAR(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 2.2, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 1.1)
            # left buttons
            button_positions = [
                (825, 350), (825, 250), (825, 150), (825, 50),
                (925, 350), (925, 250), (925, 150), (925, 50)
            ]
            tower_types = [FISHERMAN, WHALER, BOAT, FLYFISHER, NEANDERTHAL, WIZARD, SUPERFISHER, NETFISHER]
            tower_images = [buy_fisherman,buy_god,buy_boat,buy_fisherman,buy_neanderthal,buy_wizard,buy_superfisherman,buy_archer]
            for (button_x, button_y), tower_type, tower_image in zip(button_positions, tower_types,tower_images):
                tower_instance = tower_type()  # Instantiate the class to access attributes
                button = BUTTON(button_x, button_y, 75, 75, tower_type(), tower_instance.cost, tower_image)
                button.tower_type = tower_type  # Assign the class, not an instance
                button.tower_name = tower_instance.name # Access name on an instance
                self.sidebar.add_button(button)

            # Update hover states and draw the sidebar
            for button in self.sidebar.buttons:
                button.check_hover(self.mouse_x, self.mouse_y)

            self.sidebar.draw(sidebar, paper_banner)
        #else draw the upgrade sidebar
        else:
            self.upgrade_menu = SIDEBAR(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 2.2, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 1.1)
            # left buttons
            upgrade_button = BUTTON(875, 250, 75, 75,self.tower, self.upgrade_cost, upgrade)
            trash_button = BUTTON(875,125,75,75,self.tower,0,trash)
            self.upgrade_menu.add_button(upgrade_button)
            self.upgrade_menu.add_button(trash_button)

            arcade.draw_circle_filled(self.tower.center_x,self.tower.center_y,self.tower.radius,(128,128,128,128))
            if not self.upgrade_made:
                self.upgrade_menu.drawUpgrade(paper_banner, paper_banner,self.tower_name,self.tower)
            else:
                self.upgrade_made = False


        # draw the top bar
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 1.05, 1400, 44, bar)
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 5.7, SCREEN_HEIGHT // 1.05, 40, 40, coin)
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


        self.fishes.draw()
        self.towers.draw()
        self.harpoons.draw()

        # Display the currently placed tower if dragging
        if self.is_dragging and self.current_tower is not None:
            self.current_tower.draw()

        #self.draw_grid()

        #Draw Pause Button
        self.pause_button.draw()



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
    def on_update(self, delta_time):
        # If paused, return and wait to be unpaused
        hits = 0
        if self.paused:
            return
        position_list = [
            [0, 275],
            [55.835, 275],
            [111.67, 275],
            [167.5, 275],
            [223.33, 275],
            [279.165, 275],
            [335, 275],

            [335, 300],
            [335, 325],
            [335, 350],
            [335, 375],
            [335, 400],
            [335, 425],

            [310.835, 425],
            [286.67, 425],
            [262.5, 425],
            [238.33, 425],
            [214.165, 425],
            [190, 425],

            [190, 360],
            [190, 295],
            [190, 230],
            [190, 165],
            [190, 100],
            [190, 35],

            [168.335, 35],
            [146.67, 35],
            [125, 35],
            [103.33, 35],
            [81.665, 35],
            [60, 35],

            [60, 58.335],
            [60, 81.67],
            [60, 105],
            [60, 128.33],
            [60, 151.665],
            [60, 175],

            [125, 175],
            [190, 175],
            [255, 175],
            [320, 175],
            [385, 175],
            [450, 175],

            [450, 201.665],
            [450, 228.33],
            [450, 255],
            [450, 281.67],
            [450, 308.335],
            [450, 335],

            [483.335, 335],
            [516.67, 335],
            [550, 335],
            [566.665, 335],
            [583.33, 335],

            [550, 286.665],
            [550, 238.33],
            [550, 190],
            [550, 141.67],
            [550, 108.335],
            [550, 75],

            [500, 75],
            [450, 75],
            [412.5, 75],
            [375, 75],
            [337.5, 75],
            [300, 75],

            [300, 62.5],
            [300, 50],
            [300, 37.5],
            [300, 25],
            [300, 12.5],
            [300, 0]
        ]
        # Update cycle counter
        self.spawn_cycle_count += 1

        # Update fish positions
        for fish in self.fishes:
            fish.update(self.user, self.window)

        self.frame_count += 1  # Increment frame count

        # Spawn logic: spawn fish from queue if it's time
        if self.spawn_cycle_count >= 10 and len(self.fish_queue) > 0:
            self.spawn_cycle_count = 0  # Reset spawn cycle counter

            # Spawn fish from the end of the queue
            self.fishes.append(self.fish_queue.pop())

        # Pause when all fish have been spawned for the round
        if len(self.fish_queue) == 0 and len(self.fishes) == 0:
            # Pause at round end
            print("PAUSED!")
            self.user.round += 1
            self.paused = True
            self.pause_button.paused = True
            self.harpoons.clear()

            # generate wave based on round number Hard code
            # Populate fish queue based on the round
            if True == True:
                if self.user.round == 2:
                    for i in range(5):
                        balloon = BLUEFISH(position_list)
                        balloon.center_x, balloon.center_y = position_list[0]
                        self.fish_queue.append(balloon)
                    for i in range(1):
                        whale = WHALE(position_list)
                        whale.center_x, whale.center_y = position_list[0]
                        self.fish_queue.append(whale)

                elif self.user.round == 3:
                    for i in range(8):
                        balloon = BLUEFISH(position_list)
                        balloon.center_x, balloon.center_y = position_list[0]
                        self.fish_queue.append(balloon)

                elif self.user.round == 4:
                    for i in range(12):
                        balloon = BLUEFISH(position_list)
                        balloon.center_x, balloon.center_y = position_list[0]
                        self.fish_queue.append(balloon)

                elif self.user.round == 5:
                    for i in range(4):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)

                elif self.user.round == 6:
                    for i in range(8):
                        blue_fish = BLUEFISH(position_list)
                        blue_fish.center_x, blue_fish.center_y = position_list[0]
                        self.fish_queue.append(blue_fish)

                    for i in range(2):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)

                elif self.user.round == 7:
                    for i in range(9):
                        blue_fish = BLUEFISH(position_list)
                        blue_fish.center_x, blue_fish.center_y = position_list[0]
                        self.fish_queue.append(blue_fish)
                    for i in range(3):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)

                elif self.user.round == 8:
                    for i in range(10):
                        blue_fish = BLUEFISH(position_list)
                        blue_fish.center_x, blue_fish.center_y = position_list[0]
                        self.fish_queue.append(blue_fish)
                    for i in range(4):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)

                elif self.user.round == 9:
                    for i in range(5):
                        blue_fish = BLUEFISH(position_list)
                        blue_fish.center_x, blue_fish.center_y = position_list[0]
                        self.fish_queue.append(blue_fish)
                    for i in range(6):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)

                elif self.user.round == 10:
                    for i in range(8):
                        blue_fish = BLUEFISH(position_list)
                        blue_fish.center_x, blue_fish.center_y = position_list[0]
                        self.fish_queue.append(blue_fish)
                    for i in range(6):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)

                elif self.user.round == 11:
                    for i in range(8):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)
                    for _ in range(4):
                        green = GREENFISH(position_list)
                        green.center_x, green.center_y = position_list[0]
                        self.fish_queue.append(green)

                elif self.user.round == 12:
                    for i in range(8):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)
                    for _ in range(5):
                        green = GREENFISH(position_list)
                        green.center_x, green.center_y = position_list[0]
                        self.fish_queue.append(green)

                elif self.user.round == 13:
                    for i in range(3):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)
                    for _ in range(4):
                        green = GREENFISH(position_list)
                        green.center_x, green.center_y = position_list[0]
                        self.fish_queue.append(green)

                elif self.user.round == 14:
                    for _ in range(5):
                        green = GREENFISH(position_list)
                        green.center_x, green.center_y = position_list[0]
                        self.fish_queue.append(green)
                    for i in range(5):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)
                    for i in range(1):
                        shark = SHARK(position_list)
                        shark.center_x, shark.center_y = position_list[0]
                        self.fish_queue.append(shark)

                elif self.user.round == 15:
                    for i in range(8):
                        red_fish = REDFISH(position_list)
                        red_fish.center_x, red_fish.center_y = position_list[0]
                        self.fish_queue.append(red_fish)
                    for _ in range(8):
                        green = GREENFISH(position_list)
                        green.center_x, green.center_y = position_list[0]
                        self.fish_queue.append(green)
                    for i in range(1):
                        orca = ORCA(position_list)
                        orca.center_x, orca.center_y = position_list[0]
                        self.fish_queue.append(orca)


            # Add all other round definitions here...

        # Tower shooting logic remains the same
        for tower in self.towers:
            closest_fish = None
            min_distance = float('inf')

            # Find the closest fish to the current tower
            for fish in self.fishes:
                distance = math.sqrt((tower.center_x - fish.center_x) ** 2 +
                                     (tower.center_y - fish.center_y) ** 2)
                if distance <= tower.radius and distance < min_distance:
                    min_distance = distance
                    closest_fish = fish

            # If we found a fish within the tower's radius
            if closest_fish:
                # Calculate angle and rotate tower
                start_x = tower.center_x
                start_y = tower.center_y
                dest_x = closest_fish.center_x
                dest_y = closest_fish.center_y
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

                # Set the tower to face the closest fish
                tower.angle = math.degrees(angle) - 180 if tower.name == 'Boat' else math.degrees(angle) - 180

                # Shoot every `rate` frames
                if self.frame_count % tower.rate == 0:
                    bullet = arcade.Sprite(tower.bullet, tower.bullet_scale)
                    bullet.tower_source = tower
                    bullet.grace_frames = 3
                    bullet.age = 0
                    bullet.center_x = start_x
                    bullet.center_y = start_y + 10

                    # Store the tower reference in the bullet


                    # Adjust bullet angle based on tower type
                    if tower.name == "Boat":
                        bullet.angle = math.degrees(angle) + 45
                    elif tower.name == "Wizard":
                        bullet.angle = math.degrees(angle) + 135
                    else:
                        bullet.angle = math.degrees(angle)

                    # Calculate bullet trajectory
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED

                    self.harpoons.append(bullet)

                # Handle collisions
                for bullet in self.harpoons:
                    bullet.age += 1
                    if bullet.top < 0:
                        bullet.remove_from_sprite_lists()
                    else:
                        if bullet.age < bullet.grace_frames:
                            continue
                        for fish in self.fishes:
                            tower_source = bullet.tower_source

                            if arcade.check_for_collision(bullet, fish):
                                if tower_source.name == 'God':
                                    hits += 1
                                    if hits >= 2:
                                        bullet.remove_from_sprite_lists()
                                    fish.hp -= tower_source.atk
                                else:
                                    bullet.remove_from_sprite_lists()
                                    fish.hp -= tower_source.atk

                                if fish.hp <= 0:
                                    try:
                                        self.fishes.remove(fish)
                                        if isinstance(fish, BLUEFISH):
                                            self.user.money += random.randint(5, 15)
                                        elif isinstance(fish, REDFISH):
                                            self.user.money += random.randint(5, 25)
                                        elif isinstance(fish, GREENFISH):
                                            self.user.money += random.randint(10, 35)
                                        elif isinstance(fish, SHARK):
                                            self.user.money += random.randint(15, 40)
                                        elif isinstance(fish, ORCA):
                                            self.user.money += random.randint(30, 50)
                                    except ValueError:
                                        pass

                                    # Check if the removed fish is a shark
                                    if isinstance(fish, SHARK):
                                        for _ in range(1):
                                            red = REDFISH(position_list, start_x=fish.center_x, start_y=fish.center_y)
                                            self.fishes.append(red)

                                        for _ in range(1):
                                            blue = BLUEFISH(position_list, start_x=fish.center_x, start_y=fish.center_y)
                                            self.fishes.append(blue)

                                        for _ in range(1):
                                            green = GREENFISH(position_list, start_x=fish.center_x,
                                                              start_y=fish.center_y)
                                            self.fishes.append(green)
                                    if isinstance(fish, ORCA):
                                        for _ in range(4):
                                            shark = SHARK(position_list, start_x=fish.center_x, start_y=fish.center_y)
                                            self.fish_queue.append(shark)
                                    if isinstance(fish, WHALE):
                                        for _ in range(2):
                                            orca = ORCA(position_list, start_x=fish.center_x, start_y=fish.center_y)
                                            self.fish_queue.append(orca)

        # Update harpoon positions
        self.harpoons.update()




