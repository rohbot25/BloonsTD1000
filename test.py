import os
import arcade
print(os.path.exists("images/upgrade.png"))
upgrade = arcade.load_texture("images/upgrade.png")
print("Upgrade texture loaded:", upgrade)