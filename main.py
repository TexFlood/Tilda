import json
import requests
import SessionHandler
import StringParser
from Course import Course
from MeetTime import MeetTime

browser_session = requests.Session()

self_serve_portal_homepage_response = SessionHandler.get_self_portal_homepage(browser_session)
# Now we can start working on the schedule.



# Here we get all the matches to our regular expression. We need to parse them into "Semester" objects.

semesters = StringParser.parse_semesters(self_serve_portal_homepage_response)

# Populating courses in each semester
for semester in semesters:
    semesters_json_url = 'https://ssp.mycampus.ca/StudentRegistrationSsb/ssb/registrationHistory/reset?term=' + semester.code.__str__()

    response = browser_session.get(semesters_json_url)
    obj = json.loads(response.text)
    course_list = obj['data']['registrations']
    courses = []
    for item in course_list:
        meet_times = []
        for meet_time in item['meetingTimes']:
            meet = MeetTime(
                meet_time['room'],
                meet_time['beginTime'],
                meet_time['endTime'],
                meet_time['startDate'],
                meet_time['endDate'],
                meet_time['monday'],
                meet_time['tuesday'],
                meet_time['wednesday'],
                meet_time['thursday'],
                meet_time['friday'],
                meet_time['saturday'],
                meet_time['sunday'],
                meet_time['category']
            )
            meet_times.append(meet)
        course = Course(
            item['courseTitle'],
            item['subject'] + ' ' + item['courseNumber'],
            StringParser.parse_instructor_name(item['instructorNames']),
            item['courseReferenceNumber'],
            meet_times,
            item['scheduleDescription']
        )
        print(course)
        courses.append(course)
print('done')

