import random
from PIL import Image, ImageDraw
from tools.colors import *
from classes.curve import Curve
from tools.image_utils import points_along_line, calculate_offset


def generate_art(image, points_num, start=None, end=None, color=random_pastel,
                 color_change=True, steps=100, width=lambda: 5, curve_points=False,
                 draw_rect=True):

    accuracy = 0.005

    curve = Curve(
        points=points_along_line(image, points_num, start=start, end=end),
        accuracy=accuracy,
        color=color(),
        width=width())

    for _ in range(steps):
        if color_change:
            curve.color = color()
        curve.points = points_along_line(image, points_num, start=start, end=end)
        curve.width = width()
        curve.create_curve()

        if curve_points:
            curve.draw_points(image, centered=True)
        else:
            curve.draw(image, centered=True)

        image = Image.alpha_composite(image, curve.image)

    if not draw_rect:
        return image

    polygon_image = Image.new('RGBA', image.size, (0, 0, 0, 0))

    polygon_pos = [tuple(start), (end[0], start[1]), tuple(end), (start[0], end[1])]
    off_x, off_y = calculate_offset(polygon_image, polygon_pos)
    polygon_pos = [(polygon_pos[i][0] + off_x, polygon_pos[i][1] - off_y) for i in range(len(polygon_pos))]

    polygon_color = add_transparency(color(), random.randint(10, 50) / 100)

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

    img = generate_art(image=img,
                       points_num=5,
                       start=start,
                       end=end,
                       color=random_blue,
                       color_change=True,
                       curve_points=False,
                       steps=30,
                       width=lambda: random.randint(1, 15),
                       draw_rect=True)

    img = img.resize((size//factor, size//factor), resample=Image.ANTIALIAS)
    img.save('images/curvature.png')
