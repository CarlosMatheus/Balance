from pygin import *
from _ignore.game_test.game_objects.mesh_objects.test_rect import TestRect
from _ignore.game_test.game_objects.mesh_objects.test_rect2 import TestRect2
from _ignore.game_test.game_objects.mesh_objects.test_rect3 import TestRect3
from game.game_objects.mesh_objects.get_power_up_effect import GetPowerUpEffect
from _ignore.game_test.game_objects.mesh_objects.circle import Circle
from _ignore.game_test.game_objects.mesh_objects.player import Player
from pygame import Color
from pygame.math import Vector2
from _ignore.game_test.game_objects.mesh_objects.test_text import TestText


class TestSceneController(GameObject):

    def start(self):
        screen_width = 360
        screen_height = 640
        material = Material(Color(255, 0, 0))
        square = TestRect(Vector2(screen_width/2-100, screen_height/2-200), Vector2(50, 50), material)

        player = Player(Vector2(screen_width/2-100, screen_height/2-200), Vector2(50, 50), Material(C.yellow))

        Circle(Vector2(screen_width/2-50, screen_height/2-150), 40, material, layer=1)

        square4 = TestRect(Vector2(screen_width / 2 - 20, screen_height / 2 - 300), Vector2(50, 50),
                           Material(Color(0, 255, 0), 100))
        square2 = TestRect2(Vector2(screen_width / 2, screen_height / 2 - 100), Vector2(50, 50), material)
        square3 = TestRect3(Vector2(screen_width / 2 + 100, screen_height / 2 - 100), Vector2(50, 50), material)
        TestText()
        self.veri = True
        # print("This is not a coroutine")

    def update(self):
        if(self.veri):
            # print(asyncio.Task.all_tasks())
            # print("This is not a coroutine")
            # Time.test(TestSceneController.test())
            self.veri = False
        if Input.press_left_down:

            screen_width = 360
            screen_height = 640

            material = Material( Color(255, 0, 0) )

            GetPowerUpEffect(Vector2(screen_width / 2 - 50, screen_height / 2 + 50), material)
