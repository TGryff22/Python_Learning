''' 
Typecasting is the process of converting a variable from one data type to another. In 
Python, you can use the built-in functions int(), float(), str(), and bool() to typecast variables.
'''

name = "Tre"
age = 100
gpa = 3.5
is_purple = True

print(type(name)) # Output: <class 'str'>
print(type(age)) # Output: <class 'int'>
print(type(gpa)) # Output: <class 'float'>
print(type(is_purple)) # Output: <class 'bool'>
print(" ")

# Converting

# Float to Integer
gpa = int(gpa)

print(gpa) # Output: 3
print(type(gpa)) # Output: <class 'int'>
print(" ")

# Integer to Float
age =float(age)

print(age) # Output: 100.0
print(type (age)) #Output: <class 'float'>
print(" ")

# Integer to string
age = str(age)

print(age) # Output: '100.0'
print(type(age)) # Output: <class 'str'>
print(" ")

# String to Boolean
name = bool(name)
print(name) # Output: True
print(type(name)) # Output: <class 'bool'>