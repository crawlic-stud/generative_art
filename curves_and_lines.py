import random
from PIL import Image, ImageDraw
from tools.colors import random_pastel, hsv_to_rgb, add_transparency, random_gray, random_red, random_green, random_blue
from classes.curve import Curve
from tools.image_utils import create_points


def generate_art(image, points_num, lines=100, steps=10, color_change=True, color_func=random_pastel):
    width = 5
    line_width = 1
    accuracy = 0.005
    color = color_func()

    curve = Curve(
        points=create_points(image, points_num),
        accuracy=accuracy,
        color=color,
        width=width)

    for _ in range(steps):
        curve.points = create_points(image, points_num)
        curve.create_curve()

        if color_change:
            curve.color = color_func()

        curve.draw(image, centered=True)

        lines_list = []
        for _ in range(lines):
            lines_list.append(tuple(random.choice(curve.curve)))

        draw = ImageDraw.Draw(curve.image)
        draw.line(lines_list, fill=curve.color, width=line_width)

        image = Image.alpha_composite(image, curve.image)

    return image


if __name__ == '__main__':
    size = 5000
    factor = size // 1000

    my_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))

    # 5, 300, 10 - probably the best
    my_img = generate_art(image=my_img,
                          points_num=5,
                          lines=300,
                          steps=10,
                          color_change=True,
                          color_func=random_pastel)

    # makes image smoother
    my_img = my_img.resize((size//factor, size//factor), resample=Image.ANTIALIAS)
    my_img.save('images/curve.png')
