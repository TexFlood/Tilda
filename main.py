import json
import requests
import secret
import re

uuid_regex = 'sessionDataKey=(\w{8}.\w{4}.\w{4}.\w{4}.\w{12})'


# Let's start with getting our session I.D.
next_url = 'https://ssp.mycampus.ca/StudentRegistrationSsb/ssb/registrationHistory/registrationHistory?mepCode=UOIT'
response = requests.get(next_url)
response = response.text
session_key = re.search(uuid_regex,response)
print(session_key.group(1))
#Now we must get session key.




