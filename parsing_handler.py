import json

import requests
from typing import List

from Course import Course
from Course_Component import Course_Component
from exceptions import LoginFailed
from meet_time import MeetTime
from Semester import Semester
import re


def parse_homepage_to_semester_list(self_serve_portal_homepage_response: requests.Response) -> list:
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
    if(len(re_matches) == 0):
        raise LoginFailed
        print('Login failed')
    print('Login Successful')

    for i in re_matches:
        temp_sem = Semester(i[0], i[1])
        semesters.append(temp_sem)

    # They are now in Chronological order such that semesters[0] is the oldest semester available.
    semesters.sort()

    return semesters[len(semesters) - 1]

def parse_name(self_serve_portal_homepage_response: requests.Response):
    #<meta name="fullName" content="Bolivar-Hazboun, Xavier"/>
    regex_statement = '<meta name="fullName" content="(.+), (.+)"\/'
    text = self_serve_portal_homepage_response.content.decode()
    name = []
    name.append(re.search(regex_statement,text).group(2))
    name.append(re.search(regex_statement,text).group(1))
    return name

def parse_session_key(response_string: str) -> str:
    uuid_regex = 'sessionDataKey=(\w{8}.\w{4}.\w{4}.\w{4}.\w{12})'
    session_key = re.search(uuid_regex, response_string).group(1)
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


def parse_course(json) -> list:
    course_components = json['data']['registrations']
    course_list = []
    already_in_list = False
    for course_component in course_components:
        course = course_component['courseTitle']
        new_course = Course(course)
        if len(course_list) == 0:
            course_list.append(
                new_course
            )
        for existing_course in course_list:
            if existing_course.course_title == course_component['courseTitle']:
                already_in_list = True
            else:
                already_in_list = False
        if not already_in_list:
            course_list.append(
                new_course
            )
    return course_list


def parse_course_components(json_obj, course_title:str)->List[Course]:
    course_list = []
    json_course_list = json_obj['data']['registrations']
    for json_course in json_course_list:
        if json_course['courseTitle'] == course_title:
                meet_times = []
                for meet_time in json_course['meetingTimes']:
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
                course = Course_Component(
                    json_course['courseTitle'],
                    json_course['subject'] + ' ' + json_course['courseNumber'],
                    parse_instructor_name(json_course['instructorNames']),
                    json_course['courseReferenceNumber'],
                    meet_times,
                    json_course['scheduleDescription']
                )
                course_list.append(course)
    return course_list
# TODO want to move a method from main to here to maintain order in code.
def create_json_files(response:str):
    ()