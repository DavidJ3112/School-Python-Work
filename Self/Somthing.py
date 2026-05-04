#Stratring list
V1 = ["1","2","3"]

while True:
    print("Kies Option")
    print("1 - Add")
    print("2 - Remove")
    print("3 - Clear")
    print("4 - Stop")
    print(V1)
    x = input()

    if x == "1":
        print("What Do You Want to Add")
        New = input()
        V1.append(New)
    elif x == "2":
        print("What Do You Want to Remove")
        print(V1)
        remove = input()
        V1.remove(remove)

    elif x == "3":
        print("Clearing the Variable")
        V1 = [""]

    elif x == "4":
        break

    else:
        print("No Correct Input")

exit()