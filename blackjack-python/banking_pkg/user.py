def login(database, username, password):
    if username in database.keys() and database[username] == password:
        print("Welcome", username)
        return username
    elif username in database.keys() and database[username] != password:
        print("Incorrect password, please try again.")
        return ""
    else:
        print("Incorrect username, please try again.")
        return ""
def register(database, username):
    if len(username) < 10:
        if username in database.keys():
            print(username, "already registered")
            return ""
        else:
            print(username, "has been registered!")
            return username
    else:
        print("Username is too long!")