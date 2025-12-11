import math

friends = 0 

# friends = friends + 1
# friends += 1

# friends = friends - 2
# friends -= 2

# friends = friends * 3
# friends *= 3

# friends = friends / 4
# friends /= 4

# friend = friends ** 2
# friends **= 2

remainder = friends % 3

print(friends)

print(remainder)

x = 3.14
y = 4
z = 5

# result = round(x)

# result = abs(y)

# result = pow(4, 3)

# result = max(x, y, z)

result = min(x, y, z)

print(result)

# math module

x = 9.1

# print(math.pi)

# print(math.e)

# result = math.sqrt(x)

# result = math.ceil(x)

# result = math.floor(x)

print(result)

# circumference of a circle

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")

# area of a circle

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")

# hypotenuse calculator

a = (input("Enter side A: "))
b = (input("Enter side B: "))

c =  math.sqrt(pow(a, 2) + pow(b , 2))

print(f"Side C = {round(c, 2)}cm")

