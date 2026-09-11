# Maak een bestandsnaam
filename = "data_gebruikers_v1.txt"

# Verwijder de extensie .txt
filename = filename.replace(".txt", "")

# Split de bestandsnaam op _
onderdelen = filename.split("_")

# Print alle onderdelen afzonderlijk
for onderdeel in onderdelen:
    print(onderdeel)