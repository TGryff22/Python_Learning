'''
format specifier = {value:flags} format a value based on what
                    flags are inserted

.(number)f = round to that many decimal places (fixed point)
:(number) = allocate that many spaces
:03 = allocate and zero pad that many spaces
:< = left justify
:> = right justify
:^ = center align
:+ = use a plus sign to indicate positive value
:= = place sign leftmost postitive value
:  = insert a space before positive numbers
:, = comma seperator
'''

price1 = 3.1427
price2 = -997.36
price3 = 52.86

print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:+20}")
print(f"Price 3 is ${price3:+,.0f}")