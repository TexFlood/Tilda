import Course_Component


class Course():
    has_lecture_component= False
    has_tutorial_component = False
    has_lab_component= False
    course_components = []
    course_title: str

    def __init__(self, course_title):
        self.course_title = course_title

    def determine_course_type(self):
        for course_component in self.course_components:
            if (course_component.course_type == 'Lecture'):
                self.has_lecture_component = True
            if (course_component.course_type == 'Laboratory'):
                self.has_lab_component = True
            if (course_component.course_type == 'Tutorial'):
                self.has_tutorial_component = True
