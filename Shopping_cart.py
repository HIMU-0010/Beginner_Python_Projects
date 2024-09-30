foods = []
prices = []
total_price = 0

while True:
    food = input("Enter your food item to add on the list (press 'q' to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("Enter the price of this food item: BDT "))
        foods.append(food)
        prices.append(price)
        
print("------ Your Cart ------")

for food in foods:
    print(f"{food}", end= " ")
    
for price in prices:
    total_price += price

print()  
print(f"Your total cart bill is: BDT {total_price}")