'''
collections = single "variable" used to store multiple values
    List = [] oredered and changeable. Duplicates OK
    Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
    Tuple = () ordered and unchangeable. Duplicates OK. FASTER
'''

# fruits = ["apple", "orange", "banana", "coconut"] # list

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))

# print(fruits)
# print(fruits[:3])
# print(fruits[::2])
# print(fruits[::-1])

# for fruit in fruits:
    # print(fruit)

# fruits = {"apple", "orange", "banana", "coconut"} # set. no indexing because unordered

# fruits.add("pineapple")
# fruits.remove("coconut")
# fruits.pop()
# fruits.clear()

# print(fruits)

fruits = ("apple", "orange", "banana", "coconut") # tuple

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))
# print(fruits.count("coconut"))
for fruit in fruits:
    print(fruit)