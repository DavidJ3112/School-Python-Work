name = input("What's you're name? ")
age = int(input("What is you're age? "))

if age < 4:
    tarief = "Gratis"
elif age <= 11:
    tarief = "Child tarief (50% off)"
elif age <= 64:
    tarief = "Normal tarief"
elif age >= 65:
    tarief = "Senior Tarief (40% off)"

print(f"Hello {name}, you're tarief is {tarief}")