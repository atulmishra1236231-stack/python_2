
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class Calculator(BoxLayout):
    display = StringProperty("")

    def add_to_display(self, value):
        self.display += value

    def clear_display(self):
        self.display = ""

    def calculate(self):
        try:
            result = eval(self.display)

            if isinstance(result, (int, float)):
                self.display = str(result)

        except Exception:
            self.display = "Error"


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
