#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage, escape
from hashlib import sha256
import pymysql as db
from http.cookies import SimpleCookie
from shelve import open
from time import time

form_data = FieldStorage()
username = escape(form_data.getfirst("username", '').strip())
password = escape(form_data.getfirst("password", '').strip())
result = """"""

if len(form_data) > 0 :
    #try:
    connection = db.connect('cs1dev.ucc.ie', 'ajbod1', 'eimaidae', 'users_ajbod1')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT * 
                      FROM register 
                      WHERE username=%s AND userpassword=%s """, (username, password))
    
    if cursor.rowcount > 0:
        cookie = SimpleCookie()
        sid = sha256(repr(time()).encode()).hexdigest()
        cookie['sid'] = sid
        session_store = open('sessid/sess_' + sid, writeback=True)
        session_store['authenticated'] = True
        session_store['username'] = username

        cursor.execute("""SELECT role
                          FROM register 
                          WHERE username=%s """, (username))
        role = cursor.fetchall()
        session_store['role'] = role[0]['role']
        session_store.close()
        result = """<p class="center">Successful login. <a href="index.py">Click here</a></p>"""
        print(cookie)
    else :
        result = """<p class="center">Invalid Login</p>"""
    cursor.close()  
    connection.close()
    #except db.Error:
        #result = """<p class="center">Sorry! We are experiencing problems at the moment. Please call back later.</p>"""

print('Content-Type: text/html')
print()
print("""
        <html>
            <head>
                <title>Login</title>
                <link rel="stylesheet" type="text/css" href="project.css">
                <link rel="icon" type="image/png" href="logo.png">
            </head>
            <body id="bodylogin">
                <header><a href="index.py"><img src="logo.png" class="left"></a>Arcade</header>
                <a href="index.py"><img src="Home.png" class="button"></a><a href="games.py"><img src="Game.png" class="button"></a><a href="stats.py"><img src="Stats.png" class="button"></a>
                %s
                <form method="POST">
                    <fieldset>
                    <legend>Login</legend>
                    <label for="username">Username</label><br>
                    <input type="text" placeholder="Username" id="username" name="username"><br>
                    <br><label for="password">Password</label><br>
                     <input type="password" placeholder="Password" id="password" name="password"><br>
                    <br><input type="submit" value="Login" id="login" alt="login"><br>
                    <p>Don't already have an account? Sign up <a href="register.py">here</a>.</p><br>
                    </fieldset>
                </form><br>                
            <br><footer>
                    <p class="center">Copyright 2016 Adam Barry-O'Donovan</p>
                </footer>
            </body>
    </html>""" % (result))
