#!/usr/bin/env python3
import sys,os
sys.path.append(os.path.abspath("."))
sys.stdout.reconfigure(encoding='utf-8')

from utils.cookie_get import getCookie
from utils.cookie_set import setCookie
from services import user_service
from models.user import User
from utils.recipe_page import printRecipePage
from services.recipe_service import getLastPageNum
from utils.navbar import printNavbar



import cgi
#import cgitb

#cgitb.enable()

form = cgi.FieldStorage()

lastPage = getLastPageNum(3)




if(form.getvalue("pageNum")):
    currentPage = form.getvalue("pageNum")
    setCookie("lastVisitedPage", currentPage)
else:
    if(getCookie("lastVisitedPage") != None):
        currentPage = getCookie("lastVisitedPage")
    else:
        currentPage = 1



sessionCookieValue = getCookie("SESSID")

print ("Content-type:text/html\r\n")    
print("""
        <!DOCTYPE html>
        <html>
          
            <head>


                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            
                <title>Culinaria</title>
                <script src="../../pagination.js"></script>
                <script src="../../showRecipe.js"></script>
                <script src="../star_rating/index.js"></script>
                <link rel="icon" type="image/x-icon" href="../images/favicon.svg">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Signika+Negative&display=swap" rel="stylesheet">
                <link rel="stylesheet" href="../main.css">
            </head>
            
            <body style="background-color: #e96b1b;">
      """)

user:User = None
if(sessionCookieValue != None):
    user = user_service.getUserBySessid(sessionCookieValue)

printNavbar(user)    

print("""
      <div class="container mt-4">
        <div class="row justify-content-center">
            
      
      """)
    
printRecipePage(currentPage)

print("""
            
        </div>
        
      """)

#PAGINATION
print("""
        <div class="row justify-content-center fixed-bottom mt-2 mb-2">
        
            <div class="col-md-6 d-flex justify-content-end">
            <button class="btn-lg rounded" style="background-color:transparent; border-color:#fffbde" onclick = prevPage({})>
                <svg xmlns="http://www.w3.org/2000/svg" width="300" height="30" fill="#fffbde" class="bi bi-arrow-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
                </svg>
            </button>
            </div>
            
            <div class="col-md-6 d-flex justify-content-start">
            <button class="btn-lg rounded" style="background-color:transparent; border-color:#fffbde" onclick = nextPage({},{})>
                <svg xmlns="http://www.w3.org/2000/svg" width="300" height="30" fill="#fffbde" class="bi bi-arrow-right" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
                </svg>
            </button>
            </div>


      """.format(currentPage,currentPage,lastPage)) 
   
print("""      
            </div>
        </div>
    
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
            </body>
        </html>
      """)
