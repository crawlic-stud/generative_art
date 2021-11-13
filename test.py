import random

from main.tools.colors import *
from main.tools.image_utils import n_shape, rotate_center
from PIL import Image, ImageDraw
from main.classes.ArtGenerator import ArtGenerator


class Test(ArtGenerator):
    def __init__(self, size, points_num, width, color, rays):
        super().__init__(
            size=size,
            points_num=points_num,
            accuracy=0.005,
            steps=rays,
            width=width,
            color=color
        )

        self.rays = rays
        self.angle = 360 / rays
        self.radius = 2000
        self.points_func = lambda: n_shape((2500 + self.radius, 2500), 3, self.radius, numpy=True)

    def setup(self):
        super().setup()
        length = len(self.curve.curve) // 2
        self.curve.curve = rotate_center(self.curve.curve[0], self.curve.curve, self.angle)[0: length + 1]

    def main(self, dots=True, centered=False, draw=True):
        super().main(centered=centered)

    def create(self):
        resize = self.radius // self.steps
        for i in range(self.steps):
            self.angle = (360 / self.rays) * i
            self.radius -= resize // 2
            self.main()
            self.image = Image.alpha_composite(self.image, self.curve.image)


if __name__ == '__main__':
    art = Test(
        size=1000,
        points_num=25,
        width=lambda: 1,
        color=random_pastel,
        rays=1080,
    )

    art.curve.accuracy = 0.01
    art.create()
    art.get_image().save('main/images/test_image.png')
