from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

class mainWidget(Widget):
    pass

class TheLabApp(App):
    def build(self):
        return
Builder.load_file("TheLabApp.kv")

TheLabApp().run()