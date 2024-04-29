"""from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MyApp(App):
    def build(self):
        return AsyncImage(source="https://motorshow.com.br/wp-content/uploads/sites/2/2022/01/ram-trx-6x6-1.jpg")

if __name__ == "__main__":
    MyApp().run()"""

from kivy.app import App
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
    MyApp().run()