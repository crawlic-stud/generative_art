import random
from tools.bezier import create_curve
from PIL import Image, ImageDraw
import numpy as np
from tools.colors import random_saturated, hsv_to_rgb, add_transparency
from tools.image_utils import calculate_offset


class Curve:
    """Draws curve."""
    def __init__(self, points: np.array, accuracy, color, width):
        self.points = points
        self.accuracy = accuracy
        self.color = color
        self.width = width
        self.t_points = np.arange(0, 1, accuracy)
        self.curve = []
        self.image = None

    def create_curve(self):
        self.curve = [tuple(i) for i in create_curve(self.t_points, self.points)]

    def offset(self, img):
        off_x, off_y = calculate_offset(img, self.curve)
        points = [(self.curve[i][0] + off_x, self.curve[i][1] - off_y) for i in range(len(self.curve))]
        self.curve = points

    def draw(self, img, centered=False):
        self.create_curve()
        self.image = img

        if centered:
            self.offset(img)

        img_draw = ImageDraw.Draw(img)
        img_draw.line(self.curve, fill=self.color, width=self.width)

    def draw_points(self, img, centered=False):
        self.create_curve()
        self.image = img

        if centered:
            self.offset(img)

        img_draw = ImageDraw.Draw(img)
        for point in self.curve:
            img_draw.rounded_rectangle([point[0] - self.width//2, point[1] - self.width//2,
                                        point[0] + self.width//2, point[1] + self.width//2],
                                       radius=100, fill=self.color)


def generate_art(image, points_num, lines=100, steps=10,):
    width = 5
    line_width = 1
    accuracy = 0.005

    def create_points():
        pts = []
        for _ in range(points_num):
            pts.append([random.randint(20, image.size[0] - 20), random.randint(20, image.size[0] - 20)])
        pts = np.array(pts)
        return pts

    curve = Curve(
        points=create_points(),
        accuracy=accuracy,
        color=hsv_to_rgb(*random_saturated()),
        width=width)

    curves = []
    hue = random.randint(0, 100) / 100
    for _ in range(steps):
        curve.points = create_points()

        # more pastel color
        curve.color = hsv_to_rgb(h=random.randint(0, 100)/100, s=random.randint(30, 60)/100, v=1)
        # curve.color = hsv_to_rgb(*random_saturated(hue=hue))
        # curve.color = add_transparency(curve.color, random.randint(0, 100) / 100)

        curve.draw(image, centered=True)

        lines_list = []
        for _ in range(lines):
            lines_list.append(tuple(random.choice(curve.curve)))

        draw = ImageDraw.Draw(curve.image)
        draw.line(lines_list, fill=curve.color, width=line_width)
        image = curve.image
        curves.append(curve.curve)

    return curves


if __name__ == '__main__':
    size = 5000
    my_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    # 5, 300, 10 - probably the best
    generate_art(my_img, points_num=5, lines=300, steps=10)
    my_img = my_img.resize((size//5, size//5), resample=Image.ANTIALIAS)
    my_img.save('images/curve.png')
