# typecasting = The process of converting a value of one data type to another
#               (string, integer, float, boolean)
#               Explicit vs Implicit

# Explicit 
name = "Kyle"
age = 19
gpa = 1.9
student = True

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)

age = bool(age)
print(age)

name = bool(name)
print(name)

# This tells you what datatype your variable is ...
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# Implicit

x = 2

y = 2.0

x = x / y

print(x)
