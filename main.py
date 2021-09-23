import json
import sqlite3
import os
import requests
import default_apps
import session_handler
import parsing_handler

from app import app
from Course import Course
from meet_time import MeetTime
try:
    os.remove("db.sqlite")
except FileNotFoundError:
    print("Creating database...")

browser_session = requests.Session()

self_serve_portal_homepage_response = session_handler.get_self_portal_homepage(browser_session)
# Now we can start working on the schedule.
# Here we get all the matches to our regular expression. We need to parse them into "Semester" objects.

#
#
# connection = sqlite3.connect(r"db.sqlite")
#
# connection.execute("CREATE TABLE `apps` (`id` INTEGER PRIMARY KEY, `name` VARCHAR(255) NOT NULL, `url` VARCHAR(255) NOT NULL, `icon` VARCHAR(255) NOT NULL DEFAULT 'cancel', `isPinned` TINYINT(1) DEFAULT 0, `orderId` INTEGER DEFAULT NULL, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)")
# connection.execute("CREATE TABLE `bookmarks` (`id` INTEGER PRIMARY KEY, `name` VARCHAR(255) NOT NULL, `url` VARCHAR(255) NOT NULL, `categoryId` INTEGER NOT NULL, `icon` VARCHAR(255) DEFAULT '', `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)")
# connection.execute("CREATE TABLE `categories` (`id` INTEGER PRIMARY KEY, `name` VARCHAR(255) NOT NULL, `isPinned` TINYINT(1) DEFAULT 0, `orderId` INTEGER DEFAULT NULL, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)")
# connection.execute("CREATE TABLE `config` (`id` INTEGER PRIMARY KEY, `key` VARCHAR(255) NOT NULL UNIQUE, `value` VARCHAR(255) NOT NULL, `valueType` VARCHAR(255) NOT NULL, `isLocked` TINYINT(1) DEFAULT 0, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)")
# connection.execute("CREATE TABLE `weather` (`id` INTEGER PRIMARY KEY, `externalLastUpdate` VARCHAR(255), `tempC` FLOAT, `tempF` FLOAT, `isDay` INTEGER, `cloud` INTEGER, `conditionText` TEXT, `conditionCode` INTEGER, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL)")
# ## Create initial schema for sqlite database

# Populating courses in each semester
for semester in semesters:
    semesters_json_url = 'https://ssp.mycampus.ca/StudentRegistrationSsb/ssb/registrationHistory/reset?term=' + semester.code.__str__()

    response = browser_session.get(semesters_json_url)
    response_json = json.loads(response.text)
    courses = parsing_handler.parse_courses(response_json)
    semester.courses = courses








