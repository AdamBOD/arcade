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
            try:
                connection = db.connect('cs1dev.ucc.ie', 'ajbod1', 'eimaidae', 'users_ajbod1')
                cursor = connection.cursor(db.cursors.DictCursor)
                cursor.execute("""SELECT * 
                                  FROM hardpongstats 
                                  WHERE username=%s""" , (getusername))
                result = '<table><tr><th>Username</th><th>Score</th></tr>'
                for row in cursor.fetchall():
                    result += '<tr><td>%s</td><td>%i</td></tr>' % (row['username'], row['score'])
                result += '</table>'
                cursor.close()  
                connection.close()
            except db.Error:
                result = """<p class="center">Sorry! We are experiencing problems at the moment. Please call back later.</p>"""
        else :
            navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
            result = """<p class="center">You must be logged in to view this page</p>"""

    else :
        navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
    
else :
    navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
    result = """<p class="center">You must be logged in to view this page</p>"""
    

print("""
        <html>
        <head>
            <title>Personal Hard Pong Stats</title>
            <link rel="stylesheet" type="text/css" href="project.css">
            <link rel="icon" type="image/png" href="logo.png">
        </head>
        <body>
            <nav id="navbar">%s</nav>
            <header><a href="index.py"><img src="logo.png" class="left"></a>Arcade</header>
            <a href="index.py"><img src="Home.png" class="button"></a><a href="games.py"><img src="Game.png" class="button"></a><a href="stats.py"><img src="Stats.png" class="button"></a><a href="search.py"><img src="Search.png" class="search"></a>
            %s
        <footer>
                <p class="center">Copyright 2016 Adam Barry-O'Donovan</p>
            </footer>
        </body>
</html>""" % (navusername, result))
