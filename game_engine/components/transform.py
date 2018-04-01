from game_engine.component import Component


class Transform(Component):

    def __init__(self, game_object, position, rotation, scale, layer):
        """
        Set the initial parameters
        :param position.x: game_object's x initial position
        :param position.y: game_object's y initial position
        :param rotation: game_object's initial rotation in degrees
        :param scale.x: game_object's x initial scale
        :param scale.y: game_object's y initial scale
        :param layer: the layer in the order of screen
        """
        super(Transform, self).__init__(game_object)
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.layer = layer

    def translate(self, new_position):
        """
        Set the new position of the game_object (Vector2)
        :param new_position: where the game_object will go to
        """
        self.position.x = new_position.x
        self.position.y = new_position.y

    def rotate(self, rotation):
        """
        Assuming the game_object is a polygon (Does not make sense for a circle to be rotated)
        :param rotation:
        :return:
        """
        self.rotation += rotation
