def setCookie(key, value):
    print ('HTTP/2.0 200 OK')
    print ("Set-Cookie:{} = {}; Path = /".format(key,value))