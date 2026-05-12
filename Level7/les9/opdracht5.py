day_number = int(input("Enter a number from 1 to 7: "))

if day_number == 1:
    day_name = "Monday"
elif day_number == 2:
    day_name = "Tuesday"
elif day_number == 3:
    day_name = "Wednesday"
elif day_number == 4:
    day_name = "Thursday"
elif day_number == 5:
    day_name = "Friday"
elif day_number == 6:
    day_name = "Saturday"
elif day_number == 7:
    day_name = "Sunday"
else:
    day_name = None

if day_name:
    print(f"Day {day_number} is {day_name}.")
else:
    print("Invalid number, choose a number from 1 to 7.")