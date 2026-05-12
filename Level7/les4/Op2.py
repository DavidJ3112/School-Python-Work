import math
pie = (math.pi)

while True:
    straal = input("Please enter Straal: ")
    try:
        float(straal)
        break
    except:
        print("NAN")

straal = int(straal)

awnser = straal ** 2 * pie
print(awnser)