while True:
    value1 = input("Please enter value 1: ")
    try:
        value1 = float(value1)
        break
    except:
        print("NAN")

while True:
    value2 = input("Please enter value 2: ")
    try:
        value2 = float(value2)
        break
    except:
        print("NAN")

mt = input("Choose operator Type: ")
while(True):
    if mt == "+":
        Output = value1 + value2
        break
    elif mt == "-":
        Output = value1 - value2
        break
    elif mt == "/":
        Output = value1 / value2
        break
    elif mt == "*":
        Output = value1 * value2
        break
    elif mt not in ["+","-","/","*"]:
        print("Invalid operator, try again.")
        mt = input("Choose operator Type: ")

print(f"{value1} {mt} {value2} = {Output}")