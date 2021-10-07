import random
import sys
import time

import os
options = '(Default: No) [Y]es/[N]o)'
def human_to_bool(input:str):
    if(input =='Yes' or 'yes' or 'y' or 'Y'):
        return True
    return False

def repeat_character(repetitions, character):
    string = ''
    for i in range(repetitions):
        string += character
    return string


def print_tilde(first_time):
    line = []
    header = (' \n\n\n\n')
    line.append(
        '             /&&%      (&%                      ....       ....                     ....                                      .&&&,\n ')
    line.append(
        '           .&&&,      (&%           *&&,       (& &*     /&&&(                     &&&&,                                     #&&(\n    ')
    line.append(
        '        %&&*       (&%          #&&&,       .,,,      /&&&(                     &&&&,                                    /&&#\n    ')
    line.append(
        '       (&&#                     #&&&,                 /&&&(                     &&&&,                                   ,&&&.\n    ')
    line.append(
        '      ,&&&.                  &&&&&&&&&&&*   (&&&*     /&&&(         *%&&&&&&&#, &&&&,         *%&&&&&&&&&(,             %&&*\n    ')
    line.append(
        '      &&&,                   ###&&&&%###,   (&&&*     /&&&(      .&&&&&%*../%&&&&&&&,      *&&&&&&%%%%&&&&&&%.         (&&(\n    ')
    line.append(
        '     #&&(                       #&&&,       (&&&*     /&&&(     /&&&&.         %&&&&,     (&&&&.         /&&&&(       *&&&.\n    ')
    line.append(
        '    ,&&%                        #&&&,       (&&&*     /&&&(    ,&&&%            &&&&,                     .&&&&,      %&&,\n    ')
    line.append(
        '   .&&&,                        #&&&,       (&&&*     /&&&(    /&&&(            /&&&,                      /&&&#     #&&/\n    ')
    line.append(
        '   #&&(                         #&&&,       (&&&*     /&&&(    /&&&(            /&&&,    /&&&&&&&&&&&&&&&&&&&&&#    /&&%\n    ')
    line.append(
        '  *&&%                          #&&&,       (&&&*     /&&&(    ,&&&%            %&&&,    .&&&%             %&&&,    &&&.\n    ')
    line.append(
        ' .&&&.                          #&&&,       (&&&*     /&&&(     *&&&&.         #&&&&,     *&&&%           #&&&/    %&&/\n    ')
    line.append(
        ' %&&/                           (&&&&(/#*   (&&&*     /&&&(      .%&&&&#/. *#&&&&&&&,      .%&&&&&%###%&&&&&%     /&&%\n    ')
    line.append(
        '&&#                             *&&&&&&%   (&&&*     /&&&(         *#&&&&&&&%* /&&&,         ,#&&&&&&&&&#,      .&&&     ')
    footer = ('\n\n' + '\n ' + repeat_character(45,
                                                ' ') + 'Welcome to Tilde, a place for your courses to call home. \n\n')
    print(header, end='')
    if(first_time == True):

        speed = 0.11
        for l in line:
            for character in l:
                if character == ' ':
                    sys.stdout.flush()
                    print(character, end='')
                    sys.stdout.flush()
                else:
                    print(character, end='')
                    sys.stdout.flush()
                    random_int = random.randint(0,10)
                    time.sleep(0.1*random_int*speed)
                    speed= speed * 0.9
                    sys.stdout.flush()
        print(footer)
    else:
        full_str=''
        for l in line:
            full_str+=l
def wants_webpage():
    os.system('cls')
    print_tilde(False)
    wants_webpage = human_to_bool(input('Do you want to generate a webpage?'+options))
    return(wants_webpage)
def wants_ical():
    wants_ical = input(
        'iCalendar files can be imported into calendar apps such as Google Calendar. \n\n\n Do you want to generate an iCalendar file? ' + options)
def wants_json():
    wants_json = input('A JSON file of your schedule can be generated from the program. Would you like to get the JSON file? This option mostly for developers.'+options)

def get_login_credentials():
    os.system('cls')
    print_tilde(False)
    time.sleep(2)
    login_credentials = []
    login_credentials.append(human_to_bool(input('Please enter your banner ID (Student Number): ')))
    login_credentials.append(human_to_bool(input('Please enter your MyCampus password: ')))
    return login_credentials

def prompt_lecture_url(course_title):
    print_tilde(False)
    url = input('Please enter the lecture link (Google Meet, Zoom, Kaltura, BigBlueButton,etc) for ' + course_title)
    return url

def prompt_tutorial_url(course_title):
    os.system('cls')
    print_tilde(False)
    url = input('Please enter the tutorial link (Google Meet, Zoom, Kaltura, BigBlueButton,etc) for ' + course_title)
    return url

def prompt_lab_url(course_title):
    os.system('cls')
    print_tilde(False)
    url = input('Please enter the  link (Google Meet, Zoom, Kaltura, BigBlueButton,etc) for ' + course_title)
    return url

def confirm_authentication():
    return('Login Successful')




