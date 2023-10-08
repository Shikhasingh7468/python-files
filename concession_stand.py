import random
def calulate_bill(menu,cart):
    sum = 0
    for food in cart:
        sum += menu.get(food)
    return sum

def list_item(cart):
    i = 1
    for item in cart:
        print(str(i) +". "+ item)
        i+=1

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
    else:
        print(f"I apologize, but we currently don't have the {food} available. However, I can suggest {random.choice(list(menu.keys()))} as a great alternative. Would you like to try that instead?")
print("----------- YOUR ORDER ----------")
list_item(cart)
print(f"the total is ₹{calulate_bill(menu,cart):.2f}")


