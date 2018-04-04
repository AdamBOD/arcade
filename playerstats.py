#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage, escape
import pymysql as db
from os import environ
from shelve import open
from http.cookies import SimpleCookie
            
print('Content-Type: text/html')
print()

result = ''
navusername = ""
getusername = ""
snaketable = ""
snakeresult = ""
breakouttable = ""
breakoutresult = ""
easytable = ""
easyresult = ""
mediumtable = ""
mediumresult = ""
hardtable = ""
hardresult = ""
experttable = ""
expertresult = ""
form_data = FieldStorage()
playername = form_data.getfirst("playername")

cookie = SimpleCookie()
http_cookie_header = environ.get('HTTP_COOKIE')
if http_cookie_header:
    cookie.load(http_cookie_header)
    if 'sid' in cookie:
        sid = cookie['sid'].value
        session_store = open('sessid/sess_' + sid, writeback=False)
        if session_store.get('authenticated'):
            getusername = session_store.get('username')
            if session_store.get('role') == 'admin' :
                navusername = """<div class="drop"><button id="navbarbutton">%s</button><div class="droplinks"><a href="admin.py">Admin</a><a href="personalstats.py">Stats</a><a href="logout.py">Log out</a></div></div>""" % (getusername)
            else :
                navusername = """<div class="drop"><button id="navbarbutton">%s</button><div class="droplinks"><a href="personalstats.py">Stats</a><a href="logout.py">Log out</a></div></div>""" % (getusername)
        else :
            navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
    else :
        navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
else :
    navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
if len(form_data) > 0 :
    try:
        connection = db.connect('cs1dev.ucc.ie', 'ajbod1', 'eimaidae', 'users_ajbod1')
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT *
                          FROM register
                          WHERE username=%s""" , (playername))
        if cursor.rowcount > 0 :
            cursor.execute("""SELECT username, score 
                              FROM snakestats 
                              WHERE username=%s""" , (playername))
            snaketable = """<h1 class="center">%s's Snake stats</h1>""" % (playername)
            snakeresult = '<table><tr><th>Username</th><th>Score</th></tr>'
            for row in cursor.fetchall():
                snakeresult += '<tr><td>%s</a></td><td>%i</td></tr>' % (row['username'], row['score'])
            snakeresult += '</table>'

            cursor.execute("""SELECT username, score 
                              FROM breakoutstats 
                              WHERE username=%s""" , (playername))
            breakouttable = """<h1 class="center">%s's Breakout stats</h1>""" % (playername)
            breakoutresult = '<table><tr><th>Username</th><th>Score</th></tr>'
            for row in cursor.fetchall():
                breakoutresult += '<tr><td>%s</a></td><td>%i</td></tr>' % (row['username'], row['score'])
            breakoutresult += '</table>'

            cursor.execute("""SELECT username, score 
                              FROM easypongstats 
                              WHERE username=%s""" , (playername))
            easytable = """<h1 class="center">%s's Easy Single Pong stats</h1>""" % (playername)
            easyresult = '<table><tr><th>Username</th><th>Score</th></tr>'
            for row in cursor.fetchall():
                easyresult += '<tr><td>%s</a></td><td>%i</td></tr>' % (row['username'], row['score'])
            easyresult += '</table>'

            cursor.execute("""SELECT username, score 
                              FROM mediumpongstats 
                              WHERE username=%s""" , (playername))
            mediumtable = """<h1 class="center">%s's Medium Single Pong stats</h1>""" % (playername)
            mediumresult = '<table><tr><th>Username</th><th>Score</th></tr>'
            for row in cursor.fetchall():
                mediumresult += '<tr><td>%s</a></td><td>%i</td></tr>' % (row['username'], row['score'])
            mediumresult += '</table>'

            cursor.execute("""SELECT username, score 
                              FROM hardpongstats 
                              WHERE username=%s""" , (playername))
            hardtable = """<h1 class="center">%s's Hard Single Pong stats</h1>""" % (playername)
            hardresult = '<table><tr><th>Username</th><th>Score</th></tr>'
            for row in cursor.fetchall():
                hardresult += '<tr><td>%s</a></td><td>%i</td></tr>' % (row['username'], row['score'])
            hardresult += '</table>'

            cursor.execute("""SELECT username, score 
                              FROM expertpongstats 
                              WHERE username=%s""" , (playername))
            experttable = """<h1 class="center">%s's Expert Single Pong stats</h1>""" % (playername)
            expertresult = '<table><tr><th>Username</th><th>Score</th></tr>'
            for row in cursor.fetchall():
                expertresult += '<tr><td>%s</a></td><td>%i</td></tr>' % (row['username'], row['score'])
            expertresult += '</table>'
        else :
            snaketable = """<p class="center">You must enter a valid username</p>"""
        cursor.close()  
        connection.close()
    except db.Error:
        result = """<p class="center">Sorry! We are experiencing problems at the moment. Please call back later.</p>"""
else :
    snaketable = """<p class="center">You must enter a valid username</p>"""
print("""
        <html>
        <head>
            <title>Breakout Stats</title>
            <link rel="stylesheet" type="text/css" href="project.css">
            <link rel="icon" type="image/png" href="logo.png">
        </head>
        <body>
            <nav id="navbar">%s</nav>
            <header><a href="index.py"><img src="logo.png" class="left"></a>Arcade</header>
            <a href="index.py"><img src="Home.png" class="button"></a><a href="games.py"><img src="Game.png" class="button"></a><a href="stats.py"><img src="Stats.png" class="button"></a><a href="search.py"><img src="Search.png" class="search"></a>
            %s %s %s %s %s %s %s %s %s %s %s %s
        <footer>
                <p class="center">Copyright 2016 Adam Barry-O'Donovan</p>
            </footer>
        </body>
</html>""" % (navusername, snaketable, snakeresult, breakouttable, breakoutresult, easytable, easyresult, mediumtable, mediumresult, hardtable, hardresult, experttable, expertresult))
