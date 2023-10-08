weight = float(input("enter your weight: "))
unit = input("kilograms or pounds (K/L) :")

if unit == "K":
    weight = weight * 2.204
    unit = "lbs."
    print(f"your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.204
    unit = "kgs."
    print(f"your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not a valid unit")

