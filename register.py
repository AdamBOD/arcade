#!/usr/local/bin/python3
from cgitb import enable 
enable()

from cgi import FieldStorage, escape
import pymysql as db

form_data = FieldStorage()
username = escape(form_data.getfirst("username", '').strip())
password = escape(form_data.getfirst("password", '').strip())

result = """"""
if len(form_data) > 0 :
    try:
        connection = db.connect('cs1dev.ucc.ie', 'ajbod1', 'eimaidae', 'users_ajbod1')
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT * 
                          FROM register 
                          WHERE username=%s """, (username))
        if cursor.rowcount == 0 :
            cursor.fetchall()
            cursor.execute("""INSERT INTO register (username, userpassword, role)
                              VALUES (%s, %s, 'user')""", (username, password))
            connection.commit()
            
            cursor.execute("""INSERT INTO snakestats (username, score)
                              VALUES (%s, 0)""", (username))
            connection.commit()
            
            cursor.execute("""INSERT INTO breakoutstats (username, score)
                              VALUES (%s, 0)""", (username))
            connection.commit()
            
            cursor.execute("""INSERT INTO easypongstats (username, score)
                              VALUES (%s, 0)""", (username))
            connection.commit()
            
            cursor.execute("""INSERT INTO mediumpongstats (username, score)
                              VALUES (%s, 0)""", (username))
            connection.commit()
            
            cursor.execute("""INSERT INTO hardpongstats (username, score)
                              VALUES (%s, 0)""", (username))
            connection.commit()
            
            cursor.execute("""INSERT INTO expertpongstats (username, score)
                              VALUES (%s, 0)""", (username))
            connection.commit()
            connection.close()                 
            result = """<p class="center">Successful registration. <a href="login.py">Click here</a></p>"""
        else :
            result = """<p class="center">Username is already in use</p>"""
    except db.Error :
        result = """<p class="center">Sorry! We are experiencing problems at the moment. Please call back later.</p>"""
else :
    result = """<p class="center">Form must be filled out</p>"""

print('Content-Type: text/html')
print()
print("""
        <html>
            <head>
                <title>Register</title>
                <link rel="stylesheet" type="text/css" href="project.css">
                <link rel="icon" type="image/png" href="logo.png">
            </head>
                <body>
                    <header><a href="index.py"><img src="logo.png" class="left"></a>Arcade</header>
                    <a href="index.py"><img src="Home.png" class="button"></a><a href="games.py"><img src="Game.png" class="button"></a><a href="stats.py"><img src="Stats.png" class="button"></a>
                    %s
                    <form method="POST">
                        <fieldset>
                        <legend>Register</legend>
                            <label for="username">Username</label><br>
                            <input type="text" placeholder="Username" id="username" name="username"><br>
                            <br><label for="password">Password</label><br>
                            <input type="password" placeholder="Password" id="password" name="password"><br>
                            <br><input type="submit" value="Register" id="register" alt="register"><br>
                            <p>Already have an account? Log in <a href="login.py">here</a>.</p><br>
                        </fieldset>
                    </form><br>         
                    <br><footer>
                        <p class="center">Copyright 2016 Adam Barry-O'Donovan</p>
                    </footer>
                </body>
        </html>""" % (result))
