from art import logo, vs
import random
from game_data import data

def check_answer(answer, a_followers, b_followers):
    """Take a user's guess and the follower counts and return if they got it right."""
    if a_followers > b_followers:
        return answer == "a"
    else:
        return answer == "b"

def game():
    score = 0
    game_should_continue = True
    # Print 'logo'
    print(logo)

    # Generate a random account for comparison
    profile2 = random.choice(data)

    # Make profile2 the new profile1
    while game_should_continue:
          profile1 = profile2
          profile2 = random.choice(data)
          # If no profile1 is provided, select the first and second profiles randomly
          if profile1 == profile2:
              profile2 = random.choice(data)
    # Show first Instagram profile (name, description, country)
          print(f"Compare A: {profile1['name']}, a {profile1['description']}, from {profile1['country']}")
          # Print 'vs'
          print(vs)
          # Show second Instagram profile (name, description, country)
          print(f"Against B: {profile2['name']}, a {profile2['description']}, from {profile2['country']}")

          # Ask player to guess who has more followers, A or B
          answer = input("Who has more followers? Type 'A' or 'B': ").lower()

          # Get follower counts
          a_follower_count = profile1["follower_count"]
          b_follower_count = profile2["follower_count"]

          # Check if the user is correct
          is_correct = check_answer(answer, a_follower_count, b_follower_count)

          # Clear the screen after each guess
          print("\n" * 20)

          # Give feedback and update score
          if is_correct:
              score += 1
              print(f"You are correct! Current score: {score}")
          else:
              print(logo)
              if score <= 3:
                  print(f"Your final score is: {score}. C'mon, you can do better.")
              elif score > 3 and score < 6:
                  print(f"You lost, but you did pretty well. Your final score is: {score}")
              else:
                print(f"You lost, but you were amazing. Your final score is: {score}.")
              game_should_continue = False  # End the game if the guess is wrong

while True:
    game()
    continue_game = input("Do you want to play again? Type 'y' or 'n': ")
    if continue_game != 'y':
        break
