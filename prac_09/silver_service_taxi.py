from taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness: int):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flagfall = 4.50

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"
