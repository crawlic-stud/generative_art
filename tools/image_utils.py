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


def points_along_line(image, points_num, indent=50):
    start_point = [indent, indent]
    end_point = [image.size[0] - indent, image.size[1] - indent]
    pts = [start_point]

    step_length = end_point[0] // points_num
    for i in range(points_num - 1):
        new_point = [step_length * (i + 1), random.randint(0, image.size[1])]
        pts.append(new_point)

    pts.append(end_point)
    pts = np.array(pts)
    return pts


def create_image(size, steps, art_func, factor=5):
    new_size = size * factor

    image = Image.new('RGBA', (new_size, new_size), (0, 0, 0, 0))
    for _ in range(steps):
        art_func(image=image)

    image = image.resize((size, size), resample=Image.ANTIALIAS)
    return image
