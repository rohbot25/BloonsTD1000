import arcade

class SIDEBAR:
    BUY_BOX_SIZE = 75
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 500
    SCREEN_TITLE = "Fish Tower Defense"
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.tower = "tower"
        self.towerImage = "images"
        self.upgradeName = "upgrade"
        self.upgradeLevel = 0
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
            arcade.draw_rectangle_filled(box_x, box_y, self.BUY_BOX_SIZE, self.BUY_BOX_SIZE, (0, 0, 0, 128))
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 1.145,
                                      self.SCREEN_HEIGHT // 1.17,
                                      self.width,
                                      self.height // 9,
                                      paper_banner)
        arcade.draw_text(f"Fishermen",
                         start_x=self.SCREEN_WIDTH // 1.53,
                         start_y=self.SCREEN_HEIGHT // 1.2,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="right",
                         width=300,
                         font_name="Comic Sans MS")

        # Draw the buttons
        for button in self.buttons:
            button.draw()
    def drawUpgrade(self,sidebar,paper_banner,type,tower):
        arcade.draw_texture_rectangle(self.x,
                                      self.y,
                                      self.width,
                                      self.height,
                                      sidebar)
        arcade.draw_texture_rectangle(self.SCREEN_WIDTH // 1.145,
                                      self.SCREEN_HEIGHT // 1.17,
                                      self.width,
                                      self.height // 9,
                                      paper_banner)
        arcade.draw_text(type,
                         start_x=775,
                         start_y=self.SCREEN_HEIGHT // 1.2,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="left",
                         width=300,
                         font_name="Comic Sans MS")
        for button in self.buttons:
            button.draw()
        arcade.draw_text(" Level: "+str(tower.level)+"/"+str(tower.max),start_x=775,
                         start_y=300,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="left",
                         width=300,
                         font_name="Comic Sans MS")
        arcade.draw_text(" Cost: "+str(tower.upgradeCost),start_x=775,
                         start_y=175,
                         color=arcade.color.BLACK,
                         font_size=24,
                         align="left",
                         width=300,
                         font_name="Comic Sans MS")
