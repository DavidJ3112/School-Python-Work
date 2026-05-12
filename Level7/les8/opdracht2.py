import getpass

users={
    "Admin":"1234",
    "David":"12345",
    "Thijs":"Wachtwoord"
}

loginname = input("Username: ")
loginpwd = getpass.getpass("Password: ")

if loginname in users and users[loginname] == loginpwd:
    print(f"Welcome, {loginname}")
else:
    print("Invalid username or password")
