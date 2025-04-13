name = input("Please enter your full name:")
print("Your name in uppercase:", name.upper())
print("Your name in lowercase:", name.lower())

name_of_spaces = name.replace(" ", "")
print("Total number of characters (excluding spaces):", len(name_of_spaces))

name_reversed = name[::-1]
print("Your name reversed:", name_reversed)


