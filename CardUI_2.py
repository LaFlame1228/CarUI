from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

import cv2
import numpy as np

LabelBase.register(name='Font_Hanzi', fn_regular="mysh.ttf")


class CardNumber(GridLayout):
    def __init__(self, **kwargs):
        super(CardNumber, self).__init__(**kwargs)
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
    # def __init__(self, **kwargs):
    #     super(PlateNumber, self).__init__(**kwargs)
    #     self.car_type = StringProperty()
    #     self.plateNumber = StringProperty()

    # def update(self):
    pass


class LogText(BoxLayout):
    def __init__(self, **kwargs):
        super(LogText, self).__init__(**kwargs)
        self.logText = ObjectProperty(None)


class StatusBar(GridLayout):
    """
    状态框显示类
    """
    def __init__(self, **kwargs):
        """
          Parameters
          ----------
          PLC_module : label
          PLC状态模块
          Robot_module： label
          机器人状态模块
          Car_type_module： label
          车型车牌状态模块
          Car_window_module： label
          车窗定位状态模块
          Ground_sense： label
          地感线圈状态显示
          Car_stop： label
          车停状态显示
          PLC_connect： label
          PLC链接状态显示
          Ultrasonic： label
          超声波数值显示
          Robot_running： label
          机器人运行状态显示
          Card_position： TextInput
          取卡位显示
          Card_remain： label
          机器人有卡显示
          Robot_alarm： label
          机器人报警
          Micro_wave： label
          微波状态显示
          Fill_light： label
          补光灯状态显示
          Camera_running： label
          相机运行状态显示
          Plate_system： label
          车牌系统状态显示
          Up_camera： label
          上相机运行状态显示
          Down_camera： label
          下相机运行状态显示
          Window_position： TextInput
          车窗坐标位置
        """
        super(StatusBar, self).__init__(**kwargs)
        self.plc_module = ObjectProperty(None)
        self.robot_module = ObjectProperty(None)
        self.car_type_module = ObjectProperty(None)
        self.car_window_module = ObjectProperty(None)
        self.ground_sense = ObjectProperty(None)
        self.car_stop = ObjectProperty(None)
        self.plc_connect = ObjectProperty(None)
        self.ultrasonic = ObjectProperty(None)
        self.robot_running = ObjectProperty(None)
        self.card_position = ObjectProperty(None)
        self.card_remain = ObjectProperty(None)
        self.robot_alarm = ObjectProperty(None)
        self.micro_wave = ObjectProperty(None)
        self.fill_light = ObjectProperty(None)
        self.camera_running = ObjectProperty(None)
        self.plate_system = ObjectProperty(None)
        self.up_camera = ObjectProperty(None)
        self.down_camera = ObjectProperty(None)
        self.window_position = ObjectProperty(None)

    def btn(self):
        self.up_camera.background_color = (1, 0, 0, 1)


class Camera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(Camera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0/fps)

    def update(self, dt):
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
    def __init__(self, **kwargs):
        super(CardUIWindow, self).__init__(**kwargs)

        # self.leftBox = ObjectProperty(None)
        self.capture = cv2.VideoCapture(0)
        self.my_camera = Camera(capture=self.capture,fps=30.0)
        self.ids['Left'].add_widget(self.my_camera)

    def on_stop(self):
        self.capture.release()


class CardUI2App(App):

    def build(self):
        window = CardUIWindow()

        return window


if __name__ == '__main__':
    CardUI2App().run()