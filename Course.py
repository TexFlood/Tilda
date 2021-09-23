import Course_Component


class Course():
    has_lecture_component:bool
    has_tutorial_component:bool
    has_lab_component:bool
    course_components = []
    course_title:str
    def __init__(self,course_title):
        self.course_title = course_title
    def determine_course_type(self):
        for course_component in self.course_components:
            if(course_component.course_type == 'Lecture'):
                has_lecture_component = True
            if (course_component.course_type == 'Laboratory'):
                has_lecture_component = True
            if (course_component.course_type == 'Tutorial'):
                has_lecture_component = True
