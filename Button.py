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
            arcade.draw_text(
                self.tower_name,
                start_x=self.x - ((len(self.tower_name)*13)/3.3),
                start_y=self.y+45,
                color=arcade.color.BLACK,
                font_size=10,
                font_name="Courier"
            )
            arcade.draw_text(
                f"$ {self.cost}",
                start_x=self.x - ((len(str(self.cost)) * 13) / 2.5),
                start_y=self.y - 50,
                color=arcade.color.BLACK,
                font_size=10,
                font_name="Comic Sans MS"
            )

    def check_hover(self, mouse_x, mouse_y):
        # print(f"width: {self.width} // self.height: {self.height}")
        self.is_hovered = (
                self.x - self.width / 2 < mouse_x < self.x + self.width / 2 and
                self.y - self.height / 2 < mouse_y < self.y + self.height / 2
        )

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


class PauseUnpause:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.is_hovered = False
        self.paused = False
        self.pressed = False

    def draw(self):
        # Draw the button
        arcade.draw_texture_rectangle(self.x, self.y, self.width, self.height, self.image)
        if self.is_hovered:
            arcade.draw_rectangle_outline(self.x, self.y, 45, 45, arcade.color.BLACK, 3)

    def check_hover(self, mouse_x, mouse_y):
        self.is_hovered = (
            self.x - self.width / 2 < mouse_x < self.x + self.width / 2 and
            self.y - self.height / 2 < mouse_y < self.y + self.height / 2
        )

    def on_mouse_press(self, mouse_x, mouse_y, button, modifiers):
        if self.x - self.width / 2 < mouse_x < self.x + self.width / 2 and \
           self.y - self.height / 2 < mouse_y < self.y + self.height / 2:
            self.pressed = True


    def on_mouse_release(self, mouse_x, mouse_y, button, modifiers):
        if self.pressed:
            self.pressed = False
            if self.x - self.width / 2 < mouse_x < self.x + self.width / 2 and \
               self.y - self.height / 2 < mouse_y < self.y + self.height / 2:
                if (self.paused):
                    self.paused = False
                else:
                    self.paused = True
                print("Paused" if self.paused else "Unpaused")

