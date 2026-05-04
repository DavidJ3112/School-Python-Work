celsius = float(input("Voer een temperatuur in Celsius in: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C is {fahrenheit}°F")

if celsius < 0:
    print("Waarschuwing: vriespunt!")
