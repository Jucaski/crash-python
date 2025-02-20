#creating numerical lists
#range function

for value in range(1,5):
    print(value)
#python stops when reaches whe second value so the output never contains the end value

#USING LISTS

#printing the first 3 items in the lists

list = ["item1","item2", "item3", "item4", "item5" ]
print("The first 3 items of the list:")
print(list[:3])
print("Printing 3 items from the middle of the list:")
print(list[1:4])
print("Finally the last 3 items of the list:")
print(list[-3:])

favorite_food=["rice","ramen", "miso soup", "gyozas"]
friend_favorite_food=favorite_food[:]

favorite_food.append("jiaozi")
friend_favorite_food.append("pizza")
print(favorite_food)
print(f"my favorite food: {favorite_food}")
print(f"my friend's food: {friend_favorite_food}")

#iterating the list with a loop
for food in favorite_food:
    print(f"my favorite food: {food}")
for food in friend_favorite_food:
    print(f"my friend's favorite food: {food}")
