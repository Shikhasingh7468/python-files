foods = []
prices = []
total = 0

while True:
    food = input("enter the food you want to buy(q to quit)")
    if food.lower() == "q":
        break
    else:
        price = float(input("enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nyour total is {total}")