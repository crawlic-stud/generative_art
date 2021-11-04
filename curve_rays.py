import random
from PIL import Image, ImageDraw
from tools.colors import *
from classes.ArtGenerator import ArtGenerator
from tools.image_utils import points_along_line, calculate_offset, n_shape


class Rays(ArtGenerator):
    def __init__(self, size, points_num, steps, width, color,
                 center, rays_num, radius, box=True):

        super().__init__(size=size,
                         points_num=points_num,
                         accuracy=0.005,
                         steps=steps,
                         width=width,
                         color=color)

        self.center = (center[0] * 5, center[1] * 5)
        self.box = box

        self.points = n_shape(self.center, rays_num, radius * 5)

    def main(self, dots=False, centered=False, draw=True):
        for point in self.points:
            self.points_func = lambda: points_along_line(image=self.image,
                                                         points_num=self.points_num,
                                                         start=self.center,
                                                         end=point,
                                                         box=self.box)
            super().main(centered=centered)

    def create(self):
        super().create()

        polygon_image = Image.new('RGBA', self.image.size, (0, 0, 0, 0))
        polygon_color = add_transparency(self.color(), random.randint(10, 30) / 100)

        ImageDraw.Draw(polygon_image).polygon(self.points, fill=polygon_color)

        self.image = Image.alpha_composite(polygon_image, self.image)


if __name__ == '__main__':
    size = 1000

    img = Rays(size=size,
               center=(size // 2, size // 2),
               rays_num=181,
               points_num=2,
               radius=size // 3,
               steps=1,
               color=random_gray,
               width=lambda: random.randint(1, 15),
               box=True)

    img.create()
    img.get_image().save('images/rays.png')