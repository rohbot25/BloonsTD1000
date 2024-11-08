import arcade
import time
import math

# Screen title and size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Fish Tower Defense"

BULLET_SPEED = 100

from User import USER
from Sidebar import SIDEBAR
from tower import FISHERMAN, FLYFISHER, WHALER, NEANDERTHAL, WIZARD, BOAT, SUPERFISHER, NETFISHER
from Fish import FISH, REDFISH, BLUEFISH, GREENFISH, SHARK
from Button import BUTTON

import arcade
import arcade.gui

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

        balloon = BLUEFISH(position_list )

        balloon.center_x = position_list[0][0]
        balloon.center_y = position_list[0][1]

        self.fishes.append(balloon)
        self.last_spawn_time = time.time()

    def on_mouse_press(self, x, y, button, key_modifiers):
    #""" Called when the user presses a mouse button. """
        #if upgrade menu is open and your are clicking on the menu, skip
        if (self.showUpgrade and x >= 746):
            for button in self.upgradeMenu.buttons:
                if self.user.money >= button.cost and self.tower.level < self.tower.max:
                    self.user.money -= button.cost
                    self.tower.upgrade()
                    self.max = self.tower.max
                    print(f"upgrade made!")
                    paper_banner = arcade.load_texture("images/paper_banner.png")
                    self.upgradeMenu.drawUpgrade(paper_banner, paper_banner,self.towerName,self.tower)
                else:
                    print("no money or max upgrade")

        #else check if they are clicking on a tower
        else:
            self.showUpgrade = False
            for tower in self.towers:
                if tower.collides_with_point((x,y)):
                    print("open menu")
                    self.tower = tower
                    self.towerName = tower.name
                    self.upgradeLevel = tower.level
                    self.max = tower.max
                    self.upgradeCost = tower.upgradeCost
                    self.showUpgrade = True
                    


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
        if self.paused:
            self.paused = False  # Resume the game on left click
            self.user.round +=1



    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if self.is_dragging and self.current_tower:
            # Finalize tower placement
            # Check if releasing the tower in a restricted area
            # EVENTUALLY WILL DO DIFFERENTLY
                # Create a list that holds invisible blocks covering all the locations that are
                # restricted, then whenever a new tower is added, dynamically add that tower
                # location to the list
            if not (((self.tb_x_start < x < self.tbsb_x_end and self.tb_y_start < y < self.tb_y_end) or
                    (self.sb_x_start < x < self.tbsb_x_end and self.sb_y_start < y < self.sb_y_end) or
                    (0<x<300 and 250<y<300) or (300<x<350 and 250<y<450) or (175<x<350 and 400<y<450) or
                    (175<x<225 and 25<y<450) or (50<x<225 and 0<y<50) or (25<x<75 and 25<y<175) or
                    (50<x<450 and 150<y<200) or (425<x<475 and 175<y<350) or (425<x<550 and 300<y<350) or
                    (525<x<575 and 75<y<325) or (275<x<575 and 50<y<125) or (275<x<325 and 0<y<100)) and
                    (self.user.money >= self.current_tower.cost)
                # Not over another tower
                ):
                # Place tower at the released location
                
                self.current_tower.center_x = x
                self.current_tower.center_y = y

                self.towers.append(self.current_tower)  # Add the tower to the list
                self.user.money -= self.current_tower.cost  # Deduct cost
                print(f"Placed {self.current_tower.__class__.__name__} at ({x}, {y})")
            else:
                print("Cannot place tower in restricted area.")
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
        upgrade = arcade.load_texture("images/upgrade.png")
        # This command has to happen before we start drawing
        self.clear()

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
                button = BUTTON(button_x, button_y, 75, 75, tower_type(), 100, buy_fisherman)
                button.tower_type = tower_type  # Assign the class, not an instance
                self.sidebar.add_button(button)

            # Update hover states and draw the sidebar
            for button in self.sidebar.buttons:
                button.check_hover(self.mouse_x, self.mouse_y)

            self.sidebar.draw(sidebar, paper_banner)
        #else draw the upgrade sidebar
        else:
            self.upgradeMenu = SIDEBAR(SCREEN_WIDTH // 1.145, SCREEN_HEIGHT // 2.2, SCREEN_WIDTH // 3.95, SCREEN_HEIGHT // 1.1)
            # left buttons
            button = BUTTON(875, 250, 75, 75,self.tower, self.upgradeCost, upgrade)
            self.upgradeMenu.add_button(button)
            self.upgradeMenu.drawUpgrade(paper_banner, paper_banner,self.towerName,self.tower)


        #draw the map
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2.45, 825,500,self.texture)


        self.fishes.draw()
        self.towers.draw()
        self.harpoons.draw()

        # Display the currently placed tower if dragging
        if self.is_dragging and self.current_tower is not None:
            self.current_tower.draw()

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
    def on_update(self, delta_time):
        # If paused, wait to be unpaused
        if self.paused:
            return

        # Update cycle counter, each call to update is 1 cycle
        self.spawn_cycle_count += 1

        for fish in self.fishes:
            fish.update(self.user, self.window)

        self.frame_count += 1

        # Handle tower shooting and updating harpoons
        for tower in self.towers:
            if len(self.fishes) > 0:
                # Shooting logic, omitted here for brevity
                pass

        # Spawn new fish if queue has fish and the cycle count is reached
        if self.spawn_cycle_count >= 3 and len(self.fish_queue) > 0:
            # Reset update cycle counter
            self.spawn_cycle_count = 0

            # Spawn fish from the end of the queue list
            self.fishes.append(self.fish_queue.pop())

        self.harpoons.update()

        # Check if all fish are cleared, pause if so
        if len(self.fishes) == 0 and len(self.fish_queue) == 0:
            self.paused = True
            self.user.round += 1  # Move to the next round
            self.setup_round()  # Initialize the next round

    def setup_round(self):
        # Initialize fish queue for the new round
        position_list = [
            [0, 275],
            [335, 275],
            [335, 425],
            [190, 425],
            [190, 35],
            [60, 35],
            [60, 175],
            [450, 175],
            [450, 335],
            [550, 335],
            [550, 75],
            [300, 75],
            [300, 0]
        ]

        # Populate fish queue based on the round
        if self.user.round == 1:
            for i in range(3):
                balloon = BLUEFISH(position_list)
                balloon.center_x, balloon.center_y = position_list[0]
                self.fish_queue.append(balloon)

        elif self.user.round == 2:
            for i in range(6):
                balloon = BLUEFISH(position_list)
                balloon.center_x, balloon.center_y = position_list[0]
                self.fish_queue.append(balloon)

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
            for i in range(5):
                red_fish = REDFISH(position_list)
                red_fish.center_x, red_fish.center_y = position_list[0]
                self.fish_queue.append(red_fish)

        elif self.user.round == 6:
            for i in range(10):
                blue_fish = BLUEFISH(position_list)
                blue_fish.center_x, blue_fish.center_y = position_list[0]
                self.fish_queue.append(blue_fish)
            for i in range(2):
                red_fish = REDFISH(position_list)
                red_fish.center_x, red_fish.center_y = position_list[0]
                self.fish_queue.append(red_fish)

        elif self.user.round == 7:
            for i in range(8):
                blue_fish = BLUEFISH(position_list)
                blue_fish.center_x, blue_fish.center_y = position_list[0]
                self.fish_queue.append(blue_fish)
            for i in range(3):
                red_fish = REDFISH(position_list)
                red_fish.center_x, red_fish.center_y = position_list[0]
                self.fish_queue.append(red_fish)

        # Prepare to start the round on next unpause
        self.paused = True

    def on_mouse_press(self, x, y, button, modifiers):
        # Unpause the game on click
        if self.paused:
            self.paused = False


            #generate wave based on round number Hard code
        #seperate spawning of balloons by 5 update cycles
        if (self.spawn_cycle_count >= 5 and (len(self.fish_queue) > 0)):

            #reset update cycle counter
            self.spawn_cycle_count = 0

            #spawn fish from end of queue list
            self.fishes.append(self.fish_queue[(len(self.fish_queue)-1)])

            #remove fish from end of queue list
            self.fish_queue.pop()

        self.harpoons.update()
        
        
