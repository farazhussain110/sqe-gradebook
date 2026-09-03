class Student:
    def add_score(self, score):
    self.scores.append(score)
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = []

        def add_score(self, score):
    if score < 0:
        raise ValueError("Score cannot be negative")
    self.scores.append(score)


    def add_score(self, score):
    """Add a non-negative score to the student's scores."""
    if score < 0:
        raise ValueError("Score cannot be negative")
    self.scores.append(score)