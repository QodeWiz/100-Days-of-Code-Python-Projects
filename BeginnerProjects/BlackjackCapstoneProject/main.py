from art import logo
import random
startGame = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def blackjackGame():
    playerCards = random.sample(cards, 2)
    player_current_score = 0
    for card in playerCards:
        player_current_score += card
    print(f"Your cards: {playerCards}, current score = {player_current_score}")
    
    computerCards = random.sample(cards, 2)
    computer_current_score = 0
    for card in computerCards:
        computer_current_score += card
    print(f"Testing computer cards: {computerCards}, current score = {computer_current_score}")
    print(f"Computer's first card: {computerCards[0]}")

if startGame == 'y':
    print(logo)
    blackjackGame()



