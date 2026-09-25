#shopping program

foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy (press 'q' to quit): ")
    if food == "q":
        break
    else:
        price = float(input("enter the price of food: "))
        print(f"enter the price of a {food}")
        foods.append(food)
        prices.append(price)

print("----- YOUR CARD -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"the total is : {total} dollars")

