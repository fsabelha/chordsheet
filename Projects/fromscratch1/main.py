import kivy
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.label import Label
import sqlite3
from datetime import date


class SqlSaver(Widget):
    global main_widget



    def addtextlabel(self, feedback):
        print 'textlabel'
        self.textfeedback = Label(text = feedback, pos = (350, 0))
        main_widget.add_widget(self.textfeedback)


    def clearlabel(self):
        main_widget.remove_widget(self.textfeedback)

  
    def connection(self):
	self.conn = sqlite3.connect('main.db')
        self.c = self.conn.cursor()
        self.addtextlabel('Connection created.')
        

    def create_table(self):
        print 'create_table'
        self.c.execute('''CREATE TABLE firsttable
             (date, name, age)''')

        self.conn.commit()
        self.clearlabel()
        self.addtextlabel('Table created.')

    def insert_row(self, name, age):

        print name
        print age
        today = date.today()
        self.c.execute("INSERT INTO firsttable VALUES ('" + str(today) + "', '" + name + "', '" + age + "')")
        self.conn.commit()
        self.clearlabel()
        self.addtextlabel('Information added.')


    def print_something(self, feedback):
        print 'you pressed the button'
        self.addtextlabel(feedback)




class SaveToSQLApp(App):

    def build(self):
        global main_widget
        
        sqlsaver = SqlSaver()

        main_widget = Widget()
        main_widget.add_widget(sqlsaver)

        return main_widget

if __name__ == '__main__':
    SaveToSQLApp().run()