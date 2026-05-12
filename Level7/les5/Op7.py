while True:
    Prijs = input("Please enter The Price: ")
    try:
        Prijs = float(Prijs)
        break
    except:
        print("NAN")

BTW = Prijs/100*21
Total = Prijs/100*121

print(f"Prijs: €{Prijs} | BTW: €{BTW} | Totaal: €{Total}")