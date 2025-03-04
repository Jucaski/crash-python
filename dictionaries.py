person = {
        "name": "Minerva",
        "last_name": "Brown",
        "favorite_book": "It",
        "age" : "32",
        "city" : "London"
    }
print(person.get("name"))
print(person.get("last_name"))
print(person.get("favorite_book"))
print(person.get("age"))
print(person.get("city"))
print(person.get("favorite_videogame", "No favorite videogame available"))
print(person.get("favorite_animal"))
