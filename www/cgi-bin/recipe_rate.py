import sys,os
sys.path.append(os.path.abspath("."))
sys.stdout.reconfigure(encoding='utf-8')

from services.recipe_service import rateRecipe
from utils.cookie_get import getCookie
from utils.redirect import redirect
import cgi

req = cgi.FieldStorage()

print ("Content-Type: text/html\r\n\r\n")

if(getCookie("SESSID") == None):
    redirect()

rateRecipe(int(req.getvalue('recipeID')),int(req.getvalue('userID')),float(req.getvalue('rating')))