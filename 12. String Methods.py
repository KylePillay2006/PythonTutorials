# name = input("Enter your full name: ")

# phone_number = input("Enter your phone number: ")

# result = len(name)
# result = name.find("o")
# result = name.rfind("o")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")

# print(phone_number)

# print(help(str))

# Exercise

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user_name = input("Please create a user name: ")

# 1. Username must be no more than 12 characters
too_long = len(user_name) > 12

# 2. Username must not contain spaces
contains_space = " " in user_name

# 3. Username must not contain digits
contains_digit = any(char.isdigit() for char in user_name)

if too_long or contains_space or contains_digit:
    print(f"{user_name} is not a valid user name!")
else:
    print(f"{user_name} is a valid user name!")

