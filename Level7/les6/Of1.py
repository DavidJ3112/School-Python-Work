Paid = float(input("Paid: "))
Price = float(input("Price: "))
PayBack = Paid - Price

if Price < Paid:
    print(f"You recive €{PayBack}")

elif Price > Paid:
    PayBack =- PayBack
    print(f"You Have to pay €{PayBack}")
