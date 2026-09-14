import os

cwd = os.path.dirname(os.path.abspath(__file__))

def lees_data(bestand):
    data = []

    with open(bestand) as f:
        for regel in f:
            data.append(regel.strip().split(","))

    return data

print(lees_data(os.path.join(cwd, "data.csv")))


# [['"naam,leeftijd,woonplaats"'], ['"Yoana,18,Amersfoort"'], ['"Becci,20,Zwolle"'], ['"Norah,22,Den', 'Haag"']]
# het hoort comma te gebruiken en niet spatie (wit regel) dit is te zien aan den haag
# data.append(regel.split())
# [['"naam', 'leeftijd', 'woonplaats"'], ['"Yoana', '18', 'Amersfoort"'], ['"Becci', '20', 'Zwolle"'], ['"Norah', '22', 'Den Haag"']]
