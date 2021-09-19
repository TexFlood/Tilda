import requests
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
