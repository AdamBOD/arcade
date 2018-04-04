#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage, escape
import pymysql as db
username = ""
score = ""

print('Content-Type: text/plain')
print()

form_data = FieldStorage()
username = form_data.getfirst('username')
score = int(form_data.getfirst('score'))

try :
    connection = db.connect('cs1dev.ucc.ie', 'ajbod1', 'eimaidae', 'users_ajbod1')
    cursor = connection.cursor(db.cursors.DictCursor)

    cursor.execute("""SELECT score
                        FROM breakoutstats
                        WHERE username=%s;""", (username))
    old_score = cursor.fetchall()
    print (old_score)

    if int(old_score[0]['score']) < score :
        cursor.execute("""UPDATE breakoutstats
                        SET score=%s
                        WHERE username=%s""", (score, username))
        connection.commit()

    print("success")
    cursor.close()  
    connection.close()
except db.Error :
    print("Error")
