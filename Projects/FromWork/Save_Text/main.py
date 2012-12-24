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
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock


global globalLineList
global LinesList
global notescopy
LinesList = []
globalLineList = []
notescopy = []


class Sticky(Widget):
  
    def on_touch_down(self, touch):
        global globalLineList
        with self.canvas:
            globalLineList = [touch.x, touch.y]
            Color = (1, 1, 1)
            touch.ud['Line'] = Line(points=globalLineList)
 
    def on_touch_move(self, touch):
        global globalLineList
        touch.ud['Line'].points += [touch.x, touch.y]
        globalLineList = touch.ud['Line'].points

    def on_touch_up(self, touch):
        global LinesList
        LinesList.append(globalLineList)
        

class Chords(DropDown):
    pass

dropdown = Chords()
mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))


class Text_Input(Widget):
    global a
    global openFile
    global popup
  
    a = 1
    bottom_label = ObjectProperty()
    info = StringProperty()

    def save_text(self):
        pickle.dump(self.saveText.text, open('text.p', 'wb')) 
        self.saveText.text = ''
        if self.saveText.focus == True:
            self.saveText.focus = False
        self.bottom_label.text = 'Text Saved'
        
    def clear_text(self):
        self.bottom_label.text = ''

    def selection_updated(self, filechooser, selection):
        global openFile
        openFile = selection 
        popup.dismiss()
        print openFile[0]
        rText = pickle.load(open(openFile[0], "rb"))
        self.saveText.text = rText
        self.bottom_label.text = 'Stuff Retrieved'

    def choose_file(self):
        global popup
        filechooser = FileChooserIconView()              
        popup = Popup(title='Choose a File to Open', content=filechooser, size_hint=(None, None), size=(400, 400))
        popup.open()
        filechooser.bind(selection=self.selection_updated) 

        

    def copy_sticky(self):
         global notescopy
         notescopy = LinesList
         print notescopy
         pickle.dump(notescopy, open('sticky.p', 'wb'))  
           
class SaveTextApp(App):

    def add_Draw(self):
        main_deal.add_widget(sticky)


    def remove_Draw(self):
        main_deal.remove_widget(sticky)


    def get_sticky(self, filechooser, selection):
        global openFile
        global spopup
        global rSticky
        openSticky = selection 
        spopup.dismiss()
        LinesList = pickle.load(open(openSticky[0], "rb"))

        for l in LinesList:
            sticky.canvas.add(Line(points=l))

###Add and remove a feedback label
        lbl3 = Label(text = 'Stuff Retrieved')
        main_deal.add_widget(lbl3) 
        def my_callback(dt):
            main_deal.remove_widget(lbl3)
        Clock.schedule_once(my_callback, 2)


    def choose_sticky_file(self, obj):
        global spopup
        filechooser = FileChooserIconView()              
        spopup = Popup(title='Choose a File to Open', content=filechooser, size_hint=(None, None), size=(400, 400))
        spopup.open()
        filechooser.bind(selection=self.get_sticky) 
        
    

    def build(self):
        global main_deal
        global sticky
        sticky = Sticky()

        main_deal = Widget()
        textbox = Text_Input()
        main_deal.add_widget(textbox)

        getStickyBtn = Button(text="Get Sticky", size=(100, 20), pos=(250, 460))
        getStickyBtn.bind(on_release=self.choose_sticky_file)
        main_deal.add_widget(getStickyBtn)

        return main_deal
     
if __name__ == '__main__':
    SaveTextApp().run()






