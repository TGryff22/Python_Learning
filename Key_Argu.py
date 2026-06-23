# keyword arguments = arguments preceded by an identifier when 
#                     we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary
'''
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="Gee", first="Tee")
'''
# for x in range (1, 11):
    # print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=234, first=567, last=8901)

print(phone_num)