import time

t = time.localtime()
print(time.strftime("%H:%M:%S %d-%m-%Y", t))