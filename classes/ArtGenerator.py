from classes.Сurve import Curve


class ArtGenerator:
    def __init__(self, image, points_num, points_func, accuracy, width, color):
        self.curve = Curve(
            points=points_func(),
            accuracy=accuracy,
            color=color(),
            width=width
        )

        self.image = image
        self.points_num = points_num
        self.color = color

    def main(self, steps):
        for _ in range(steps):
            self.curve.curve.color = self.color()
