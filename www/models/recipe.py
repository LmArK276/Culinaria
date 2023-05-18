class Recipe():
    def __init__(self, id, name, description, userID, prepSteps, ingredients, image, cookTime, servings) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.userID = userID
        self.prepSteps = prepSteps
        self.ingredients = ingredients
        self.image = image
        self.cookTime = cookTime
        self.servings = servings