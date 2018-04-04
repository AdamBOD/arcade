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
            result = """<h1 class="snake">Snake Game</h1>
                <p class="snake">Use the directional arrows on your keyboard to direct your snake. Collect the food to extend your snake and win the game.</p>
                <main>
                <canvas height="500px" width="500px" id="snake"></canvas>
                </main><br>
                <div class="center">
                <p id="last"><a href="snake.py"><img src="Restart.png" class="restart"></a></p>
                </div>
                <br>"""
        else :
            navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
            result = """<p class="center">You must be logged in to play</p>"""

    else :
        navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""

else :
    navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
    result = """<p class="center">You must be logged in to play</p>"""
    
    
print('Content-Type: text/html')
print()
print("""
    <html>
        <head>
            <title>Snake</title>
            <link rel="stylesheet" type="text/css" href="project.css">
            <link rel="icon" type="image/png" href="logo.png">
            <script src="snake.js"></script>
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
