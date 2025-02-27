# IF
car = "bmw"
print(f"Is the car a 'bmw'? {car  =='bmw'}")
print(f"Is the car a 'byd'? {car  =='byd'}, the car is: {car}")


age = 23


if age < 2:
    print("you are a baby")
elif age < 4:
    print("you are a toddler")
elif age < 13:
    print("you are a kid")
elif age < 20:
    print("you are a teenager")
elif age < 65:
    print("you are an adult")
elif age >= 65:
    print("you are an elder")


names = ["Jordan", "Mali", "Sora", "admin", "Capri"]

if names:
    for name in names:
        if name == "admin":
            print(f"do you want to see some reports {name}?")
        else:
            print(f"Nice to see you {name}")
else: 
    print("the list of names is empty")



new_users = ["capriz", "malu", "Mara", "lina", "aden"] 
registered_users = ["malu", "mara", "aden"] 

for new_user in new_users:
    if new_user.lower() in registered_users:
        print(f" You are already registered: {new_user}")
    else:
        print(f"Welcome {new_user}")

