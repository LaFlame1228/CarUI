from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

import cv2
import numpy as np

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

class Camera(Image):
    def __init__(self,capture,fps,**kwargs):
        super(Camera, self).__init__(**kwargs)
        # self = Image(source= 'logo.png')
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0/fps)

    def update(self,dt):
        # self.capture = cv2.VideoCapture(0)
        ret, frame = self.capture.read()
        if ret:
            # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = texture1


class CardUIWindow(BoxLayout):
    def __init__(self,**Kwargs):
        super(CardUIWindow, self).__init__(**Kwargs)

        self.leftBox = ObjectProperty(None)
        self.capture = cv2.VideoCapture(0)
        self.my_camera = Camera(capture= self.capture,fps=30.0)
        self.ids['Left'].add_widget(self.my_camera)

    def on_stop(self):
        self.capture.release()

class CardUI2App(App):

    def build(self):
        window = CardUIWindow()

        # Clock.schedule_interval(window.update, 1.0 / 30)

        # self.capture = cv2.VideoCapture(0)
        # self.my_camera = Camera(capture=self.capture, fps=30)

        return window





if __name__ == '__main__':
    CardUI2App().run()