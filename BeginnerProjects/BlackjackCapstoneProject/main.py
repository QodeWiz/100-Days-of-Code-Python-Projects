from art import logo
import random
startGame = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def winCondition(player_score, computer_score):
    if player_score > 21:
        print("You went over! You lose")
    elif computer_score > 21:
        print("Opponent went over! You win")
    elif player_score < computer_score:
        print("You lose")
    else:
        print("You win")

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
    while computer_current_score <= 16:
        ComputerNextCard = random.choice(cards)
        computerCards.append(ComputerNextCard)
        computer_current_score += ComputerNextCard
        print(f"Testing computer cards: {computerCards}, current score = {computer_current_score}")

    shouldContinue = True

    while shouldContinue:
        drawNextCard = input("Type 'y' to get another card, type 'n' to pass: ")
        if drawNextCard == 'y':
            PlayerNextCard = random.choice(cards)
            playerCards.append(PlayerNextCard)
            player_current_score += PlayerNextCard
            print(f"Your cards: {playerCards}, current score = {player_current_score}")
            winCondition(player_score=player_current_score, computer_score=computer_current_score)
        else:
            shouldContinue = False
            winCondition(player_score=player_current_score, computer_score=computer_current_score)

if startGame == 'y':
    print(logo)
    blackjackGame()



