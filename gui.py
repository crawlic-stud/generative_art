from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from main.curves_and_lines import CurvesAndLines
from main.shapes import Shapes
from main.curvature import Curvature
from main.circle import Rays
from main.star import Star

from main.tools.image_utils import calculate_offset, create_box
from main.tools.colors import *


Window.clearcolor = (1, 1, 1, .1)
Window.size = (414, 896)


class Next(Button):
    pass


class Back(Button):
    pass


class Draw(Button):
    pass


class CustomLayout(GridLayout):
    pass


class MainMenu(Screen):
    pass


class Generator(Screen):
    path = ""
    art = None

    def draw(self):
        self.art.create()
        self.art.get_image().save(self.path)


class CurvesLinesArt(Generator):
    path = "main/images/curve.png"

    def draw(self):
        self.art = CurvesAndLines(
            size=1000,
            points_num=5,
            lines=300,
            steps=10,
            width=lambda: 5,
            color=random_pastel)
        super().draw()


class ShapesArt(Generator):
    path = "main/images/shape.png"

    def draw(self):
        self.art = Shapes(
            size=1000,
            points_num=10,
            steps=30,
            color=random_pastel
        )
        super().draw()


class CurvatureArt(Generator):
    path = 'main/images/curvature.png'

    def draw(self):
        start = [random.randint(10, 20), random.randint(10, 200)]
        end = [random.randint(980, 990), random.randint(500, 990)]

        self.art = Curvature(
            size=1000,
            points_num=random.randint(5, 10),
            start=start,
            end=end,
            color=random_pastel,
            width=lambda: random.randint(1, 15),
            draw_rect=True,
            box=True,
            steps=random.randint(20, 40)
        )

        off_x, off_y = calculate_offset(self.art.image, create_box(self.art.start, self.art.end))
        self.art.start = [self.art.start[0] + off_x, self.art.start[1] - off_y]
        self.art.end = [self.art.end[0] + off_x, self.art.end[1] - off_y]

        super().draw()


class CircleArt(Generator):
    path = 'main/images/rays.png'

    def draw(self):
        self.art = Rays(
            size=1000,
            center=(1000 // 2, 1000 // 2),
            rays_num=91,
            points_num=3,
            radius=400,
            steps=3,
            color=random_pastel,
            width=lambda: random.randint(1, 15),
            box=True)
        super().draw()


class StarArt(Generator):
    path = 'main/images/star.png'

    def draw(self):
        self.art = Star(
            size=1000,
            rays_num=random.randrange(7, 14, 2),
            width=lambda: random.randint(1, 3),
            color=random_pastel,
            steps=25,
            bend=2,
            radius=400,
            box=True,
            centered=False)
        super().draw()


class WindowManager(ScreenManager):

    def __init__(self):
        super().__init__()
        self.add_widget(MainMenu(name="menu"))
        self.add_widget(CurvesLinesArt(name="curves_lines"))
        self.add_widget(ShapesArt(name="shape"))
        self.add_widget(CurvatureArt(name="curvature"))
        self.add_widget(CircleArt(name="circle"))
        self.add_widget(StarArt(name="star"))

        self.current = "menu"


class GenerativeArt(App):
    def build(self):
        return WindowManager()


if __name__ == '__main__':
    GenerativeArt().run()
