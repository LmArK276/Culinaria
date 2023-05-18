#!/usr/bin/env python3
import sys,os
sys.path.append(os.path.abspath("."))
sys.stdout.reconfigure(encoding='utf-8')

from utils.cookie_get import getCookie
from utils.redirect import redirect
from utils.navbar import printNavbar
from services import user_service
from models.user import User
from services.recipe_service import getRecipesByUserID
from services.recipe_service import deleteRecipeById

sessionCookieValue = getCookie("SESSID")

import cgi

form = cgi.FieldStorage()

print ("Content-type:text/html\r\n")    

if(form.getvalue('recipeID')):
    recipeToDeleteID = form.getvalue('recipeID')
    recipeToDeleteImageName = form.getvalue('imgName')
    deleteRecipeById(recipeToDeleteID, recipeToDeleteImageName)

user:User = None
if(sessionCookieValue != None):
    user = user_service.getUserBySessid(sessionCookieValue)
    print("""
        <!DOCTYPE html>
        <html>
          
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title>My recipes</title>
                <meta name="description" content="">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="icon" type="image/x-icon" href="../images/favicon.svg">
                <link rel="stylesheet" href="../main.css">
                <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Signika+Negative&display=swap" rel="stylesheet">
                <link rel="stylesheet" href="../main.css">
            </head>
            
            <body style="background-color: #e96b1b;">
      
      """)
    
    printNavbar(user)
    
else:
    redirect("http://localhost:8000/cgi-bin/main_page.py")
    
print("""
            
                <div class="container mt-5">
                    
      """)
    

userRecipes = getRecipesByUserID(user.id)


if(userRecipes != None):
    print("""
            <div class='card-columns mt-5'> 
          """)
    for recipe in userRecipes:
        pathToImage = "../user_images/{}".format(recipe.image)
        print("""
                <div class='card' data-aos="fade-up" data-aos-duration="1500">
                    <img class="card-img-top" src='{}' width="500"><br>
                    
                    <div class="card-body">
                    
                        <h4 class="card-title">{}</h4>
                        <p class="card-text">{}</p>
                        
                        <div class="row">
                            <div class="col-md-6">
                                <span onclick=ajaxDeleteRecipe('{}','{}') style="cursor:pointer">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                        <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                                        <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                                    </svg> Delete the recipe
                                </span>
                            </div>
                         
                            <div class="col-md-6">
                                <span onclick=editRecipe({}) style="cursor:pointer">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                                        <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                                        <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                                    </svg> Edit the recipe
                                </span>                             
                            </div>
                        </div>
                        

                        

                    
                    </div>
                </div>
            <div>
            """.format(pathToImage, recipe.name, recipe.description, recipe.id, recipe.image, recipe.id))
        
else:
    print("""
            <div class="row align-items-center justify-content-center">
                <div class="col-md-12 d-flex justify-content-center ">
                    <h1>You currently have no recipes posted!</h1>
                </div>
            </div>
          
          
          """)
   
   
print("""
                <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
                <script>

                    function ajaxDeleteRecipe(recipeID, imgName){
                        
                        Swal.fire({
                            
                            title: 'Do you want to delete this recipe?',
                            showDenyButton: true,
                            showCancelButton: true,
                            confirmButtonText: 'Delete',
                            denyButtonText: `Keep`,
                                    
                        }).then((result) => {
                            
                            if (result.isConfirmed) {
                                
                                var req = new XMLHttpRequest()
                                var postData = encodeURIComponent('recipeID') + '=' + encodeURIComponent(recipeID)+"&"
                                postData += encodeURIComponent('imgName') + '=' + encodeURIComponent(imgName)
                                
                                req.onload = function(){
                                    document.body.innerHTML = this.response
                                    Swal.fire('Deleted!', '', 'success')
                                }
                                
                                req.open("POST","my_recipes_page.py",true)
                                req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8')
                                req.send(postData)
                                
                            } else if (result.isDenied) {
                                
                                Swal.fire('Recipe kept', '', 'info')
                                
                            }
                        })
                        
                        
                        
   
                    }
                    
                    function editRecipe(recipeID){
                        window.location.href = "recipe_edit.py?recipeID="+recipeID
                    }

                </script>

                <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
                <script>
                    AOS.init();
                </script>
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
            </body>
        </html>
      """)