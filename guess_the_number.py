from art_number import logo
print(logo)
import random

def guess_number():
    """A function that generates a random number between 1 and 100,
    and asks the user to guess the number. The user can choose
    between two difficulty levels: 'easy' or 'hard'."""

    print("I'm thinking of a number between 1 and 100.")
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    # Ask the user to choose a difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # Set the number of attempts based on the chosen difficulty
    if difficulty == 'hard':
        attempts = 5
        print("You have 5 attempts remaining to guess the number.")
    else:
        attempts = 10
        print("You have 10 attempts remaining to guess the number.")

    # Start the guessing loop
    while attempts > 0:
        guess = int(input("Make a guess: "))
        # Check if the guess is too high
        if guess > number:
            print("Too high")
            # Decrease the number of attempts
            attempts -= 1
            # Inform the user about the remaining attempts
            print(f"You have {attempts} attempts left.")

        # Check if the guess is too low
        elif guess < number:
            print("too low")
            attempts -= 1
            print(f"You have {attempts} attempts left.")

        # If the guess is correct
        else:
            print("You got it right!")
            break

    # If the player runs out of attempts, show the correct number
    else:
        print(f"You lost... The number was {number}")

guess_number()
