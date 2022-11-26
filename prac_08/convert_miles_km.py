from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

KILOMETER_VALUE = 1.60934


class DistanceConverter(App):
    message = StringProperty()

    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = ""
        return self.root

    def handle_calculate(self):
        value = self.get_valid_number()
        result = value * KILOMETER_VALUE
        self.message = str(result)

    def handle_increment(self, change):
        value = self.get_valid_number() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_valid_number(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


app = DistanceConverter()
app.run()
