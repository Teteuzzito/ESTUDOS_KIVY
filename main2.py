from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class MyApp(App):
    def build(self):
        layout =  BoxLayout(orientation='vertical')
        self.lab1 = Label(
            text='1', color=[1,0,0,1],
            font_size=40, bold=True
        )
    
        self.lab2 = Label(
            text='Sesi', color=[0,1,0,1],
            font_size=40, italic=True
        )

        self.lab3 = Label(
            text='Enem', color=[0,0,1,1],
            font_size=40, underline=True
        )

        layout2 =  BoxLayout(orientation='horizontal')
        self.lab1_1 = Button(
            text='Senai', font_size=40, bold=True, background_color=get_color_from_hex('#7331E0'), on_press=botao_pressionado
        )
    
        self.lab2_1 = Button(
            text='Sesi', font_size=40, italic=True, background_color=get_color_from_hex("#7331E0"), on_release=self.incrementar
        )

        self.lab3_1 = Button(
            text='Enem', font_size=40, underline=True, background_color=get_color_from_hex("#7331E0"), size_hint=(0.5, 0.2)
        )

        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(self.lab3)

        layout2.add_widget(self.lab1_1)
        layout2.add_widget(self.lab2_1)
        layout2.add_widget(self.lab3_1)
        
        layout.add_widget(layout2)
        return layout
    
    def incrementar(self, button):
        self.lab1.text = str(int(self.lab1.text)+1)
    
def botao_pressionado(instance):
    print("Botão pressionado!")


if __name__ == "__main__":
    MyApp().run()
