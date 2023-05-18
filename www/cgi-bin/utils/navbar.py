import sys,os
sys.path.append(os.path.abspath(".."))

from services.recipe_service import getRecipesPage
from services.recipe_service import getRecipeRating
from models.user import User


def printNavbar(user:User):
    myPath = os.environ['SCRIPT_NAME']
    
    
    print("""
        <nav class="navbar navbar-expand-sm sticky-top navbar-light background-light mb-0">
            <div class="d-flex flex-grow-1">
                <span class="w-100 d-lg-none d-block"><!-- hidden spacer to center brand on mobile --></span>
                <a class="navbar-brand" href="main_page.py">
                    <img src="../images/logo-no-background.svg" width="300" height="50" >
                </a>
                <div class="w-100 text-right">
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#myNavbar7">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                </div>
            </div>
            <div class="collapse navbar-collapse flex-grow-1 text-right" id="myNavbar7">
                <ul class="navbar-nav ml-auto flex-nowrap">
        """)
    
    
    if(user == None):
        if(myPath.endswith("login.py")):
            print("""
                            <li class="nav-item active">
                                <a href="user_login.py" class="nav-link">Login</a>
                            </li>
                """)
        else:
            print("""
                            <li class="nav-item">
                                <a href="user_login.py" class="nav-link">Login</a>
                            </li>
                """)
        
        if(myPath.endswith("register.py")):
            print("""
                            <li class="nav-item active">
                                <a href="user_register.py" class="nav-link">Register</a>
                            </li>
                """)
        else:
            print("""
                            <li class="nav-item">
                                <a href="user_register.py" class="nav-link">Register</a>
                            </li>
                """)
        print("")
        
    else:
        print("""
                <div class="btn-group">
                    <button class="btn dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
                            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3Zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"/>
                        </svg> {}
                    </button>
              
              
              """.format(user.username))
        
        
        print("""
                <div class="dropdown-menu dropdown-menu-right"> 
            """)
        
        
        if(myPath.endswith("recipe_new.py")):
            print("""     
                    <a href="recipe_new.py" class="dropdown-item active">New recipe</a>        
                """)
        else:
            print("""
                    <a href="recipe_new.py" class="dropdown-item">New recipe</a>
                """)
        
        if(myPath.endswith("my_recipes_page.py")):
            print("""

                    <a href="my_recipes_page.py" class="dropdown-item active">My recipes</a>

                """)
        else:
            print("""
                    <a href="my_recipes_page.py" class="dropdown-item">My recipes</a>
                """)
            
        print("""
              
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="user_logout.py">Logout</a>
              
              """)        
    
        print("""
                    </div>
                </div>
              
              """)
    
    
    print("""
                </ul>
            </div>
        </nav>
          """)