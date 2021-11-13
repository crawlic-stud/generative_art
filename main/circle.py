import random
from PIL import Image, ImageDraw
from main.tools.colors import *
from main.classes.ArtGenerator import ArtGenerator
from main.tools.image_utils import points_along_line, calculate_offset, n_shape


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
        step = 2
        for i, point in enumerate(self.points):
            try:
                end = self.points[i + step]
            except IndexError:
                end = self.points[i]
            self.points_func = lambda: points_along_line(image=self.image,
                                                         points_num=self.points_num,
                                                         start=point,
                                                         end=end,
                                                         box=self.box)
            super().main(centered=centered)

            self.points_func = lambda: points_along_line(image=self.image,
                                                         points_num=self.points_num,
                                                         start=self.center,
                                                         end=end,
                                                         box=self.box)
            super().main(centered=centered)

    def create(self):
        super().create()

        polygon_image = Image.new('RGBA', self.image.size, (0, 0, 0, 0))
        polygon_color = add_transparency(self.color(), random.randint(10, 30) / 100)

        points = [tuple(i) for i in self.points]
        ImageDraw.Draw(polygon_image).polygon(points, fill=polygon_color)

        self.image = Image.alpha_composite(polygon_image, self.image)


if __name__ == '__main__':
    size = 1000

    img = Rays(size=size,
               center=(size // 2, size // 2),
               rays_num=91,
               points_num=3,
               radius=size // 3,
               steps=3,
               color=random_blue,
               width=lambda: random.randint(1, 15),
               box=True)

    img.create()
    img.get_image().save('images/rays.png')
