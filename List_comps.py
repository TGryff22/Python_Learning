# List comprehensions = a concise way to create lists in Python. Compact and easier to read than traditional loops
#                       [expression for value inn iterable if condition]

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)