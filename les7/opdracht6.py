antwoord1 = 12
antwoord2 = 25
antwoord3 = 49

score = 0

gok1 = int(input("Hoeveel is 4 x 3? "))
if gok1 == antwoord1:
    score = score + 1

gok2 = int(input("Hoeveel is 5 x 5? "))
if gok2 == antwoord2:
    score = score + 1

gok3 = int(input("Hoeveel is 7 x 7? "))
if gok3 == antwoord3:
    score = score + 1

print(f"Je score is {score} van de 3!")

if score == 3:
    print("Uitstekend gedaan, je hebt alles goed!")
