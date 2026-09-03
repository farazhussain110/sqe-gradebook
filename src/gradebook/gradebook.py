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




    def add_score(self, student_score):
    """Add a valid score between 0 and 100 to the student's scores."""
    if not isinstance(student_score, (int, float)):
        raise ValueError("Score must be a number")
    if student_score < 0 or student_score > 100:
        raise ValueError("Score must be between 0 and 100")
    self.scores.append(student_score)