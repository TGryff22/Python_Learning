'''
nested loop = A loop within another loop (outer, inner)
                outer loop:
                    inner loop:
'''

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):  # print three times
    for y in range(columns):
        print(symbol, end = "")  # prints all numbers on one line
    print() # print on seperate lines

'''
for x in range(3):  # print three times
    for y in range(1, 10):
        print(y, end = "")  # prints all numbers on one line
    print() # print on seperate lines
'''