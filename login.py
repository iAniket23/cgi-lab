import cgi
import secret
from http import cookies

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

if username == secret.username and password == secret.password:
    print(f"Set-Cookie: username = {username}\r\nSet-Cookie: password = {password}")