import json
import os
import requests

import cli_handler
import html_bridge
import session_handler
import parsing_handler

# def populate_semester(browser_session, semester):
#     url = 'https://ssp.mycampus.ca/StudentRegistrationSsb/ssb/registrationHistory/reset?term=' + semester.code.__str__()
#     response = browser_session.get(semesters_json_url)
#     response_json = json.loads(response.text)
#     semester.courses = parsing_handler.parse_course(response_json)


browser_session = requests.Session()

self_serve_portal_homepage_response = session_handler.get_self_portal_homepage(browser_session)

# Instantiate a new semester
semester = parsing_handler.parse_homepage_to_semester_list(self_serve_portal_homepage_response)
# Get the usernames real name
(first_name, last_name) = parsing_handler.parse_name(self_serve_portal_homepage_response)


# Populating courses in each semester
semesters_json_url = 'https://ssp.mycampus.ca/StudentRegistrationSsb/ssb/registrationHistory/reset?term=' + semester.code.__str__()

response = browser_session.get(semesters_json_url)
response_json = json.loads(response.text)

semester.courses = parsing_handler.parse_course(response_json)
semester.student_name = first_name

for course in semester.courses:
    course.course_components = parsing_handler.parse_course_components(response_json, course.course_title)
    course.determine_course_type()

course_list_lectures = []
course_list_tutorials = []

dump = json.dumps(semester,
                  default=lambda x: x.__dict__)  # Idk what this is but it's magic so lets leave it as that...

try:
    os.remove('fill_me.dat')
except FileNotFoundError:
    ()

f = open('json_raw_mycampus.json', 'w')
f.write(response.text)

f = open('json_dump_uoit_schedule.json', 'w')
f.write(dump)

cli_handler.print_tilde(True)

html_bridge.generate_webpage(semester)







