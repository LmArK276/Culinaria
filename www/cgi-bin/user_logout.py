from utils.cookie_delete import deleteCookie
from utils.redirect import redirect

deleteCookie("SESSID")
deleteCookie("lastVisitedPage")

redirectURL = "http://localhost:8000/cgi-bin/main_page.py"

print ("Content-type:text/html\r\n")
redirect(redirectURL)