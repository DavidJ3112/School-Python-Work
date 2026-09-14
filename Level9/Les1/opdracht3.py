import csv

path = "C:/Git_repos/School-Python-Work/Level9/Les1-2"
file = "data.csv"

file_path = path + "/" + file

with open(file_path, "r") as csv_file:
    text = csv_file.readlines()

print("Alle regels:")
for row in text:
    print(row)

regels = []

for row in text:
    onderdelen = row.strip().split(',')
    regels.append(onderdelen)

print("\nEerste deel van elke regel:")
for row in regels:
    print(row[0])

print("\nEerste regel:", regels[0])
print("Laatste regel:", regels[-1])
print("Totaal aantal regels:", len(regels))