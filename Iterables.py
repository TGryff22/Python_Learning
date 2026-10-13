# Iterable = An object/collection capable of returning its members one at a time. 
#            allowing it to be iterated over in a for-loop.
'''
numbers = [1, 2, 3, 4, 5]

# for number in reversed(numbers):
    # print(number, end=" - ")

for number in numbers:
     print(number)
'''

'''
fruits = {"apple", "orange", "banana", "coconut"}

for fuit in reversed(fruits):  # You cannot reverse sets
    print(fruit)
'''

'''
name = "Tre Gryff"

for character in name:
    print(character, end=" ")
'''

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    # print(key, value)
    print(f"{key} = {value}")