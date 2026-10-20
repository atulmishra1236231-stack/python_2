from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        for i in range(5):
            button = Button(text=f"Button {i + 1}")
            layout.add_widget(button)

        return layout


MyApp().run()