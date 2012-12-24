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

global globalLineList
global LinesList
global notescopy
LinesList = []
globalLineList = []
notescopy = []

''' Do we want to add/remove canvas items?, 
or add/remove the entire widget (canvas included)

Well, to pickle, I think we need to pickle the list so 
that would mean we have to extract the ud.touch['Line'] list 
from the canvas, and then redraw the line.

Unfortunatly it only copies the last on_touch_down because the touch 
dictionary resets.  The line is drawn and kept on the canvas however.
It would be nice to extract the canvas 'children' like on a widget, 
but maybe there is a better way.
'''


class MyNotes(Widget):

    def on_touch_down(self, touch):
        global globalLineList
        with self.canvas:
            globalLineList = [touch.x, touch.y]
            touch.ud['line'] = Line(points=globalLineList)
            color = (1, 1, 1)
        

    def on_touch_move(self, touch):
        global globalLineList
        touch.ud['line'].points += [touch.x, touch.y]
        globalLineList = touch.ud['line'].points

    def on_touch_up(self, touch):
        global LinesList
        LinesList.append(globalLineList)

class MyGUI(Widget):
    pass


class MyAppApp(App):

    def build(self):


        notes = MyNotes()
        rootWid = Widget()

        rootWid.add_widget(MyGUI())
        rootWid.add_widget(notes)

        def copynotes(self):
            global notescopy
            notescopy = LinesList
            print LinesList
        button = Button(text='copy')
        button.bind(on_release=copynotes)
        rootWid.add_widget(button)

        def remove_note(self):
            notes.canvas.clear()
        button1 = Button(text='hide notes', size=(200, 200), pos=(200,200))
        button1.bind(on_release=remove_note)
        rootWid.add_widget(button1)

        def paste(self):
            global notescopy
            for l in notescopy:
                notes.canvas.add(Line(points=l))
        button2 = Button(text='Paste', pos=(400,400))
        button2.bind(on_release=paste)
        rootWid.add_widget(button2)

        def delnotes(self):
            global notescopy
            notescopy = []
        button4 = Button(text='delete notes', size=(150, 40), pos = (10, 250))
        button4.bind(on_release=delnotes)
        rootWid.add_widget(button4)
 

        return rootWid

MyAppApp().run()