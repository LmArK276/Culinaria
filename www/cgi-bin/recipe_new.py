#!/usr/bin/env python3
import sys,os
sys.path.append(os.path.abspath("."))
sys.stdout.reconfigure(encoding='utf-8')

from utils.cookie_get import getCookie
from services.user_service import getUserBySessid
from models.user import User
from services.recipe_service import newRecipe
from models.recipe import Recipe
from utils.redirect import redirect
from utils.navbar import printNavbar

import html
import cgi
import pathlib
redirectURL = "http://localhost:8000/cgi-bin/main_page.py"

sessionCookieValue = getCookie("SESSID")

print ("Content-type:text/html\r\n")    


if(sessionCookieValue != None):
    user = getUserBySessid(sessionCookieValue)
    
    
    print("""
        <!DOCTYPE html>
        <html>

            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title>Add a new recipe</title>
                <meta name="description" content="">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                
                <script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>
                <link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">
                
                <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
                <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
                
                <link rel="icon" type="image/x-icon" href="../images/favicon.svg">
                <link rel="stylesheet" href="../main.css">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Signika+Negative&display=swap" rel="stylesheet">
                <link rel="stylesheet" href="../main.css">
            </head>
      
      """)
    
    printNavbar(user)
    
    print("""
        <body style="background-color: #e96b1b;">

                <div class="container py-5">
                    <div class="row d-flex justify-content-center align-items-center">
                    <div class="col col-xl-12">
                        <div class="card" style="border-radius: 1rem;">
                        <div class="row g-0 justify-content-center">
                            <div class="col-md-10 col-lg-10 d-flex align-items-center">
                            <div class="card-body p-5 p-lg-5 text-black">

                                <form action="recipe_new.py" method="post" enctype="multipart/form-data">

                                <h4 class="fw-normal mb-3 pb-1" style="letter-spacing: 1px;">Add a new recipe</h4>

                                <div class="form-outline mb-3">
                                    <label class="form-label" for="recipeName">Enter a name for your recipe:</label>
                                    <input type="text" name="name" class="form-control" required>
                                </div>

                                <div class="form-outline mb-3">
                                    <label class="form-label" for="recipeDescription">Enter a short description:</label>
                                    <input type="text" name="description" class="form-control" required>
                                </div>

                                <label>Describe the preparation steps: </label>
                                <div id="prepStepsEditor" class="mb-3"></div>
                                <input type="hidden" name="prepSteps" id="prepStepsOutput">

                                <label>List the ingredients needed here: </label>
                                <div id="ingredientsEditor" class="mb-3"></div>
                                <input type="hidden" name="ingredients" id="ingredientsOutput">

                                <div class="form-row mb-3">
                                    <div class="col">
                                      <label>What's the cooktime? </label>
                                      <input type="text" class="form-control" name="cooktime" required>
                                    </div>
                                    <div class="col">
                                      <label>How many people does the recipe serve? </label>
                                      <input type="number" class="form-control" name="servings" required min="1">
                                    </div>
                                  </div>
                                  
                                <div class="mb-3">
                                    <label class="form-label">Provide an image that describes your recipe:</label>
                                    <input class="form-control-file" type="file" name="image" accept="iamge/*" required>
                                </div>


                                <div class="pt-1 mb-4" data-aos="zoom-out">
                                    <input type="submit" class="btn btn-dark btn-lg btn-block" value="Save the recipe" name="newRecipe">
                                </div>

                                </form>

                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>

                    <script>
                        var prepStepsQuill = new Quill('#prepStepsEditor', {
                            modules: {
                            toolbar: [
                                ['bold', 'italic', 'underline', 'strike'],
                                [{ 'header': 1 }, { 'header': 2 }],
                                [{ 'list': 'ordered' }, { 'list': 'bullet' }],
                                [{ 'script': 'sub' }, { 'script': 'super' }],
                                [{ 'indent': '-1' }, { 'indent': '+1' }],
                                [{ 'direction': 'rtl' }],
                                [{ 'size': ['small', false, 'large', 'huge'] }],
                                [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
                                [{ 'color': [] }, { 'background': [] }],
                                [{ 'font': [] }],
                                [{ 'align': [] }],
                                ['clean']
                            ],
                            },
                            placeholder: "List the preparation steps here",
                            theme: 'snow'
                        });


                        var ingredientsQuill = new Quill('#ingredientsEditor', {
                            modules: {
                            toolbar: [
                                ['bold', 'italic', 'underline', 'strike'],
                                [{ 'header': 1 }, { 'header': 2 }],
                                [{ 'list': 'ordered' }, { 'list': 'bullet' }],
                                [{ 'script': 'sub' }, { 'script': 'super' }],
                                [{ 'indent': '-1' }, { 'indent': '+1' }],
                                [{ 'direction': 'rtl' }],
                                [{ 'size': ['small', false, 'large', 'huge'] }],
                                [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
                                [{ 'color': [] }, { 'background': [] }],
                                [{ 'font': [] }],
                                [{ 'align': [] }],
                                ['clean']
                            ],
                            },
                            placeholder: "List the ingredients here",
                            theme: 'snow'
                        });
                    </script>
                    
                    <script>
                        prepStepsQuill.on('text-change', function() {
                            document.getElementById('prepStepsOutput').value = prepStepsQuill.root.innerHTML;
                        });

                        ingredientsQuill.on('text-change', function(){
                            document.getElementById('ingredientsOutput').value = ingredientsQuill.root.innerHTML
                        })
                    </script>

                    <script>
                        AOS.init();
                    </script>

                </div>
          """)
    
    form = cgi.FieldStorage()

    if(form.getvalue('newRecipe')):
        
        
        image = form['image']
        imgName = None
        if image.filename:
            imgName = os.path.basename(image.filename)
            pathToSave = pathlib.Path(__file__).resolve().parents[1]/'user_images'/imgName
            open(pathToSave, 'wb').write(image.file.read())
            
        prepStepsEnc = html.escape(str(form.getvalue('prepSteps')))
        ingredientsEnc = html.escape(str(form.getvalue('ingredients')))
            
        recipeToAdd = Recipe(
                                None,
                                form.getvalue('name'),
                                form.getvalue('description'),
                                user.id,
                                prepStepsEnc,
                                ingredientsEnc,
                                imgName,
                                form.getvalue('cooktime'),
                                form.getvalue('servings')
                            )
        
        newRecipe(recipeToAdd)
    
        redirect(redirectURL)
            
    print("""
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                </body>
            </html>
        """)

    
else:
    redirect(redirectURL)

