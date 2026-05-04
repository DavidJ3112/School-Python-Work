import random
# Variable setup
numbers = []

# Random number generation and added to list
for i in range(10):
    numbers.append(random.randint(0, 100))
#print(numbers)

for n in range(10):
    print(f"current number is {numbers[n]}")
    hl = int(input("Enter 1 (higher) or 0 (lower): "))

    if n >= 9: break

    if hl == 1:
        if numbers[n+1] > numbers[n]:
            print("True")
        elif numbers[n+1] < numbers[n]:
            print("False")

    elif hl == 0:
        if numbers[n+1] > numbers[n]:
            print("False")
        elif numbers[n+1] < numbers[n]:
            print("True")