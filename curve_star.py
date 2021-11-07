import random

from classes.ArtGenerator import ArtGenerator
from PIL import Image, ImageDraw
from tools.colors import *
from tools.image_utils import create_points, points_along_line, n_shape, ray_star


class Star(ArtGenerator):
    def __init__(self, size, rays_num, width, color, steps, bend, radius, box=True, centered=True):
        super().__init__(size=size,
                         points_num=rays_num,
                         accuracy=0.005,
                         width=width,
                         color=color,
                         steps=steps)

        self.bend = bend
        self.box = box
        self.centered = centered
        self.points = ray_star(center=(self.image.size[0]//2, self.image.size[1]//2),
                               rays_num=rays_num,
                               radius=radius * 5)

    def main(self, dots=False, centered=False, draw=True):
        for line in self.points[1:]:
            self.points_func = lambda: points_along_line(image=self.image,
                                                         points_num=self.bend,
                                                         start=line[0],
                                                         end=line[1],
                                                         box=self.box)
            super().main(centered=self.centered)


if __name__ == '__main__':
    art = Star(
        size=1000,
        rays_num=11,
        width=lambda: random.randint(1, 5),
        color=random_blue,
        steps=100,
        bend=2,
        radius=300,
        box=True,
        centered=False
    )

    art.create()
    art.get_image().save('images/star.png')
