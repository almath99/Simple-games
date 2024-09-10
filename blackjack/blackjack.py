import art
from art import logo
import random

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare_scores(user_score, comp_score):
    blackjack = 21
    if user_score > blackjack:
        return(f"Your hand is {user_score}. You lost..")
    elif comp_score > blackjack:
        #print(f"Computer's hand is {comp_score}.")
        return("You won!")
    elif user_score == blackjack:
        return("You have Blackjack! You won!")
    elif comp_score == blackjack:
        return("Computer has Blackjack! You lost..")
    elif user_score == comp_score:
        return("It's a draw!")
    elif user_score > comp_score and user_score < blackjack:
        return(f"Computer's hand is {comp_score}. Your hand is {user_score}. You won!")
    else:
        return(f"Computer's hand is {comp_score}. Your hand is {user_score}. You lost...")


def blackjack_game():
    print (logo)
    start = input("Do you wanna play a game of Blackjack? Type 'y' or 'n': ")
    if start == 'y':
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_cards = [random.choice(cards), random.choice(cards)]
        comp_cards = [random.choice(cards), random.choice(cards)]

        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)


        print(f"Your cards: {user_cards}. Your current score is {user_score} ")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 21 or comp_score == 21:
            print(compare_scores(user_score, comp_score))
            # return

        while user_score < 21:
            more = input("Type 'y' to get another card or 'n' to pass: ")
            if more == 'y':
                user_cards.append(random.choice(cards))
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}. Your current score is {user_score} ")
            else:
                break

        while comp_score < 17:
            comp_cards.append(random.choice(cards))
            comp_score = calculate_score(comp_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
        print(compare_scores(user_score, comp_score))


while True:
    blackjack_game()
    continue_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if continue_game != 'y':
        print("Hope you had fun! See you later!")
        break
