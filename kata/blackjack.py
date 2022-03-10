# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random

def create_deck():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    random.shuffle(cards)
    return cards

def blackjack():
    user_cards = []
    computer_cards = []
    game_over = False

    deck = create_deck()

    for _ in range(2):
        user_cards.append(deck.pop())
        computer_cards.append(deck.pop())

    def calculate_score(cards):
    #0 == blackjack in the game.
        if sum(cards) == 21 and len(cards) == 2:
            return 0
    # Checking for an ace. If the score is over 21 => removing the 11 and replacing it with 1.
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if user_score > 21 and computer_score > 21:
            return "You went over. You lose"

        if user_score == computer_score:
            return "It's a draw"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack"
        elif user_score == 0:
            return "Win with a Blackjack"
        elif user_score > 21:
            return "You went over. You lose"
        elif computer_score > 21:
            return "Opponent went over. You win"
        elif user_score > computer_score:
            return "You win"
        else:
            return "You lose"

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deck.pop())
            else:
                game_over = True

    # The computer keep drawing cards as long as it has a score less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deck.pop())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final card: {user_cards}, final score is {user_score}")
    print(f"   Computer's final card: {computer_cards}, final score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    blackjack()
