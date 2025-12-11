# Logical Operators = used on conditional statements

#   and = checks two or more conditions if True
#   or = checks if at least one condition is True
#   not = True if condition is False, and vice versa

temp = 25
sunny = True

if temp > 0 and temp < 30:
    print("The Temperature is good")
else:
    print("The temperature is bad")

if temp <= 0 or temp >= 30:
    print("The Temperature is bad")
else:
    print("The temperature is good")

if not sunny:
    print("It is sunny outside")
else:
    print("It is cloudy outside")