import json
import importlib.resources
def loadMealData(mealName):
    with importlib.resources.open_text("restoran.resources.mealData", mealName) as f:
        data = json.load(f)
    return data
def writeMealData(data, fileName):
    with importlib.resources.open_text("restoran.resources.mealData", mealName) as f:
        data = json.dump(f)