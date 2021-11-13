from main.classes.Сurve import Curve
from PIL import Image


class ArtGenerator:
    """Class for creating art using different combinations of Bezier curves."""
    def __init__(self, size, points_num, accuracy, steps, width, color):
        self.curve = Curve(
            points=[[0, 0], [1, 1]],
            accuracy=accuracy,
            color=color,
            width=width
        )

        self.steps = steps
        self.image = Image.new('RGBA', (size * 5, size * 5), (0, 0, 0, 0))
        self.points_num = points_num
        self.color = color
        self.points_func = None
        self.width = width

    def setup(self):
        """Setups new params for curve."""

        if self.points_func is None:
            raise(ValueError('please fill points_func for curve.'))

        # color and width are changeable (that's why they're functions),
        # if you want them not to be - set them as lambda: <your_value>
        self.curve.color = self.color()
        self.curve.width = self.width()

        self.curve.points = self.points_func()
        self.curve.create_curve()

    def main(self, dots=False, centered=True, draw=True):
        """Main function for repeatable operations"""

        self.setup()

        if not draw:
            return

        if not dots:
            self.curve.draw(self.image, centered=centered)
        else:
            self.curve.draw_points(self.image, centered=centered)

    def get_image(self):
        """Returns original size image."""
        width, height = self.image.size
        image = self.image.resize((width//5, height//5), resample=Image.ANTIALIAS)
        return image

    def create(self):
        """Repeats main function <steps> times and combines it to one piece"""
        for _ in range(self.steps):
            self.main()
            self.image = Image.alpha_composite(self.image, self.curve.image)


# Basic template (copy & create your own)
class YourClass(ArtGenerator):
    def __init__(self, size, points_num, steps, width, color):
        super().__init__(
            size=size,
            points_num=points_num,
            accuracy=0.005,
            steps=steps,
            width=width,
            color=color)

        # REMEMBER:
        # self.points_func = lambda: <your func>
