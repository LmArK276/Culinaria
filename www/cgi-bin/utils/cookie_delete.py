def deleteCookie(key):
    print ('HTTP/2.0 200 OK')
    print ("Set-Cookie:{} = deleted; Expires = Wed, 28 Aug 2013 18:30:00 GMT;Path = /".format(key))