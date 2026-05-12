import random

# Variable construction
number = round(random.uniform(0.0, 100.0), 1)
guess = 0

# quick awnser
print(number)

def Guesing():
    while True:
        guess = input("Please enter your guess: ")
        try:
            return round(float(guess), 1)
        except ValueError:
            print("NAN")

guess = Guesing()
while True:
    if guess > number:
        print("Lower")
        guess = Guesing()
    elif guess < number:
        print("Higher")
        guess = Guesing()
    else:
        print("You did it")
        break
