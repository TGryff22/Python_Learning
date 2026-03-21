'''
logical operators = evaluate multiple conditions at the same time
or = at least one condition is true
and = all conditions must be true
not = reverse the result, returns false if the result is true
'''

temp = 28
is_raining = True
is_sunny = False

'''
if temp > 30 or temp < 0 or is_raining:
    print("Event cancelled due to extreme weather conditions.")
else:
    print("Event will proceed as scheduled.")
'''

if temp >= 28 and is_sunny:
    print("It is Hot outside 🥵")
    print("It is Sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is cold outside 🥶")
    print("It is sunny ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside 😊")
    print("It is sunny ☀️")
elif temp >= 28 and not is_sunny:
    print("It is Hot outside 🥵")
    print("It is Sunny ☀️")
elif temp <= 0 and not is_sunny:
    print("It is cold outside 🥶")
    print("It is sunny ☀️")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside 😊")
    print("It is sunny ☀️")