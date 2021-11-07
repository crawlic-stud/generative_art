import random
from PIL import Image, ImageDraw
from tools.colors import random_pastel, hsv_to_rgb, add_transparency, random_gray, random_red, random_green, random_blue
from classes.Сurve import Curve
from classes.ArtGenerator import ArtGenerator
from tools.image_utils import create_points


class Shapes(ArtGenerator):
    def __init__(self, size, points_num, steps, color):
        super().__init__(size=size,
                         points_num=points_num,
                         accuracy=0.005,
                         steps=steps,
                         width=lambda: 0,
                         color=color)

        self.points_func = lambda: create_points(self.image, self.points_num)

    def main(self, dots=False, centered=True, draw=False):
        super().main(draw=False)

        polygon_img = Image.new('RGBA', self.image.size, (0, 0, 0, 0))
        polygon_color = add_transparency(self.color(), random.randint(10, 50)/100)
        ImageDraw.Draw(polygon_img).polygon(self.curve.create_curve(), fill=polygon_color)

        self.curve.image = polygon_img


if __name__ == '__main__':
    size = 1000

    img = Shapes(size=size,
                 points_num=10,
                 steps=30,
                 color=random_pastel)

    img.create()
    img.get_image().save('images/shape.png')
