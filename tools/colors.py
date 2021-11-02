import random
import colorsys


def random_rgb():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def random_hsv():
    return (
        random.randint(0, 100) / 100,
        random.randint(0, 100) / 100,
        random.randint(0, 100) / 100
    )


def random_saturated(hue=None):
    saturation = 1

    if hue is None:
        hue = random.randint(10, 100) / 100

    return (
        hue,
        saturation,
        random.randint(10, 100) / 100
    )


def random_pastel():
    hue = random.randint(0, 100) / 100
    saturation = random.randint(30, 60) / 100

    return (
        hue,
        saturation,
        1
    )


def hsv_to_rgb(h, s, v):
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return (
        int(rgb[0] * 255),
        int(rgb[1] * 255),
        int(rgb[2] * 255)
    )


def add_transparency(color, transparency):
    color = list(color)
    color += [int(transparency * 255)]
    return tuple(color)
