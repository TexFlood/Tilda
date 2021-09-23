class MeetTime:
    begin_time = 'str'
    end_time = 'str'
    begin_date = None
    end_date = None
    location = None
    # Creating a list of days might be better.
    is_course_on_monday = False
    is_course_on_tuesday = False
    is_course_on_wednesday = False
    is_course_on_thursday = False
    is_course_on_friday = False
    is_course_on_saturday = False
    is_course_on_sunday = False
    category = None

    # Boolean values to see when the class is


    def __init__(self, location,begin_time,end_time,begin_date,end_date,is_course_on_monday,is_course_on_tuesday,is_course_on_wednesday,is_course_on_thursday,is_course_on_friday,is_course_on_saturday,is_course_on_sunday,category):
        self.location = location
        self.begin_time = begin_time
        self.end_time = end_time
        self.begin_date = begin_date
        self.end_date = end_date
        self.location = location
        self.is_course_on_monday = is_course_on_monday
        self.is_course_on_tuesday = is_course_on_tuesday
        self.is_course_on_wednesday = is_course_on_wednesday
        self.is_course_on_thursday = is_course_on_thursday
        self.is_course_on_friday = is_course_on_friday
        self.is_course_on_saturday = is_course_on_saturday
        self.is_course_on_sunday = is_course_on_sunday
        self.category = category # week 1 or week 2
    def __str__(self):
        return 'From ' + str(self.begin_time) + ' to ' + str(self.end_time)
