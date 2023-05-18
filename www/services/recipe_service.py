import sys,os
sys.path.append(os.path.abspath(".."))

from pathlib import Path
from models.recipe import Recipe
from models.rating import Rating
import sqlite3
from math import ceil


dbPath = Path(__file__).resolve().parents[2]/"lite.db"
connection = sqlite3.connect(dbPath)
connection.row_factory = sqlite3.Row
#connection.set_trace_callback(print)
cursor = connection.cursor()

def newRecipe(recipe:Recipe):
    query = "INSERT INTO recipe(name,description,prepSteps,ingredients,image,cookTime,servings,userID) VALUES (?,?,?,?,?,?,?,?)"
    data = (recipe.name, recipe.description, recipe.prepSteps, recipe.ingredients, recipe.image, recipe.cookTime, recipe.servings, recipe.userID)
    cursor.execute(query,data)
    connection.commit()
    
def getRecipesPage(pageSize, pageNum)->list[Recipe]:
    pageNum = int(pageNum)
    offset = (pageNum-1) * pageSize
    
    query = "SELECT * FROM recipe LIMIT ? OFFSET ?"
    data = (pageSize, offset)
    cursor.execute(query,data)
    if(cursor.rowcount == 0):    
        return False
    
    rows = cursor.fetchall()
    recipeList:list = []
    
    for row in rows:
        currRecipe = Recipe(
            row['id'],
            row['name'],
            row['description'],
            row['userID'],
            row['prepSteps'],
            row['ingredients'],
            row['image'],
            row['cookTime'],
            row['servings']
        )
        recipeList.append(currRecipe)
         
    return recipeList
    
def getRecipeById(recipeID)->Recipe:
    query = "SELECT * FROM recipe WHERE id=?"
    data = (recipeID,)
    cursor.execute(query,data)
    res = cursor.fetchone()
    
    return Recipe(
        res['id'],
        res['name'],
        res['description'],
        res['userID'],
        res['prepSteps'],
        res['ingredients'],
        res['image'],
        res['cookTime'],
        res['servings']
    )
    
def getLastPageNum(pageSize):
    countQuery = "SELECT count(*) FROM recipe"
    cursor.execute(countQuery)
    countRes = cursor.fetchone()
    numRows = countRes['count(*)']
    
    lastPage = ceil(numRows/pageSize)
    
    return lastPage

def rateRecipe(recipeID, userID, rating):
    checkExist = "SELECT * FROM rating WHERE userID={} AND recipeID={}".format(userID,recipeID)
    cursor.execute(checkExist)
    rows = cursor.fetchall()
    if(len(rows) > 0):
        print("fail")
        return False
    
    query = "INSERT INTO rating(userID,recipeID,rating) VALUES (?,?,?)"
    data = (userID,recipeID,rating)
    cursor.execute(query,data)
    connection.commit()
    print("success")
    
def getRecipesByUserID(userID)->list[Recipe]:
    query = "SELECT * FROM recipe WHERE userID=?"
    data = (userID,)
    cursor.execute(query,data)
    rows = cursor.fetchall()
    
    if (len(rows) == 0):
        return None
    else:
        recipeList = []
        for row in rows:
            currRecipe = Recipe(
                row['id'],
                row['name'],
                row['description'],
                row['userID'],
                row['prepSteps'],
                row['ingredients'],
                row['image'],
                row['cookTime'],
                row['servings']
            )
            recipeList.append(currRecipe)
            
        return recipeList
    
def deleteRecipeById(recipeID, imgName):
    query = "DELETE FROM recipe WHERE id = ?"
    data = (recipeID,)
    cursor.execute(query, data)
    connection.commit()
    if(imgName != None and imgName != "None"):
        imgPath = Path(__file__).resolve().parents[1]/"user_images"/imgName
        Path.unlink(imgPath)
    
def updateRecipe(updatedRecipe:Recipe):
    query = """UPDATE recipe
        SET name = ?,
            description = ?,
            prepSteps = ?,
            ingredients = ?,
            image = ?,
            cookTime = ?,
            servings = ?
        WHERE id = ?
    """
    data = (
        updatedRecipe.name,
        updatedRecipe.description,
        updatedRecipe.prepSteps,
        updatedRecipe.ingredients,
        updatedRecipe.image,
        updatedRecipe.cookTime,
        updatedRecipe.servings,
        updatedRecipe.id
    )
    cursor.execute(query,data)
    connection.commit()
    
def getRecipeRating(recipeID):
    query = "SELECT sum(rating)/count(rating) AS meanRating FROM rating WHERE recipeID=?"
    data = (recipeID,)
    cursor.execute(query,data)
    res = cursor.fetchone()
    if(res != None):
        meanRating = res['meanRating']
        return meanRating
    else:
        return 0
    