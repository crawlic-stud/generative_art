import random

from main.classes.ArtGenerator import ArtGenerator
from PIL import Image, ImageDraw
from main.tools.colors import *
from main.tools.image_utils import create_points, points_along_line, n_shape, ray_star


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
        self.curves = []

    def main(self, dots=False, centered=False, draw=True):
        for line in self.points[1:]:

            self.points_func = lambda: points_along_line(image=self.image,
                                                         points_num=self.bend,
                                                         start=line[0],
                                                         end=line[1],
                                                         box=self.box)

            super().main(centered=self.centered, draw=True)

            polygon = Image.new('RGBA', self.image.size, (0, 0, 0, 0))
            polygon_color = add_transparency(self.color(), random.randint(10, 30)/100)
            ImageDraw.Draw(polygon).polygon(self.curve.curve, fill=polygon_color)

            self.curve.image = polygon
            self.image = Image.alpha_composite(self.image, self.curve.image)


if __name__ == '__main__':
    art = Star(
        size=1000,
        rays_num=9,
        width=lambda: random.randint(1, 5),
        color=random_pastel,
        steps=25,
        bend=2,
        radius=300,
        box=True,
        centered=False
    )

    art.create()
    art.get_image().save('images/shapestar.png')