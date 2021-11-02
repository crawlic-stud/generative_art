import random
from PIL import Image, ImageDraw
from tools.colors import *
from classes.Сurve import Curve
from tools.image_utils import points_along_line, calculate_offset, ray_circle


def generate_art(image, center, rays_num, points_num, radius, steps=10, color=random_pastel, width=lambda: 3, box=True):
    accuracy = 0.005

    points = ray_circle(center, rays_num, radius)
    curve = Curve(
        points=[],
        accuracy=accuracy,
        color=color(),
        width=width())

    for _ in range(steps):
        for point in points:

            curve.points = points_along_line(image, points_num, center, point, box=box)
            curve.color = color()
            curve.width = width()
            curve.create_curve()

            curve.draw(image)

        image = Image.alpha_composite(image, curve.image)

    polygon_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
    polygon_color = add_transparency(color(), random.randint(10, 30) / 100)

    ImageDraw.Draw(polygon_image).polygon(points, fill=polygon_color)

    image = Image.alpha_composite(polygon_image, image)

    return image


if __name__ == '__main__':
    size = 5000
    factor = size // 1000

    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    img = generate_art(image=img,
                       center=(size//2, size//2),
                       rays_num=181,
                       points_num=2,
                       radius=size//3,
                       steps=1,
                       color=random_gray,
                       width=lambda: random.randint(1, 15),
                       box=True)

    img = img.resize((size//factor, size//factor), resample=Image.ANTIALIAS)
    img.save('images/rays.png')
