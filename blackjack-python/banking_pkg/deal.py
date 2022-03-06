from banking_pkg.sit import update_balance,get_balance
from banking_pkg.bet import bet
from banking_pkg.cards import deal,total,deck
from banking_pkg.print import printer



def play(username):
    while True:
        bet_amt = bet(username)
        hand,dealer_hand=deal()
        while True:
            print("Your hand is: ")
            printer(hand)
            print("")
            print("Dealer Hand is: ")
            printer(dealer_hand)
            player_score, dealer_score = total(hand), total(dealer_hand)
            print("")
            print("You are showing: ", player_score)
            print("The dealer is showing: ", dealer_score)
            if (player_score == dealer_score == 21):
                print("")
                print("It's a push!")
                print("Your new balance is: $", get_balance(username))
                break
            elif dealer_score == 21:
                print("")
                print("The dealer wins!")
                update_balance(username, -1 * bet_amt)
                print("")
                print("Your new balance is: $", get_balance(username))
                break
            elif player_score == 21:
                print("")
                print("You have blackjack!")
                update_balance(username, 1.5 * bet_amt)
                print("")
                print("Your new balance is: $", get_balance(username))
                break
            elif dealer_score != 21 and player_score != 21 and player_score != 10 and player_score !=11:
                user_input = input("Would you like to hit? (H/S): ").lower()
                while user_input == "h" or user_input =="hit":
                    print("")
                    hand.append(deck.pop())
                    print("You draw a card...")
                    print("Your new hand is: ")
                    printer(hand)
                    print("")
                    player_score = total(hand)
                    print("You are showing: ", player_score)
                    if player_score <= 21:
                        user_input =input("Would you like to hit? (H/S)")
                    else:
                        user_input = "s"
                if player_score > 21:
                    print("")
                    print("You bust!")
                    update_balance(username, -1 * bet_amt)
                    print("Your new balance is: $", get_balance(username))
                else:
                    while dealer_score <= 17:
                        print("")
                        dealer_hand.append(deck.pop())
                        print("The dealer draws a card...")
                        print("Dealer's new Hand: ")
                        print("")
                        printer(dealer_hand)
                        dealer_score = total(dealer_hand)
                        print("The dealer is showing: ", dealer_score)
                    if dealer_score > 21:
                        print("")
                        print("Dealer bust")
                        print("You win!")
                        update_balance(username, 1 * bet_amt)
                        print("Your new balance is: $", get_balance(username))
                    elif dealer_score > player_score:
                        print("")
                        print("The Dealer wins!")
                        update_balance(username, -1 * bet_amt)
                        print("Your new balance is: $", get_balance(username))
                    elif dealer_score == player_score:
                        print("")
                        print("You push.")
                        print("Your new balance is: $", get_balance(username))
                    else:
                        print("")
                        print("You win!")
                        update_balance(username, 1 * bet_amt)
                        print("Your new balance is: $", get_balance(username))
                break
            elif player_score == 10 or player_score == 11:
                user_input = input("Would you like to hit, stand or double down? (H/S/D): ").lower()
                if user_input == "h" or user_input == "hit":
                    print("")
                    hand.append(deck.pop())
                    print("You draw a card...")
                    print("Your new hand is: ")
                    printer(hand)
                    print("")
                    player_score = total(hand)
                    print("You are showing: ", player_score)
                    while player_score <= 21: 
                        user_input =input("Would you like to hit? (H/S)")
                        if user_input == "h" or user_input == "hit":
                            print("")
                            hand.append(deck.pop())
                            print("You draw a card...")
                            print("Your new hand is: ")
                            printer(hand)
                            player_score = total(hand)
                            print("You are showing: ", player_score)
                            if player_score <= 21:
                                user_input =input("Would you like to hit? (H/S)")
                            else:
                                user_input = "s"
                        else:
                            user_input = "s"
                elif user_input == "s" or user_input == "stand":
                    while dealer_score <= 17:
                        print("")
                        dealer_hand.append(deck.pop())
                        print("The dealer draws a card...")
                        print("Dealer's new Hand: ")
                        printer(dealer_hand)
                        print("")
                        dealer_score = total(dealer_hand)
                        print("The dealer is showing: ", dealer_score)
                    if dealer_score > 21:
                        print("")
                        print("Dealer bust")
                        print("You win!")
                        update_balance(username, 1 *bet_amt)
                        print("Your new balance is: $", get_balance(username))
                    elif dealer_score > player_score:
                        print("")
                        print("The Dealer wins!")
                        update_balance(username, -1 * bet_amt)
                        print("Your new balance is: $", get_balance(username))
                    elif dealer_score == player_score:
                        print("")
                        print("You push.")
                        print("Your new balance is: $", get_balance(username))
                    else:
                        print("")
                        print("You win!")
                        update_balance(username, 1 * bet_amt)
                        print("Your new balance is: $", get_balance(username))
                elif user_input == "d" or user_input =="double down":
                    print("")
                    hand.append(deck.pop())
                    print("You draw a card...")
                    print("Your new hand is: ")
                    printer(hand)
                    print("")
                    player_score = total(hand)
                    print("You are showing: ", player_score)
                    while dealer_score < 17:
                        print("")
                        dealer_hand.append(deck.pop())
                        print("The dealer draws a card...")
                        print("Dealer's new Hand: ")
                        printer(dealer_hand)
                        print("")
                        dealer_score = total(dealer_hand)
                        print("The dealer is showing: ", dealer_score)
                    if dealer_score > 21:
                        print("")
                        print("Dealer bust")
                        print("You win!")
                        update_balance(username, 2 *bet_amt)
                        print("Your new balance is: $", get_balance(username))
                    elif dealer_score > player_score:
                        print("")
                        print("The Dealer wins!")
                        update_balance(username, -2 * bet_amt)
                        print("Your new balance is: $", get_balance(username))
                    elif dealer_score == player_score:
                        print("")
                        print("You push.")
                        print("Your new balance is: $", get_balance(username))
                    else:
                        print("")
                        print("You win!")
                        update_balance(username, 2 * bet_amt)
                        print("Your new balance is: $", get_balance(username))
                    break
        choice = input("\nWould you like to play again?").lower()
        print("")
        if choice == "y" or choice == "yes" or choice == " y":
            hand = []
            dealer_hand = []
            continue
        else:
            print("Thanks for playing!")
            print("Your ending balance is: $",get_balance(username))
            hand = []
            dealer_hand = []
            break