menu = {
    "dosa" : 3.00,
    "pizza" : 5.00,
    "burger" : 4.50,
    "fries" : 2.50,
    "soft drinks" : 1.50
}

cart = []
total = 0
print("-----menu-------------------------------------------------------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
    
print("----------------------------------------------------------------")

while True:
    food = input("select the food: ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-----food in cart-------------------------------------")
for food in cart:
    total += menu.get(food)
    print(food ,end=" ")
print()

print(f"Total: ${total:.2f}")