while True:
    weight = input("Please enter The weight in KG: ")
    try:
        weight = float(weight)
        break
    except:
        print("NAN")

while True:
    Length = input("Please enter The Length in Meters: ")
    try:
        Length = float(Length)
        break
    except:
        print("NAN")

bmi = weight/Length**2

print(f"You're Total bmi is: {bmi}")