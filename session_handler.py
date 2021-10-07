import json

import requests
import parsing_handler
import secret


def get_self_portal_homepage(browser_session: requests.Session) -> requests.Response:
    try:
        open('secret.py')
        student_number = secret.student_number
        password = secret.password
    except:
        FileNotFoundError
        student_number = input('Please enter your Student Number: ')

        # password = pwinput.pwinput("Please enter your MyCampus Password")

        password = input('Please enter your password')

    login_page_url = 'https://ssp.mycampus.ca/StudentRegistrationSsb/ssb/registrationHistory/registrationHistory?mepCode=UOIT'

    response = browser_session.get(login_page_url)

    session_key = parsing_handler.parse_session_key(response.text)

    # Now we can login to the self-serve portal

    login_post_url = 'https://eidp.mycampus.ca/commonauth'
    self_serve_portal_homepage_response = browser_session.post(login_post_url, data={'username': student_number,
                                                                                     'password': password,
                                                                                     'sessionDataKey': session_key
                                                                                     }
                                                               )

    return self_serve_portal_homepage_response
