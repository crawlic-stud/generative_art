import random
import numpy as np
from PIL import Image


def calculate_offset(image, points):
    width, height = image.size

    x_list = [point[0] for point in points]
    y_list = [point[1] for point in points]

    x_min = min(x_list)
    x_max = max(x_list)
    y_min = min(y_list)
    y_max = max(y_list)

    offset_x = (width - x_max - x_min) / 2
    offset_y = (y_min - height + y_max) / 2

    return offset_x, offset_y


def create_points(image, points_num, indent=50):
    pts = []
    for _ in range(points_num):
        pts.append([random.randint(indent, image.size[0] - indent), random.randint(indent, image.size[0] - indent)])
    pts = np.array(pts)
    return pts


def is_horizontal(start, end):
    """Calculates general orientation of a line.
    True - line is generally horizontal, False - line is generally vertical."""

    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]
    return abs(delta_x) >= abs(delta_y)


def points_along_line(image, points_num, start=None, end=None, indent=50):
    """Draws random points along line from start point to end point."""
    if start is None:
        start = [indent, indent]
    if end is None:
        end = [image.size[0] - indent, image.size[1] - indent]

    pts = [start]

    for i in range(points_num - 1):

        if is_horizontal(start, end):
            step_length = (end[0] - start[0]) // points_num
            new_point = [start[0] + step_length * (i + 1), random.randint(0, image.size[1])]
        else:
            step_length = (end[1] - start[1]) // points_num
            new_point = [random.randint(0, image.size[1]), start[1] + step_length * (i + 1)]

        pts.append(new_point)

    pts.append(end)
    pts = np.array(pts)
    return pts


def create_image(size, steps, art_func, factor=5):
    new_size = size * factor

    image = Image.new('RGBA', (new_size, new_size), (0, 0, 0, 0))
    for _ in range(steps):
        art_func(image=image)

    image = image.resize((size, size), resample=Image.ANTIALIAS)
    return image
