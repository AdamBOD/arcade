#!/usr/local/bin/python3
from cgitb import enable 
enable()

from cgi import FieldStorage, escape
import pymysql as db

form_data = FieldStorage()
username = escape(form_data.getfirst("username", '').strip())

result = """"""

if len(form_data) > 0 :
    try:
        connection = db.connect('cs1dev.ucc.ie', 'ajbod1', 'eimaidae', 'users_ajbod1')
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT * 
                          FROM register 
                          WHERE username=%s """, (username))
        if cursor.rowcount == 1 :
            cursor.fetchall()
            cursor.execute("""DELETE FROM register 
                              WHERE username=%s""", (username))
            connection.commit()
            cursor.execute("""DELETE FROM snakestats 
                              WHERE username=%s""", (username))
            connection.commit()
            cursor.execute("""DELETE FROM breakoutstats 
                              WHERE username=%s""", (username))
            connection.commit()
            cursor.execute("""DELETE FROM easypongstats 
                              WHERE username=%s""", (username))
            connection.commit()
            cursor.execute("""DELETE FROM mediumpongstats 
                              WHERE username=%s""", (username))
            connection.commit()
            cursor.execute("""DELETE FROM hardpongstats 
                              WHERE username=%s""", (username))
            connection.commit()
            cursor.execute("""DELETE FROM expertpongstats 
                              WHERE username=%s""", (username))
            connection.commit()
            connection.close()                 
            result = """<p class="center">Successfully deleted user %s.</p>""" % (username)
            title= "User deleted"
        else :
            result = """<p class="center">User does not exist</p>"""
            title = "Invalid Username"
    except db.Error :
        result = """<p class="center">Sorry! We are experiencing problems at the moment. Please call back later.</p>"""
        title = "Experiencing issues"
else :
    result = """<p class="center">Form must be filled out</p>"""
    title = "Form must be completed"
    
print('Content-Type: text/html')
print()
print("""
        <html>
            <head>
                <title>%s</title>
                <link rel="stylesheet" type="text/css" href="project.css">
                <link rel="icon" type="image/png" href="logo.png">
            </head>
                <body>
                    <header><a href="index.py"><img src="logo.png" class="left"></a>Arcade</header>
                    <a href="index.py"><img src="Home.png" class="button"></a><a href="games.py"><img src="Game.png" class="button"></a><a href="stats.py"><img src="Stats.png" class="button"></a>
                    %s
                    <br>
                    <div class="center">
                        <p id="last"><a href="admin.py"><img src="Back.png" class="restart"></a></p>
                    </div>
                    <br><footer>
                        <p class="center">Copyright 2016 Adam Barry-O'Donovan</p>
                    </footer>
                </body>
        </html>""" % (title, result))
