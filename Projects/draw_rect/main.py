import kivy
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label

from kivy.graphics import Color, Ellipse, Line, Rectangle
import sqlite3
from datetime import date







class DrawRect(Widget):
    def draw_rect(self):
        with self.canvas:
            Color(1, 1, 1)
            self.r = Rectangle(pos=[400,400], size=[300,300])

    def del_rect(self):
        self.canvas.remove(self.r)
    
class MyDrawingApp(App):
    
    def build(self):
   
        rootWid = Widget()
        rootWid.add_widget(DrawRect())
        
        return rootWid

if __name__ == '__main__':
    MyDrawingApp().run()