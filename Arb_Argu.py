# *args      = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments 
#           * unpacking operator 
#           1. positional 2. default 3. keyword  4. ARBITRARY
'''
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))
'''
'''
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr." "Spongebill", "Bob", "Tripants", "III")
'''
'''
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street= "123 Tree St.",
              apt="Unit 999",
              city="Miami", 
              state="Florida", 
              zip="98765")
'''

def shipping_label(*args, **kwargs): # args before kwargs
    for arg in args:
        print(arg, end= " ")
    print()
    
    print(f"{kwargs.get('street')}") # using single quotes here because of python error
    
    if "apt" in kwargs:    
        print(f"{kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
    else:
        pass
    
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr." "Spongebill", "Tripants", "III",
                street= "123 Tree St.",
                # apt="Unit 999",
                pobox="PO Box #5432",
                city="Miami", 
                state="Florida", 
                zip="98765")