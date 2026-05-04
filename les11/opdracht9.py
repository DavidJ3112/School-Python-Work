juiste_pin = "1234"
pogingen = 3

while pogingen > 0:
    pin = input("Voer je PIN in: ")

    if pin == juiste_pin:
        print("Toegang verleend!")
        break
    else:
        pogingen -= 1
        if pogingen > 0:
            print(f"Foute PIN. Nog {pogingen} {'pogingen' if pogingen > 1 else 'poging'}.")
        else:
            print(f"Foute PIN. Nog 0 pogingen.")
            print("Geblokkeerd! Te veel foute pogingen.")
