from init import *

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = "Text.txt"
try:
    file = open(CURRENT_DIR + "/" + FILENAME, "x")
except FileExistsError:
    pass

file = open(CURRENT_DIR + "/" + FILENAME, "a")

file.write(f"cool{ANSI.NEW_LINE}")

file.close()



file = open(CURRENT_DIR + "/" + FILENAME, "r")
for i, line in enumerate(file, start=1):
    print(f"{ANSI.CYAN}{i}: {line.strip()}{ANSI.RESET}")