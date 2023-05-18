import sys,os
sys.path.append(os.path.abspath("."))
sys.stdout.reconfigure(encoding='utf-8')

from services.user_service import getUserBySessid
from services.recipe_service import getRecipeById
from utils.cookie_get import getCookie
from utils.navbar import printNavbar

import cgi
import html

form = cgi.FieldStorage()

recipeID = form.getvalue("recipeID")
recipe = getRecipeById(recipeID)

print ("Content-type:text/html\r\n") 
sessid = getCookie("SESSID")

print("""
        <!DOCTYPE html>
        <html>
          
            <head>

                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title>{}</title>
                <meta name="description" content="">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="icon" type="image/x-icon" href="../images/favicon.svg">
                <link rel="stylesheet" href="../main.css">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Signika+Negative&display=swap" rel="stylesheet">
                <link rel="stylesheet" href="../main.css">
                
                
            </head>
            
            <body style="background-color: #e96b1b;">
      
      """.format(recipe.name))
user = None
if(sessid != None):
    user = getUserBySessid(sessid)


printNavbar(user)

pathToImage = "../user_images/{}".format(recipe.image)

unescapedPrepSteps = html.unescape(recipe.prepSteps)
unescapedIngredients = html.unescape(recipe.ingredients)

print("""
        <div class="container mt-5 rounded" style="background-color:#fffbde">
        
        <div class="row mt-3 mb-3 justify-content-center align-items-center">
            <div class="col-md-6 gy-0 px-0">
                <img class="img-fluid rounded-top-left-1" src='{}'>
            </div>
            
            <div class="col-md-6  justify-content-center">
                    <h1 class='font-weight-bold px-2 mb-3'>{}</h1>
                    <h5 class='font-weight-bold px-2 mb-3'>{}</h5>
            </div>
                     
        <div>
        <div class="row mt-3 justify-content-center">
        
            <div class="col-md-12 mb-2">
                <div class="text-align-center px-2 mx-2" style:"word-wrap:break-all">
                    {}
                </div>
            </div>
            
            <div class="col-md-12 mb-2">
                <div class="text-align-center px-2 mx-2" style:"word-wrap:break-all">
                    {}
                </div>
            </div>
        </div>    
        
        <div class="row mt-2 justify-content-center">
                <div class="col-md-6 mb-2 justify-content-center text-center">
                    <h5>This recipe takes {} to make. </h5>
                </div>
                
                <div class="col-md-6 mb-2 justify-content-center text-center">
                    <h5>This recipe serves {} people.</h5>
                </div>
        </div>
            
        


        
        """.format(pathToImage, recipe.name, recipe.description, unescapedIngredients, unescapedPrepSteps, recipe.cookTime, recipe.servings))


#Recipe rating

if(user != None):
    print("""
            <div class="row mt-2 mb-3 justify-content-center align-items-center">
                <div class="starRatingContainer d-flex align-items-center">
                    <div class="className">
                    </div>
                </div>
            </div>
            <div class="row mt-2 mb-3 justify-content-center align-items-center">
                <div id='recipeRate'>
                    <input type='hidden' value='0' class="ratingHolder" name='recipeRating' id='myRating'>
                    <button class='btn-lg' name='rate' value='Rate the recipe' onclick='sendRating()'>Rate the recipe</button>
                </div>
            </div>
          """)


print("""   
            </div>
         </div>
      
                <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
                <script>
                    function sendRating(){
                        
                        rating = document.getElementById('myRating').value
                        
                        let req = new XMLHttpRequest();
                        req.open("get", "recipe_rate.py?userID=%s&recipeID=%s&rating="+rating, true);
                        req.send();
                        req.onload = function () {
                            if (this.status == 200 && this.readyState == 4)
                            {       

                                if(this.responseText.trim() === 'success')
                                {
                                    Swal.fire(
                                        'Success',
                                        'You rated the recipe!',
                                        'success'
                                    )
                                }
                                else
                                {
                                    Swal.fire(
                                        'Sorry',
                                        'You have already rated this recipe',
                                        'error'
                                    )
                                }
                            }
                        }
                        

                    }
                </script>
      
      """%(user.id, recipeID))


print("""       
                <script src="../star_rating/index.js"></script>
                <script>
                        var properties1=[
                            {"rating":"1", "maxRating":"5", "minRating":"0.5", "readOnly":"no", "starImage":"../star_rating/star.png", "emptyStarImage":"../star_rating/starbackground.png", "starSize":"30", "step":"0.5"},
                        ];
                rateSystem('className', properties1, function(rating, ratingTargetElement){  ratingTargetElement.parentElement.parentElement.parentElement.getElementsByClassName("ratingHolder")[0].innerHTML = rating; document.getElementById('myRating').value = rating });
                
                
                </script>
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
            </body>
        </html>
      """)