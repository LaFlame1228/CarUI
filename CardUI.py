from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
LabelBase.register(name='Font_Hanzi',fn_regular="mysh.ttf")

class CardUIWindow(BoxLayout):
    pass

class CardUIApp(App):

    def build(self):
        return CardUIWindow()

if __name__ == '__main__':
    CardUIApp().run()