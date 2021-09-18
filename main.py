import json
import requests
import secret
import re

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
response = browser_session.post(login_post_url, data={'username': secret.student_number,
                                               'password': secret.password,
                                               'sessionDataKey': session_key
                                                      }
                                )

semesters_list_regex = '<option value="(\d+)" >([A-Za-z]+(?:(?:\/[A-Za-z]+ \d{4})|(?: \d{4})))'
