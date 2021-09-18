class Semester :
    def __init__(self, code, title):
        self.title = title
        self.code = code

    def __str__(self) -> str:
        return self.title
