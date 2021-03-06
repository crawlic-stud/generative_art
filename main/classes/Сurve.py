from main.tools.bezier import create_curve
import numpy as np
from main.tools.image_utils import calculate_offset
from PIL import ImageDraw


class Curve:
    """Draws curve."""
    def __init__(self, points: np.array, accuracy, color, width):
        self.points = points
        self.accuracy = accuracy
        self.color = color
        self.width = width
        self.curve = []
        self.image = None

    def create_curve(self):
        """Creates curve from given points (attribute curve) and returns points of curve."""
        t_points = np.arange(0, 1, self.accuracy)
        curve = [tuple(i) for i in create_curve(t_points, self.points)]
        self.curve = curve
        return curve

    def offset(self, img):
        """Offsets curve to center."""
        off_x, off_y = calculate_offset(img, self.curve)
        points = [(self.curve[i][0] + off_x, self.curve[i][1] - off_y) for i in range(len(self.curve))]
        self.curve = points

    def draw(self, img, centered=False):
        """Draws standard curve."""
        self.image = img

        if centered:
            self.offset(img)

        img_draw = ImageDraw.Draw(img)
        img_draw.line(self.curve, fill=self.color, width=self.width)

    def draw_points(self, img, centered=False):
        """Draw curve as dots (according to accuracy could look similar to standard, but impacts performance)."""
        self.image = img

        if centered:
            self.offset(img)

        img_draw = ImageDraw.Draw(img)
        for point in self.curve:
            img_draw.rounded_rectangle([point[0] - self.width//2, point[1] - self.width//2,
                                        point[0] + self.width//2, point[1] + self.width//2],
                                       radius=100, fill=self.color)
