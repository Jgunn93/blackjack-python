
def sit_down():
    print("")
    print("   === Welcome To The Golden Nugget ===   ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.     Register      |")
    print("------------------------------------------")
    print("| 3.    Buy In    | 4.        Play       |")
    print("------------------------------------------")
    print("| 5.   Logout     | 6.        Quit       |")
    print("------------------------------------------")

balances = {'admin':1000}

def get_balance(username):
    if username in balances.keys():
        return balances[username]
    else:
        return 0

def buy_in(username):
    while True:
        deposit_amt = input("Enter amount to buy in with: ")
        if deposit_amt.isnumeric():
            deposit_amt = int(deposit_amt)
            if username in balances.keys():
                new_balance = balances.get(username) + deposit_amt
            else:
                new_balance = deposit_amt
            print(username + " has bought in for $ " + str(deposit_amt))
            print("Thank you for your buy in.")
            balances[username] = new_balance
            return new_balance
        else:
            print("Please enter a valid number to buy in for.")

def update_balance(username,amount):
    if username in balances.keys():
        new_balance = balances.get(username) + amount
        balances[username] = new_balance
        return new_balance