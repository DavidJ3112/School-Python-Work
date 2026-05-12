prijs = float(input("Wat is de prijs van het product? "))
geld = float(input("Hoeveel geld heb je? "))

if geld >= prijs:
    wisselgeld = geld - prijs
    print(f"Je hebt genoeg geld! Je wisselgeld is €{wisselgeld:.2f}.")
else:
    tekort = prijs - geld
    print(f"Je hebt niet genoeg geld. Je komt €{tekort:.2f} tekort.")