import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle

class DrawRect(Widget):

    def draw_line(self):
        with self.canvas:
            Color(1, 1, 1)
            Line(points=[400,400,300,300])
        
    
    
class MyDrawingApp(App):

    	
    def build(self):
   
        rootWid = Widget()

        rootWid.add_widget(DrawRect())
 
       
        return rootWid

if __name__ == '__main__':
    MyDrawingApp().run()

    