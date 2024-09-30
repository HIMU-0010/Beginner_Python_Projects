menu = {"dumpling": 120,
        "ramen": 200,
        "rice bowl": 180,
        "wedges": 70,
        "pepsi": 35}

cart = []
bill = 0

print("---------MENU---------")
for key, value in menu.items():
    print(f"{key:10}:{value:.2f}")
print("----------------------")

while True:
    food = input("Enter an food item from the menu: (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print()     
print("----------YOUR ORDER-----------")
for food in cart:
    bill += menu.get(food)
    print(f"{food}", end=" ")

print()
print(f"Your bill is: BDT {bill}")
print()
        