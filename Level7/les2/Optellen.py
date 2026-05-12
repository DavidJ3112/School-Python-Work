print("Value A")
a = float(input())
print("Value B")
b = float(input())
print("Choose Math Type")
mt = input()
while(True):
    if(mt=="+"):
        c = a + b
        break
    elif(mt=="-"):
        c = a - b
        break
    elif(mt=="/"):
        c = a / b
        break
    elif(mt=="*"):
        c = a * b
        break

print("Output")
print(c)