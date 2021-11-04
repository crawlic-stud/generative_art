import random
from PIL import Image, ImageDraw
from tools.colors import *
from classes.ArtGenerator import ArtGenerator
from tools.image_utils import create_points


class CurvesAndLines(ArtGenerator):
    def __init__(self, size, points_num, steps, width, color, lines=100, line_width=1):
        super().__init__(size=size,
                         points_num=points_num,
                         accuracy=0.005,
                         steps=steps,
                         width=width,
                         color=color)

        self.lines = lines
        self.line_width = line_width

    def main(self, dots=False, centered=True, draw=True):
        super().main()

        lines_list = []
        for _ in range(self.lines):
            lines_list.append(tuple(random.choice(self.curve.curve)))

        draw = ImageDraw.Draw(self.curve.image)
        draw.line(lines_list, fill=self.curve.color, width=self.line_width)


if __name__ == '__main__':
    size = 1000

    # points_num=5, lines=300, steps=10 - probably the best settings
    my_img = CurvesAndLines(size=size,
                            points_num=5,
                            lines=300,
                            steps=10,
                            width=lambda: 5,
                            color=random_red)

    my_img.points_func = lambda: create_points(my_img.image, my_img.points_num)
    my_img.create()
    my_img.get_image().save('images/curve.png')
