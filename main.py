from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation = "vertical")
        button = Button(text = "Hello, World!")
        label = Label(text = "Olá, Mundo!")
        box.add_widget(button)
        box.add_widget(label)

        box2 = BoxLayout(orientation = "horizontal")
        button2 = Button(text = "Hello, World!")
        label2 = Label(text = "Olá, Mundo!")
        box2.add_widget(button2)
        box2.add_widget(label2)

        box.add_widget(box2)
        return box
    
Teste().run()
