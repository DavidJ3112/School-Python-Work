animals = {
    "cat": 4,
    "dog": 4,
    "cow": 4,
    "horse": 4,
    "sheep": 4,
    "zebra": 4,
    "chicken": 2,
    "spider": 8
}

animal = input("Enter an animal: ").lower()

if animal in animals and animals[animal] == 4:
    print(f"Correct! A {animal} has four legs.")
else:
    print(f"A {animal} does not have four legs, or is not in the list.")