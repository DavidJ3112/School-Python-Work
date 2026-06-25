from init import *

def cal(num):
    num = num * 2
    num = num + 10
    num = num / 10
    return num

print(f"{ANSI.CYAN}{cal(10)}")
print(f"{ANSI.CYAN}{cal(20)}")
print(f"{ANSI.CYAN}{cal(40)}")