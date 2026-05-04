import random

getal = random.randint(1, 10)
gok = int(input("Raad een getal tussen 1 en 10: "))

if gok < getal:
    print("Het getal ligt hoger.")
elif gok > getal:
    print("Het getal ligt lager.")
else:
    print(f"Goed geraden! Het getal was {getal}.")
