import random

# Variable construction
number = random.randint(0, 100)
guess = 0

# quick awnser
print(number)

def Guesing():
    while True:
        guess = input("Please enter your guess: ")
        try:
            return int(guess)
        except:
            print("NAN")

guess = Guesing()
while True:
    if guess < number:
        print("Lower")
        guess = Guesing()
    elif guess > number:
        print("Higher")
        guess = Guesing()
    else:
        print("You did it")
        break
