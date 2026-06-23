# function = A  block of reusable code
#            place () after the function name to call it
'''
def happy_birthday(name, age): # position of the parameters matters
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print()

happy_birthday("Bro", 20)
happy_birthday("Joe", 30)
happy_birthday("Mike", 35)
'''

# return = A function can return a value back to the caller
'''
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))
'''
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("tee", "gee")

print(full_name)