import os


def generate_webpage(semester):
    name = semester.student_name

    def indent(repetition):
        str = ''
        for i in range(repetition):
            str += '\t'
        return str

    try:
        os.remove('index.html')
    except:
        print('Creating HTML File...')

    file = open('index.html', 'a')

    file.write("""<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<meta http-equiv="X-UA-Compatible" content="ie=edge" />
		<title>Home</title>
		<link rel="icon" href="favicon.ico" type="image/x-icon" />
		<link rel="stylesheet" href="style/reset.css" />
		<link rel="stylesheet" href="style/style.css" />
		<link rel="stylesheet" href="style/owfont-regular.min.css" />
		<link
			href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900"
			rel="stylesheet"
		/>
	</head>
	<body>
		<div id="title">
			<div id="date"></div>
			<h1>
				""")

    file.write(str.upper(name) + "'s ~")
    file.write("""
			</h1>
		</div>
		<div id="bookmarks">
			<h1>
			</h1>
			<div id="links">
				<ul>
					<li class="itemtitle"><a href="https://learn.ontariotechu.ca">Canvas</a></li>
					<li class="itemtitle"><a href="https://ontariotechu.ca/current-students/academics/mycampus.php">OntarioTech Software Portal</a></li>
					<li class="itemtitle"><a href="https://software.ontariotechu.ca/login.php">My Campus</a></li>
					<li class="itemtitle"><a href="https://mail.google.com">Gmail</a></li>
				</ul>
				<ul>
				</ul>
				<ul>
				</ul>""")
    for course in semester.courses:
        file.write("""
                <ul>        
					<li class="itemtitle">""" + course.course_title + """</li>""" + '\n' + "                    ")
        for course_component in course.course_components:
            if course_component.course_type == 'Lecture':
                file.write("""<li><a href=""" + course_component.url + """"">Lecture</a></li>
					""")
            if course_component.course_type == 'Lecture':
                file.write("""<li><a href=""" + course_component.url + """"">Tutorial</a></li>
					""")
            if course_component.course_type == 'Laboratory':
                file.write("""<li><a href=""" + course_component.url + """"">Lab</a></li>
				""")
        file.write("""</ul>""")
    file.write("""		<div id="weather">
			<h1 id="location"></h1>
			<div id="stats"></div>
		</div>
		<div id="eventlist">
			<h1 id="eventTitle">EVENTS</h1>
			<ul id="events"></ul>
		</div>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script src="js/script.js"></script>
		<script
			async
			defer
			src="https://maps.googleapis.com/maps/api/js?key=[googleAPI]&callback=initMap"
		></script>
	</body>
</html>
""")
    file.close()
