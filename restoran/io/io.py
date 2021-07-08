import json
import importlib.resources
import os
def loadMealData(mealName):
    with importlib.resources.open_text("restoran.resources.mealData", mealName + ".json") as f:
        data = json.load(f)
    return data
def writeMealData(data, mealName):
    with open(f"/home/krsmav/Faks/MIS/Projekat/restoran/resources/mealData/{mealName}.json", 'w') as f:
        json.dump(data, f)
    #with importlib.resources.open_text("restoran.resources.mealData", mealName + ".json") as f:
    #    json.dump(f)
def openDocs(docsName):
    with importlib.resources.open_binary("restoran.resources.docs", docsName) as f:
        path = f.name
    os.system(f"libreoffice --writer {path}")
if __name__ == "__main__":
    print(loadMealData('omlet'))