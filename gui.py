from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from curves_and_lines import CurvesAndLines
from tools.colors import *


class MainMenu(Screen):
    pass


class CurvesLines(Screen):
    path = "images/curve.png"

    def draw(self):
        art = CurvesAndLines(
            size=1000,
            points_num=5,
            lines=300,
            steps=10,
            width=lambda: 5,
            color=random_pastel)

        art.create()
        art.get_image().save(self.path)

    def back(self):
        WindowManager().current = "enter"


class WindowManager(ScreenManager):

    def __init__(self):
        super().__init__()
        self.add_widget(MainMenu(name="menu"))
        self.add_widget(CurvesLines(name="curves_lines"))

        self.current = "menu"


class GenerativeArt(App):
    def build(self):
        return WindowManager()


if __name__ == '__main__':
    GenerativeArt().run()
