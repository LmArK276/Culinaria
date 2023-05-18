#!/usr/bin/env python3
import sys,os
sys.path.append(os.path.abspath("."))


from services.user_service import login
from utils.cookie_set import setCookie
from utils.redirect import redirect
from utils.cookie_get import getCookie
from utils.navbar import printNavbar
import cgi




form = cgi.FieldStorage()
success = False
loginAtempted = False
if(form.getvalue("login")):
    res = login(form.getvalue("email"), form.getvalue("password"))
    loginAtempted = True
    if(res):
        setCookie("SESSID",res)
        success = True


redirectURL = "http://localhost:8000/cgi-bin/main_page.py"
print ("Content-type:text/html\r\n")

printNavbar(None)

if(getCookie("SESSID") != None):
    redirect(redirectURL)
    

print("""
      
      <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title>Login</title>
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
                <div class="container py-5">
                    <div class="row d-flex justify-content-center align-items-center">
                    <div class="col col-xl-10">
                        <div class="card" style="border-radius: 1rem;">
                        <div class="row g-0">
                            <div class="col-md-6 col-lg-5 d-none d-md-block">
                            <img src="../images/bread-g0d60ba534_1920.jpg"
                                alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
                            </div>
                            <div class="col-md-6 col-lg-7 d-flex align-items-center">
                            <div class="card-body p-4 p-lg-5 text-black">

                                <form action="user_login.py" method="post">

                                <h4 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into your account</h4>

                                <div class="form-outline mb-4">
                                    <input type="email" name="email" class="form-control form-control-lg">
                                    <label class="form-label" for="form2Example17">Email address</label>
                                </div>

                                <div class="form-outline mb-4">
                                    <input type="password" name="password" class="form-control form-control-lg" />
                                    <label class="form-label" for="form2Example27">Password</label>
                                </div>

                                <div class="pt-1 mb-4">
                                    <input type="submit" class="btn btn-dark btn-lg btn-block" value="Login" name="login">
                                </div>

                                </form>

                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>


        
      """)



if(success):
    redirect(redirectURL)
else:
    if(loginAtempted):
        print("""
                <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
                <script>
                    Swal.fire({
                        
                            icon: 'error',
                            title: 'Wrong credentials',
                            text: 'Incorrect email or password',
                    })
                
                </script>
            """)
    
    
print("""
                
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
            </body>
        </html>
      
      """)