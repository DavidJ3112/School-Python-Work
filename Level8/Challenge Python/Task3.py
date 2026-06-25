from getpass import getpass
import json
import os
import hashlib

FILE = "users.json"


#!# =========================================================
#!# VERSIE 1: HARDCODED
#!# =========================================================
class LoginScreenV1:
    def __init__(self):
        self.user = "admin"
        self.password = "admin"

    def run(self):
        print("=== LOGIN V1 (HARDCODED) ===")

        username = input("Gebruikersnaam: ")
        password = getpass("Wachtwoord: ")

        if username == self.user and password == self.password:
            print("Login succesvol!")
            print(f"Welkom {username}")
        else:
            print("Foute login.")


#!# =========================================================
#!# VERSIE 2: JSON BESTAND
#!# =========================================================
def load_users_v2():
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_users_v2(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)


class LoginScreenV2:
    def __init__(self):
        self.users = load_users_v2()

    def login(self):
        username = input("Gebruikersnaam: ").strip()
        password = getpass("Wachtwoord: ")

        if username in self.users and self.users[username] == password:
            print("Login succesvol!")
        else:
            print("Foute login.")

    def register(self):
        username = input("Nieuwe gebruikersnaam: ").strip()

        if username in self.users:
            print("Bestaat al.")
            return

        password = getpass("Wachtwoord: ")

        self.users[username] = password
        save_users_v2(self.users)

        print("Account aangemaakt.")

    def run(self):
        while True:
            print("\n=== LOGIN V2 (JSON) ===")
            print("1. Login")
            print("2. Register")
            print("3. Exit")

            choice = input("> ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.register()
            elif choice == "3":
                break


#!# =========================================================
#!# VERSIE 3: HASHED WACHTWOORDEN
#!# =========================================================
def hash_password(password, salt="static_salt"):
    return hashlib.sha256((password + salt).encode()).hexdigest()


def load_users_v3():
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_users_v3(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)


class LoginScreenV3:
    def __init__(self):
        self.users = load_users_v3()

    def login(self):
        username = input("Gebruikersnaam: ").strip()
        password = getpass("Wachtwoord: ")

        hashed = hash_password(password)

        if username in self.users and self.users[username] == hashed:
            print("Login succesvol!")
            print(f"Welkom {username}")
        else:
            print("Foute login.")

    def register(self):
        username = input("Nieuwe gebruikersnaam: ").strip()

        if username in self.users:
            print("Bestaat al.")
            return

        password = getpass("Wachtwoord: ")

        self.users[username] = hash_password(password)
        save_users_v3(self.users)

        print("Account aangemaakt.")

    def run(self):
        while True:
            print("\n=== LOGIN V3 (HASHED) ===")
            print("1. Login")
            print("2. Register")
            print("3. Exit")

            choice = input("> ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.register()
            elif choice == "3":
                break


#!# =========================================================
#!# START KEUZE
#!# =========================================================
if __name__ == "__main__":
    print("Kies versie:")
    print("1. Hardcoded")
    print("2. JSON users")
    print("3. Hashed passwords")

    choice = input("> ")

    if choice == "1":
        LoginScreenV1().run()
    elif choice == "2":
        LoginScreenV2().run()
    elif choice == "3":
        LoginScreenV3().run()