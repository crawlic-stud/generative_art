import random
from PIL import Image, ImageDraw
from tools.colors import random_pastel, hsv_to_rgb, add_transparency
from classes.curve import Curve
from tools.image_utils import create_points


def generate_art(image, points_num, lines=100, steps=10,):
    width = 5
    line_width = 1
    accuracy = 0.005

    curve = Curve(
        points=create_points(image, points_num),
        accuracy=accuracy,
        color=hsv_to_rgb(*random_pastel()),
        width=width)

    for _ in range(steps):
        curve.points = create_points(image, points_num)
        curve.color = hsv_to_rgb(*random_pastel())
        curve.create_curve()

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
    my_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    # 5, 300, 10 - probably the best
    my_img = generate_art(my_img, points_num=5, lines=300, steps=10)
    my_img = my_img.resize((size//5, size//5), resample=Image.ANTIALIAS)
    my_img.save('images/curve.png')
