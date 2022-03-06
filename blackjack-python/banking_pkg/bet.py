from banking_pkg.sit import get_balance

def bet(username):
    while True:
        bet_amt = input("Please input your bet amount: ")
        if bet_amt.isnumeric():
            if int(bet_amt) < 5:
                print("Minimum bet is $5, please make a valid bet.")
                continue
            if int(bet_amt) > get_balance(username):
                print("\nYou cannot bet more than you have bought in for.\n")
            else:
                print("Thank you for your bet.\n")
                return int(bet_amt)
        else:
            print("\nPlease note the casino only accepts bets in whole dollar amounts.\n")
            continue