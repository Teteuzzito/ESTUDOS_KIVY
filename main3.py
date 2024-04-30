"""from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MyApp(App):
    def build(self):
        return AsyncImage(source="https://motorshow.com.br/wp-content/uploads/sites/2/2022/01/ram-trx-6x6-1.jpg")

if __name__ == "__main__":
    MyApp().run()"""

"""from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        slider = Slider(min=0, max=100, value=70, step=1)
        slider.bind(value=self.atualizar_label)
        self.label = Label(text=f"Valor Slider: {int(slider.value)}")

        layout.add_widget(slider)
        layout.add_widget(self.label)

        return layout
    
    def atualizar_label(self, instance, valor):
        self.label.text = f"Valor Slider: {int(valor)}"
    
if __name__ == "__main__":
    MyApp().run()"""

"""from kivy.app import App
from kivy.uix.progressbar import ProgressBar

class MyApp(App):
    def build(self):
        return ProgressBar(value=90)
    
if __name__ == "__main__":
    MyApp().run()"""

"""from kivy.app import App
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        return TextInput(text="Texto inicial")
    
if __name__ == "__main__":
    MyApp().run()"""

"""from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout_principal = BoxLayout(orientation='vertical')

        self.input_nome = TextInput(hint_text = "Digite seu nome: ")
        layout_principal.add_widget(self.input_nome)

        botao_enviar = Button(text="Enviar", on_press=self.exibir_mensagem)
        layout_principal.add_widget(botao_enviar)

        self.label_mensagem = Label()
        layout_principal.add_widget(self.label_mensagem)

        return layout_principal
    
    def exibir_mensagem(self, instance):
        nome = self.input_nome.text
        mensagem = f"Olá {nome}, você está avançando no Kivy! Parabéns SESIANO!!!"
        self.label_mensagem.text = mensagem

if __name__ == "__main__":
    MyApp().run()"""

"""from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class MyApp(App):
    def build(self):
        return ToggleButton(text="Ligado", state="normal")
    
if __name__ == "__main__":
    MyApp().run()"""

"""from kivy.app import App
from kivy.uix.switch import Switch

class MyApp(App):
    def build(self):
        return Switch(active=False)

if __name__ == "__main__":
    MyApp().run()"""

"""from kivy.app import App
from kivy.uix.video import Video

class MyApp(App):
    def build(self):
        return Video(source='C:/GitHUB/ESTUDOS_KeIVY/video-de-1-segundo.mp4')

if __name__ == "__main__":
    MyApp().run()"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        layout = Label(text="PRAIAS NORDESTINA", font_size=50, bold=True)
        layout_principal = BoxLayout(orientation='vertical', spacing=30, padding=[50,50, 50, 30])
        botao1 = Button(text="Botão 1")
        botao2 = Button(text="Botão 2")
        botao3 = Button(text="Botão 3")
        layout_principal.add_widget(layout)
        layout_principal.add_widget(botao1)
        layout_principal.add_widget(botao2)
        layout_principal.add_widget(botao3)
        return layout_principal

if __name__ == "__main__":
    MyApp().run()