for getal in range(1, 21):
    if getal % 3 == 0 and getal % 5 == 0:
        print("FizzBuzz")
    elif getal % 3 == 0:
        print("Fizz")
    elif getal % 5 == 0:
        print("Buzz")
    else:
        print(getal)
