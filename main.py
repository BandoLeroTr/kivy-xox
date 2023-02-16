from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
import random

Window.size = (400, 700)

Builder.load_file("main.kv")

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
start_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
x_list = []

class Game(Screen):
    def click(self, id):
        self.ids[id].text = text

        if text == "X":
            if len(list) > 0:
                list.remove(id)
                x_list.append(id)

                if len(x_list) == 4:
                    print(x_list)
                    x_list.clear()

            if len(list) > 0:
                bot = random.choice(list)
                list.remove(bot)
                self.ids[bot].text = "O"

            if x_list == ["1", "2", "3"]:
                self.final()

            if x_list == ["4", "5", "6"]:
                self.final()

            if x_list == ["7", "8", "9"]:
                self.final()

            if x_list == ["1", "4", "7"]:
                self.final()

            if x_list == ["2", "5", "8"]:
                self.final()

            if x_list == ["3", "6", "9"]:
                self.final()

            if x_list == ["1", "5", "9"]:
                self.final()

            if x_list == ["3", "5", "9"]:
                self.final()

            if x_list == ["7", "5", "3"]:
                self.final()

            if x_list == ["9", "5", "1"]:
                self.final()

            if x_list == ["2", "1", "3"]:
                self.final()

            if x_list == ["3", "1", "2"]:
                self.final()

            if x_list == ["5", "4", "6"]:
                self.final()

        if text == "O":
            if len(list) > 0:
                list.remove(id)
                x_list.append(id)

                if len(x_list) == 4:
                    print(x_list)
                    x_list.clear()

            if len(list) > 0:
                bot = random.choice(list)
                list.remove(bot)
                self.ids[bot].text = "X"

            if x_list == ["1", "2", "3"]:
                self.final()

            if x_list == ["4", "5", "6"]:
                self.final()

            if x_list == ["7", "8", "9"]:
                self.final()

            if x_list == ["1", "4", "7"]:
                self.final()

            if x_list == ["2", "5", "8"]:
                self.final()

            if x_list == ["3", "6", "9"]:
                self.final()

            if x_list == ["1", "5", "9"]:
                self.final()

            if x_list == ["3", "5", "9"]:
                self.final()

            if x_list == ["7", "5", "3"]:
                self.final()

            if x_list == ["9", "5", "1"]:
                self.final()

    def select(self):
        if len(list) < 9:
            list.clear()
            for i in start_list:
                self.ids[i].text = ""
                x_list.clear()
                list.append(i)

        popup = Popup(title="Seçim Ekranı",
                      content = MDBoxLayout(
                          Button(text = "X", font_size = 100,
                                 on_press = lambda x: self.text_func("X")),

                          Button(text = "O", font_size = 100,
                                 on_press = lambda x: self.text_func("O")),
                      ),
                      size_hint = (.5, .5)
                      )
        popup.open()

    def text_func(self, text2):
        global text
        text = text2

    def final(self):
        popup = Popup(title="Oyun bitti",
                  content = Label(text="Oyun Bitti"),
                  size_hint = (.5, .5)
                  )
        popup.open()

class Main(MDApp):
    def build(self):
        return Game()

Main().run()
