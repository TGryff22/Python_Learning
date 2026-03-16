# if = condition is true, do something
# else = if condition is false, do something else
# elif = if the previous conditions were false, then try this condition. Can have as many elif statements as you want, but only one else statement 
# == comparison operator, checks if the values on either side are equal

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You are not born yet.")
elif age >= 100:
    print("You are super old.")
else:
    print("You are a child.")