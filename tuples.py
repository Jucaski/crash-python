#Tuples are inmutable, the values cannot change throughout the life of the program

foods = ("pizza", "ramen", "gyozas", "sushi", "onigiri")
print(foods)

for food in foods:
    print(f"this is my favorite food: {food}")

#But you can reasign the variable

foods = ("food1", "food2", "food3", "food4")
print(foods)
