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
from kivy.uix.scatter import Scatter




class Lyrics(Widget):

    global main_widget

    def add_lyric1(self, lyric):
        lyric_lbl1 = Label(text=lyric, pos=(25, 430))
        lyric_lbl1.bind(texture_size=lyric_lbl1.setter('size'))
        main_widget.add_widget(lyric_lbl1)
        
        


class Chords(Widget):
    chordDis = StringProperty('')

    def change_chord(self, c):
        chordDis += c


        


class ChordSheetApp(App):

    def add_new_chord(self, chord):
        scatter = Scatter(do_rotation=False, do_scale=False)
        scatter.add_widget(Label(text=chord))
        main_widget.add_widget(scatter)
        print scatter.children[0].text

    def build(self):
        global main_widget
        main_widget = Widget()
        lyrics = Lyrics()
        chords = Chords()
        main_widget.add_widget(lyrics)
        main_widget.add_widget(chords)

        return main_widget

if __name__ == '__main__':
    ChordSheetApp().run()