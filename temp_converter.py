unit = input("Is this temprature in Celcius or Fahrenheit (C/F): ")
temp = float(input("enter the temprature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temprature is in Fahrenheit is {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temprature is in Calcius is {temp}°C")
else:
    print(f"{unit} is a invalid unit of temprature")

