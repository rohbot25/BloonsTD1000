import arcade
import arcade.gui
from GameView import GameView

# Screen title and size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Fish Tower Defense"


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
