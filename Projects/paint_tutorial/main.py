from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class ButtonThing(Widget):

    def do_action():
        print "hi annabelle"



class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        self.touch = touch
        color = (random(), 1, 1)
        if touch.x > 100 and touch.y > 100:
            with self.canvas:
                Color(*color, mode='hsv')
                d = 2.
                Ellipse(pos=(self.touch.x - d / 2, self.touch.y - d / 2), size=(d, d))
                self.touch.ud['Line'] = Line(points=(self.touch.x, self.touch.y))

    def on_touch_move(self, touch):

        if touch.x > 100 and touch.y > 100:
            self.touch = touch
            self.touch.ud['Line'].points += [self.touch.x, self.touch.y]


    def del_line():
        print 'pressed'

class MyPaintApp(App):

    def build(self):
        parent = Widget()
        painter = MyPaintWidget()
        btnthing = ButtonThing()

        def hiannabelle(obj):
            popup = Popup(title= "Pop Up Window", content=Label(text='Hi Annabelle!!!'), size_hint=(None, None), size=(300,300))
            popup.open()
        button = Button(text='newbutton', pos=(200, 400))
        button.bind(on_release=hiannabelle)

        parent.add_widget(painter)  

        parent.add_widget(btnthing)
        parent.add_widget(button)



        return parent


if __name__ == '__main__':
    MyPaintApp().run()
