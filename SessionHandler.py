import requests
import StringParser
import secret


def get_self_portal_homepage(browser_session: requests.Session) -> requests.Response:
    login_page_url = 'https://ssp.mycampus.ca/StudentRegistrationSsb/ssb/registrationHistory/registrationHistory?mepCode=UOIT'

    response = browser_session.get(login_page_url)

    session_key = StringParser.parse_session_key(response.text)

    # Now we can login to the self-serve portal

    login_post_url = 'https://eidp.mycampus.ca/commonauth'
    self_serve_portal_homepage_response = browser_session.post(login_post_url, data={'username': secret.student_number,
                                                                                     'password': secret.password,
                                                                                     'sessionDataKey': session_key
                                                                                     }
                                                               )

    return self_serve_portal_homepage_response
