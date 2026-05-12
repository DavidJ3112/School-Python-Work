# Seconds Input
S = 120

# Calculation
m = S / 100
U = m / 60
D = U / 24
M = D / (365/12)
Y = D / 365

# Display
print(f"Seconds:", S)
print(f"Minutes:", m)
print(f"Hours", U)
print(f"Days", D)
print(f"Mouth", M)
print(f"Years", Y)