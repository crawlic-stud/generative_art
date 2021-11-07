from tools.image_utils import ray_star, n_shape, spiral_points
from PIL import Image, ImageDraw
from classes.ArtGenerator import ArtGenerator
from tools.colors import *


if __name__ == '__main__':
    img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))

    draw = ImageDraw.Draw(img)

    #points = ray_star((500, 500), 12, 300)
    #for line in points:
    #    draw.line(line, fill='green')

    # points = [tuple(i) for i in spiral((500, 500), 10, 300, offset=10)]
    # print(points)
    # draw.line(points, fill='red')

    # img.show()

    art = ArtGenerator(
        size=1000,
        points_num=3,
        accuracy=0.005,
        steps=1,
        width=lambda: 5,
        color=random_red,
    )

    for i in range(100):
        art.points_func = lambda: n_shape((500 + random.randint(-100, 100), 500 + random.randint(-100, 100)), 3, 1500, numpy=True)
        art.create()
    art.get_image().show()
