import requests
from Semester import Semester
import re


def parse_semesters(self_serve_portal_homepage_response: requests.Response) -> list:
    semesters_list_regex = '<option value="(\d+)" >([A-Za-z]+(?:(?:\/[A-Za-z]+ \d{4})|(?: \d{4})))'

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


def parse_session_key(response: requests.Response) -> str:
    uuid_regex = 'sessionDataKey=(\w{8}.\w{4}.\w{4}.\w{4}.\w{12})'
    session_key = re.search(uuid_regex, response.text).group(1)
    print(session_key)
    return session_key
