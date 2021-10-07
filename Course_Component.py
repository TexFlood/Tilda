import datetime
from meet_time import MeetTime


class Course_Component:
    course_number = None
    course_title = None
    instructor_name = None
    crn = None
    meeting_times = None
    course_type = None
    url = 'https://example.org/'

    def __init__(
            self,
            course_title: str,
            course_number: int,
            instructor_name: str,
            crn: str,
            meeting_times: MeetTime,
            course_type: str
    ):
        self.course_title: str = course_title
        self.course_number = course_number
        self.instructor_name = instructor_name
        self.crn = crn
        self.meeting_times = meeting_times
        self.course_type = course_type

    def __str__(self):
        return_string: str = ''
        for meet_time in self.meeting_times:
            return_string += 'Course code: ' + self.course_number + '    Course Title: ' + ' ' + self.course_title + ' at ' + str(
                meet_time) + '\n'
        return return_string
    #
    # def get_sql_commands(self, index):
    #     time = datetime.datetime.now().__str__()
    #     time = time[:len(time) - 2] + " +00:00"
    #     commands = []
    #     values = []
    #     commands.append("INSERT INTO categories(name,isPinned,createdAt,updatedAt,id) VALUES(?,?,?,?,?)")
    #     tuple = (self.course_title, "1", time, time, index)
    #     values.append(tuple)
    #     commands.append("INSERT INTO bookmarks(name,url,createdAt,updatedAt,categoryId) VALUES(?,?,?,?,?)")
    #     tuple = ('Canvas Page', 'https://example.org', time, time, index)
    #     values.append(tuple)
    #     commands.append("INSERT INTO bookmarks(name,url,createdAt,updatedAt,categoryId) VALUES(?,?,?,?,?)")
    #     tuple = ('Lecture Link', 'https://example.org', time, time, index)
    #     values.append(tuple)
    #     commands.append("INSERT INTO bookmarks(name,url,createdAt,updatedAt,categoryId) VALUES(?,?,?,?,?)")
    #     tuple = ('Tutorial Link', 'https://example.org', time, time, index)
    #     values.append(tuple)
    #     commands.append("INSERT INTO bookmarks(name,url,createdAt,updatedAt,categoryId) VALUES(?,?,?,?,?)")
    #     tuple = ('Lab Link', 'https://example.org', time, time, index)
    #     values.append(tuple)
    #     return commands, values
