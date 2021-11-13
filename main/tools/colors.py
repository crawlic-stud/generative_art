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

    return hsv_to_rgb(
        hue,
        saturation,
        random.randint(10, 100) / 100
    )


def random_pastel():
    hue = random.randint(0, 100) / 100
    saturation = random.randint(30, 60) / 100

    return hsv_to_rgb(
        hue,
        saturation,
        1
    )


def random_red():
    hue = random.randint(0, 20) / 360
    return hsv_to_rgb(
        hue,
        random.randint(60, 100) / 100,
        random.randint(60, 100) / 100
    )


def random_green():
    hue = random.randint(61, 140) / 360
    return hsv_to_rgb(
        hue,
        random.randint(50, 100) / 100,
        random.randint(50, 100) / 100
    )


def random_blue():
    hue = random.randint(170, 240) / 360
    return hsv_to_rgb(
        hue,
        random.randint(50, 100) / 100,
        random.randint(50, 100) / 100
    )


def random_gray():
    gray = random.randint(50, 200)
    return gray, gray, gray


def random_dark(hue=None):
    if hue is None:
        hue = random.randint(0, 360) / 360

    return hsv_to_rgb(
        hue,
        random.randint(50, 80) / 100,
        random.randint(20, 40) / 100
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
