import random
from PIL import Image, ImageDraw
from tools.colors import *
from classes.Сurve import Curve
from tools.image_utils import points_along_line, calculate_offset, create_box


def generate_art(image, points_num, start=None, end=None, color=random_pastel,
                 color_change=True, steps=100, width=lambda: 5, curve_points=False,
                 draw_rect=True, box=False):

    accuracy = 0.005

    curve = Curve(
        points=points_along_line(image, points_num, start=start, end=end),
        accuracy=accuracy,
        color=color(),
        width=width())

    for _ in range(steps):
        if color_change:
            curve.color = color()
        curve.points = points_along_line(image, points_num, start=start, end=end, box=box)
        curve.width = width()
        curve.create_curve()

        if curve_points:
            curve.draw_points(image, centered=True)
        else:
            curve.draw(image, centered=False)

        image = Image.alpha_composite(image, curve.image)

    if not draw_rect:
        return image

    polygon_image = Image.new('RGBA', image.size, (0, 0, 0, 0))

    polygon_pos = create_box(start, end)
    polygon_color = add_transparency(color(), random.randint(10, 30) / 100)

    ImageDraw.Draw(polygon_image).polygon(polygon_pos, fill=polygon_color)

    image = Image.alpha_composite(image, polygon_image)

    return image


if __name__ == '__main__':
    size = 5000
    factor = size // 1000
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    indent = 10
    start = [random.randint(indent, size - indent), random.randint(indent, size - indent)]
    end = [random.randint(indent, size - indent), random.randint(indent, size - indent)]

    # start = [indent, indent]
    # end = [size - indent, size - indent]

    box = create_box(start, end)
    off_x, off_y = calculate_offset(img, box)

    img = generate_art(image=img,
                       points_num=25,
                       start=(start[0] + off_x, start[1] - off_y),
                       end=(end[0] + off_x, end[1] - off_y),
                       color=random_red,
                       color_change=True,
                       curve_points=False,
                       steps=20,
                       width=lambda: random.randint(1, 15),
                       draw_rect=True,
                       box=True)

    img = img.resize((size//factor, size//factor), resample=Image.ANTIALIAS)
    img.save('./images/curvature.png')
