menu = {
    "pizza": 1000,
    "nachos": 200,
    "popcorn": 700,
    "fries": 100,
    "chips": 50,
    "pretzel": 150,
    "soda": 70,
    "lemonade": 300
}

cart = []
total = 0

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:10}: ₹{value:.2f}")
print("--------MENU--------")

while True:
    food = input("enter the food you want to choose (q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------- YOUR ORDER ----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"the total is ₹{total:.2f}")
    


