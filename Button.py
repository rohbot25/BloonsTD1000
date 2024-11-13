import arcade

class BUTTON:
    def __init__(self, x, y, width, height, tower_type, cost, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tower_type = tower_type
        self.cost = cost
        self.image = image
        self.is_hovered = False
        self.tower_name = tower_type.name

        # Create the text objects for `tower_name` and `cost`
        self.name_text = arcade.Text(
            self.tower_name,
            start_x=self.x - ((len(self.tower_name)*13)/3.3),
            start_y=self.y+45,
            color=arcade.color.BLACK,
            font_size=10,
            font_name="Courier"
        )
        self.cost_text = arcade.Text(
            f"$ {self.cost}",
            start_x=self.x - ((len(str(self.cost))*13)/3),
            start_y=self.y - 50,
            color=arcade.color.BLACK,
            font_size=10,
            font_name="Comic Sans MS"
        )

    def draw(self):
        # Draw the button
        arcade.draw_texture_rectangle(self.x,
                                      self.y,
                                      self.width,
                                      self.height,
                                      self.image)
        if self.is_hovered:
            arcade.draw_rectangle_outline(self.x, self.y, 75, 75, arcade.color.BLACK, 3)
            arcade.draw_texture_rectangle(self.x,
                                          self.y+50,
                                          (len(self.tower_name)*13),
                                          self.height // 4.5,
                                          arcade.load_texture("Images/paper_banner.png"))
            arcade.draw_texture_rectangle(self.x,
                                          self.y - 45,
                                          self.width,
                                          self.height // 4.5,
                                          arcade.load_texture("Images/paper_banner.png"))


            # self.name_text.start_x = self.x - ((len(self.tower_name)*13) / 2)
            # self.name_text.start_y = self.y + 45
            # Draw the tower name
            self.name_text.draw()
            # Draw the cost text
            self.cost_text.draw()


    def check_hover(self, mouse_x, mouse_y):
        # print(f"width: {self.width} // self.height: {self.height}")
        self.is_hovered = (
                self.x - self.width / 2 < mouse_x < self.x + self.width / 2 and
                self.y - self.height / 2 < mouse_y < self.y + self.height / 2
        )

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass