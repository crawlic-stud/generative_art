from PIL import ImageDraw
from tools.image_utils import rotate_center, spiral_points
from math import radians


class Spiral:
    def __init__(self, start, radius, angle, smoothness, color, width, offset_x=1.0, offset_y=1.0):
        self.start = start
        self.radius = radius
        self.angle = radians(angle)
        self.smoothness = smoothness
        self.color = color()
        self.width = width()
        self.off_x = offset_x
        self.off_y = offset_y

        self.points = []

    def create_spiral(self):
        points = spiral_points(self.start, self.smoothness, self.radius,
                               offset=(self.off_x, self.off_y))
        self.points = points
        return points

    def rotate_points(self):
        points = rotate_center(self.start, self.create_spiral(), self.angle)
        self.points = points
        return points

    def draw(self, image):
        ImageDraw.Draw(image).line(self.rotate_points(), fill=self.color, width=self.width)
