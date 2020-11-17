from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.core.text import LabelBase
LabelBase.register(name='Font_Hanzi',fn_regular="mysh.ttf")

class CardNumber(GridLayout):
    def __init__(self, **kwargs):
        super(CardNumber,self).__init__(**kwargs)
        self.init_card = NumericProperty(0)
        self.sent_card = NumericProperty(0)
        self.recycled_card = NumericProperty(0)
        self.remaining_card = NumericProperty(0)
        self.card_counter = 1
        self.recycle_flag = 0
        self.send_flag = 0

    def update(self):
        if self.recycle_flag == 1:
            self.remaining_card.text = str(int(self.init_card.text) - self.card_counter)
            self.recycled_card.text = str(int(self.recycled_card.text) + 1)
        if self.send_flag == 1:
            self.remaining_card.text = str(int(self.init_card.text) - self.card_counter)
            self.sent_card.text = str(int(self.sent_card.text) + 1)

    def btn_recycle(self):
        self.recycle_flag = 1

    def btn_send(self):
        self.send_flag = 1

    def release(self):
        self.update()
        self.card_counter += 1
        self.recycle_flag = 0
        self.send_flag = 0


class PlateNumber(GridLayout):
    pass

class LogText(BoxLayout):
    pass

class StatusBar(GridLayout):
    pass

class CardUIWindow(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
        pass

class CardUI2App(App):

    def build(self):

        return CardUIWindow()

if __name__ == '__main__':
    CardUI2App().run()