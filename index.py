#!/usr/local/bin/python3

from cgitb import enable 
enable()

from os import environ
from shelve import open
from http.cookies import SimpleCookie

result = ""
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
        else :
            navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""

    else :
        navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
        
else :
    navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""

print('Content-Type: text/html')
print()
print("""
    <html>
        <head>
            <title>Home</title>
            <link rel="stylesheet" type="text/css" href="project.css">
            <link rel="icon" type="image/png" href="logo.png">      
        </head>
        <body>
            <nav id="navbar">%s</nav>
            <header><img src="logo.png" class="left">Arcade</header>
            <a href="index.py"><img src="Home.png" class="button"></a><a href="games.py"><img src="Game.png" class="button"></a><a href="stats.py"><img src="Stats.png" class="button"><a href="search.py"><img src="Search.png" class="search"></a>
            <fieldset class="welcome">
                <legend>Welcome</legend>
                <p>Welcome to my arcade. This site is full of classic arcade games. To be able to play any of these games you will need to either <a href="login.py">log in</a> or <a href="register.py">register</a>. The process is very simple and doesn't take long. (For tesing purposes the Username test and the Password test will work).</p>
            </fieldset><br>            
            <footer>
                <p class="center">Copyright 2016 Adam Barry-O'Donovan</p>
            </footer>
        </body>
    </html>""" % (navusername))
