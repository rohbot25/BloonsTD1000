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

    def draw(self):
        # Draw the button
        arcade.draw_texture_rectangle(self.x,
                                      self.y,
                                      self.width,
                                      self.height,
                                      self.image)

        if self.is_hovered:
            text_sprite = arcade.draw_text(self.tower_name, start_x=self.x, start_y=self.y, color=arcade.color.BLACK,
                                                         font_size=10, font_name="Comic Sans MS")
            text_width = text_sprite.width
            arcade.draw_rectangle_outline(self.x, self.y, 75, 75, arcade.color.BLACK, 3)
            arcade.draw_texture_rectangle(self.x,
                                          self.y+50,
                                          self.width,
                                          self.height // 5,
                                          arcade.load_texture("Images/paper_banner.png"))
            arcade.draw_text(self.tower_name,
                             start_x= self.x-(text_width/2),
                             start_y=self.y + 45,
                             color=arcade.color.BLACK,
                             font_size=10,
                             align="right",
                             width=50,
                             font_name="Comic Sans MS")
            arcade.draw_text(f"$ {self.cost}",
                             start_x=self.x - 30,
                             start_y=self.y - 50,
                             color=arcade.color.BLACK,
                             font_size=10,
                             align="right",
                             width=50,
                             font_name="Comic Sans MS")

    def check_hover(self, mouse_x, mouse_y):
        # print(f"width: {self.width} // self.height: {self.height}")
        self.is_hovered = (
                self.x - self.width / 2 < mouse_x < self.x + self.width / 2 and
                self.y - self.height / 2 < mouse_y < self.y + self.height / 2
        )

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass