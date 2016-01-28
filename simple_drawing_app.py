from kivy.app import App

from kivy.uix.widget import Widget
from kivy.graphics import Line


class DrawInput(Widget):
    def on_touch_down(self, touch):
        # print("touch_down", touch)
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        # print("touch_move", touch)
        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        print("touch_up", touch)


class KivyApp(App):
    def build(self):
        return DrawInput()

if __name__ == "__main__":
    KivyApp().run()
