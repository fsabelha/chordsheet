import kivy
import pickle
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.factory import Factory

linePointList = []

class Garbage():
    '''

            

'''

class MyNotes(Widget):

    global globalLineList
    globalLineList = []
  
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            color = (1, 1, 1)
        

    def on_touch_move(self, touch):
        global globalLineList
        touch.ud['line'].points += [touch.x, touch.y]
        globalLineList = touch.ud['line'].points

    def draw_line(self):
        print 'draw_line'
        self.canvas.add(Line(points=[0,0, 400, 400]))

    

       
class MyGUI(Widget):

    def call_draw_line(self):
        MyNotes().draw_line()
   

class MyStickyApp(App):

    rootWid = Widget()

    def getit(self, obj):
        print 'getit'
        MyNotes().get_note()
    
    def addthewidget(self):
        self.notesWid = MyNotes()
        self.rootWid.add_widget(self.notesWid)

    def removethewidget(self):
        self.rootWid.remove_widget(self.notesWid)

    def build(self):
       
        btn1 = Button(text="get the note", pos=(400, 500) )
        btn1.bind(on_press=MyNotes().canvas.add(Line(points=[100,100,300,300])))

        self.rootWid.add_widget(MyGUI())
        self.rootWid.add_widget(btn1)
        return self.rootWid



if __name__ == '__main__':
    MyStickyApp().run()

    