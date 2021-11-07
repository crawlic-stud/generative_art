import random
import numpy as np
from PIL import Image
from math import sin, cos, radians, sqrt


def calculate_offset(image, points):
    """Calculates offset from image center for each point in point list."""
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
    """Creates numpy list of random points on image with indent."""
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


def points_along_line(image, points_num, start=None, end=None, indent=100, box=False):
    """Draws random points along line from start point to end point."""
    if start is None:
        start = [indent, indent]
    if end is None:
        end = [image.size[0] - indent, image.size[1] - indent]

    pts = [start]
    if box:
        min_x = int(min(start[0], end[0]))
        box_width = int(max(start[0], end[0]) - min_x)
        min_y = int(min(start[1], end[1]))
        box_height = int(max(start[1], end[1]) - min_y)
    else:
        min_x, box_width, min_y, box_height = 0, image.size[0], 0, image.size[1]

    for i in range(points_num - 1):

        if is_horizontal(start, end):
            step_length = (end[0] - start[0]) // points_num
            new_point = [start[0] + step_length * (i + 1), random.randint(min_y - indent, box_height + min_y + indent)]

        else:
            step_length = (end[1] - start[1]) // points_num
            new_point = [random.randint(min_x - indent, min_x + box_width + indent), start[1] + step_length * (i + 1)]

        pts.append(new_point)

    pts.append(end)
    pts = np.array(pts)
    return pts


def n_shape(center, sides_num, radius, numpy=False):
    """Creates round polygon with n sides."""
    angle = radians(360 / sides_num)
    points = []
    for i in range(sides_num):
        x = center[0] - radius * cos(angle * i)
        y = center[1] - radius * sin(angle * i)
        points.append([x, y])
    if numpy:
        return np.array(points + [points[0]])
    return points + [points[0]]


def ray_star(center, rays_num, radius, smoothness=1080):
    """Creates circle of rays."""
    circle_points = n_shape(center, smoothness, radius)
    step = smoothness // rays_num

    points = []
    for i in range(0, smoothness//2, step):
        line = [circle_points[i], circle_points[i + smoothness//2]]
        points.append(line)

    return points


def spiral_points(center, smoothness, radius, offset, numpy=False):
    """Creates spiral points."""
    circle = n_shape(center, smoothness, radius)
    points = []
    while radius >= offset[0] * smoothness:
        points += [(circle[i][0] + i * offset[0], circle[i][1] + i * offset[1]) for i in range(len(circle))]
        radius -= offset[0] * smoothness
        circle = n_shape(center, smoothness, radius)
    if numpy:
        return np.array(points)
    return points


def points_distance(p1, p2):
    """Calculates distance between two points."""
    x1, y1 = p1
    x2, y2 = p2

    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)


def create_box(start, end):
    """Creates bounding box for given line."""
    box = [tuple(start), (end[0], start[1]), tuple(end), (start[0], end[1])]
    return box


def rotate_center(center, points, angle):
    """Rotates list of points around given center."""
    result = []
    for point in points:
        x1, y1 = center
        x2, y2 = point

        new_x = x1 + cos(angle) * (x2 - x1) - sin(angle) * (y2 - y1)
        new_y = y1 + sin(angle) * (x2 - x1) + cos(angle) * (y2 - y1)

        result.append((new_x, new_y))

    return result


if __name__ == '__main__':
    print(points_distance((100, 200), (300, 900)))
