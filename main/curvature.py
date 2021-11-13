import random
from PIL import Image, ImageDraw
from main.tools.colors import *
from main.classes.ArtGenerator import ArtGenerator
from main.tools.image_utils import points_along_line, calculate_offset, create_box


class Curvature(ArtGenerator):
    def __init__(self, size, points_num, width, steps, color,
                 start=None, end=None, draw_rect=True, box=False):

        super().__init__(size=size,
                         points_num=points_num,
                         accuracy=0.005,
                         color=color,
                         steps=steps,
                         width=width)

        self.start = [i * 5 for i in start]
        self.end = [i * 5 for i in end]
        self.points_func = lambda: points_along_line(self.image, self.points_num, self.start, self.end, box=box)
        self.draw_rect = draw_rect

    def main(self, dots=False, centered=True, draw=True):
        super().main(centered=False)

    def create(self):
        super().create()

        if not self.draw_rect:
            return

        polygon_image = Image.new('RGBA', self.image.size, (0, 0, 0, 0))

        polygon_pos = create_box(self.start, self.end)
        polygon_color = add_transparency(self.color(), random.randint(10, 30) / 100)

        ImageDraw.Draw(polygon_image).polygon(polygon_pos, fill=polygon_color)

        self.image = Image.alpha_composite(self.image, polygon_image)


if __name__ == '__main__':
    size = 1000

    indent = 0
    start = [random.randint(indent, size - indent), random.randint(indent, size - indent)]
    end = [random.randint(indent, size - indent), random.randint(indent, size - indent)]

    # start = [indent, indent]
    # end = [size - indent, size - indent]

    curvature = Curvature(size=size,
                          points_num=5,
                          start=start,
                          end=end,
                          color=random_blue,
                          width=lambda: random.randint(1, 15),
                          draw_rect=True,
                          box=True,
                          steps=20)

    off_x, off_y = calculate_offset(curvature.image, create_box(curvature.start, curvature.end))
    curvature.start = [curvature.start[0] + off_x, curvature.start[1] - off_y]
    curvature.end = [curvature.end[0] + off_x, curvature.end[1] - off_y]

    curvature.create()
    curvature.get_image().save('./images/curvature.png')
