#BASE DE UMA PÁGINA
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation = "vertical")
        button = Button(text = "Hello, World!", font_size = 30)
        label = Label(text = "Olá, Mundo!", font_size = 30)
        box.add_widget(button)
        box.add_widget(label)
        return box
    
Teste().run()
"""




#EVENTOS E VARIÁVEIS DE INSTÂNCIA
#(MUDA O TEXTO DO BOTÃO AO CLICAR)
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation = "vertical")
        button = Button(text = "Hello, World!", font_size = 30, on_realease = self.incrementar)
        label = Label(text = "Olá, Mundo!", font_size = 30)
        box.add_widget(button)
        box.add_widget(label)
        return box
    
    def incrementar(self, button):
        button.text = "Soltei"
    
Teste().run()
"""




#EVENTOS E VARIÁVEIS DE INSTÂNCIA
#(MUDANDO TEXTO DA LABEL AO CLICAR NO BOTÃO)
'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Teste(App):
    def build(self):
        box = BoxLayout(orientation = "vertical")
        button = Button(text = "Hello, World!", font_size = 30, on_release = self.incrementar)
        self.label = Label(text = '1', font_size = 30)
        box.add_widget(button)
        box.add_widget(self.label)
        return box
    
    def incrementar(self, button):
        self.label.text = str(int(self.label.text) + 1)
    
Teste().run()
'''




#ENTENDENDO O KIVY
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Incrementador(BoxLayout):
    pass

class Teste(App):
    def build(self):
        return Incrementador()
    
Teste().run()