from tools.image_utils import ray_star, n_shape
from PIL import Image, ImageDraw


if __name__ == '__main__':
    img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))

    draw = ImageDraw.Draw(img)

    points = ray_star((500, 500), 50, 300)
    for line in points:
        draw.line(line, fill='red')
    img.show()