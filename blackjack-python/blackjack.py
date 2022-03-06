from banking_pkg.sit import sit_down,get_balance,buy_in
from banking_pkg.user import login,register
from banking_pkg.deal import play

database = {'admin':'password123'}
authorized_user = ""

while True:
    sit_down()

    if authorized_user == "":
        print("You must be logged in to play.")
    else:
        print("Logged in as: ", authorized_user)

    menu_input = input("Choose an option: ")
    if menu_input == "1":
        username = input("\nEnter Username: ").lower()
        password = input("Enter Password: ")
        authorized_user = login(database, username, password)
    elif menu_input == "2":
        username = input("Enter Username: ").lower()
        password = input("Enter Password: ")
        if len(password) > 4:
            authorized_user = register(database, username)
            if authorized_user != "":
                database[username] = password
        else:
            print("Password must be at least 5 characters!")
    elif menu_input == "3":
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            balance = buy_in(authorized_user)
    elif menu_input == "4":
        if authorized_user == "":
            print("\nYou must be logged in to play.")
        elif get_balance(username) == 0:
            print("You must buy in to place a wager.")
        else:
            play(username)
    elif menu_input == "5":
        if authorized_user == "":
            print("\nYou are not logged in!")
            continue
        else:
            print("")
            print("Join us again soon!")
            authorized_user = ""
    elif menu_input == "6":
        if authorized_user == "":
            print("")
            print("Thank you for visiting!")
            break
        else:
            user_input = input("Would you like to withdraw your balance? (Y/N): ").lower()
            if user_input == "y" or user_input == "yes":
                print("Your balance of:",get_balance(username),"has been deposited into your bank.")
                print("\nThank you for playing with us and have a great day!")
            else:
                print("We cannot store your balance once you exit the casino.")
                exit_input = input("Are you sure you do not want to take your balance with you? (Y/N): ").lower()
                if exit_input == "y" or exit_input =="yes":
                    print("\nThank your for your contribution!")
                    break
                else:
                    continue
            break
    else:
        print("Please select a valid option")
        continue