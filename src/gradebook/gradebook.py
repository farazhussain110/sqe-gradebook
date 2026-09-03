class Student:
    def add_score(self, score):
    self.scores.append(score)
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = []