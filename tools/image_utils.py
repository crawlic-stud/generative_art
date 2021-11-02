import random
import numpy as np


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


def create_points(image, points_num):
    pts = []
    for _ in range(points_num):
        pts.append([random.randint(20, image.size[0] - 20), random.randint(20, image.size[0] - 20)])
    pts = np.array(pts)
    return pts
