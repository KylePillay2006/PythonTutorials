# Weight Conversion Exercise

weight = float(input("Enter your weight"))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight*2.205
    unit = "Lbs"
    print(F"Your weight is: {round(weight, 1 )} {unit}")
elif unit == "L":
    weight = weight/2.205
    unit = "Kgs"
    print(F"Your weight is: {round(weight, 1 )} {unit}")
else:
    print(f"Sorry, {unit} was not valid")


 