#!/usr/local/bin/python3

from cgitb import enable 
enable()

from os import environ
from shelve import open
from http.cookies import SimpleCookie

print('Content-Type: text/html')
print()

result = '<p class="center">You are already logged out</p>'
try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sessid/sess_' + sid, writeback=True)
            session_store['authenticated'] = False
            session_store.close()
            result = """
                <p class="center">You have now logged out.</p>
                <p class="center"><a href="login.py">Login again</a></p>"""
except IOError:
    result = '<p class="center">Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <html>
        <head>
            <title>Home</title>
            <link rel="stylesheet" type="text/css" href="project.css">
            <link rel="icon" type="image/png" href="logo.png">      
        </head>
        <body>
            <header><img src="logo.png" class="left">Arcade</header>
            <a href="index.py"><img src="Home.png" class="button"></a><a href="games.py"><img src="Game.png" class="button"></a><a href="stats.py"><img src="Stats.png" class="button"></a>
            %s         
            <footer>
                <p class="center">Copyright 2016 Adam Barry-O'Donovan</p>
            </footer>
        </body>
    </html>""" % (result))
