class Guitar:
    def __init__(self, name="", year=0, cost=0.0, age=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = age

    def __str__(self):
        return "{} ({}) : $ {}".format(self.name, self.year, self.cost)

    def get_age(self, current_year=2022):
        self.age = current_year - self.year
        return self.age

    def is_vintage(self):
        return self.age >= 50
