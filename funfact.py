import random
fun_facts = [
    "Bananas are berries, but strawberries are not!",
    "Honey never spoils; edible honey has been found in ancient Egyptian tombs.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    "Octopuses have three hearts and blue blood.",
    "A day on Venus is longer than a year on Venus.",
    "Wombat poop is cube-shaped to prevent it from rolling away.",
    "There's a species of jellyfish that is biologically immortal; it can revert back to its juvenile form.",
    "The Eiffel Tower can grow more than 6 inches during summer due to heat expansion.",
    "A group of flamingos is called a 'flamboyance.'",
    "Sharks existed before trees; they've been around for over 400 million years."
]

print("Hi, do you know something??")

Input = input("Enter any number to know!!! : ")
if Input.isdigit() :
    print(random.choice(fun_facts))
