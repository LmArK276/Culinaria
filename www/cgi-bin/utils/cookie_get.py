from os import environ

def getCookie(cookieKey):
    cookies = str(environ.get('HTTP_COOKIE'))
    if cookies != None:
        for cookie in map(str.strip, cookies.split(";")):
            keyvalue = cookie.split("=")  
            if len(keyvalue) > 1:
                key = keyvalue[0]
                value = keyvalue[1]         
                if key == cookieKey:
                    return value
    return None