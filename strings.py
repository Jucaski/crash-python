name = "ada lovelace"

print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
# the f is for formating
print(f"{first_name} {last_name}")
print(f"Hello, {first_name.title()}")
print(f"Hello: \t{first_name.title()}")
print(f"Hello: \n{first_name.title()}")

#removing the spaces at the end of the string or the right side of the string

message = "This is a message "
clean_message = message.rstrip()
print(message)
print(clean_message)

#Removing the spaces from the left side of the string
message = " This is my message "
clean_message = message.lstrip()
print(clean_message)

#And finally removing both sides of the strings

clean_message = message.strip()
print(clean_message)

#Removing a prefix in a url

url = "https://jucaski.github.io"
url_without_prefix = url.removeprefix("https://")
print(url_without_prefix)

#exercise 
student_name = "Lina"
print(f"Hello {student_name}, do you want to study some python today?")
print(f"Hello {student_name.title()}, do you want to study some python today?")
print(f"Hello {student_name.upper()}, do you want to study some python today?")
print(f"Hello {student_name.lower()}, do you want to study some python today?")

quote = " A person who never made a mistake never tried anything new "
author = "Albert Einstein"
print(f"{author} once said: '{quote}'")
print(f"{author} once said: \n'{quote.strip()}'")

file_name = "hello_world.py"
print(f"{file_name.removesuffix(".py")}")