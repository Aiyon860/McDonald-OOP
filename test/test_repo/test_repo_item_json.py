import json

# Function to Print Out
def readAndPrintData(type):
    x = open("D:/ExpertProgrammer/Projects/Languages/Python/McDonalds_OOP/repo/JSON/menu.json")
    data = json.load(x)
    
    for y in data[type]:
        print(y)

    x.close()
    
# Breakfast
# readAndPrintData("Breakfast")

# Beef
# readAndPrintData("Beef")

# Chicken
# readAndPrintData("Chicken")

# Fish
# readAndPrintData("Fish")

# Beverage
# readAndPrintData("Beverage")

# Dessert
# readAndPrintData("Dessert")

# HappyMeal
# readAndPrintData("HappyMeal")

# FamilyMeal
# readAndPrintData("FamilyMeal")

# McCafe
# readAndPrintData("McCafe")

# Snack
# readAndPrintData("Snack")
