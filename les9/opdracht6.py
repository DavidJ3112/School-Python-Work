amount = float(input("Enter the purchase amount: "))
member = input("Are you a member? (yes/no): ").lower()

is_member = member == "yes"

if is_member and amount >= 50:
    discount = 0.20
elif is_member or amount >= 50:
    discount = 0.10
else:
    discount = 0.0

final_amount = amount * (1 - discount)

print(f"Discount: {discount * 100}%. Final amount: {final_amount:.2f}.")