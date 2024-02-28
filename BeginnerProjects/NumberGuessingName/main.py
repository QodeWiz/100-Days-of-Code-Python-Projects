from art import logo
import random

NUMBER = random.randint(1,100)
easy_attempts = 10
hard_attempts = 5

def check_guess():
    guess = int(input("Make a guess: "))
    if guess == NUMBER:
        print(f"You guessed it, you win! The answer is {guess}")
        return False
    elif guess < NUMBER:
        print("Too low. \nGuess Again")
        return True
    else:
        print("Too high. \nGuess Again")
        return True

def easy_game():
    global easy_attempts
    print(f"You have {easy_attempts} attempts to guess the number.")
    if easy_attempts == 0:
        print("Game over! You lost")
        exit()
    if check_guess():
        easy_attempts -= 1
        easy_game()

def hard_game():
    global hard_attempts
    print(f"You have {hard_attempts} attempts to guess the number.")
    if hard_attempts == 0:
        print("Game over! You lost")
        exit()
    if check_guess():
        hard_attempts -= 1
        hard_game()

def start_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    print(f"pss number is {NUMBER}")
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        easy_game()
    elif difficulty == "hard":
        hard_game()
    else:
        print("Error: Invalid input")

start_game()
