from meet_time import MeetTime


class Course:
    course_number = None
    course_title = None
    instructor_name = None
    crn = None
    meeting_times = None
    course_type = None

    def __init__(
            self,
            course_title: str,
            course_number: int,
            instructor_name: str,
            crn: str,
            meeting_times: MeetTime,
            course_type: str,
    ):
        self.course_title = course_title
        self.course_number = course_number
        self.instructor_name = instructor_name
        self.crn = crn
        self.meeting_times = meeting_times
        self.course_type = course_type

    def __str__(self):
        return_string: str = ''
        for meet_time in self.meeting_times:
            return_string += 'Course Title: ' + ' ' + self.course_title + ' ' + str(meet_time) + '\n'
        return return_string
