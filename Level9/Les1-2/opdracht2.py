data = {
    "David": {"Name": "David", "Last_name": "Schreurs", "Age": 18},
    "Rose": {"Name": "Rose", "Last_name": "Cellia", "Age": 19}
}

print(data)
print(data["David"])
print(data["Rose"])

data["David"]["city"] = "Amsterdam"
data["Rose"]["city"] = "Amsterdam"

print(data)
print(data["David"])
print(data["Rose"])

del data["David"]["city"]
del data["Rose"]["city"]

print(data)
print(data["David"])
print(data["Rose"])
