from art import *
from game_data import data
import random

def format_data(account):
    """ Takes the account data and returns it in printable form """
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """ Takes a user guess and follower count and retusn if they got it right or not """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(higher_lower_logo)
score = 0
account_b = random.choice(data)

# Make the game repeatable
game_should_continue = True

while game_should_continue:
    # generate random account from game data
    account_a =  account_b 
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    print(vs_logo)
    print(f"Against B: {format_data(account_b)}.")

    # ask user for guess

    guess = input("Who has more followes? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(higher_lower_logo)
    
    # check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"Your're right! Current score {score}")
    else:
        print(f"Sorry, you're wrong. Final score: {score}")
        game_should_continue = False


# Make account at position B become account at position A

