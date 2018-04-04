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
                result = """<div class="admin">
                <form method="POST" action="changename.py">
                    <fieldset>
                    <legend>Change Username</legend>
                    <label for="oldusername">Old Username</label><br>
                    <input type="text" placeholder="Old Username" id="oldusername" name="oldusername"><br>
                    <br><label for="newusername">New Username</label><br>
                    <input type="text" placeholder="New Username" id="newusername" name="newusername"><br>
                    <br><input type="submit" value="Change"><br>
                    </fieldset>
                </form>
                <form method="POST" action="changepassword.py">
                    <fieldset>
                    <legend>Change Pasword</legend>
                    <label for="username">Username</label><br>
                    <input type="text" placeholder="Username" id="username" name="username"><br>
                    <br><label for="oldpassword">Old Password</label><br>
                    <input type="password" placeholder="Old Password" id="oldpassword" name="oldpassword"><br>
                    <br><label for="newpassword">New Password</label><br>
                    <input type="password" placeholder="New Password" id="newpassword" name="newpassword"><br>
                    <br><input type="submit" value="Change"><br>
                    </fieldset>
                </form><br>
                <form method="POST" action="deluser.py">
                    <fieldset>
                    <legend>Delete User</legend>
                    <label for="username">Username</label><br>
                    <input type="text" placeholder="Username" id="username" name="username"><br>
                    <br><input type="submit" value="Delete"><br>
                    </fieldset>
                </form>
                <form method="POST" action="changerole.py">
                    <fieldset>
                    <legend>Change user role</legend>
                    <label for="username">Username</label><br>
                    <input type="text" placeholder="Username" id="username" name="username"><br>
                    <br><label for="role">Role</label><br>
                    <input type="text" placeholder="Role" id="role" name="role"><br>
                    <br><input type="submit" value="Change"><br>
                    </fieldset>
                </form>        
            </div>    
        <br>"""
            else :
                navusername = """<div class="drop"><button id="navbarbutton">%s</button><div class="droplinks"><a href="personalstats.py">Stats</a><a href="logout.py">Log out</a></div></div>""" % (getusername)
                result = """<p class="center">You do not have sufficient priviledges to view this page</p>"""
        else :
            navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
            result = """<p class="center">You do not have sufficient priviledges to view this page</p>"""
    else :
        navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
else :
    navusername = """<div class="loginbutton"><a id="loginbutton" href="login.py">Login</a> or <a id="loginbutton" href="register.py">Register</a></div>"""
    result = """<p class="center">You do not have sufficient priviledges to view this page</p>"""
    
print('Content-Type: text/html')
print()
print("""
    <html>
        <head>
            <title>Admin</title>
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
