from classes.Spiral import Spiral
from classes.ArtGenerator import ArtGenerator
import random
from PIL import Image
from tools.colors import *
from tools.image_utils import n_shape


def kaleidoscope(size, start, radius, angle, smoothness, color, width,
                 offset_x, offset_y):

    factor = 5
    image = Image.new('RGBA', (size * factor, size * factor), (0, 0, 0, 0))
    step = 360 // angle

    spiral = Spiral(
        start=[start[0] * factor, start[1] * factor],
        radius=radius * 5,
        angle=angle,
        smoothness=smoothness,
        color=color,
        width=width,
        offset_x=offset_x,
        offset_y=offset_y
    )

    start = spiral.start
    for i in range(0, 360, step):
        spiral.angle = step * i
        spiral.color = color()
        spiral.width = width()
        spiral.radius += 5
        #spiral.start[0] += random.randint(1, 10)
        #spiral.start[1] += random.randint(1, 10)
        # spiral.off_y = random.randint(1, 10)

        spiral.draw(image)

    return image.resize((size, size), resample=Image.ANTIALIAS)


if __name__ == '__main__':
    angle = random.randint(1, 60)

    spiral = kaleidoscope(
        size=1000,
        start=(500, 500),
        radius=200,
        angle=angle,
        smoothness=100,
        color=random_pastel,
        width=lambda: random.randint(1, 2),
        offset_x=2,
        offset_y=10
    )

    spiral.save('images/spiral.png')
