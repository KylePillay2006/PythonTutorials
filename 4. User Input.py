# User Input

name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
age = age + 1

print(f"Hello {name}")
print(f"You are {age} years old")

# Mad Libs
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter an verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today is went to a {adjective1} zoo.")
print(F"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

# Area Calculator

print("Area Calculator")

length = float(input("Enter the Length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))

area = length*width

print(f"The area is: {area}cm^2")

# Shopping Cart

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity =  int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total), 2}")
