woord = input("Voer een woord in: ")
lengte = len(woord)

if lengte < 5:
    print(f"'{woord}' is een kort woord ({lengte} letters).")
elif lengte >= 10:
    print(f"'{woord}' is een lang woord ({lengte} letters).")
else:
    print(f"'{woord}' is een gemiddeld woord ({lengte} letters).")
