filename = "data_gebruikers_v1.txt"

filename = filename.replace(".txt", "")

onderdelen = filename.split("_")

for onderdeel in onderdelen:
    print(onderdeel)