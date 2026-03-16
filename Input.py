# input = A function that prompts the user for input and returns it as a string

input("How are you doing?: ")
age = input("How old are you?: ")
# or age = int(input("How old are you?: ")) to convert to integer in line instead of adding new line."

age = int(age) # Convert the age from a string to an integer
age = age + 1 # Add 1 to the age

print ("That great to hear! Have a great day!")
print (f"Wow! You are {age} years old! That's amazing!") # Only need f when using variable