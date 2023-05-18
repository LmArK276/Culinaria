import sys,os
sys.path.append(os.path.abspath(".."))

from models.user import User
from pathlib import Path
from passlib import hash
import sqlite3
import random

dbPath = Path(__file__).resolve().parents[2]/"lite.db"
connection = sqlite3.connect(dbPath)
connection.row_factory = sqlite3.Row
#connection.set_trace_callback(print)
cursor = connection.cursor()

def register(user:User):
    passwordHash = hash.sha256_crypt.hash(user.password)
    sessid = str(int(random.random()*1e16))[:14]
    query = "INSERT OR IGNORE INTO user(email,username,password,sessid) VALUES (?,?,?,?) RETURNING sessid"
    data = (user.email,user.username,passwordHash,sessid)
    cursor.execute(query,data)
    row = cursor.fetchone()
    newUserSessid = row['sessid'] if row else None
    connection.commit()
    return newUserSessid

def login(email, password):
    query = "SELECT * FROM user WHERE email = ?"
    data = (email,)
    cursor.execute(query,data)
    res = cursor.fetchone()
    
    if(res == None):
        return False
    
    hashedPass = res['password']

    isValid = hash.sha256_crypt.verify(password, hashedPass)
    
    if(isValid):
        return res['sessid']
    else:
        return False


    
def getUserBySessid(sessid)->User:
    query = "SELECT * FROM user WHERE sessid = {}".format(sessid)
    cursor.execute(query)
    res = cursor.fetchone()
    
    if(res != None):
        rowData = res
        return User(rowData['id'],rowData['email'],rowData['username'],rowData['password'],rowData['sessid'])
    else:
        return False
    
