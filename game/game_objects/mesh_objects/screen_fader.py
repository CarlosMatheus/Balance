from pygin import *
from pygame.math import Vector2


class ScreenFader(BasicRectangle):

    def __init__(self, fade="in", fade_duration=0.7):
        """
        Constructor, will decide whether to fade in or fade out
        :param fade: string telling fade in or out
        """
        self.fade = fade
        self.fade_duration = fade_duration
        if fade == "in":
            alp = 255
        else:
            alp = 0
        super().__init__(Vector2(0, 0), Vector2(Engine.screen_width, Engine.screen_height),
                         Material(Color.black, alpha=alp), 1000)

    def start(self):
        """
        Create a animation that fades the entire screen
        Pass this animation to animator and play it
        """
        key_frames = list()
        if self.fade == "in":
            key_frames.append(KeyFrame(0.0, alpha=255))
            key_frames.append(KeyFrame(self.fade_duration, alpha=0))
        else:
            key_frames.append(KeyFrame(0.0, alpha=0))
            key_frames.append(KeyFrame(self.fade_duration, alpha=255))
        self.animation = Animation(self, key_frames, should_loop=False, unscaled="True")
        self.animator = Animator(self, animation_list=[self.animation])
        self.animator.play()
        self.creation_time = Time.now()

    def update(self):
        """
        Will destroy the animation after finished it
        """
        if Time.now() - self.creation_time > self.fade_duration*2:
            GameObject.destroy(self)
