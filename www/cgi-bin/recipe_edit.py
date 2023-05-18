#!/usr/bin/env python3
import sys,os
sys.path.append(os.path.abspath("."))
sys.stdout.reconfigure(encoding='utf-8')

from utils.cookie_get import getCookie
from services.user_service import getUserBySessid
from services.recipe_service import updateRecipe
from services.recipe_service import getRecipeById
from models.recipe import Recipe
from utils.redirect import redirect
from utils.navbar import printNavbar


import html
import cgi
import pathlib
redirectURL = "http://localhost:8000/cgi-bin/my_recipes_page.py"

sessionCookieValue = getCookie("SESSID")



print ("Content-type:text/html\r\n")    

form = cgi.FieldStorage()

if(form.getvalue("recipeID") == None):
    redirect(redirectURL)


recipeToUpdate = getRecipeById(form.getvalue('recipeID'))

if(sessionCookieValue != None):
    print("""
        <!DOCTYPE html>
        <html>

            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title>Edit a recipe</title>
                <link rel="icon" type="image/x-icon" href="../images/favicon.svg">
                <meta name="description" content="">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                
                <script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>
                <link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">
                
                <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
                <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
                
                <link rel="stylesheet" href="../main.css">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Signika+Negative&display=swap" rel="stylesheet">
                <link rel="stylesheet" href="../main.css">
            </head>
            
            <body>
      
    """)
    
    user = getUserBySessid(sessionCookieValue)
    
    printNavbar(user)
    
    unescapedPrepSteps = html.unescape(str(recipeToUpdate.prepSteps).replace("&quot","&lsquo"))
    unescapedIngredients = html.unescape(str(recipeToUpdate.ingredients).replace("&quot","&lsquo"))
    
    
    
    print("""
        <body style="background-color: #e96b1b;">

                <div class="container py-5">
                    <div class="row d-flex justify-content-center align-items-center">
                    <div class="col col-xl-12">
                        <div class="card" style="border-radius: 1rem;">
                        <div class="row g-0 justify-content-center">
                            <div class="col-md-10 col-lg-10 d-flex align-items-center">
                            <div class="card-body p-5 p-lg-5 text-black">

                                <form action="recipe_edit.py" method="post" enctype="multipart/form-data">

                                <h4 class="fw-normal mb-3 pb-1" style="letter-spacing: 1px;">Edit the recipe</h4>
                                
                                <input type='hidden' name='recipeID' value='{}'>

                                <div class="form-outline mb-3">
                                    <label class="form-label" for="recipeName">Change the name of your recipe:</label>
                                    <input type="text" name="name" class="form-control" value='{}'>
                                </div>

                                <div class="form-outline mb-3">
                                    <label class="form-label" for="recipeDescription">Change the description:</label>
                                    <input type="text" name="description" class="form-control" value='{}'>
                                </div>

                                <label>Change the preparation steps: </label>
                                <div id="prepStepsEditor" class="mb-3">{}</div>
                                <input type="hidden" name="prepSteps" id="prepStepsOutput" value="{}">

                                <label>Change the ingredients needed: </label>
                                <div id="ingredientsEditor" class="mb-3">{}</div>
                                <input type="hidden" name="ingredients" id="ingredientsOutput" value="{}">

                                <div class="form-row mb-3">
                                    <div class="col">
                                      <label>Change the cooktime: </label>
                                      <input type="text" class="form-control" name="cooktime" value='{}'>
                                    </div>
                                    <div class="col">
                                      <label>Change the number of servings: </label>
                                      <input type="text" class="form-control" name="servings" value='{}'>
                                    </div>
                                  </div>
                                  
                                <label>Current image:</label><br>
                                <img class="img-thumbnail mb-3" src='../user_images/{}' width="250" height="250"><br>
                                  
                                <div class="mb-3">
                                    <label class="form-label">Change the image of your recipe:</label>
                                    <input class="form-control-file" type="file" name="image" accept="image/*">
                                </div>


                                <div class="pt-1 mb-4" data-aos="zoom-out">
                                    <input type="submit" class="btn btn-dark btn-lg btn-block" value="Save changes" name="saveChanges">
                                </div>

                                </form>

                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>
          """.format(
              recipeToUpdate.id,
              recipeToUpdate.name,
              recipeToUpdate.description,
              unescapedPrepSteps,
              unescapedPrepSteps,
              unescapedIngredients,
              unescapedIngredients,
              recipeToUpdate.cookTime,
              recipeToUpdate.servings,
              recipeToUpdate.image
          ))
    
    
    print("""
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
          
          """)

    if(form.getvalue('saveChanges')):

        #TODO srediti da imena slika budu unique
        oldImagePath = pathlib.Path(__file__).resolve().parents[1]/"user_images"/recipeToUpdate.image
        #pathlib.Path.unlink(oldImagePath)
        
        image = form['image']
        imgName = None
        if image.filename:
            imgName = os.path.basename(image.filename)
            pathToSave = pathlib.Path(__file__).resolve().parents[1]/'user_images'/imgName
            open(pathToSave, 'wb').write(image.file.read())
            
        
        if(imgName == None):
            imgName = recipeToUpdate.image    
        
        prepStepsEnc = html.escape(str(form.getvalue('prepSteps')))
        ingredientsEnc = html.escape(str(form.getvalue('ingredients')))
        
        update = Recipe(
                        form.getvalue('recipeID'),
                        form.getvalue('name'),
                        form.getvalue('description'),
                        user.id,
                        prepStepsEnc,
                        ingredientsEnc,
                        imgName,
                        form.getvalue('cooktime'),
                        form.getvalue('servings')
                    )
        
        updateRecipe(update)
        
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
