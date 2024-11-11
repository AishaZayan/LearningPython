import random

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    # Check for blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Adjust Ace value if total exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    results = {
        "draw": "draw ☺️  \n\n",
        "user_over": "you went over 21, sorry. 🫢 \n\n",
        "computer_over": "computer went over 21, you win. ⭐️ \n\n",
        "user_21": "you won with a blackjack. 😎👌🏻🔥 \n\n",
        "computer_21": "sorry, computer had a blackjack. 😱 \n\n",
        "user_win": "you win. 🥰 \n\n",
        "user_lose": "you lose. 😕 \n\n",
    }

    if user_score == computer_score:
        return results["draw"]
    elif user_score > 21:
        return results["user_over"]
    elif computer_score > 21:
        return results["computer_over"]
    elif user_score == 0:
        return results["user_21"]
    elif computer_score == 0:
        return results["computer_21"]
    elif user_score > computer_score:
        return results["user_win"]
    else:
        return results["user_lose"]

def game():
    user_cards = [deal_cards() for _ in range(2)]
    computer_cards = [deal_cards() for _ in range(2)]

    game_continue = True
    while game_continue:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\n\n\nYour cards are {user_cards}, current score is {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_continue = False
        else:
            user_needs_another_card = input("Get another card? (y/n): ").lower()
            if user_needs_another_card == "y":
                user_cards.append(deal_cards())
            else:
                game_continue = False

        # Computer's turn: Continue until score reaches at least 17
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_cards())
            computer_score = calculate_score(computer_cards)

        print(f"\nYour final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

user_input = input("Choose a game to start...\n1-Froogy \n2-Twenty One \n3-Snake \n").lower()
while user_input == "twenty one" or user_input == "2":
    game()
    user_input = input("Play again? Type 'twenty one' or '2' to play again, or any other key to quit: ").lower()