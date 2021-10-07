

class Semester:
    courses = []
    student_name = None

    def __init__(self, code, title):
        self.title = title
        self.code = code

    def __str__(self) -> str:
        return self.title

    def __lt__(self, other):
        return self.code < other.code
