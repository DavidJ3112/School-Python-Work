antwoord = "ja"

while antwoord == "ja":
    getal = int(input("Van welk getal wil je de tafel zien? "))

    for i in range(1, 11):
        print(f"{i} x {getal} = {i * getal}")

    antwoord = input("Nog een tafel zien? (ja/nee) ")

print("Tot ziens!")
