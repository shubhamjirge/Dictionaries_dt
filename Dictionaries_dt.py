# Dictionaries

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "loop": "The action doing something over again and again"
}

print(programming_dictionary["Function"])

programming_dictionary["ship"] = "the action of floating on the sea surface level."


# empty_dictionary = {}

# wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# edit an item in dictionary
programming_dictionary["Bug"] = "virus in the computer."
print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
