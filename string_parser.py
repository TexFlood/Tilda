import json

import requests

from Course import Course
from meet_time import MeetTime
from Semester import Semester
import re


def parse_semesters(self_serve_portal_homepage_response: requests.Response) -> list:

    semesters_list_regex = '<option value="(\d+)" >([A-Za-z]+(?:(?:\/[A-Za-z]+ \d{4})|(?: \d{4})))'

    # This RegEx will return a few groups. The RegEx essentially says find me something that looks like this (for
    # example each capture group will be between ***):

    # <option value="***201909***" >***Fall 2019***</option>
    # <option value="***202001***" >***Winter 2020***</option>
    # <option value="***202005***" >***Spring/Summer 2020***</option>
    # <option value="***202009***" >***Fall 2020***</option>
    # <option value="***202101***" >***Winter 2021***</option>
    # <option value="***202105***" >***Spring/Summer 2021***</option>
    # <option value="***202109***" >***Fall 2021***</option>

    re_matches = re.findall(semesters_list_regex, self_serve_portal_homepage_response.text)
    semesters = []
    for i in re_matches:
        temp_sem = Semester(i[0], i[1])
        semesters.append(temp_sem)

    # They are now in Chronological order such that semesters[0] is the oldest semester available.
    semesters.sort()
    for i in semesters:
        print(i)
    return semesters


def parse_session_key(response_string: str) -> str:
    uuid_regex = 'sessionDataKey=(\w{8}.\w{4}.\w{4}.\w{4}.\w{12})'
    session_key = re.search(uuid_regex, response_string).group(1)
    print(session_key)
    return session_key


def parse_instructor_name(list_of_names: list) -> str:
    instructor = ''
    if (len(list_of_names) == 0):
        instructor = 'Not Specified'
    elif (len(list_of_names) == 1):
        for name in list_of_names:
            instructor += name
    elif (len(list_of_names) > 1):
        instructor = list_of_names[0]
        for count in range(len(list_of_names) - 1):
            instructor = instructor + ' and ' + list_of_names[count + 1]

    return instructor

def parse_courses(json_string)->list:
    course_list = json_string['data']['registrations']
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
            parse_instructor_name(item['instructorNames']),
            item['courseReferenceNumber'],
            meet_times,
            item['scheduleDescription']
        )
        courses.append(course)
    return course_list

