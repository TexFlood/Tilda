import json
import sqlite3

import requests

import default_apps
import session_handler
import string_parser
from App import App
from Course import Course
from meet_time import MeetTime

browser_session = requests.Session()

self_serve_portal_homepage_response = session_handler.get_self_portal_homepage(browser_session)
# Now we can start working on the schedule.



# Here we get all the matches to our regular expression. We need to parse them into "Semester" objects.

semesters = string_parser.parse_semesters(self_serve_portal_homepage_response)

# Populating courses in each semester
for semester in semesters:
    semesters_json_url = 'https://ssp.mycampus.ca/StudentRegistrationSsb/ssb/registrationHistory/reset?term=' + semester.code.__str__()

    response = browser_session.get(semesters_json_url)
    response_json = json.loads(response.text)
    courses = string_parser.parse_courses(response_json)





connection = sqlite3.connect(r"db.sqlite")
# Need to do error handling here in the future, but this will do for now to ensure we are connected to the database.
print(connection.total_changes)
cursor = connection.cursor()

#Create "default"

for app in default_apps.app_list:
    cursor.execute(app.get_sql_command())

print(connection.total_changes)
connection.commit()
connection.close()



