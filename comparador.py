from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color



class Background(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    pass

class Comp(BoxLayout):
    def build(self):
        return Background()


class Comparador(App):
    def build(self):
        return Comp()

Comparador().run()
