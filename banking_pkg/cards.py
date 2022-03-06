import random

suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
cards = [2,3,4,5,6,7,8,9,10,11,12,13,14]

deck = []

for suit in suits:
    for card in cards:
        deck.append((suit,card))
        deck.append((suit,card))

def deal():
    hand = []
    dealer_hand = []
    random.shuffle(deck)
    hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    return hand,dealer_hand

def total(hand):
    total_score = 0
    for current_card in sorted(hand):
        value = current_card[1]
        if value in range(11,14):
            total_score += 10
        elif value == 14:
            if total_score >= 11:
                total_score += 1
            else:
                total_score += 11
        else:
            total_score += value
    return total_score