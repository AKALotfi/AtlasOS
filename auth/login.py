def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if username == "lotfi" and password == "1234":
            print("\nWelcome", username, "\n")
            return True
        else:
            print("\nIncorrect Credentials. Please Try Again.\n")