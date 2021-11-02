import random
from PIL import Image, ImageDraw
from tools.colors import random_pastel, hsv_to_rgb, add_transparency
from classes.curve import Curve
from tools.image_utils import create_points


def generate_art(image, points_num, steps=1):
    acc = 0.005
    width = 5

    curve = Curve(
        points=create_points(image, points_num),
        accuracy=acc,
        color=hsv_to_rgb(*random_pastel()),
        width=width
    )

    for _ in range(steps):

        curve.points = create_points(image, points_num)
        points = curve.create_curve()

        new_img = Image.new('RGBA', image.size, (0, 0, 0, 0))
        new_draw = ImageDraw.Draw(new_img)

        color = hsv_to_rgb(*random_pastel())
        polygon_color = add_transparency(color, random.randint(10, 50)/100)
        new_draw.polygon(points, fill=polygon_color)

        image = Image.alpha_composite(image, new_img)

    return image


if __name__ == '__main__':
    size = 2000
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    img = generate_art(img, points_num=5, steps=20)
    img = img.resize((size//2, size//2), resample=Image.ANTIALIAS)
    img.save('images/shape.png')
