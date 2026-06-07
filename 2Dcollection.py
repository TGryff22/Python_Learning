# 2dlist =  a list made of lists. Can also be tuples or sets

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats] # below is same thing, different look

groceries = [["apple", "orange", "banana", "coconut"],
            ["celery", "carrots", "potatoes"],
            ["chicken", "fish", "turkey"]]

# print(groceries[0][1]) # first number is list. seconds number is contents

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
