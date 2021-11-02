import random
from PIL import Image, ImageDraw
from tools.colors import *
from classes.curve import Curve
from tools.image_utils import points_along_line, create_image


def generate_art(image, points_num, color_func=random_pastel, width=5):
    accuracy = 0.005
    color = color_func()

    curve = Curve(
        points=points_along_line(image, points_num),
        accuracy=accuracy,
        color=color,
        width=width)

    curve.create_curve()
    curve.draw(image, centered=True)


if __name__ == '__main__':
    size = 5000
    factor = size // 1000
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    for _ in range(100):
        generate_art(image=img,
                     points_num=10,
                     color_func=random_pastel,
                     width=random.randint(1, 3))

    img = img.resize((size//factor, size//factor), resample=Image.ANTIALIAS)
    img.save('images/curvature.png')
