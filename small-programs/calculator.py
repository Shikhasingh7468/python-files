print("1. addition(+)")
print("2. subtraction(-)")
print("3. multiplication(*)")
print("4. division(/)")

operators = int(input("choose a number for calculation "))
num1 = int(input("enter first number "))
num2 = int(input("enter second number "))

match operators:
    case 1:
        print(f"the addition of {num1} and {num2} is {num1+num2}")
    case 2:
        print(f"the subtraction of {num1} and {num2} is {num1-num2}")
    case 3:
        print(f"the multiplication of {num1} and {num2} is {num1*num2}")
    case 4:
        print(f"the division of {num1} and {num2} is {num1/num2}")
    case _:
        print("enter a valid operator no.")

