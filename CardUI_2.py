from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
LabelBase.register(name='Font_Hanzi',fn_regular="mysh.ttf")

class CardUIWindow(Widget):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
        pass

class CardNumber(Widget):
    pass


class CardUI2App(App):

    def build(self):
        return CardUIWindow()

if __name__ == '__main__':
    CardUI2App().run()