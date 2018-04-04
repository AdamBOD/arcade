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
            <title>Games</title>
            <link rel="stylesheet" type="text/css" href="project.css">
            <link rel="icon" type="image/png" href="logo.png">      
        </head>
        <body>
            <nav id="navbar">%s</nav>
            <header><a href="index.py"><img src="logo.png" class="left"></a>Arcade</header>
            <a href="index.py"><img src="Home.png" class="button"></a><a href="games.py"><img src="Game.png" class="button"></a><a href="stats.py"><img src="Stats.png" class="button"></a><a href="search.py"><img src="Search.png" class="search"></a>
            <p class="center"><a href="snake.py"><img src="Snake_icon.png" class="game"></a><a href="breakout.py"><img src="Breakout_icon.png" class="game"></a><a href="pongselect.py"><img src="Pong_icon.png" class="game"></a></p>
            <footer>
                <p class="center">Copyright 2016 Adam Barry-O'Donovan</p>
            </footer>
        </body>
    </html>""" % (navusername))
