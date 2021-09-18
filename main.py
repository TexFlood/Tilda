import requests
import secret
import re
from Semester import Semester

uuid_regex = 'sessionDataKey=(\w{8}.\w{4}.\w{4}.\w{4}.\w{12})'

browser_session = requests.Session()
# preauth = 'http://portal.mycampus.ca/cp/home/login'
# response = requests.post(preauth, data={'username': secret.student_number,
#                                         'password': secret.password,
#                                         'uuid': secret.uuid
#                                         }
#                          )

# Let's start with getting our session I.D.
next_url = 'https://ssp.mycampus.ca/StudentRegistrationSsb/ssb/registrationHistory/registrationHistory?mepCode=UOIT'
response = browser_session.get(next_url)
response_text = response.text

session_key = re.search(uuid_regex, response_text).group(1)

# Now we can login to the self-serve portal

login_post_url = 'https://eidp.mycampus.ca/commonauth'
self_serve_portal_homepage_response = browser_session.post(login_post_url, data={'username': secret.student_number,
                                               'password': secret.password,
                                               'sessionDataKey': session_key
                                                      }
                                )

# Now we can start working on the schedule.

# This RegEx will return a few groups. The RegEx essentially says find me something that looks like this (for example
# each capture group will be between ***):

# <option value="***201909***" >***Fall 2019***</option>
# <option value="***202001***" >***Winter 2020***</option>
# <option value="***202005***" >***Spring/Summer 2020***</option>
# <option value="***202009***" >***Fall 2020***</option>
# <option value="***202101***" >***Winter 2021***</option>
# <option value="***202105***" >***Spring/Summer 2021***</option>
# <option value="***202109***" >***Fall 2021***</option>

semesters_list_regex = '<option value="(\d+)" >([A-Za-z]+(?:(?:\/[A-Za-z]+ \d{4})|(?: \d{4})))'

# Here we get all the matches to our regular expression. We need to parse them into "Semester" objects.
re_matches = re.findall(semesters_list_regex,self_serve_portal_homepage_response.text)
semesters = []
print(type(re_matches))
for i in re_matches:
    temp_sem = Semester(i[0],i[1])
    semesters.append(temp_sem)
sorted(semesters)


