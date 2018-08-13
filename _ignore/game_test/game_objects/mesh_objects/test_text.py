from pygin import *
from pygame.math import Vector2


class TestText(Text):

    def __init__(self):
        position = Vector2(0, 0)
        message = "test"
        self.material = Material(color=Color.white, alpha=55)
        size = 100
        font_path = "/Users/carlosmatheus/Documents/Balance/_ignore/game_test/assets/fonts/neuropolxrg.ttf"
        super().__init__(position, message, self.material, size, font_path)
        self.transform.position.x = 10
        self.transform.position.y = Engine.screen_height/2
