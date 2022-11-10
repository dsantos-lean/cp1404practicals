COMPLETE_PROJECT = 100


class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {int(self.priority)}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return int(self.priority) < int(other.priority)

    def __ge__(self, other):
        return self.start_date >= other.start_date

    def is_completed(self):
        return self.completion_percentage == COMPLETE_PROJECT

