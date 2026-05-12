while True:
    a = input("Enter Number: ")
    try:
        b = float(a)
        break
    except:
        print("Not A Value")

print(b)